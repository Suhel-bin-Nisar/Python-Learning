# Write a program using functions to find greatest of three numbers.

def Greatest(num1, num2, num3):
    if (num1 >= num2 and num1 >= num3):
     return num1
    #  print(num1)
    elif(num2 >= num1 and num2 >= num3):
     return num2
    #  print(num2)
    else :
        return num3   #Here we use return if we want to print it from the outside of the function..
        # print(num3)    #But when we use print here then we just need to call the funtion no need to use print statement to show thw greatest number...

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))


# Greatest(number1, number2, number3)     #This will work with the print statement in defining a function...


# Greatest_number = Greatest(number1, number2, number3)    # We can use this line if we want to store the greatest number in a variable...
print(f"The greatest number is {Greatest(number1, number2, number3)}")  #This will work when we use return in place of print in defining of a functio.....


