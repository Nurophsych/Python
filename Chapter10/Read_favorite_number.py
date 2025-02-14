import json

filename = "favorite_number.json"

try:
    with open(filename, "r") as file:
        favorite_number = json.load(file)
    print(f"I know your favorite number! It’s {favorite_number}.")
except FileNotFoundError:
    print("No favorite number found. Please run the first program to store one.")
