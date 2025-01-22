guest_list = ['Marley', 'Jacob', 'Peter']

for i in range(0,3):
    print(f'To my esteemed guest {guest_list[i]} we invite you to join us for a miraculous evening!')
    
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    
guest_list[1] = 'Jimothy'
for i in range(0,3):
    print(f'To my esteemed guest {guest_list[i]} we invite you to join us for a miraculous evening!')
    print("However all I have found a bigger table")
    
    
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
    
guest_list.insert(0,"Rathew")
guest_list.insert(2, "Michael")
guest_list.append("Toby")

for i in range(0,6):
    print(f'To my esteemed guest {guest_list[i]} we invite you to join us for a miraculous evening!')
  
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

print("unfortuantely only two may feast")

for i in range(0,4):
    x = guest_list.pop(0)
    print(f'I am so sorry {x} due to the late table you must leave.')
print(guest_list)
    

del guest_list[1]
del guest_list[0]

print(guest_list)