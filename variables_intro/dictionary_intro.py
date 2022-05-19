# Dictionary (Key:Value Pairs)

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

# TASK FOR TOMORROW
# MAKE A DICTIONARY FOR YOUR FAVOURITE THINGS (FILMS, CARS ETC)
