rental_car = input("What kind of rental car would you like? ")

print(f"Let me see if I can find you a {rental_car}.")
 
print('7-2') #

# Ask the user for the number of people in their dinner group
group_size = int(input("How many people are in your dinner group? "))

# Check if the group size is more than 8
if group_size > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")
    
print('7-3') #

# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is a multiple of 10
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")


