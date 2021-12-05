import time
import requests
import pyfiglet
banner = pyfiglet.figlet_format("WDS")
print(banner)
print("[$] Webhook Discord Spamer by @blacksreaze")
msg = input("[?] Input spam message > ")
webhook = input("[?] Input webhook URL > ")
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"[!] MSG Send! {msg}")
        except:
            print("[!] Bad webhook! " + webhook)
            exit()
blackscreaze = 1
while blackscreaze == 1:
    spam(msg, webhook)