import json

filename = "user_info.json"

try:
    with open(filename, "r") as file:
        user_data = json.load(file)
    print("\nHere’s what I remember about you:")
    for key, value in user_data.items():
        print(f"{key.capitalize()}: {value}")
except FileNotFoundError:
    user_data = {}
    user_data["name"] = input("Enter your name: ")
    user_data["age"] = input("Enter your age: ")
    user_data["favorite_color"] = input("Enter your favorite color: ")

    with open(filename, "w") as file:
        json.dump(user_data, file)

    print("Your information has been stored.")
