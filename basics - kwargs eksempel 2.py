

def show_info(**kwargs):
    for navn, nummer in kwargs.items():
        print(navn, nummer)

show_info(nicolai = 99887766, silje = 44332211)
