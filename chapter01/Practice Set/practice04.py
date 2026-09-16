# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
# Label the program written in problem 4 with comments.  Ans- Already commented by the chatgpt.


import os

# change this to whichever directory you wanna snoop on
path = "/"

try:
    # os.listdir returns a list of everything in that directory
    contents = os.listdir(path)
    
    print(f"Contents of '{path}':")
    for entry in contents:
        print(entry)

except FileNotFoundError:
    print("Error: That path doesn’t exist!")
except PermissionError:
    print("Error: You don’t have permission to see this directory!")
