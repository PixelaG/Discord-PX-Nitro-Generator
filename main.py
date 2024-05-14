import requests
import string
import random
import time
import threading

discord_webhook_url = "https://discord.com/api/webhooks/1240051671204368406/pOj9Te7vrcE-RsUK-t-pXKKrcdazE6YO5lLv_eYm6NBclXtm19F1BAdjCmwnTq13Vpgw"

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def send_to_discord(message):
    payload = {"content": message}
    requests.post(discord_webhook_url, json=payload)

def generate_random_string(length=18):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def check_and_send(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        send_to_discord(f"Valid gift code found: {code}")
        print(GREEN + f"Valid gift code found: {code}" + RESET)
    else:
        print(RED + f"Invalid gift code: {code}" + RESET)

def generate_and_check_codes():
    while True:
        code = generate_random_string()
        check_and_send(code)

num_threads = 10

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=generate_and_check_codes)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()