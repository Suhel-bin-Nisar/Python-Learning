marks = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    0 : 'Zero'
}

# print(marks, type (marks))

# print(marks.items()) 
# print(marks.keys()) 
# print(marks.values()) 

# marks.update({'Bob' : 95})
# print(marks)


print(marks.get('Charlie2'))   #Prints none that is the different betweent this and next line.
print(marks["Charlie2"])        #Returns an error 