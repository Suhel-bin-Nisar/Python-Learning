# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = { 
    'madad' : 'help',
    'paani' : 'water',
    'bhook' : 'hunger',
    'dost' : 'friend',
}
word = input("Enter the Hindi word you want to translate : ")

print(words[word])