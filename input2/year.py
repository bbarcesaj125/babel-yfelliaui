import datetime


def validate_year(user_input):
    year = user_input
    now = datetime.datetime.now()
    year_now = now.year
    # print(year)
    # print(str(year)[:2])
    # print(len(str(year)))
    form = ""
    print(len(str(year)))
    print(str(year)[:2])

    if len(str(year)) == 4:
        if str(year)[:2] == 19:
            form += "19XX"
            print(form)
        elif str(year)[:2] == 20:
            form = "20XX"
        else:
            form = "Unknown"
    elif len(str(year)) == 2:
        form = "XX"
        print(form)
    else:
        form = "Unknown"

    return form


validate_year(197440)

