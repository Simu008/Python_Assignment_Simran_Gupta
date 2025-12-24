#Tuple with mutable elements and modify them
t = (1, 2, [10, 20, 30])

# Modify the list inside the tuple
t[2][1] = 99

print(t)

