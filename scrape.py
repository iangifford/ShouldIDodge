#Author: Ian Gifford
#Project: Should I Dodge?
#For those high-elo players who dodge to avoid L's, this will help give a less subjectiv answer on whether or not you should dodge.
import requests
import json
import bs4 as soup
import time


#Not currently working. It seems league data sites like to load their data from javascript, meaning it can't be scraped
#like this. Looking for an endpoint instead by reverse engineering the javscript as well as contacting the sites.
#champ: champion name to get data on
#lane: lane name to get data for that champ in
def scrape_winrate(champ):
    try:
        cleaned_champ = sanitize_champ(champ)
        r = requests.get("https://u.gg/lol/champions/" + cleaned_champ + "/build")
        if r.ok:
            html = soup.BeautifulSoup(r.content, "lxml")
            champ_data = html.find_all("div", class_="champion-ranking-stats")[0]

            champ_winrate = champ_data.find_all("div", class_="win-rate")[0]
            value = champ_winrate.find_all("div", class_="value")[0]
            return float(value.text.strip("%"))
        else:
            print(str(r.reason))
            return -1
    except:
        print("exception")
        return -1
#Cleans a champs name for URL purposes
#champ: Champ name to clean
def sanitize_champ(champ):
    cleaned = champ.strip().replace(" ","").replace("'","")
    if cleaned == "Nunu&Willump":
        return "Nunu"
    else:
        return cleaned
#Replaces all of the files with updated versions.
def update_all_champ_data():
    for champion in open("configs/champions.txt", "r").readlines():
        champion = champion.strip()
        built_data = {"primary_winrate_percent": 0, "matchups_top": None, "matchups_jungle": None, "matchups_mid": None,
                      "matchups_adc": None, "matchups_support": None}
        print(champion)
        winrate = scrape_winrate(champion)
        while winrate == -1:
            scrape_winrate(champion)
            time.sleep(3)
        built_data["primary_winrate_percent"] = winrate
        out = open("champion_data/" + champion + ".json", "w+")
        json.dump(built_data, out)
        out.close()


update_all_champ_data()