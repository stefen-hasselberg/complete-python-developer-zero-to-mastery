basket = [1, 2, 3, 4, 5]
print(len(basket))

# append changes list in place.  Doesn't not return a value
new_list = basket.append(100)

print(basket)
print(new_list)

# insert changes the list in place.
basket.insert(4, 101)
print(basket)

# need to pass in a object that can be looped over
basket.extend([101, 102])

print(basket)

# removing the last item of the list
basket.pop()
print(basket)

# or we can pass in a index to remove
basket.pop(2)
print(basket)

# remove an item by passing in what item you want to remove
# update the list
basket.remove(4)
print(basket)

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

# will raise an error if it can't find it
print(basket.index('c'))

# or we can use 'in' which returns True or False
print('d' in basket)

print(basket.count('d'))

# sorted returns a new list
sorted(basket)
# basket.sort()
print(sorted(basket))
print(basket)


# creates a new list
new_list = basket.copy()

basket.reverse()
print(basket)

print(len(basket))
print(basket[::-1])

# generate a list 1 - 100 excluse

print(list(range(1, 100)))

# join two
sentence = ' '

# creates a new object
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Jojo'])
print(new_sentence)


# list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
