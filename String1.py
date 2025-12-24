#Program to count the no. of vowels, consonants, digits, and special characters in a given string
s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for i in s:
    if i.lower() in "aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1
    elif i.isdigit():
        digits += 1
    else:
        special += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Digits:", digits)
print("Numvber of Special characters:", special)
