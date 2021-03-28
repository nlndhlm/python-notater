points = {"a" : 1, "b" : 2}

def show_points(**kwargs):
    print(kwargs.items())

    for item in kwargs.items():
        print(item)

show_points(**points)
