# det er egentlig stjerna * som er viktig her, ikke ordet args
# vi kan altså bruke hvilket som helst annet navn enn 'arg' etter stjerna

# stjerna gjør at vi ikke trenger å spesifisere antallet argumenter vi gir til funksjonen på forhånd

def pluss(*args):

    sum = 0

    for arg in args:
        sum = sum + arg
    
    print(sum)

pluss(1,2,3,4,5)

