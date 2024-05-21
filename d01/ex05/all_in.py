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

def is_state_exist(state_name):
    for state in states:
        if state == state_name:
            return True
    return False


def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val.lower() == value.lower():
            return key
    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    expressions = sys.argv[1].split(",")
    for expression in expressions:
        expression = expression.strip()
        if expression == "":
            continue
        if is_state_exist(expression):
            print(f"{expression} is a state")
        elif get_key_by_value(capital_cities, expression) is not None:
            print(f"{expression} is the capital of {get_key_by_value(states, get_key_by_value(capital_cities, expression))}")
        else:
            print(f"{expression} is neither a capital city nor a state")
