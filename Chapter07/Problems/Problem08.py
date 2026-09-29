'''
Write a program to print the following star pattern: 
*
**
*** for n = 3
'''


'''
Write a program to print the following star pattern.
  *
 ***
***** for n = 3
'''

n = int(input("Enter the number of rows you want : "))

for i in range (1, n+1):
    print("*"*(i))
    # print(" "*(n-i) + "*"*(2*i-1))  # Another way to print 2 statement in a single line... without moving to the next line..
    