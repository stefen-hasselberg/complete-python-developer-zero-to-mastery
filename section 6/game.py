# OOP Inhertiance

# BASE Class
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


# Sub Class
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows} ")


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')


print(wizard1)
wizard1.sign_in()
print(wizard1.email)
wizard1.attack()


print(isinstance(wizard1, Wizard))

print(dir(wizard1))
