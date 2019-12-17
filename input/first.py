fullname = input("Please enter your first and last names:")

print(fullname)

names = fullname.split(" ")
print(names)
print(type(names))
print(len(names))

input_length = len(names)
print(input_length)

if input_length == 2:
    print("First name " + names[0] + " Last name: " + names[1])
elif input_length == 3:
    print(f"First name {names[0]}, Middle {names[1]} Last name {names[1]}")
elif input_length == 1:
    print("Last name only: " + names[0])
else:
    print("Format: First name <Middle> Last name")
    print(names[3:])
    print("What to do with: " + " ".join(names[3:]))


length = len(names)

for item in range(length):
    names[item] = str(item) + ") " + names[item]

print(names)
