#Program to demonstrate string immutability by attempting to modify a character handling the error
s = "Python"

try:
    s[0] = 'P'   
except TypeError as e:
    print("Error:", e)

print("String after attempt:", s)
