import copy

original = [1, 2, [3, 4]]

shallow = original.copy()
deep = copy.deepcopy(original)

original[2][0] = 99

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
