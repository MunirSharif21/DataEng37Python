weekday_int = 6

match weekday_int:
    case 0:
        weekday = "Sunday"
    case 1:
        weekday = "Monday"
    case 2:
        weekday = "Tuesday"
    case 3:
        weekday = "Wednesday"
    case 4:
        weekday = "Thursday"
    case 5:
        weekday = "Friday"
    case 6:
        weekday = "Saturday"
    case _:
        weekday = None

weekday_int_dict = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday"
}

weekday = weekday_int_dict[1]
print(weekday)