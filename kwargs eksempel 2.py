

def show_info(**kwargs):
    for navn, nummer in kwargs.items():
        print(navn, nummer)

show_info(nicolai = 97426020, silje = 95868014)