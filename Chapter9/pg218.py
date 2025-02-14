import random as r

class die_face:
    def __init__(self, sides =6):
        self.sides = sides
    
    def roll_die(self):
        return r.randint(1, self.sides)

        
        
dice_6 = die_face()
print("Rolling a 6-sided die 10 times:")
for i in range(10):
    print(dice_6.roll_die(), end=" ")
print("\n")

print()

dice_10 = die_face(10)
print("Rolling a 10-sided die 10 times:")
for i in range(10):
    print(dice_10.roll_die(), end=" ")
print("\n")

print()

dice_20 = die_face(20)
print("Rolling a 20-sided die 10 times:")
for i in range(10):
    print(dice_20.roll_die(), end=" ")
print("\n")

print('LOTTERY')

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

my_ticket = (3,'A',4,'D')

winning_ticket = r.sample(lottery_pool, 4)

attempts = 0

while True:
    attempts += 1
    winning_ticket = r.sample(lottery_pool, 4)
    if set(winning_ticket) == set(my_ticket):
        break


print("Winning ticket numbers/letters are:", winning_ticket)
print("Any ticket matching these 4 numbers or letters wins a prize!")
print()
print()
print("Winning ticket numbers/letters are:", winning_ticket)
print(f"It took {attempts} attempts to win the lottery!")