# Lists or Arrays
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd']
li3 = [1, 2, 'a', 'b', True]


# Data Structures
# a container around our data
# eg a backpack: good at storing stuff but hard to search for things

amazon_cart = [
    "notebooks",
    "sunglasses",
    "toys",
    "grapes"
]

print(amazon_cart)

# List Slicing creates a new list doesn't replace existing one
print(amazon_cart[0:2])
# start at the begin and go to the end, stepping over very second one
print(amazon_cart[::2])

# list are mutable
amazon_cart[0] = "laptop"

print(amazon_cart[0:3])
print(amazon_cart)
