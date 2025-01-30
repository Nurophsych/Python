# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left. Move each design to
    completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)





print("8-16")
# greetings.py

def say_hello(name):
    """Print a greeting."""
    print(f"Hello, {name}!")
    
    
    #method2
# main_program.py

# Importing the entire module
import greetings
greetings.say_hello('Alice')

# Importing a specific function from the module
from greetings import say_hello
say_hello('Bob')

# Importing a function with an alias
from greetings import say_hello as greet
greet('Charlie')

# Importing the module with an alias
import greetings as greet_module
greet_module.say_hello('Dave')

# Importing all functions from the module
from greetings import *
say_hello('Eve')






print('8-17')
#before styling
def make_sandwich(*items):
    for item in items:
        print(f"- {item}")
print("Your sandwich is ready!\n")

