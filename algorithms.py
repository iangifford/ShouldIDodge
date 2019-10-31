# Author: Ian Gifford
# Project: Should I Dodge?
# For those high-elo players who dodge to avoid L's, this will help give a less subjectiv answer on whether or not you should dodge.
import json
from loader import loader
import math
from scrape import get_champ_keys, sanitize_champ

riot_order_to_ugg_order = {0: "4", 1: "1", 2: "5", 3: "3", 4: "2"}


# Calculates and returns the lane and game winrates. In more advanced iterations, this will have winrates involving each
# lane and return a singular percentage per lane.
# blue: array of blue team champ names
# red: array of red team champ names
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


# Calculates and returns the lane and game winrates. In more advanced iterations, this will have winrates involving each
# lane and return a singular percentage per lane.
# blue: array of blue team champ names
# red: array of red team champ names
def advancedcalc(blue, red):
    champkeys = get_champ_keys()
    redkeys = []

    for champ in red:
        redkeys.append(champkeys[sanitize_champ(champ)])

    bluewins = []

    for i in range(5):
        item = blue[i]
        ugg_lane = riot_order_to_ugg_order[i]
        #try:
        f = open("champion_data/" + item + ".json", "r")
        data = json.load(f)
        lane_matchups = data["matchups"][ugg_lane]
        found = False
        for set in lane_matchups:
            print(redkeys[i])
            print(set[0])
            if set[0] == int(redkeys[i]):
                found = True
                print("found!")
                enemywins = float(set[1])
                games = float(set[2])
                if games > 25:

                    bluewins.append(100*(1-(enemywins/games)))
                else:
                    found = False
        if not found:
            print("matchup not found!",ugg_lane, redkeys[i])
            bluewins.append(float(data["lane_winrates"][ugg_lane]))
        f.close()
    #except Exception as e:
        #print(e)


    bluenums = []
    for item in bluewins:
        if item == "Unknown":
            bluenums.append(50)
        else:
            bluenums.append(float(item))

    results = []
    rednums = [50,50,50,50,50]
    redwins = ["50","50","50","50","50"]
    results.extend(bluewins)

    results.append(algorithm_basic(bluenums, rednums))

    results.extend(redwins)
    #print(results)
    return results


# The formula for calculating the likelihood of a team winning.
# Formula for magnifying win% is ln((power_base^winrate)/(power_base^50)) + 50.
# This formula was designed to best match the winrates to the outcomes of the sample game data set.
# blue_winrates: array of blue team winrates, as floats
# red_winrates: array of red team winrates, as floats
def algorithm_basic(blue_winrates, red_winrates):
    l = loader()
    weights = l.getLaneWeights()
    power_base = l.getAlgorithmConstants()['basic power_base']
    divisor = power_base ** 50
    for i in range(len(weights)):
        blue_winrates[i] = math.log((power_base ** blue_winrates[i]) / divisor) + 50
        red_winrates[i] = math.log((power_base ** red_winrates[i]) / divisor) + 50
        blue_winrates[i] *= weights[i]
        red_winrates[i] *= weights[i]
    blue_tot = 0
    for item in blue_winrates:
        blue_tot += item

    red_tot = 0
    for item in red_winrates:
        red_tot += item

    total = blue_tot + red_tot

    return 100*blue_tot / total
