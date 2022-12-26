# *args and **kwargs

# *args combines the arguments into a tuple
# when using keywords for passing in arguments
# you need to use **kwargs to combine them into
# dict

def super_func(*args, **kwargs):
    print(type(args))
    print(kwargs)
    return sum(args)


print(super_func(1, 2, 3, 4, 5, num1=5, numb2=10))

# Rule: params, *args, default parameters, **kwargs
# def super_func(name, **args, i='hi', **kwargs)
