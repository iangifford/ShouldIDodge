#Author: Ian Gifford
#Project: Should I Dodge?
#For those high-elo players who dodge to avoid L's, this will help give a less subjectiv answer on whether or not you should dodge.
import json
from loader import loader
import math
#Calculates and returns the lane and game winrates. In more advanced iterations, this will have winrates involving each
#lane and return a singular percentage per lane.
#blue: array of blue team champ names
#red: array of red team champ names
def basiccalc(blue, red):
    bluewins = []
    for item in blue:
        try:
            f = open("champion_data/" + item.strip() + ".json", "r")
            data = json.load(f)
            bluewins.append(str(data['primary_winrate_percent']))
            f.close()
        except:
            bluewins.append("Unknown")

    redwins = []
    for item in red:
        try:
            f = open("champion_data/" + item.strip() + ".json", "r")
            data = json.load(f)
            redwins.append(str(data['primary_winrate_percent']))
            f.close()
        except:
            redwins.append("Unknown")

    bluenums = []
    rednums = []
    for item in bluewins:
        if item == "Unknown":
            bluenums.append(50)
        else:
            bluenums.append(float(item))
    for item in redwins:
        if item == "Unknown":
            rednums.append(50)
        else:
            rednums.append(float(item))

    results = []
    results.extend(bluewins)

    results.append(algorithm_basic(bluenums, rednums))

    results.extend(redwins)
    return results

#The formula for calculating the likelihood of a team winning.
#Formula for magnifying win% is ln((power_base^winrate)/(power_base^50)) + 50.
#This formula was designed to best match the winrates to the outcomes of the sample game data set.
#blue_winrates: array of blue team winrates, as floats
#red_winrates: array of red team winrates, as floats
def algorithm_basic(blue_winrates, red_winrates):
    l = loader()
    weights = l.getLaneWeights()
    power_base = l.getAlgorithmConstants()['basic power_base']
    divisor = power_base**50
    for i in range(len(weights)):
        blue_winrates[i] = math.log((power_base**blue_winrates[i])/divisor)+50
        red_winrates[i] = math.log((power_base**red_winrates[i])/divisor)+50
        blue_winrates[i] *= weights[i]
        red_winrates[i] *= weights[i]
    blue_tot = 0
    for item in blue_winrates:
        blue_tot += item

    red_tot = 0
    for item in red_winrates:
        red_tot += item

    total = blue_tot + red_tot

    return blue_tot / total
