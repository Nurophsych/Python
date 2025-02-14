# Program to read and print file contents twice

# Read the entire file and print it
#Using with makes sure that the file is properly closed when the block of code is finished
# You don't need to manually call file.close(), as it's done automatically when the block is exited.
with open('learning_python.txt', 'r') as file:
    contents = file.read()
    print(contents)
    
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Read the file into a list of lines, then loop over each line to print
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Strip newline characters
        
        
print()
print('10-2')
print()

# Replace "Python" with "C" in each line from the file

with open('learning_python.txt', 'r') as file:
    lines = file.readlines()

    # Replace 'Python' with 'C' in each line
    for line in lines:
        modified_line = line.replace('Python', 'C')
        print(modified_line.strip())  # Print the modified line


print()
print('10-3')
print()


# Simplified code using splitlines() directly in the loop

with open('learning_python.txt', 'r') as file:
    contents = file.read()

    # Loop directly over splitlines()
    for line in contents.splitlines():
        print(line.strip())  # Print each line without extra newline characters
