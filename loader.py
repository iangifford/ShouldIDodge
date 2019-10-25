#Author: Ian Gifford
#Project: Should I Dodge?
#For those high-elo players who dodge to avoid L's, this will help give a less subjectiv answer on whether or not you should dodge.
import json
class loader:
    champs = []

    #Loads the list of champions from the config file
    def loadChamps(self):
        self.champs = ['']
        f = open("configs/champions.txt")
        for line in f.readlines():
            self.champs.append(line.strip())
        f.close()
    #Outside access source for getting the list of champs. Just makes sure the list of champions
    #isn't built from the file multiple times as that would be unnecessary
    def getChamps(self):
        if len(self.champs) == 0:
            self.loadChamps()

        return self.champs

    #Returns how each lane is weighted. Weeee, shifting meta and unbalanced lane priority.
    def getLaneWeights(self):
        f = open("configs/lane_weights.txt","r")
        weights = []
        for line in f.readlines():
            weights.append(float(line))
        return weights
    #Gets the constants for the various algorithms.
    def getAlgorithmConstants(self):
        f = open('configs/config.txt', "r")
        data = json.load(f)
        return data['algorithm constants']
