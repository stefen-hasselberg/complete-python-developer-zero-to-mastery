# OOP
class PlayerCharacter:
    # Class Object Attribute - Static Property
    # will be the same value across all instances
    # can not update
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

    # Create a class Method
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    def speak(self):
        print(f"my name is {self.name} and I am {self.age} years old.")


player1 = PlayerCharacter('Stefen', 48)

print(player1.run())
print(player1.age)
print(player1.membership)
print(player1.adding_things(2, 3))
player1.speak()
