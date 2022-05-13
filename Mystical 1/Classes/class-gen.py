loc = open("class-loc.txt", "w")
com = open("class-com.txt", "w")

classes = ["Azurite", "Adamite", "Apatite", "Boleite", "Brookite", "Celestite", "Cryolite", "Dolomite", "Forsterite", "Gahnite", "Goethite", "Howlite", "Leucite", "Painite", "Pyrite", "Selenite", "Sphalerite", "Thaumasite", "Witherite", "Zultanite"]

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