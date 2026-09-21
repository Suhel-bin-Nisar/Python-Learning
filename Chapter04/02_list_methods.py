'''
LIST METHODS :
• l1.sort(): updates the list to [1,2,7,8,15,21]

• l1.reverse(): updates the list to [15,21,2,7,8,1]

• l1.append(8): adds 8 at the end of the list

• l1.insert(3,8): This will add 8 at 3 index

• l1.pop(2): Will delete element at index 2 and return its value.
 
• l1.remove(21): Will remove 21 from the list.

'''



friends = ["Alice", "Bob", "Charlie", "David" , 5 , 0.2563 , False ]
print(friends)
friends.append("Saad")  #To add the object at the end of the list
print(friends)


L1 = [89, 54, 67,43 ,23 ,69 , 75]
L1.sort()   #It sort the given list in the ascending order
# L1.reverse()  # It sort the list in reverse means the last value will come first
L1.insert(1 , 12563)  #If we have to insert an object at an particular index
L1.sort()   #After the insert it will sort again 
print(L1)


L2 = ["Bananan" , "Dog" , "Apple" , "Elephant"]
# L2.sort()
print(L2)
L2.remove("Bananan")  #It will remove the given object from the list
print(L2)