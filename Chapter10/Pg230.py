# 10-4: Guest: Write a program that prompts the user for their name
# and writes their name to a file called guest.txt.

name = input("What is your name? ")
with open('Guest.txt', 'w') as file:
    file.write(name)

print(f"Thank you, {name}! Your name has been written to guest.txt.")

# 10-5: Guest Book: Write a while loop that prompts users for their name.
# Collect all the names and write them to a file called guest_book.txt.

while True:
    name = input("What is your name acally wag tell us or quit!!")
    if name.lower() == 'quit':
        break
    with open('Guest_list.txt', 'a') as file:  # 'a' mode to append new names
        file.write(name + '\n')

print("Thank you for visiting! All names have been written to Guest_list.txt.")