# Dictionary - Hash Table, Object
# data Structure
# unordered key pair
# not stored next to other in memory

dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True

}

# print(dictionary['c'])

user = {
    "basket": [1, 2, 3],
    "greet": 'hello',
    "age": 20
}

# check if key exists
print(user.get('age'))

# check if key exists, if not then use the defalut value
print(user.get('age', 55))

user2 = dict(name="JohnJohn")
print(user2)

print('hello' in user.values())

# clear the dictionary - empty dict
# user.clear()
user2 = user.copy()

print(user)
print(user2)

user.update({'age': 55})
# removes the last item added to dictionary
print(user)
print(user.popitem())
