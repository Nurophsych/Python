person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

# Print each piece of information stored in the dictionary
print(f"First Name: {person['first_name']}")
print(f"Last Name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")


#6-2
favorite_numbers = {
    'Alice': 7,
    'Bob': 3,
    'Charlie': 12,
    'David': 5,
    'Eve': 8
}

# Print each person's name and their favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")


#6-3
# Dictionary storing programming words and their meanings
glossary = {
    'variable': 'A reserved memory location to store values.',
    'function': 'A block of code that only runs when it is called.',
    'loop': 'A block of code that repeats as long as a specified condition is met.',
    'list': 'An ordered collection of elements that can hold different types of data.',
    'dictionary': 'A collection of key-value pairs, where each key is unique.'
}

# Print each word and its meaning with a blank line between each pair
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n    {meaning}\n")
