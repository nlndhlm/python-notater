# EKSEMPEL 1:
# generere liste med tall fra 0 til 19:
tall = [x for x in range(0, 20)]

print(tall)



# EKSEMPEL 2:
# generere liste med partall fom 0 til men ikke med 20
partall = [x for x in range(0, 20) if x %2 == 0]

print(partall)