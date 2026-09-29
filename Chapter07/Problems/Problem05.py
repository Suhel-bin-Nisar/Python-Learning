# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a natural number: "))
i = 1
sum_natural = 0 
while i <= n:
    sum_natural += i
    i += 1  
print("The sum of first", n, "natural numbers is:", sum_natural)