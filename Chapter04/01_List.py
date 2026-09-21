friends = ["Alice", "Bob", "Charlie", "David" , 5 , 0.2563 , False ]

print(friends)   #Print the entire list
# print(friends[3])  #Print the element at index 5
friends[3] = "Suhel"  #Lists are mutable means that we can make changes in the current list item unlike string we dont need to create a new string with updated version.
print(friends)
print(friends[1:4])  #Print from index 1 to index 3 (4-1 =3)