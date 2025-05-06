# ProxyDDoS Tool

ProxyDDoS is an educational tool designed for stress-testing and simulating real-world DDoS attacks using proxies. It leverages HTTP GET floods routed through SOCKS/HTTP proxies to test server resilience, load balancing, and firewall protection.

> ❗ **DISCLAIMER:** This tool is strictly for **educational**, **research**, and **authorized testing** purposes. Do not use this against servers you do not own or have explicit permission to test.

---

## 🚀 Features

- 🔁 Infinite request flooding via proxy rotation
- 🔗 HTTP GET flood using raw sockets
- 🌐 Full proxy support (HTTP, HTTPS, SOCKS4/5)
- 🔍 Real-time request logging
- 🧠 Multi-threaded high-speed requests
- 🎨 Stylish terminal UI with animated startup

---

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/719d424c-90ff-4314-a467-4face1397da3)

![image](https://github.com/user-attachments/assets/8814bc11-a10f-4143-973f-341825a2782b)


---

## 🧠 How It Works

The tool establishes a `CONNECT` tunnel via each proxy to the target host, then sends repeated `GET` requests through that tunnel. This simulates legitimate web traffic, bypassing some weak DDoS protections.

---

## 📦 Requirements

- Python 3.8+
- `pystyle` (for UI effects)

### Install dependencies:

pip install pystyle

#⚙️ Usage
Clone the repo:

git clone https://github.com/Threadlinee/Proxy-DDoS.git
cd Proxy-DDoS
Add your proxy list to a file named proxys.txt:

192.168.1.1:8080
51.91.123.7:3128
203.0.113.5:8080
Run the script:

python ProxyDDoS.py
Input the target URL (example: http://example.com)

# ℹ️ The attack will run infinitely until you stop the script manually (Ctrl+C).

# 🛡️ Legal & Ethical Use
This software is created for:

Penetration testing labs

Load testing under permission

Cybersecurity research

Academic purposes

Do not use it for:

Attacking government, financial, or third-party services

Any illegal or unauthorized testing

# 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

# 💬 Credits
Made by Threadlinee

Styled with pystyle

Educational use only. Stay ethical.

# ☕ Support
If you find this tool useful, drop a ⭐ or fork it. Contributions and proxy improvements are welcome.

[![Buy Me a Coffee](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G114SBVV)
