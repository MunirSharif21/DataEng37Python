# Dictionary (Key:Value Pairs)
"""
data_eng_37 = {
    "course_name": "Data Engineering 37",
    "client": "Home Office",
    "trainer": {
        "name": "David Harvey",
        "energy_levels": "low"
    }
}

print(data_eng_37, type(data_eng_37))
print(data_eng_37["client"])  # get value for the client key

# data_eng_37["trainer"] = "David Harvey"  # alter the value for the trainer key
data_eng_37["trainees"] = ["Munir", "Darnell", "Abhiram", "Ahmed"]
print(data_eng_37)

print(data_eng_37["trainer"]["energy_levels"])
print(data_eng_37.get("course_name"))

print(data_eng_37.get("missing_key"))
# print(data_eng_37["missing_key"])  # fail nosily with error

print(bool(data_eng_37.get("is this key here?")))
data_eng_37.update({"course_length": "8 weeks"})
print(data_eng_37)
"""

# MAKE A DICTIONARY FOR YOUR FAVOURITE THINGS (FILMS, CARS ETC)
film = {
    "film_title": "The Shawshank Redemption",
    "release_year": 1991,
    "favourite": False,
    "actor": {
        "name": "Morgan Freeman",
        "age": 84,
        "test": {
            "something": "Hello!"
        }
    }
}

print(bool(film.get("The Shawshank Redemption")))
film.update({"age": 30})
print(film["actor"]["age"])
print(film["actor"]["test"]["something"])

me = {'name': 'Munir', 'age': 22}
print(me)
print(type(me['name']))
print(type(me['age']))
print(f'{me["name"]}')
print(f'My name is {me["name"]} and I am {me["age"]} years old.')

mcu = {"Iron Man", "Thor", "Captain America", "Hulk"}
print(mcu, type(mcu))  # type is a set
# there is no order in a set, so running print on it will output in a different order every time

fs = frozenset(mcu)
# find out more about frozen sets
