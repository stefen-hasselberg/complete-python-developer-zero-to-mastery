def multiply_by2(li):
    return li * 2

#map(action, iterable)
# map returns an object so we need to
# put into a list


print(list(map(multiply_by2, [1, 2, 3])))
