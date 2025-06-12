# Polymorphism with inheritance , i.e. using overriding

class Weapon:
    def attack(self):    # overridden method
        pass

class Gun(Weapon):
    def attack(self):    # overriding method
        print("Attack with Gun")
    def fillbullets(self):
        print("Fill bullets in the Gun")



class Sword(Weapon):     # overriding method
    def attack(self):
        print("Attack with Sword")


class Bomb(Weapon):
    def attack(self):    # overriding method
        print("Attack with Bomb")


def perform(ref):
    ref.fillbullets()   # it will not work when we pass "Bomb" or "Sword"
    ref.attack()


perform(Gun())
perform(Bomb())  # AttributeError: 'Bomb' object has no attribute 'fillbullets'
perform(Sword())  # AttributeError: 'Sword' object has no attribute 'fillbullets'

