# Write a python function which converts inches to cms.


def inches_to_cms(inches):
    cms = inches * 2.54
    return cms

inches = float(input("Enter the length in inches: "))
print(f"The length in centimeters is {inches_to_cms(inches)} cm")