import os
from os import renames


import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


name = input("Your Name?")
print("Hello,", name)
