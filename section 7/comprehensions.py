# COMPREHENSIONS
# list, sets, dictionary
# quick way to create a list rather than looping
# my_list = [param in param in iterable]
# my_list = [param in param in iterable condition]
my_list = [char.upper() for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num * 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

# for char in 'hello':
#     my_list.append(char)

print(my_list4)


# SET Comprehension
my_set = {char for char in 'hello'}
print(my_set)


# DICTIONARY COMPREHENSION
simple_dict = {'a': 1, 'b': 2}
my_dict = {
    key: value**2 for key, value in simple_dict.items()
}
my_dict2 = {num: num * 2 for num in [1, 2, 3]}

print(my_dict2)
