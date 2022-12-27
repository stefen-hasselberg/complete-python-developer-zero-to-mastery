from functools import reduce

# square the list
my_list = [5, 4, 3]

print(list(map(lambda x: x * x, my_list)))

# list sorting on the second value
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)
