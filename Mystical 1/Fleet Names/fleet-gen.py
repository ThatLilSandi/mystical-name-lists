com = open("fleet-com.txt", "w")
loc = open("fleet-loc.txt", "w")

gems = ["Sapphire", "Amethyst", "Emerald", "Ruby", "Garnet", "Topaz", "Lapis Lazuli", "Turquoise", "Agate", "Opal", "Beryl", "Obsidian", "Jasper"]

com.write("\t\trandom_names = {\n")
com.write("\t\t\t")

for gem in gems:
	var = "MYSTICAL1_FLEET_" + gem + "Robe"
	str = gem + " " + "Robe"
	
	loc.write(" " + var + ":0 " + "\"" + str + "\"\n")
	com.write(var + " ")

com.write("\n")
com.write("\t\t}\n")
com.write("\t\tsequential_name = MYSTICAL1_xxFLEET_ORD\n")

loc.write(" MYSTICAL1_xxFLEET_ORD:0 \"$0$ Robe\"\n")

com.close()
loc.close()