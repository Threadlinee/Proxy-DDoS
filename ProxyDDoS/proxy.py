import requests

def get_and_save_proxies(api_url="https://proxylist.geonode.com/api/proxy-list?limit=50&sort_by=lastChecked&sort_type=desc", output_file="proxys.txt"):
    print(f"[~] Fetching proxies from: {api_url}")
    
    try:
        print("[~] Sending request...")

        response = requests.get(
            api_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10 
        )

        print(f"[~] Response status: {response.status_code}")
        print(f"[~] Raw response (first 300 chars): {response.text[:300]}")

        if response.status_code != 200:
            print(f"[!] Failed to fetch proxies. Status code: {response.status_code}")
            return

        data = response.json().get("data", [])

        if not data:
            print("[!] No proxies returned from API.")
            return

        with open(output_file, "w") as f:
            for proxy in data:
                ip = proxy.get("ip")
                port = proxy.get("port")
                proto = proxy.get("protocols", ["http"])[0]
                line = f"{proto}://{ip}:{port}"
                print(f"[+] Saving proxy: {line}")
                f.write(line + "\n")

        print(f"[✓] Saved {len(data)} proxies to {output_file}")

    except requests.exceptions.Timeout:
        print("[!] Request timed out — server might be slow or blocking you.")
    except requests.exceptions.ConnectionError:
        print("[!] Connection error — check internet or if API is online.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

get_and_save_proxies()
