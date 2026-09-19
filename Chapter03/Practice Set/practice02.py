# Write a program to fill in a letter template given below with name and date.

letter = ''' Dear <|NAME|>,
            Your are selected!
            <|DATE|>'''

print(letter.replace("<|NAME|>", "Suhel").replace("<|DATE|>", "1st JAN 2026"))