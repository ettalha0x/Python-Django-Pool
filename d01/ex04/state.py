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

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    state_abbreviation = get_key_by_value(capital_cities ,sys.argv[1])
    if state_abbreviation is None:
        print("Unknown capital city")
    else:
        print(get_key_by_value(states, state_abbreviation))
