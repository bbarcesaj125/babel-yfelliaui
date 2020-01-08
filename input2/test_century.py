# import datetime


def calculate_century():
    user_input = input("Enter a date in YYYY-MM-DD format: ")
    year, month, day = map(str, user_input.split("-"))
    form = validate_year(user_input)
    century = ""

    if form == "YYYY":
        if year[-2:] == "00":
            century = int(year[:2])
        else:
            century = int(year[:2]) + 1
    elif form == "YYY":
        if year[-2:] == "00":
            century = int(year[:1])
        else:
            century = int(year[:1]) + 1

    elif form == "YY" or form == "Y":
        century = 1

    print(century)


def validate_year(user_input):
    # user_input = input("Enter a date in YYYY-MM-DD format: ")
    year, month, day = map(str, user_input.split("-"))
    form = ""

    if len(year) == 4:
        form = "YYYY"
    elif len(year) == 3:
        form = "YYY"
    elif len(year) == 2:
        form = "YY"
    elif len(year) == 1:
        form = "Y"
    else:
        form = "Error"
    return form


if __name__ == "__main__":
    calculate_century()
