'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

'''
This is the second way to solve this problem using recursion.. where function call itself again and again until the base condition is met..
def pattern(n):
    if (n == 0):
        return
    print("*" * n)
    pattern(n - 1)

pattern(3)

'''
def print_pattern(n):
    for i in range (n, 0, -1):
        print('*' * i)


number = (int(input("Enter the number of lines: ")))
print_pattern(number)
