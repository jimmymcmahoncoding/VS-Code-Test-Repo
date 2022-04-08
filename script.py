import math
import os
import sys
from os import renames


import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


print(greet("World"))
print(greet("Jimmy"))
r = requests.get("https://www.google.com")
print(r.status_code)


name = input("Your Name?")
print("Hello,", name)
