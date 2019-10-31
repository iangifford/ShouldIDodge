#Author: Ian Gifford
#Project: Should I Dodge?
#For those high-elo players who dodge to avoid L's, this will help give a less subjectiv answer on whether or not you should dodge.
import requests
import json
import bs4 as soup
import time

import tkinter.ttk

#Not currently working. It seems league data sites like to load their data from javascript, meaning it can't be scraped
#like this. Looking for an endpoint instead by reverse engineering the javscript as well as contacting the sites.
#champ: champion name to get data on
#lane: lane name to get data for that champ in
def scrape_stats(champ):
    try:
        cleaned_champ = sanitize_champ(champ)
        #print(cleaned_champ)
        champ_keys= get_champ_keys()
        key = champ_keys[cleaned_champ]
        #print(key)
        url = "https://stats2.u.gg/lol/1.1/rankings/9_21/ranked_solo_5x5/"+key+"/1.2.6.json"

        r = requests.get(url)

        if r.ok:
            data = r.json()
            lanes = list(data["12"]["10"].keys())
            #print(str(lanes))
            lanewins = {}
            matchups = {"1":None,"2":None,"3":None,"4":None,"5":None}
            for lane in lanes:
                lanewins[lane] = 100*(data["12"]["10"][lane][0]/data["12"]["10"][lane][1])
                matchups[lane] = data["12"]["10"][lane][12]

            return lanewins,matchups
            #print(data)
        else:
            print("status code: " + str(r.status_code))
            return (-1, -1)
    except Exception as e:
        print("Exception:",e)

        return (-1, -1)
def get_champ_keys():
    champ_keys = open("configs/champion_keys","r+")
    data = json.load(champ_keys)
    return data

#Cleans a champs name for URL purposes
#champ: Champ name to clean
def sanitize_champ(champ):
    cleaned = champ.strip().replace(" ","").replace("'","").replace(".","").lower()
    if cleaned == "nunu&willump":
        return "nunu"
    elif cleaned == "wukong":
        return "monkeyking"
    else:
        return cleaned

#Replaces all of the files with updated versions.
def update_all_champ_data(progress,window):
    champlist = open("configs/champions.txt", "r").readlines()
    numchamps = len(champlist)

    for champion in champlist:
        champion = champion.strip()
        built_data = {"primary_winrate_percent": 0,
                      "winrate_top": None, "winrate_jungle": None, "winrate_mid": None,
                      "winrate_adc": None, "winrate_support": None, "roles": None,
                      "matchups_top":None,"matchups_jungle":None,"matchups_mid":None,
                      "matchups_adc":None,"matchups_support":None}

        winrates,matchups = scrape_stats(champion)
        n = 0
        while winrates == -1 and n<100:
            winrates,matchups = scrape_stats(champion)
            n+=1
        if (n >= 100):
            print("Failed loading " + champion)
        roles = get_roles()
        keys = get_champ_keys()
        while(roles == -1):
            roles = get_roles()
        built_data["roles"] = roles[keys[sanitize_champ(champion)]]
        #print(built_data["roles"])
        built_data["winrate_top"] = winrates["4"]
        built_data["winrate_jungle"] = winrates["1"]
        built_data["winrate_mid"] = winrates["5"]
        built_data["winrate_adc"] = winrates["3"]
        built_data["winrate_support"] = winrates["2"]
        built_data["matchups_top"] = matchups["4"]
        built_data["matchups_jungle"] = matchups["1"]
        built_data["matchups_mid"] = matchups["5"]
        built_data["matchups_adc"] = matchups["3"]
        built_data["matchups_support"] = matchups["2"]
        built_data["primary_winrate_percent"] = winrates[str(built_data["roles"][0])]
        out = open("champion_data/" + champion + ".json", "w+")
        json.dump(built_data, out)
        out.close()
        progress['value'] += numchamps/190
        window.update()
    progress.pack_forget()
def get_roles():
    try:
        url = "https://stats2.u.gg/lol/1.1/primary_roles/9_21/1.2.6.json"
        r = requests.get(url)
        if r.ok:
            data = r.json()
            return data
            #print(data)
        else:
            print("status code: " + str(r.status_code))
            return -1
    except Exception as e:
        print("Exception:",e)

        return -1
def set_champ_keys():

    r = requests.get("https://static.u.gg/assets/lol/riot_static/9.21.1/data/en_US/champion.json?v9.21.2")

    if r.ok:
        f = open("configs/champion_keys","w+")
        keys = {}
        data = r.json()['data']
        for champ in data.keys():
            keys[sanitize_champ(champ)] = data[champ]['key']
        json.dump(keys,f)
        f.close()
    else:
        print(str(r.reason))
        return -1
set_champ_keys()
