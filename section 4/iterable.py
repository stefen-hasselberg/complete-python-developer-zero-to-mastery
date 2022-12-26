# Iterable
# a collection that can be iterate over
# can be list, dictionary, tuple, set , string
# iterated -> one by one check each item in the collection

for item in {1, 2, 3, 4, 5}:  # set
    for x in ['a', 'b', 'c']:  # list
        print(item, x)


user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item[0], item[1])


for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)
