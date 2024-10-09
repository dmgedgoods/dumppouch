from pwn import log
from scapy.all import rdpcap, IP, TCP, Raw
import re

# Initialize pwntools logging
logger = log.progress("Analyzing PCAP file")

# Function to load and parse the pcap file
def load_pcap(file_path):
    logger.status("Loading PCAP file")
    try:
        packets = rdpcap(file_path)
        logger.success(f"Loaded {len(packets)} packets")
        return packets
    except Exception as e:
        logger.failure(f"Error loading pcap: {e}")
        return None

# Function to detect credentials in payloads
def detect_credentials(payload):
    # Ensure it's a POST request, as credentials are typically sent in POST
    if "POST" in payload and re.search(r"(username|password|user|pass|login|token|auth)", payload, re.IGNORECASE):
        return True
    return False

# Extract usernames and passwords from the payload
def extract_credentials(payload):
    # Regex to extract common credential patterns like "u=username" and "p=password"
    user_match = re.search(r"u=(\w+)", payload)
    pass_match = re.search(r"p=(\w+)", payload)
    
    if user_match and pass_match:
        username = user_match.group(1)
        password = pass_match.group(1)
        return username, password
    return None, None

# Detect HTTP response codes to determine login success or failure
def detect_http_status(payload):
    # Common successful and failed login status codes
    success_codes = ["200", "302"]
    failure_codes = ["401", "403"]
    
    if any(code in payload for code in success_codes):
        return "success"
    elif any(code in payload for code in failure_codes):
        return "failure"
    return None

# Analyze the network packets for potential threats and sensitive data
def analyze_packets(packets):
    logger.status("Analyzing packets for potential threats and sensitive data")
    
    for packet in packets:
        if IP in packet and TCP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            sport = packet[TCP].sport
            dport = packet[TCP].dport

            log.info(f"Packet from {ip_src}:{sport} to {ip_dst}:{dport}")
            
            # Add logic to inspect the payload for sensitive information
            if Raw in packet:  # Check if the packet contains raw data (i.e., payload)
                payload = str(packet[Raw].load)
                
                # Check if payload contains sensitive data
                if detect_credentials(payload):
                    username, password = extract_credentials(payload)
                    if username and password:
                        log.critical(f"Potential credential leak detected: Username='{username}', Password='{password}' in packet from {ip_src} to {ip_dst}")
                    else:
                        log.critical(f"Potential credential leak detected in packet: {payload}")
                
                # Check for HTTP response codes indicating login success or failure
                status = detect_http_status(payload)
                if status == "success":
                    log.success(f"Successful login detected from {ip_src} to {ip_dst}")
                elif status == "failure":
                    log.error(f"Failed login attempt detected from {ip_src} to {ip_dst}")

            # Add detection for unusual ports
            if is_unusual_port(dport):
                log.warning(f"Unusual port detected: {dport} from {ip_src}")

# Helper function to check if a port is unusual (same as before)
def is_unusual_port(port):
    if 49152 <= port <= 65535:
        return False
    return port not in [80, 443, 21, 22, 23, 25, 53, 110, 143, 993, 995, 3306]

# Entry point
if __name__ == "__main__":
    pcap_file = "httpLogin.pcapng"  # Make sure this file exists or use the correct path
    packets = load_pcap(pcap_file)
    
    if packets:
        analyze_packets(packets)
    log.success("Threat analysis complete")

