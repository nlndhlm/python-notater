# kwargs står for keyword arguments
# *kwargs gjør at funksjonen kan ta imot en dictionary eller annen iterabel med vilkårlig lengde som argument

info = {
    "navn" : "Nicolai",
    "alder" : 35,
    "favorittfarge" : "rosa",
    "bilmerke" : "VW"
}


def show_info(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())


# må kalles med to stjerner i argumentet:
show_info(**info)



