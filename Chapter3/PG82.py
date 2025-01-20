import random as r



list_of_friends = ["Josh", "Connor", "Jack", "Bussisiwe", "Ashleigh"]

for i in range (0,5):
    print(list_of_friends[i])
    
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        
list_of_friends = ["Josh", "Connor", "Jack", "Bussisiwe", "Ashleigh"]

for i in range (0,5):
    print(f"To my dearest friend {list_of_friends[i]}")
    
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
lis_o_cars = ["Honda", "Jeep", "Toyota", "Mercedes", "BMW", "Kia", "Suzuki"]
lis_o_stat = ["I would like to own a ", "I would love to drive in a ", "Since when do you own a "]

for j in range (0, 7):
    print(lis_o_stat[r.randint(0,2)] + lis_o_cars[j])