##Inheritance allows a class(child) to inherit attributes and methods from another class(parent class).
# Parent class pass down attributes aand methods to the child classs
##base class
class Animal:
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
    def speaks(self,sound):
        print(f"{self.name} says {sound}")
    def eat_what(self):
        print("the animal is eating")
##derived class 1
class Fish(Animal):
    def swim(self):
        print("I am swimming")
    def eat_what(self):##overriding the ear_what in the parent class
        print ("the fish eat food")
    def speaks(self,sound):
        print("heeiii")
        super().speaks("jjjjj")

#derived class 2
class Dog(Animal):
    pass
tuna=Fish("tuna",12,"fish")
print(tuna.age)
tuna.speaks("poof")
# tuna.eat_what()
# dog1=Dog("buddy",2,"land type")
# dog1.speaks("woof")