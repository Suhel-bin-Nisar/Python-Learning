# Write a program to calculate the factorial of a given number using for loop.

# 5! = 5 × 4 × 3 × 2 × 1 = 120

n = int(input("Enter the number to find its factorial : "))

product = 1

for i in range(1 , n+1):
    # product = product * i 
    product *= i 

# print("The factorial of", n, "is:", product)
print(f"The factorial of {n} is : {product}")