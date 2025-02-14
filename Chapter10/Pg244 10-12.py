import json

filename = "favorite_number.json"

try:
    with open(filename, "r") as file:
        favorite_number = json.load(file)
    print(f"I know your favorite number! It’s {favorite_number}.")
except FileNotFoundError:
    favorite_number = input("Enter your favorite number: ")
    with open(filename, "w") as file:
        json.dump(favorite_number, file)
    print("Your favorite number has been stored.")
