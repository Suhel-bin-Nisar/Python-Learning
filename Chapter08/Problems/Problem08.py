# Write a python function to print multiplication table of a given number.

def multiplication_table(n):
    for i in range(1, 11):
     print(f"{n} x {i} = {n * i}")

number = int(input("Enter a number to print its multiplication table : "))
multiplication_table(number)