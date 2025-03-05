import requests

from colorama import Fore, init
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize Colorama
init(autoreset=True)

# Function to print with Linux-like prompt
def linux_print(color, text):
    print(f"{Fore.YELLOW}$ {color}{text}")

def dir_enum(domain):
    with open("dir.txt","r") as file:
        directories=file.readlines()
        for dir in directories:
            dir=dir.strip()
            directory=f"{domain}/{dir}"
            try:
                dir_response=requests.get(directory, allow_redirects=True, timeout=5)
                if dir_response.status_code == 200:
                    print(Fore.GREEN + f"Found: {directory} | Status Code: {dir_response.status_code}")
                else:
                    print(Fore.MAGENTA + f"Found: {directory} | Status Code: {dir_response.status_code}")
            except requests.exceptions.RequestException:
                print(Fore.RED + f"Failed: {directory}")
