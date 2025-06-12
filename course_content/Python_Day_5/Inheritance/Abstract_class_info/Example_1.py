# "abc"  is a module
# "ABC" is a class inside "abc" module
# "abstractmethod" is a function inside "abc" module

from abc import ABC, abstractmethod

class Person(ABC):
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
    def sleep(self):
        print("I can sleep")
    @abstractmethod
    def performduties(self):
        pass

class Teacher(Person):
    def performduties(self):
        print("Perform teacher's duties")

class HouseWife(Person):
    def performduties(self):
        print("Perform HouseWife's duties")

class Soldier(Person):
    def performduties(self):
        print("Perform Soldier's duties")


def perform(ref):
    ref.walk()
    ref.talk()
    ref.eat()
    ref.sleep()
    ref.performduties()


perform(Teacher())
perform(Soldier())
perform(HouseWife())

#ob = Person()   #  TypeError: Can't instantiate abstract class Person with abstract method performduties


