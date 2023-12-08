import requests
from utils.common import *

def deleteWebhook(url):
    set_console_title("Acid Delete Webhook")
    requests.delete(url)
    print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}C{Fore.WHITE}] Deleted Webhook")
    sleep(1)