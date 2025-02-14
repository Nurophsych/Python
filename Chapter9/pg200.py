class Resturants:
    def __init__(self, name, cusine):
        self.name = name
        self.cusine = cusine
        
    def description(self):
        print(f'Resturant name:{self.name}')
        print(f"Cuisine type: {self.cusine}")
        
    def open_resturant(self):
        print(f'{self.name.title()} is OPEN!!!!!!!!!!')
        
resturant = Resturants('El Commadore', 'Mexican Cuisine')

resturant2 = Resturants('Fishaways', 'Seafood')

resturant3 = Resturants('KFC','Fast food')

print(resturant.name)
print(resturant.cusine)

resturant.open_resturant()
resturant.description()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
resturant2.open_resturant()
resturant2.description()

resturant3.open_resturant()
resturant3.description()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
class User:
    def __init__(self,f_name,l_name,number,address):
        self.f_name=f_name
        self.l_name = l_name
        self.number = number
        self.address = address
        
    def user_info(self):
        print(f'The user first name is: {self.f_name}') 
        print(f'The user last name is: {self.l_name}') 
        print(f'The user phone number is: {self.number}') 
        print(f'The user address is: {self.address}') 
        
    def greetings(self):
        print(f'Well...hello there {self.f_name}')

person1 = User('Keenan','Van Straaten',22,'10 Pruinosa')
person2 = User('Matt', "Pritt", 34, "12 Glendale Ave")
person3 = User("Ratthew", 'Rice', 53, '13 Hughjass lane')

person1.greetings()
person1.user_info()
print()
person2.greetings()
person2.user_info()
print()
person3.greetings()
person3.user_info()
