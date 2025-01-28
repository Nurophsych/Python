# Dictionary storing programming words and their meanings
glossary = {
    'variable': 'A reserved memory location to store values.',
    'function': 'A block of code that only runs when it is called.',
    'loop': 'A block of code that repeats as long as a specified condition is met.',
    'list': 'An ordered collection of elements that can hold different types of data.',
    'dictionary': 'A collection of key-value pairs, where each key is unique.',
    'string': 'A sequence of characters.',
    'integer': 'A whole number, positive or negative, without decimals.',
    'boolean': 'A data type that can have one of two values: True or False.',
    'tuple': 'An ordered collection of elements, similar to a list, but immutable.',
    'set': 'An unordered collection of unique elements.'
}

# Loop through the dictionary and print each word and its meaning
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n    {meaning}\n")


#6-5
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.\n")

print("Rivers in the dictionary:")
for river in rivers.keys():
    print(river)

print("\nCountries in the dictionary:")
for country in rivers.values():
    print(country)
    
#6-6
# Dictionary of people and their favorite languages
favorite_languages = {
    'Alice': 'Python',
    'Bob': 'JavaScript',
    'Charlie': 'Ruby'
}

# List of people who should take the poll (including some who have already responded)
people_to_poll = ['Alice', 'Bob', 'David', 'Eve', 'Charlie', 'Frank']

# Loop through the list of people to poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for responding, {person}!")
    else:
        print(f"Hi {person}, please take our favorite languages poll!")

