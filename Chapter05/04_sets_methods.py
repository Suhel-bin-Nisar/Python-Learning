s = {1, 5, 32, 7, 7, 7, "Suhel"}

print(s, type(s))

s.add(4556)

print(s, type(s))
''' 
len(s)
s.remove(8)  # It will throw an error if the element is not present in the set.
s.discard(8)  # It will not throw an error if the element is not present in the set.

s.pop() # Removes a random element from the set.
s.clear() # Empties the set.
s.union({8,11})  #Returns a new set with all items from both sets. {1,8,2,3,11}.
s.intersection({8,11}  #Return a set which contains only item in both sets {8}.

'''