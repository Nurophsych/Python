# Function to create a sandwich order
def make_sandwich(*items):
    print("Making a sandwich with the following ingredients:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!\n")

# Calling the function with different numbers of arguments
make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "tomato", "avocado", "mayo")
make_sandwich("chicken", "pickles")


print('8-13')
# Function to build a user profile
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Creating a profile for myself
my_profile = build_profile('John', 'Doe', location='New York', age=25, occupation='Software Developer')

# Printing the profile
print(my_profile)





print('8-14')
# Function to store car information
def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Creating a car dictionary with additional information
car = make_car('Subaru', 'Outback', color='blue', tow_package=True)

# Printing the car dictionary
print(car)






