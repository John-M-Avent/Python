## Python Homework Extra: Colors
# John M. Avent 
# ENG 101-06 
# 5/1/2017 
# 
Names = ['black', 'white', 'red', 'blue', 'yellow', 'orange', 'green']              # Names of colors. 
HexCodes = ['000000', 'FFFFFF', 'FF0000', '0000FF', 'FFFF00', 'FFA500', '008000']   # Hex codes of colors. 
ColorDictionary = {}                                                                # Blank dictionary. 
for Name, Hex in zip(Names,HexCodes):                                               # Goes through both list simultaneously one item at a time. 
    ColorDictionary[Name] = Hex                                                     # Name is the dictionary key, Hex is the dictionary value. 
print (ColorDictionary)                                                             # Prints the dictionary. 
