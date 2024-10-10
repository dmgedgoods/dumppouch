use reqwest::Client; use serde::Deserialize; use std::error::Error;
use std::time::{Duration, Instant};
use rpassword::read_password;
use std::io::{self, Write};

// Struct to hold the authentication response
#[derive(Deserialize, Debug)]
struct AuthData {
    ticket: String,
    CSRFPreventionToken: String,
}

#[derive(Deserialize, Debug)]
struct AuthResponse {
    data: Option<AuthData>, // Optional in case the data field is null or malformed
}

// Struct to manage the session and re-authentication
struct ProxmoxSession {
    ticket: String,
    csrf_token: String,
    client: Client,
    server_url: String, // Store the server URL for further API calls
    session_start: Instant,
    session_duration: Duration,
}

impl ProxmoxSession {
    // Function to authenticate
    async fn authenticate(server_url: &str, username: &str, password: &str) -> Result<Self, Box<dyn Error>> {
        let client = Client::builder()
            .danger_accept_invalid_certs(true) // Disable SSL verification (for self-signed certs)
            .build()?;

        let params = [("username", username), ("password", password)];
        let auth_url = format!("{}/api2/json/access/ticket", server_url); // Dynamically insert server URL

        let response = client
            .post(&auth_url)
            .form(&params)
            .send()
            .await?;

        // Deserialize the response into AuthResponse struct
        let auth_response: AuthResponse = response.json().await?;

        // Ensure we have the necessary fields in the response
        if let Some(auth_data) = auth_response.data {
            println!("Authentication successful!");

            Ok(ProxmoxSession {
                ticket: auth_data.ticket,
                csrf_token: auth_data.CSRFPreventionToken,
                client,
                server_url: server_url.to_string(), // Store server URL for future API calls
                session_start: Instant::now(),
                session_duration: Duration::from_secs(7200), // 2 hours
            })
        } else {
            Err(Box::from("Authentication failed: No data returned from Proxmox API"))
        }
    }

    // Fetch VM data and other methods can go here
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Prompt for server name
    print!("Enter your Proxmox server name: ");
    io::stdout().flush()?;
    let mut server_name = String::new();
    io::stdin().read_line(&mut server_name)?;
    let server_name = server_name.trim(); // Remove newline characters

    // Autoformat URL
    let server_url = format!("https://{}:8006", server_name);

    // Prompt for username
    print!("Enter your Proxmox username (e.g., root@pam): ");
    io::stdout().flush()?;
    let mut username = String::new();
    io::stdin().read_line(&mut username)?;
    let username = username.trim();

    // Prompt for password
    print!("Enter your Proxmox password: ");
    io::stdout().flush()?;
    let password = read_password()?; // Secure password input

    // Authenticate and create session
    let mut _session = ProxmoxSession::authenticate(&server_url, &username, &password).await?;

    // Session is ready to use
    println!("Session is now ready for further API calls.");
    // Add VM fetching or further operations here

    Ok(())
}
