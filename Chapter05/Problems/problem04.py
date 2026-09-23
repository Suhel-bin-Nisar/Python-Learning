'''

What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

'''

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))  # Output: 2 

#It returns 2 because 20 and 20.0 are considered the same in Python sets, while '20' is a different string value....