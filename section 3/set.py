# SET
my_set = {1, 2, 3, 4, 5, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(len(my_set))

# get the difference from the first set against the
# the second set
print(my_set.difference(your_set))

my_set.discard(5)

# remove any elements that are in both sets
# my_set.difference_update(your_set)

print(my_set)

# return back elements that are common in both sets
print(my_set.intersection(your_set))

# disjoint - return true if both sets don't have anything
# in common with each other
print(my_set.isdisjoint(your_set))

# union - joins two set together
print(my_set.union(your_set))
# print(my_set | your_set)

# issubset - elements on the left must be in the other set
print(my_set.issubset(your_set))

# issuperset - elements on the right be in the set on the left
print(my_set.issuperset(your_set))
