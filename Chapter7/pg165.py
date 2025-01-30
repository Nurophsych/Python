# List of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'veggie', 'turkey', 'ham']

# Empty list to store finished sandwiches
finished_sandwiches = []

# Loop through each sandwich in the sandwich_orders list
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    
    # Move the sandwich to the finished_sandwiches list
    finished_sandwiches.append(sandwich)

# Print the list of finished sandwiches
print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")


print("7-9")

# List of sandwich orders, with 'pastrami' appearing multiple times
sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami', 'turkey', 'ham']

# Empty list to store finished sandwiches
finished_sandwiches = []

# Print message about pastrami being unavailable
print("The deli has run out of pastrami!\n")

# Use a while loop to remove all 'pastrami' sandwiches from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through each sandwich in the sandwich_orders list
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    
    # Move the sandwich to the finished_sandwiches list
    finished_sandwiches.append(sandwich)

# Print the list of finished sandwiches
print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")

print('7-10')
# Empty dictionary to store the poll results
vacation_poll = {}

# Collect responses from users
while True:
    # Prompt user for their name and dream vacation destination
    name = input("What is your name? (or type 'quit' to exit): ")
    
    if name.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'
    
    vacation_spot = input(f"Hi {name}, if you could visit one place in the world, where would you go? ")
    
    # Store the response in the dictionary
    vacation_poll[name] = vacation_spot      #comment this out <<<<<<<<<<

# Print the poll results
print("\n--- Vacation Poll Results ---")
for name, vacation_spot in vacation_poll.items():
    print(f"{name} would like to visit {vacation_spot}.")
