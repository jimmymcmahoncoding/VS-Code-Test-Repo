import os
from os import renames
import sys

import requests

print(sys.version)
print(sys.executable)

test_variable = 1

test_browser = "I am a new edit from the browser"

def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


name = input("Your Name?")
print("Hello,", name)


def new_function():
    print("I am a new function.")


new_function()

for i in range(1, 4):
    print(i)
