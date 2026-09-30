# Write a python program using function to convert Celsius to Fahrenheit.

def Celsius_to_Fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in celsius: "))

print(f"The temperature in Fahrenheit is {Celsius_to_Fahrenheit(celsius)}°F")