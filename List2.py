#Given a list of numbers, create a new list containing only even numbers using list comrehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = []
for n in numbers:
    if n % 2 == 0:
       even_numbers.append(n)
print(even_numbers)




