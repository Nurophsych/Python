for i in range(1, 21):
    print(i)
    
#4-4  
list1 = []
for i in range(1,1000001):
    list1.append(i)
#print(list1)

print(max(list1))

print(min(list1))

print(sum(list1))

for i in range(1, 1000001, 2):
    list1.append(i)
#print(list1)

for i in range(0, 30, 3):
    print(i)
    
for i in range(1, 11):
    print(2**i)
    
squares = [i**2 for i in range(1, 11)]
print(squares)