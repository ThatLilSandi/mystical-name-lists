loc = open("planet-loc.txt", "w")
com = open("planet-com.txt", "w")

prefixes = ["Granite", "Basalt", "Pumice", "Scoria", "Tuff", "Chalk", "Claystone", "Flint", "Marl", "Marble" ,"Skarn", "Slate"]
suffixes = ["Barony", "County", "Duchy", "Earldom", "March", "Manor"]

com.write("\t\t\tnames = {\n")
com.write("\t\t\t\t")

for prefix in prefixes:
	for suffix in suffixes:
		var = "MYSTICAL1_PLANET_" + prefix + suffix
		str = prefix + " " + suffix
		
		loc.write(" " + var + ":0 \"" + str + "\"\n")
		com.write(var + " ")

com.write("\n")
com.write("\t\t\t}")

loc.close()
com.close()