# def hello():
#     print("hellllllooo")


# greet = hello
# del hello
# print(greet())
# pass in a function and then invoke it
# def hello(func):
#     func()

# our function


def greet():
    print('still here')


# print(hello(greet))

# Higher Order Function
# function that accepts another function
# def greet(func):
#       func()

# or a function that returns another function
#  def greet2():
#       def func():
#          return 5
#       return func


# Decorator
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***********************')
        func(*args, **kwargs)
        print('***********************')
    return wrap_func


@my_decorator
def hello(string, emoji='😔'):
    print(string, emoji)


hello("hello")
