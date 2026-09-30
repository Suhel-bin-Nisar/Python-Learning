# Write a recursive function to calculate the sum of first n natural numbers.   
'''
Sum of natural numbers :-
sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6
sum(4) = 1 + 2 + 3 + 4 = 10
sum(n) = 1 + 2 + 3 + .... + n = n + sum(n-1)

'''

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

number = int(input("Enter a natural number: "))
print(f"The sum of first {number} natural numbers is {sum(number)}")