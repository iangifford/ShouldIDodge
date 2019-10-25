# Author: Ian Gifford
# Project: Should I Dodge?
# For those high-elo players who dodge to avoid L's, this will help give a less subjectiv answer on whether or not you should dodge.



#This is just a crap convenience file for manually inputting data while I still work out the webscraper.
#Currently, I either need to find a source that doesn't block webscraping by having the information be loaded
#by javascript, or to find an endpoint that I can access directly for the data.
import json
for champion in open("configs/champions.txt","r").readlines():
    built_data = {"primary_winrate_percent":0,"matchups_top":None,"matchups_jungle":None,"matchups_mid":None,"matchups_adc":None,"matchups_support":None}
    print(champion)
    built_data["primary_winrate_percent"] = float(input())
    out = open("champion_data/"+champion+".json","w+")
    json.dump(built_data,out)
    out.close()


