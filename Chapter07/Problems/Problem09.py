'''
Write a program to print the following star pattern.
***
* *      for n = 3
***
'''

n = int(input("Enter the number of rows you want : "))  

for i in range(1 , n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
       print("*" , end="")
       print(" " * (n-2) , end="")
       print("*")
       
    #    print("*" + " " * (n-2) + "*")  another way to do the same thing in a single line