import json

filename = "username.json"

#function is made
def get_new_username():
    username = input("Enter your name: ")#collect input
    with open(filename, "w") as file:#specifies to write
        json.dump(username, file)#dumps it into a json file
    return username

try:
    with open(filename, "r") as file:#to read
        stored_username = json.load(file)

    confirm = input(f"Is your name {stored_username}? (yes/no): ").strip().lower()
    if confirm == "yes":
        print(f"Welcome back, {stored_username}!")
    else:
        new_username = get_new_username()
        print(f"Your name has been updated. Welcome, {new_username}!")
except FileNotFoundError:
    new_username = get_new_username()
    print(f"Welcome, {new_username}!")
