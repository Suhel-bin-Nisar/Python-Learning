# If the names of 2 friends are same; what will happen to the program in problem 6?

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