loc = open("ship-loc.txt", "w")
com = open("ship-com.txt", "w")
classes = ["corvette", "destroyer", "cruiser", "battleship", "titan", "colossus", "juggernaut", "science", "colonizer", "constructor", "transport", "military_station_small", "ion_cannon"]
prefixes = [["Lord", "Lady"],["Baron", "Baroness"],["Count", "Countess"],["Duke", "Duchess"],["King", "Queen"],["Prince", "Princess"],["Emperor", "Empress"],["Sire", "Madame"],["Laird"],["Sir", "Madam"],["Thane"],["Marquess", "Marchioness"],["Marcher Lord", "Marcher Lady"]]
suffixes = ["Copper", "Pewter", "Iron", "Nickel", "Tungsten", "Zinc", "Titanium", "Cobalt", "Silver", "Platinum", "Gold", "Tin", "Lead", "Aluminum"]

for shipClass in classes:
	com.write("\t\t" + shipClass + " = {\n")
	com.write("\t\t\t")
	for prefix in prefixes[classes.index(shipClass)]:
		for suffix in suffixes:
			var = "MYSTICAL1_SHIP_" + prefix.replace(" ", "") + "OF" + suffix
			str = prefix + " of " + suffix
			loc.write(" "+ var + ":0 \"" + str + "\"\n")
			com.write(var + " ")
	com.write("\n")
	com.write("\t\t}\n")
	com.write("\n")
loc.close()
com.close()