# CyberRecon - Advanced Reconnaissance Tool

CyberRecon is an advanced reconnaissance tool designed for security researchers and penetration testers. It helps gather crucial information about a target domain, including subdomains, directories, open ports, and IP accessibility.

---

## 🚀 Features
- **Subdomain Enumeration**: Finds subdomains using a predefined wordlist.
- **Directory Enumeration**: Checks for common directories on the target domain.
- **Port Scanning**: Uses `nmap` to scan for open ports.
- **IP Accessibility Check**: Determines if the target can be accessed via its IP address.
- **User-Friendly Interface**: Linux-style terminal outputs with color coding and an ASCII banner.

---

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CyberRecon.git
   cd CyberRecon
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure `nmap` is installed:
   ```bash
   sudo apt install nmap  # For Linux
   brew install nmap      # For macOS
   ```

---

## 🔧 Usage
Run the tool using Python:
```bash
python cyberrecon.py
```
### 📜 Menu Options:
1️⃣ **Subdomain Enumeration** - Finds active subdomains from `sub.txt`

2️⃣ **Directory Enumeration** - Scans directories listed in `dir.txt`

3️⃣ **Open Port Scanning** - Uses `nmap` to scan common ports

4️⃣ **Exit** - Quits the tool

---

## 📂 File Structure
```
CyberRecon/
├── cyberrecon.py      # Main script
├── directory_enum.py  # Directory enumeration function
├── sub.txt            # Subdomains wordlist
├── dir.txt            # Directories wordlist
├── requirements.txt   # Required Python modules
└── README.md          # This documentation
```

---

## 🎨 Tool Preview
```
   ____      _               ____                      
 / ___|   _| |__   ___ _ __|  _ \ ___  ___ ___  _ __  
| |  | | | | '_ \ / _ \ '__| |_) / _ \/ __/ _ \| '_ \ 
| |__| |_| | |_) |  __/ |  |  _ <  __/ (_| (_) | | | |
 \____\__, |_.__/ \___|_|  |_| \_\___|\___\___/|_| |_|
      |___/                                           

  🔍 Advanced Reconnaissance Tool | Version 1.0
```

---

## 📌 Notes
- The tool requires **root privileges** to run `nmap`.
- For best results, update `sub.txt` and `dir.txt` with custom wordlists.
- Ensure `requests` and `colorama` are installed properly.

---

## 📜 License
CyberRecon is an open-source project released under the **MIT License**.

---

## 🤝 Contributing
Pull requests are welcome! Feel free to fork the repository and submit improvements.

---

## ✨ Author
Developed by Shubham Chauhan

GitHub: https://github.com/shubham-c01

