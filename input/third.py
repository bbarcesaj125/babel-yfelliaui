from second import validate, validate_string
from second import F_ERROR


if validate_string("yusuf"):
    print("Ok")

print("THIRD")
d = validate("Yusuf47 Felly")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)
