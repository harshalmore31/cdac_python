# Polymorphism with member functions  # Duck Typing

class India:
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is developing country")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")


def perform(obj):
    obj.capital()
    obj.language()
    obj.type()

perform(India())
print("Let's pass USA")
perform(USA())

