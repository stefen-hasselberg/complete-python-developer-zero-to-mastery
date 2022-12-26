print(True == 1)  # True
print("" == 1)  # false
print([] == 1)  # false
print(10 == 10.0)  # True
print([] == [])  # true


# IS check to see whether the location in memory
# is the same.
a = [1, 2, 3]
b = a
print(True is 1)  # True
print("" is 1)  # false
print([] is 1)  # false
print(10 is 10.0)  # True
print([] is [])  # true
print(a is b)
