# Lambda
# anonymous functions used for simple function
# one time,  no name
# lambda param:  action(param)
from functools import reduce

my_list = [1, 2, 3]

print(list(map(lambda x: x * 2, my_list)))

print(list(filter(lambda x: x % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list, 0))
