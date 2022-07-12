# Admin Login Finder - Find Admin Page Login
# Author : DociTeam - https://github.com/DociTeam

import requests
import os
import time

def clear_console():
    if os.name in ('nt', 'dos'): #Check OS name for using correct command
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass
def change_title():
    if os.name in ('nt', 'dos'):
        try:
            os.system('title "DociTeam | Admin Login Finder"')
        except:
            pass
    else:
            pass


clear_console()
change_title()

class color : 
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'



dociteam = color.Cyan+"""
                                     ____             _ _____                    
                                    |  _ \  ___   ___(_)_   _|__  __ _ _ __ ___  
                                    | | | |/ _ \ / __| | | |/ _ \/ _` | '_ ` _ \ 
                                    | |_| | (_) | (__| | | |  __/ (_| | | | | | |
                                    |____/ \___/ \___|_| |_|\___|\__,_|_| |_| |_|
"""

banner =color.Magenta+ f"""
            ______              
         .-'      `-.           
       .'            `.         
      /                \        
     ;                 ;`       
     |  {color.Red}Admin Login{color.Magenta}     | ;       
     ;                 ; |
     '\               / ;       
      \`.           .' /        
       `.`-._____.-' .'         
         / /`_____.-'           
        / / /                   
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/
"""


def slowprint(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

print(dociteam)
time.sleep(2)
clear_console()
print(banner)
time.sleep(1)
slowprint(color.Yellow+"\n\n|---------- Welcome to Admin Login Finder ----------|\n",0.07)
slowprint(color.Yellow+"[!] This Project is Education Purpose Only!\n",0.07)

URL = str(input(color.Cyan+f"[+] URL (Example : https://google.com) : {color.White}")).strip()

print(color.Yellow+"\n[+] Finding Admin Login For : "+color.White+URL)
time.sleep(2)

with open("wordslist.txt","r",encoding="UTF-8") as words:
    for word in words.readlines():
        adminpage = URL+"/"+word.strip("\n")
        try:
            rq = requests.get(adminpage)
        except Exception as e:
            print(color.Red+"\n[!] Error -> "+e)
        if rq.status_code == 200:
            print(color.Green+"\n[+] Admin Page Found -> "+color.White+adminpage)
            with open("AdminPages.txt",'a',encoding="UTF-8") as admin:
                admin.writelines(adminpage+"\n")
        else:
            print(color.Red+"\n[-] Admin Page Not Found")
input(color.Cyan+"\n[+] Done! Press enter to exit..... ")