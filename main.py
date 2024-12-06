class Getlower:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value.lower() if isinstance(value, str) else value
    def __delete__(self, instance):
        del instance.__dict__[self.name]
class Car:
    attribute = Getlower("a")
class Animal:
    attribute = Getlower("a")
a = Car()
b = Animal()
a.attribute = "BMW"
b.attribute = "Dog"
print(a.attribute)
print(b.attribute)