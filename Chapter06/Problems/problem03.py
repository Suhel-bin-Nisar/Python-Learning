# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this",  "click this".  Write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

text = input("Enter the text of the comment :")

if (p1 in text) or (p2 in text) or (p3 in text) or (p4 in text):
    print("This is a spam comment.")

else :
    print("This is not a spam comment.")