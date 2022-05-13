import random

random.seed(2)
loc = open("character-loc.txt", "w")
com = open("character-com.txt", "w")


nouns = ["Eyes", "Friends", "Sun", "Ruler", "Hand", "Fear", "Dawn", "Eventide", "Scent", "Trouble", "Grace"]
verbs = [ "Looks", "Thinks", "Strikes", "Hides", "Swims", "Moves", "Shimmers", "Smells", "Fetches", "Has", "Fears", "Brings", "Holds", "Summons", "Fights", "Defends", "Drift", "Laughs", "Pursues"]
adjectives = ["Smooth", "Rough", "Kind", "Humble", "Graceful", "Persistant", "Lost"]
prefixes = [nouns, verbs, adjectives]

forNouns = ["of", "in", "with", "above", "before", "from"]
forVerbs = ["to", "through", "with", "after", "by"]
forAdjectives = ["as", "like", "beside", "toward", "without"]
preps = [forNouns, forVerbs, forAdjectives]

suffixes = ["Gold", "the Dawn", "Darkness", "the End", "Foundations", "Beginning", "Silver", "Kings", "Queens", "the Found", "Stone", "Gems", "the Prepared", "those who Seek", "all who Find", "the Flame"]

nameVar = []
nameStr = []

for (prefixList, prepList) in zip(prefixes, preps):
	for prefix in prefixList:
		for prep in prepList:
			for suffix in suffixes:
				if(random.randrange(10) == 0):
					nameVar.append("MYSTICAL1_CHR_" + prefix + prep + suffix.replace(" ", ""))
					nameStr.append(prefix + " " + prep + " " + suffix)



com.write("\t\t\tfull_names = {\n")
com.write("\t\t\t\t")
for name in nameVar:
	com.write(name + " ")
	
com.write("\n")
com.write("\t\t\t}\n")
com.write("\n")
com.write("\t\t\tregnal_full_names = {\n")
com.write("\t\t\t\t")
for name in nameVar:
	com.write(name + " ")
	
com.write("\n")
com.write("\t\t\t}\n")

for (var, str) in zip(nameVar, nameStr):
	loc.write(" " + var + ":0 \"" + str + "\"\n")

loc.close()
com.close()