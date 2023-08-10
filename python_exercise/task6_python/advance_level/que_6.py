'''Create the custom python classes which has methods and attributes and implement single inheritance,
multiple inheritance and multilevel inheritance

'''
class Animal :
 def walk(self):
     return "animal can walk"

class Dog(Animal) :
    def bark(self):
        return "baww baww" 
class Cat(Animal):
    def sound(self) :
        return "meow meow"

class pet(Dog,Cat):
    def loyal(self):
        return "they are pet"

          