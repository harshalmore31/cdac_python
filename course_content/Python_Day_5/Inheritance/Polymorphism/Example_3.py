# Polymorphism with inheritance , i.e. using overriding
# Check if "ref" contains "Sword" then only invoke "attack()"

class Weapon:
    def attack(self):    # overridden method
        pass

class Gun(Weapon):
    def attack(self):    # overriding method
        print("Attack with Gun")


class Sword(Weapon):     # overriding method
    def attack(self):
        print("Attack with Sword")


class Bomb(Weapon):
    def attack(self):    # overriding method
        print("Attack with Bomb")


def perform(ref):
    if isinstance(ref,Sword):
        ref.attack()


perform(Gun())
perform(Bomb())
perform(Sword())

