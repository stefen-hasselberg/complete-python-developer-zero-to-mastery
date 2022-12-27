# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Sally', 10)
cat2 = Cat('John', 2)
cat3 = Cat('Bob', 1)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    age = 0
    for cat in args:
        if cat.age > age:
            return cat


old_cat = oldest_cat(cat1, cat2, cat3)
print(
    f"The oldest cat is {old_cat.age} years old. {old_cat.name} will be the oldest cat")

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
