# Exercise: Check for duplicates in list

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in my_list:
    print(value)
    if my_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
