import socket
import requests
import subprocess
import time
from colorama import Fore, init
import urllib3
from directory_enum import dir_enum
import pyfiglet

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def linux_print(color, text):
    print(f"{Fore.YELLOW}$ {color}{text}")
# Initialize Colorama
init(autoreset=True)

# Tool Name & Header
tool_name = "CyberRecon"
ascii_banner = pyfiglet.figlet_format(tool_name)
print(Fore.RED + ascii_banner)
print(Fore.YELLOW + "=" * 50)
print(Fore.GREEN + "🔍 Advanced Reconnaissance Tool | Version 1.0")
print(Fore.YELLOW + "=" * 50)
time.sleep(1)


# Get User Input
url = input(f"\n{Fore.GREEN}🌍 Enter the Target URL: {Fore.WHITE}").strip()
domain = url.replace("https://", "").replace("http://", "").split("/")[0]

# Function to Check URL Status
def check_by_url(url):
    try:
        linux_print(Fore.CYAN, f"Checking status for {url} ...")
        response = requests.get(url, allow_redirects=True)
        color = Fore.GREEN if response.status_code == 200 else Fore.RED
        linux_print(color, f"Status Code: {response.status_code}")
        return response.status_code, response.text[:500]
    except requests.exceptions.RequestException as e:
        linux_print(Fore.RED, f"Error checking domain status: {e}")
        return None, None

# Function to Check if Domain is Accessible via IP
def check_by_ip(domain, original_content):
    try:
        ip = socket.gethostbyname(domain)
        linux_print(Fore.BLUE, f"🌐 Resolved IP for {domain}: {ip}")

        headers = {"Host": domain}
        response = requests.get(f"https://{ip}", headers=headers, verify=False, allow_redirects=False)

        color = Fore.GREEN if response.status_code == 200 else Fore.RED
        linux_print(color, f"📡 Status Code for {ip}: {response.status_code}")
        if "Location" in response.headers:
            linux_print(Fore.YELLOW, f"🔄 Redirected To: {response.headers['Location']}")

        if response.status_code == 200 and original_content and response.text[:500] == original_content:
            linux_print(Fore.GREEN, "✅ The website is accessible via IP!")
        else:
            linux_print(Fore.RED, "❌ The content differs, IP-based access may not work correctly.")
    except requests.exceptions.RequestException as e:
        linux_print(Fore.RED, f"🚫 Error: {e}")

# Function for Subdomain Enumeration
def subdomain_enum():
    linux_print(Fore.CYAN, f"🌍 Scanning for subdomains of {domain}...")
    with open('sub.txt', 'r') as file:
        subdomains = file.readlines()
    for sub in subdomains:
        sub = sub.strip()
        subdomain = f"http://{sub}.{domain}"
        try:
            sub_response = requests.get(subdomain, allow_redirects=True, timeout=5)
            color = Fore.GREEN if sub_response.status_code == 200 else Fore.RED
            linux_print(color, f"🌎 Found: {subdomain} | Status Code: {sub_response.status_code}")
        except requests.exceptions.RequestException:
            linux_print(Fore.RED, f"❌ Failed: {subdomain}")

# Function for Directory Enumeration
def directory_enum():
    linux_print(Fore.CYAN, f"📂 Starting directory enumeration on {domain}...")
    dir_enum(url)

# Function for Port Scanning
def scan_ports(domain):
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        linux_print(Fore.RED, "❌ Error: Could not resolve domain to an IP address.")
        return
    
    COMMON_PORTS = [21, 22, 23, 25, 53, 110, 123, 135, 139, 143, 161, 179, 389, 445, 465, 514, 587, 636, 993, 995, 1433, 1521, 1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 9200, 27017]
    open_ports = []
    
    linux_print(Fore.CYAN, f"🚀 Scanning open ports on {ip} using Nmap...")
    port_list = ",".join(map(str, COMMON_PORTS))
    
    try:
        cmd = ["sudo", "nmap", "-p", port_list, "--open", "-Pn", ip]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        for line in result.stdout.split("\n"):
            if "/tcp" in line and "open" in line:
                port = line.split("/")[0].strip()
                open_ports.append(port)
        
    except Exception as e:
        linux_print(Fore.RED, f"[-] Error scanning ports: {e}")
    
    color = Fore.GREEN if open_ports else Fore.RED
    linux_print(color, f"✅ Open Ports: {', '.join(open_ports)}" if open_ports else "❌ No open ports found.")

# Run Initial Domain Checks
linux_print(Fore.YELLOW, "🚀 Initializing CyberRecon scans...")
domain_status, domain_content = check_by_url(url)
if domain_status:
    check_by_ip(domain, domain_content)

# Interactive Menu for User Choices
while True:
    print(Fore.YELLOW + "\n" + "=" * 50)
    print(Fore.CYAN + f"🔎 CyberRecon Main Menu")
    print(Fore.YELLOW + "=" * 50)
    
    choice = input(
        f"{Fore.MAGENTA}$ Choose an option:\n"
        f" 1️⃣  Subdomain Enumeration\n"
        f" 2️⃣  Directory Enumeration\n"
        f" 3️⃣  Open Port Scanning\n"
        f" 4️⃣  Exit\n"
        f"{Fore.MAGENTA}$ Enter your choice: {Fore.WHITE}"
    ).strip()

    if choice == "1":
        subdomain_enum()
    elif choice == "2":
        directory_enum()
    elif choice == "3":
        scan_ports(domain)
    elif choice == "4":
        linux_print(Fore.YELLOW, "🚀 Exiting CyberRecon... Goodbye!")
        break
    else:
        linux_print(Fore.RED, "❌ Invalid choice! Please enter 1, 2, 3, or 4.")
