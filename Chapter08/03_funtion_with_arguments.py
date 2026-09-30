# Function with a single argument
'''
def goodDay(name):
    print(f"Good day, {name}!")

goodDay("Alice")
goodDay("Bob")
goodDay("Charlie")
goodDay("Diana")
'''
# Function with multiple arguments
'''
def goodDay(name, ending):
    print(f"Good day, {name}!")
    print(ending)

goodDay("Alice", "Have a nice day!")
goodDay("Bob" , "See you later!")
goodDay("Charlie" , "Take care!")
goodDay("Diana" , "All the best!")
'''

#Function with return
def goodDay(name, ending):
    print(f"Good day, {name}!")
    print(ending)
    return "Greeting sent successfully."

a = goodDay("Alice", "Have a nice day!")
print(a)


