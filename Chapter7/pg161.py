# Start an infinite loop to prompt for pizza toppings
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    # Check if the user wants to quit
    if topping.lower() == 'quit':
        break
    
    # Print a message confirming the topping will be added
    print(f"Adding {topping} to your pizza.")

print("Your pizza is ready!")

print('7-5')

# Loop to keep asking for age and displaying ticket price
while True:
    # Ask the user for their age
    age = int(input("Please enter your age (or enter '0' to exit): "))

    # Check if the user wants to exit the program
    if age == 0:
        print("Thank you for using the movie ticket service!")
        break

    # Determine the ticket price based on age
    if age < 3:
        ticket_price = 0  # Free ticket for ages under 3
    elif 3 <= age <= 12:
        ticket_price = 10  # $10 ticket for ages between 3 and 12
    else:
        ticket_price = 15  # $15 ticket for ages over 12

    # Print the ticket price
    print(f"The ticket price for someone who is {age} years old is ${ticket_price}.")

print('7-6') #v1
# Loop to ask for age until a certain condition is met
age = None  # Initialize the age variable
while age != 'quit':
    age = input("Please enter your age (or type 'quit' to exit): ")
    
    # Check if user wants to exit
    if age.lower() == 'quit':
        print("Thank you for using the movie ticket service!")
        break

    # Check if the input is a valid number
    if age.isdigit():
        age = int(age)  # Convert to integer
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        print(f"The ticket price for someone who is {age} years old is ${ticket_price}.")
    else:
        print("Please enter a valid age or 'quit'.")
#v2
# Loop controlled by an active variable
counter = 0  # Active variable controlling loop
max_attempts = 5  # Max number of attempts

while counter < max_attempts:
    age = input("Please enter your age (or type 'quit' to exit): ")
    
    if age.lower() == 'quit':
        print("Thank you for using the movie ticket service!")
        break

    if age.isdigit():
        age = int(age)
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        print(f"The ticket price for someone who is {age} years old is ${ticket_price}.")
    else:
        print("Please enter a valid age or 'quit'.")
    
    counter += 1  # Increment the active variable

if counter == max_attempts:
    print(f"You've reached the maximum number of attempts ({max_attempts}).")
#v3
# Loop with a break statement to exit on 'quit'
while True:
    age = input("Please enter your age (or type 'quit' to exit): ")

    if age.lower() == 'quit':
        print("Thank you for using the movie ticket service!")
        break  # Exit the loop if 'quit' is entered

    if age.isdigit():
        age = int(age)
        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15
        print(f"The ticket price for someone who is {age} years old is ${ticket_price}.")
    else:
        print("Please enter a valid age or 'quit'.")

print("7-7")

var1 = True

while var1 == True:
    print(var1)
