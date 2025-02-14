class Resturants:
    def __init__(self, name, cusine):
        self.name = name
        self.cusine = cusine
        self.serving = 0
        
    def description(self):
        print(f'Resturant name:{self.name}')
        print(f"Cuisine type: {self.cusine}")
        
    def open_resturant(self):
        print(f'{self.name.title()} is OPEN!!!!!!!!!!')
        
    def who_is_served(self):
        print(f'{self.serving} customers tended to')
        
    def add_serving(self,order):
        self.serving += int(order)
        
resturant = Resturants('El Commadore', 'Mexican Cuisine')

resturant2 = Resturants('Fishaways', 'Seafood')

resturant3 = Resturants('KFC','Fast food')

# print(resturant.name)
# print(resturant.cusine)
# print('\\\\\\\\\\\\\\\\\\\\\\')
# resturant.add_serving(6)
# resturant.open_resturant()
# resturant.description()
# resturant.who_is_served()
# print()   
# resturant2.add_serving(12) 
# resturant2.open_resturant()
# resturant2.description()
# resturant2.who_is_served()
# print()
# resturant3.add_serving(22)
# resturant3.open_resturant()
# resturant3.description()
# resturant3.who_is_served()

# print()
# print()
# print()
class IceCream(Resturants):
    
    def __init__(self,name,cusine,flavors):
        super().__init__(name,cusine) 
        self.flavors = flavors
        
    def displaygoods(self):
        print("Good day our flavors are:")
        for cream in self.flavors:
            print(cream)
 
icecreamstand =IceCream('Ahoy','Ice-cream desserts',['rocky road','chocolate', 'vanilla', 'strawberry', 'tin roof', 'banana', 'caramel', 'berry nice', 'choc mint'])
 
 
 
# icecreamstand.description()  
# icecreamstand.displaygoods()  



#9-7
"a class used to gather user data"
class User:
    def __init__(self, f_name, l_name, number, address):
        self.f_name = f_name
        self.l_name = l_name
        self.number = number
        self.address = address
        self.log_attempts = 0
        
    def user_info(self):
        print(f'The user first name is: {self.f_name}') 
        print(f'The user last name is: {self.l_name}') 
        print(f'The user phone number is: {self.number}') 
        print(f'The user address is: {self.address}') 
        
    def greetings(self):
        print(f'Well...hello there {self.f_name}')
        
    def increment_attempt(self):
        self.log_attempts += 1
        print(f'login attempts: {self.log_attempts}')
        
    def log_res(self):
        self.log_attempts = 0
        print(f'Attempts reset: {self.log_attempts}')


# person1 = User('Keenan', 'Van Straaten', 22, '10 Pruinosa')
# person2 = User('Matt', "Pritt", 34, "12 Glendale Ave")
# person3 = User("Ratthew", 'Rice', 53, '13 Hughjass lane')

# person1.greetings()
# person1.user_info()
# for i in range(1, 4):
#     person1.increment_attempt()
# person1.log_res()
# print()
# person2.greetings()
# person2.user_info()
# for i in range(1, 4):
#     person2.increment_attempt()
# person2.log_res()
# print()
# for i in range(1, 4):
#     person3.increment_attempt()
# person3.log_res()
# person3.greetings()
# person3.user_info()

class Privileges:
    def __init__(self, privileges = None):
        if privileges is None:
            privileges = [
            "can add post", 
            "can delete post", 
            "can ban user", 
            "can promote user"
        ]
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, f_name, l_name, number, address):
        super().__init__(f_name, l_name, number, address)
        self.priv = Privileges()  # Create an instance of Privileges

    def show_priv(self):
        # Use the Privileges class to display the admin's privileges
        self.priv.show_privileges()

# Create an Admin object
admin1 = Admin('Joshua', 'Hadley', '22', '13 Eye Africa')

print("\nAdmin Details:")
# admin1.greetings()
# admin1.user_info()
# admin1.show_priv()


#9-9

class Battery:
    def __init__(self, battery_size=50):
        """Initialize the battery with a default size."""
        self.battery_size = battery_size

    def get_range(self):
        """Return the range of the car based on the battery size."""
        if self.battery_size == 50:
            return 200  # Range for 50 kWh battery
        elif self.battery_size == 65:
            return 250  # Range for upgraded 65 kWh battery
        else:
            return 0  # If the battery size is invalid

    def upgrade_battery(self):
        """Upgrade the battery to 65 kWh if it's not already upgraded."""
        if self.battery_size != 65:
            print("Upgrading the battery to 65 kWh...")
            self.battery_size = 65
        else:
            print("The battery is already upgraded to 65 kWh.")
        
class ElectricCar:
    def __init__(self, make, model, year, battery_size=50):
        """Initialize the electric car with basic attributes and a battery."""
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery(battery_size)

    def get_range(self):
        """Return the range of the electric car based on the battery size."""
        return self.battery.get_range()

# Create an electric car with the default battery size (50 kWh)
# my_car = ElectricCar('Tesla', 'Model S', 2020)

# # Get the range with the default battery
# print(f"Range before upgrading the battery: {my_car.get_range()} miles")

# # Upgrade the battery to 65 kWh
# my_car.battery.upgrade_battery()

# # Get the range after upgrading the battery
# print(f"Range after upgrading the battery: {my_car.get_range()} miles")
