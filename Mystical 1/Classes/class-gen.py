loc = open("class-loc.txt", "w")
com = open("class-com.txt", "w")
minerals = open("minerals.txt", "r")

classes = []
for line in minerals:
	classes.append(line.strip())

com.write("\t\tgeneric = {\n")
com.write("\t\t\t")
for shipClass in classes:
    var = "MYSTICAL1_CLASS_" + shipClass
    str = shipClass
    loc.write(" " + var + ":0 \"" + str + "\"\n")
    com.write(var + " ")
    
com.write("\n")
com.write("\t\t}\n")

loc.close()
com.close()