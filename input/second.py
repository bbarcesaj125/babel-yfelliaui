import re


F_FIRST = "first_name"
F_LAST = "last_name"
F_MIDDLE = "middle_name"
F_FULL = "full_name"
F_ERROR = "error"


def validate_string(input):
    # Verify if empty
    # Remove spaces
    # Uppercases or Lowercases
    if not len(input):
        return False
    r = re.match("^[A-Za-z]+$", input)
    print(r)
    return True if r else False


def manage_input():
    input_fullname = input("Please enter your first and last names:")
    print(input_fullname)
    validate(input_fullname)


def validate(input_list):
    """ Function to validate user input """

    names = input_list.split(" ")
    print(names)
    print(type(names))
    print(len(names))

    input_length = len(names)
    print(input_length)
    type(names)
    for n in names:
        # Remove spaces
        n = n.strip()
        if not validate_string(n):
            # Error
            return {F_ERROR: "Validation error " + n}

    dic = {}

    if input_length == 2:
        # print("First name " + names[0] + " Last name: " + names[1])
        dic[F_FIRST] = names[0]
        dic[F_LAST] = names[1]
        dic[F_FULL] = names[0] + " " + names[1]
        print(dict)
    elif input_length == 3:
        dic[F_FIRST] = names[0]
        dic[F_MIDDLE] = names[1]
        dic[F_LAST] = names[2]
        dic[F_FULL] = names[0] + " " + names[1] + " " + names[2]
        print(dict)
        # print(f"First name {names[0]}, Middle {names[1]} Last name {names[1]}")
    elif input_length == 1:
        # print("Last name only: " + names[0])
        dic[F_LAST] = names[0]
        print(dict)
    else:
        error = "Format: First name <Middle> Last name"
        if input_length == 0:
            error += " <<< Input is empty!"
        else:
            error += "What to do with: " + " ".join(names[3:])
        # print(names[3:])
        # print("What to do with: " + " ".join(names[3:]))
        dic[F_ERROR] = error
        print(dict)
    return dict


if __name__ == "__main__":
    manage_input()
