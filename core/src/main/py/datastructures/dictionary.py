# dictionary data structure: a collection of relationship pair

province_capitals = {
    "Quebec": "Québec City",
    "Ontario": "Toronto",
    "Newfoundland and Labrador": "St. John’s",
    "Prince Edward Island": "Charlottetown",
    "Nova Scotia": "Halifax",
    "New Brunswick": "Fredericton",
    "Manitoba": "Winnipeg",
    "Saskatchewan": "Regina",
    "Alberta": "Edmonton",
    "British Columbia": "Victoria",
    "Nunavut": "Iqaluit",
    "Northwest Territories": "Yellowknife",
    "Yukon Territory": "Whitehorse"
}

print("there are " + str(len(province_capitals)) + " provinces or territories.")
for p in province_capitals.keys():
    print(p + "'s capital is " + province_capitals[p])
