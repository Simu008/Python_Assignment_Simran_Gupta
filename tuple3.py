#Program to count the occurance of an elements in a tuple without using in buil-in methods
t = (1, 2, 3, 2, 4, 2, 5)
element = 2

count = 0
for i in t:
    if i == element:
        count += 1

print("Count:", count)
