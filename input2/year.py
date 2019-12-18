import datetime

""" This is a simple python program that calculates the age based on user input. """


def display_year(input_display):
    """ This is the main function that displays the calculated age based on the value entered by the
    user. """

    dic_values = calculate_year(input_display)
    if dic_values["error"]:
        print(dic_values["error"])
    else:
        print(
            "You are "
            + str(dic_values["nb_years"])
            + " years old"
            + ", and you were born in the "
            + str(dic_values["century"])
            + " century!"
        )


def calculate_year(input_year):
    """ This function is where the actual calculations are made.
    Before doing any calculations it calls validate_year() to verify the entered values. """

    now = datetime.datetime.now()
    year_now = now.year
    year_now_trimmed = str(year_now)[2:]
    # print(year_now_trimmed)

    dic = {}
    dic["error"] = ""

    form = validate_year(input_year)
    # print(form)

    if form != "Malformed input!":

        if len(form) == 4:
            dic["nb_years"] = now.year - int(input_year)

            if form == "19XX":
                dic["nb_years"] = now.year - input_year
                dic["century"] = "20th"
            elif form == "20XX":
                dic["nb_years"] = now.year - input_year
                dic["century"] = "21st"

            elif form == "XXXX":
                dic["nb_years"] = now.year - int(input_year)
                dic["century"] = int(str(input_year)[:2]) - 1
            else:
                dic["error"] = "Error"

        elif form == "XX":
            if int(year_now_trimmed) <= int(input_year):
                converted = int("19" + str(input_year))
                dic["nb_years"] = now.year - converted
                dic["century"] = "20th"
                # print(nb_years)
            else:
                converted = int("20" + str(input_year))
                dic["nb_years"] = now.year - converted
                dic["century"] = "21th"
        else:
            dic["error"] = "Input either too long or too short!!"
    else:
        dic["error"] = form

    return dic


def validate_year(user_input):
    """ This functions takes in the user input and verify it according to a set of criteria. """

    year = str(user_input)
    # print(year)
    # print(str(year)[:2])
    # print(len(str(year)))
    form = ""
    # print(len(str(year)))
    # print(str(year)[:2])

    if year.isdigit():

        if len(year) == 4:
            if (year)[:2] == "19":
                form = "19XX"
            elif (year)[:2] == "20":
                form = "20XX"
            else:
                form = "XXXX"
        elif len(year) == 2:
            form = "XX"
        else:
            form = "Unknown"
        # print(form)
    else:
        # Showing an error if the entered string contains letters
        try:
            int(year)
        except:
            form = "Malformed input!"

    return form


if __name__ == "__main__":
    display_year(74)
