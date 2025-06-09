class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "I am a Person"

p1=Person("Sachin",25)
print(p1)    #  proves that internally __str__ magic or dunder function gets called