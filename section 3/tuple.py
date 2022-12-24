# Tuple
# like a list but you can't change them

my_tuple = (1, 2, 3, 4, 5)

# can't change it
# my_tuple[2] = 'z'
print(my_tuple[1])

print(5 in my_tuple)

# we can slice a tuple
new_tuple = my_tuple[1:4]
print(new_tuple)

# unpacking
x, y, z, *other = my_tuple

print(x)
print(y)

print(my_tuple.count(5))

print(my_tuple.index(5))
