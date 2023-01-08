import requests
import colorama
from colorama import *
from os import system
init()


system('cls')
system("title Feds Biolink Checker ^| By: https://feds.lol/data")

with open('usernames.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()
    all_usernames = len(usernames)
    if all_usernames == 0:
        print(f'{Fore.LIGHTRED_EX} [!] No usernames found!\n Make sure to paste them into usernames.txt and save.{Fore.RESET}')
        quit()



def banner():
    print(f'''{Fore.LIGHTCYAN_EX}

  ______       _       _       _ 
 |  ____|     | |     | |     | |
 | |__ ___  __| |___  | | ___ | |
 |  __/ _ \/ _` / __| | |/ _ \| |
 | | |  __/ (_| \__ \_| | (_) | |
 |_|  \___|\__,_|___(_)_|\___/|_|

      _____ _               _             
     / ____| |             | |            
    | |    | |__   ___  ___| | _____ _ __ 
    | |    | '_ \ / _ \/ __| |/ / _ \ '__|
    | |____| | | |  __/ (__|   <  __/ |   
     \_____|_| |_|\___|\___|_|\_\___|_|  
                                 
                                 
   {Fore.RESET}
    ''')



def check():
    while True:
        
        for username in usernames:

            r = requests.get(f'https://feds.lol/{username}', allow_redirects=True)

            if '<meta http-equiv="refresh" content="0;url=https://feds.lol/doesnt_exist">' in r.text:
                print(f" [{Fore.LIGHTGREEN_EX}+{Fore.RESET}] {username} is Available")
                with open('hits.txt', 'a') as f:
                    f.write(f"{username}\n")

            else:
                print(f" [{Fore.LIGHTRED_EX}-{Fore.RESET}] {username} is Not Available")
            
        break
    input("\n Done Checking Links, Press any key to exit...")


banner()
check()