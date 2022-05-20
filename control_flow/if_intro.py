"""
age = 13
with_parent = True
has_ticket = True

if age >= 15 or with_parent:
    print("You can watch this film")
elif age == 14 and has_ticket:  # else if
    print("Come back next year")
else:
    print("You cannot watch this film")
print("Back to the baseline. This will always run.")

film_rating = "12A"

if film_rating.lower() == "U":
    print("Should be suitable for audiences aged four years and over.")
elif film_rating.lower() == "PG":
    print("Suitable for general viewing")
elif film_rating.lower() == "12" or "12A":
    print("May contain material that is not generally suitable for children"
          " aged under 12. \nNo one younger than 12 may see a 12A film in a"
          " cinema unless accompanied by an adult.")
elif film_rating.lower() == "15":
    print("Media is suitable only for persons aged 15 or over.")
elif film_rating.lower() == "18":
    print("Media is suitable only for persons aged 18 or over.")
else:
    print("Film rating does not exist.")
"""

age = 17
has_ticket = True

if has_ticket:
    if age >= 15:
        print("You can see this film.")
    else:
        print("Come back when you're older.")
else:  # for when has_ticket is FALSE
    print("You need a ticket, go buy one.")
