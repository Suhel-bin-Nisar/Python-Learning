# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

s1 = int(input("Enter the marks of subject 1: "))
s2 = int(input("Enter the marks of subject 2: "))
s3 = int(input("Enter the marks of subject 3: "))

total_percentage = (s1 + s2 + s3) / 300 * 100


if total_percentage >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33:
    print("Congratulations! You have PASSED.")
else:
    print("Sorry, you have FAILED.")

print("Total Percentage:", total_percentage)