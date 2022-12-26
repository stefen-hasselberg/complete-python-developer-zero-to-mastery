def test(a):
    '''
    Info: This function test and prints param a
    '''
    print(a)

    test(a)


# to read docstring
help(test)

# magic or dunder methods
print(test.__doc__)
