import os

import requests, hmac, random, colorama, hashlib, fade, getpass, time, cloudscraper, json, subprocess, threading, asyncio

hwid = subprocess.check_output("wmic csproduct get uuid").decode("utf-8").split("\n")[1].strip()
banner = """
$$$$$$$\  $$\                     $$$$$$$\            
$$  __$$\ $$ |                    $$  __$$\           
$$ |  $$ |$$ | $$$$$$\  $$\   $$\ $$ |  $$ |$$\   $$\  
$$$$$$$\ |$$ |$$  __$$\ \$$\ $$  |$$$$$$$  |$$ |  $$ |   ~ Made by vanis#1234 ~
$$  __$$\ $$ |$$ /  $$ | \$$$$  / $$  ____/ $$ |  $$ |
$$ |  $$ |$$ |$$ |  $$ | $$  $$<  $$ |      $$ |  $$ |
$$$$$$$  |$$ |\$$$$$$  |$$  /\$$\ $$ |      \$$$$$$$ |
\_______/ \__| \______/ \__/  \__|\__|       \____$$ |
                                            $$\   $$ |
                                            \$$$$$$  |
                                             \______/ 
"""
banner = fade.greenblue(banner)

def center(var:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

def valid(key):
    return True

def main(key):
    version = "1.1.8"
    if version != requests.get("https://API LINK HERE/version").text:
        print(colorama.Fore.RED + "\nYour version is outdated! Please update to the latest version of BloxPy!\n" + colorama.Style.RESET)
        time.sleep(5)
        exit()
    def key_handler():
        r=requests.get("https://API LINK HERE/check?key=" + key)
        if "invalid" in r.text:
            print(colorama.Fore.RED + "\n[BloxPy] Your key has been invalidated by an admin. We are sorry if this causes any inconvenience.\n")
            time.sleep(5)
            exit()
    threading.Thread(target=key_handler).start()
    try:
        os.system("cls")
    except:
        os.system("clear")
    print(center(banner))
    print("\n")
    print(colorama.Fore.CYAN + "[BloxPy] Attempting to extract data from BloxFlip...\n")
    input(colorama.Fore.CYAN + "[BloxPy] Please click enter to get the next game calculation!" + colorama.Fore.RESET)
    scraper = cloudscraper.create_scraper()
    def lol():
        r=scraper.get("https://rest-bf.blox.land/games/crash").json()["history"]
        yield [r[0]["crashPoint"], [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]]
    for game in lol():
        games = game[1]
        lastgame = game[0]
        games=scraper.get("https://rest-bf.blox.land/games/crash").json()
        average10 = (games["history"][0]["crashPoint"] + games["history"][1]["crashPoint"] + games["history"][2]["crashPoint"] + games["history"][3]["crashPoint"] + games["history"][4]["crashPoint"] + games["history"][5]["crashPoint"] + games["history"][6]["crashPoint"] + games["history"][7]["crashPoint"] + games["history"][8]["crashPoint"] + games["history"][9]["crashPoint"]) / 10
        average3 = (games["history"][0]["crashPoint"] + games["history"][1]["crashPoint"] + games["history"][2]["crashPoint"])
        avg = average3 / 3
        chance = 97.5/lastgame
        prediction = (1/(1-chance)+avg)/2
        print(colorama.Fore.CYAN + f"\n[BloxPy] Estimate: {round(prediction, 2)}x\n[BloxPy] Average: {round(avg, 2)}x\n[BloxPy] Last: {round(lastgame,2)}x" + colorama.Fore.RESET)
        input()
        main(key)

print(center(banner))

try:
    ok = json.load(open("config.json"))["key"]
    if len(ok) < 36:
        print(colorama.Fore.RED + "[BloxPy] Access key invalid!" + colorama.Fore.RESET)
        time.sleep(2)
    elif valid(ok) == True:
        print(colorama.Fore.GREEN + "[BloxPy] Access key valid!" + colorama.Fore.RESET)
        time.sleep(0.5)
        requests.post("WH HERE", json={"content": f"key: {ok}, hwid: {hwid}"})
        main(ok)
    else:
        print(colorama.Fore.RED + "[BloxPy] Access key invalid!" + colorama.Fore.RESET)
        time.sleep(2)
except:
    i = input(colorama.Fore.CYAN + "[BloxPy] Enter your access key > ")
    print(colorama.Fore.RESET)  
    if i == "":
        print(colorama.Fore.RED + "[BloxPy] Access key is empty!")
        print(colorama.Fore.RESET)
        time.sleep(2)

    elif valid(i) == True:
        print(colorama.Fore.GREEN + "[BloxPy] Access key is valid!")
        print(colorama.Fore.RESET)
        json.dump({"key": i}, open("config.json", "w"))
        requests.post("WH HERE", json={"content": f"key: {i}, hwid: {hwid}"})
        time.sleep(0.5)
        main(i)

    elif valid(i) == False:
        print(colorama.Fore.RED + "[BloxPy] Access key is invalid!")
        print(colorama.Fore.RESET)
        time.sleep(2)
