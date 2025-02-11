import time
import random
import requests

def ping_website():
    url = "https://spousetaker.onrender.com"
    while True:
        try:
            response = requests.get(url)
            print(f"Pinged {url} - Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Failed to ping {url}: {e}")
        
        # Wait for a random time between 40 and 160 seconds
        wait_time = random.randint(40, 160)
        print(f"Waiting for {wait_time} seconds before the next ping...")
        time.sleep(wait_time)

if __name__ == "__main__":
    ping_website()
