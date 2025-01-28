usernames = ['admin', 'jaden', 'alex', 'emily', 'john']  # You can modify this list

# Loop through the list and greet each user
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
        
#5-9

usernames = [] 
# Check if the list is empty
if not usernames:
    print("We need to find some users!")
else:
    # Loop through the list and greet each user
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")

#5-10
current_users = ['alice', 'bob', 'charlie', 'dave', 'eve']

new_users = ['bob', 'John', 'Sally', 'ALICE', 'frank']

# Make a copy of current_users with all usernames in lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through the new_users list
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' has already been taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
        
#5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the list and print the proper ordinal ending
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
        
        
#5-12 NA

