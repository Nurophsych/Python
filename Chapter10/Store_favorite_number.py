import json

favorite_number = input("Enter your favorite number: ")
filename = "favorite_number.json"

with open(filename, "w") as file:
    json.dump(favorite_number, file)

print("Your favorite number has been stored.")
