# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

name = str(input("Enter your name friend 1: "))
lang = str(input("Enter your favorite language: "))

d.update({name : lang})

name = str(input("Enter your name friend 2: "))
lang = str(input("Enter your favorite language: "))

d.update({name : lang})

name = str(input("Enter your name friend 3: "))
lang = str(input("Enter your favorite language: "))

d.update({name : lang})

name = str(input("Enter your name friend 4: "))
lang = str(input("Enter your favorite language: "))

d.update({name : lang})

print(d)