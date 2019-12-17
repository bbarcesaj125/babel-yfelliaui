"""
SETUP
Changelog:
    - First test
    - Pending
"""
# My first program

import sys
import os
import datetime


def printseparator():
    """ Function to display a separator line """
    print("_" * 50)


a = "Hello World!"
print(a)  # Print a
printseparator()
print(sys.executable)
print(sys.platform)
print(sys.path)

print(sys.version_info)
v = sys.version_info
print(type(v))
print(dir(v))

# print(f'Python version {v.major}.{v.minor}.{v.micro}')
print("Python version {}.{}.{}".format(v.major, v.minor, v.micro))
print("Python version %s.%s.%s" % (v.major, v.minor, v.micro))

printseparator()
print("Env variable: " + os.getenv("PYTHONPATH", "Empty"))

printseparator()
print(datetime)
print(datetime.__file__)

dt = datetime.datetime.now()
print(f"Date & Time {dt} - Year {dt.year}")

printseparator()

help(printseparator)
