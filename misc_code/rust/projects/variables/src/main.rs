use std::io;

fn main() {

    println!("Chose a number");
    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    let guess: u8 = guess.trim().parse().expect("Not a number!");

    println!("{guess}");

    let y: f32 = 3.23;
    println!("{y}")
}
