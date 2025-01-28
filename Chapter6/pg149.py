# Dictionaries representing different people
person_1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person_2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person_3 = {
    'first_name': 'Sam',
    'last_name': 'Brown',
    'age': 35,
    'city': 'Chicago'
}

# List of people (each person is represented by a dictionary)
people = [person_1, person_2, person_3]

# Loop through the list of people and print everything about each person
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")
    
#6-8
# Dictionaries representing different pets
pet_1 = {
    'animal': 'dog',
    'owner': 'Alice'
}

pet_2 = {
    'animal': 'cat',
    'owner': 'Bob'
}

pet_3 = {
    'animal': 'parrot',
    'owner': 'Charlie'
}

pet_4 = {
    'animal': 'hamster',
    'owner': 'David'
}

# List of pets
pets = [pet_1, pet_2, pet_3, pet_4]

# Loop through the list of pets and print everything about each pet
for pet in pets:
    print(f"Animal: {pet['animal'].capitalize()}")
    print(f"Owner: {pet['owner']}\n")
    
#6-9
# Dictionary storing people's favorite places
favorite_places = {
    'Alice': ['Paris', 'Tokyo', 'New York'],
    'Bob': ['London', 'Sydney'],
    'Charlie': ['Rome', 'Barcelona', 'Tokyo']
}

# Loop through the dictionary and print each person's name and their favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"  - {place}")
    print()  # Blank line for better readability

#6-10
# Dictionary storing people's favorite numbers
favorite_numbers = {
    'Alice': [7, 12, 21],
    'Bob': [3, 15],
    'Charlie': [9, 18, 24],
}

# Loop through the dictionary and print each person's name and their favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f"  - {number}")
    print()  # Blank line for better readability

#6-11
# Dictionary storing information about cities
cities = {
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'Known as the "City that Never Sleeps."'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Home to the world\'s busiest railway station.'
    },
    'Paris': {
        'country': 'France',
        'population': 2148327,
        'fact': 'Famous for the Eiffel Tower and its art museums.'
    }
}

# Loop through the dictionary and print each city's name and information
for city, info in cities.items():
    print(f"City: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
    
#6-12
# Dictionary storing information about cities with additional details
cities = {
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'Known as the "City that Never Sleeps."',
        'year_established': 1624,
        'landmarks': ['Statue of Liberty', 'Central Park', 'Empire State Building'],
        'timezone': 'Eastern Standard Time (EST)'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Home to the world\'s busiest railway station.',
        'year_established': 1603,
        'landmarks': ['Shibuya Crossing', 'Tokyo Tower', 'Meiji Shrine'],
        'timezone': 'Japan Standard Time (JST)'
    },
    'Paris': {
        'country': 'France',
        'population': 2148327,
        'fact': 'Famous for the Eiffel Tower and its art museums.',
        'year_established': '3rd century BC',
        'landmarks': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral'], # type: ignore
        'timezone': 'Central European Time (CET)'
    }
}

# Loop through the dictionary and print each city's name and extended information
for city, info in cities.items():
    print(f"City: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")
    print(f"  Year Established: {info['year_established']}")
    print(f"  Famous Landmarks: {', '.join(info['landmarks'])}")
    print(f"  Timezone: {info['timezone']}\n")



