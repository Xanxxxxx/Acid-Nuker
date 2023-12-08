import requests
from utils.common import *

def tokenInfo(token):
    set_console_title("Acid Token Info")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
[{Fore.LIGHTGREEN_EX}User ID{Fore.RESET}]         {userID}
[{Fore.LIGHTGREEN_EX}User Name{Fore.RESET}]       {userName}
[{Fore.LIGHTGREEN_EX}2 Factor{Fore.RESET}]        {mfa}
[{Fore.LIGHTGREEN_EX}Email{Fore.RESET}]           {email}
[{Fore.LIGHTGREEN_EX}Phone number{Fore.RESET}]    {phone if phone else "None"}
[{Fore.LIGHTGREEN_EX}Token{Fore.RESET}]           {token}
            ''')
            input('hit the keys')