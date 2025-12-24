#To Check whether a given String is Palindrome using indexing and slicing
s = input("Enter a string: ")

# Using slicing
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
