# en class kan ses på som oppskriften på et objekt
# når vi kaller class opprettes et tilfelle av objektet

class Customer:

    # denne kjøres hver gang det lages en ny Customer:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def greet(self):
        print("Hei", self.name)

    # methods MÅ ha et parameter
    def message(tilfeldig_parameternavn):
        print("Dette er en beskjed")


# lager et Customer-objekt:
c1 = Customer("Jacob", 98765432)

print(c1.name)
print(c1.number)

# greet() og message() er methods
c1.greet()
c1.message()