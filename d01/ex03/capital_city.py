import sys

states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def get_capital_city(state_name):
    if len(sys.argv) != 2:
        return
    state_abbreviation = states.get(state_name)
    if state_abbreviation is None:
        print("Unknown state")
        return
    capital_city = capital_cities.get(state_abbreviation)
    print(capital_city)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    get_capital_city(sys.argv[1])