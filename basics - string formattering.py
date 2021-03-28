navn = "Louie"

print("Hello {}".format(navn))



navneliste = ["Nicolai", "Silje"]

print("Hei, {} og {}".format(*navneliste))
print("Hei, {1} og {0}".format(*navneliste))

# såkalt f-string
print(f"Hallo, {navneliste[0]} og {navneliste[1]}!")
