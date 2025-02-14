try:
    # Prompt for two numbers
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    # Convert inputs to integers and perform the addition
    result = int(num1) + int(num2)
    
    # Print the result
    print(f"The sum of {num1} and {num2} is: {result}")
    
except ValueError:
    print("Oops! Please enter valid numbers.")


#10-7

while True:
    try:
        # Prompt for two numbers
        num1 = input("Enter the first number (or 'quit' to exit): ")
        if num1.lower() == 'quit':
            break
        num2 = input("Enter the second number: ")
        
        # Convert inputs to integers and perform the addition
        result = int(num1) + int(num2)
        
        # Print the result
        print(f"The sum of {num1} and {num2} is: {result}")
    
    except ValueError:
        print("Oops! Please enter valid numbers.")
        
        
        
#10-8

    
try:
    with open('cats.txt', 'r') as cats_file:
        print("Cats:")
        for line in cats_file:
            print(line.strip())
    
    with open('dogs.txt', 'r') as dogs_file:
        print("Dogs:")
        for line in dogs_file:
            print(line.strip())

except FileNotFoundError:
    print("One of the files is missing. Please check the file paths and try again.")
    
    
#10-9

try:
    with open('cats.txt', 'r') as cats_file:
        print("Cats:")
        for line in cats_file:
            print(line.strip())
    
    with open('dogs.txt', 'r') as dogs_file:
        print("Dogs:")
        for line in dogs_file:
            print(line.strip())

except FileNotFoundError:
    pass  # Fail silently, no message is printed



10-10
    
# Open the file and read its content
try:
    with open('Movie.txt', 'r') as file:
        text = file.read().lower()  # Convert to lowercase for case-insensitive counting
    
    # Count occurrences of the word 'the '
    word_count = text.count('rat ')
    
    print(f"The word 'rat' appears {word_count} times in the text.")
except FileNotFoundError:
    print("The specified text file was not found.")


