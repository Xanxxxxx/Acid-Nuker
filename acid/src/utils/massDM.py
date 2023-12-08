import requests
from utils.common import *

def massDM(token, content):
    set_console_title("Acid Mass Dm")
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            headers=headers,
            data={"content": f"{content}"})
            print(f"[ {Fore.LIGHTGREEN_EX}C{Fore.RESET} ] {Fore.LIGHTGREEN_EX}ID: "+channel['id'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")