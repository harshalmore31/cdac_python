# Polymorphism with inheritance , i.e. using overriding
# Check if "ref" contains "Gun" then only invoke "fillbullets()" along with "attack()"

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
    if isinstance(ref,Gun):
        ref.fillbullets()
        
    ref.attack()


perform(Gun())
perform(Bomb())  
perform(Sword())  

