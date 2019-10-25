#Author: Ian Gifford
#Project: Should I Dodge?
#For those high-elo players who dodge to avoid L's, this will help give a less subjectiv answer on whether or not you should dodge.
import requests
import json
from bs4 import BeautifulSoup


#Not currently working. It seems league data sites like to load their data from javascript, meaning it can't be scraped
#like this. Looking for an endpoint instead by reverse engineering the javscript as well as contacting the sites.
#champ: champion name to get data on
#lane: lane name to get data for that champ in
def scrape(champ,lane):
    url = "https://u.gg/lol/champions/"+champ+"/matchups?role="+lane
    print(url)
    r = requests.get(url)
    print(r.content)
    soup = BeautifulSoup(r.content,'lxml')
    slots = soup.find_all('div')
    for thing in slots:
        print(thing)


scrape("kai'sa","top")
