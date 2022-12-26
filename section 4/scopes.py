
# global scope
a = 1


def parent():
    # a = 10
    b = 1 + a

    def confusion():
      # local scope
        return b
    return confusion()


print('Global scope:',  a)
print(parent())


# 1 - start wtih local
# 2 - Parent local
# 3 - Global
# 4 - Built in python functions

# to Access Global Varaible
total = 0


def count():
    global total
    total += 1  # this won't work as we haven't defined total
    return total


print(count())


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner ', x)

    inner()
    print("outer: ", x)


outer()
