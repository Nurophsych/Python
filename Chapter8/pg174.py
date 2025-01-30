# Function to summarize a shirt's size and message
def make_shirt(size, message):
    print(f"The shirt size is {size} and the message on it is: {message}.")

# Call the function using positional arguments
make_shirt("Medium", "Python Rocks!")

# Call the function using keyword arguments
make_shirt(size="Large", message="I Love Coding!")










print('8-4')

# Function to make a shirt with default values for size and message
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message on it is: {message}.")

# Call the function with the default size and message (Large shirt with "I love Python")
make_shirt()

# Call the function with a medium shirt and the default message
make_shirt(size="Medium")

# Call the function with a custom message and a different size
make_shirt(size="Small", message="Hello World!")








print(8-5)
# Function to describe a city with its country
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Call the function for three cities
describe_city("Reykjavik")  # Default country is Iceland
describe_city("Paris", "France")  # Custom country
describe_city("Tokyo", "Japan")  # Custom country
