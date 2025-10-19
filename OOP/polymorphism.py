##types of polymorphism
#duck type, method overloading and operaotr overloading
# duck type if it look like duck quark linke duck walk like duck then is duck
class Dog:
    def speak(self):
        return "woof"
class Car:
    def speak(self):
        return "vroooom"  ##they both share same method so is a duck type
    
##so if u do
owas=[Dog(),Car()]
for owa in owas:
    print(owa.speak())
def say(att):##att is just ca parameter , u can nameis what u want
    print(att.speak())
dog1=Dog()
car1=Car()
say(dog1)

##method overloading , assumming there is a function with 4 paramters ,with the help of method ov
# erloadin it help us to make the code a way that if the user input one parameter or 2 or 3 or all 4 it shoud work
# class Calculator:
#     def sum(self,num1=None,num2=None,num3=None):
#         if num1 !=None and num2 !=None and num3!=None:
#             print(num1+num2+num3)
#         elif num1!=None and num2!=None:
#             print(num1+num2)
#         elif num1!=None:
#             print(num1)
#         else:
#             print(0)
# calc=Calculator()
# calc.sum(2,2,2)
# calc.sum(2,2)
# calc.sum(2)
# calc.sum()##u see with this any number of parameter it acceptes whether 1 ,2 or 3 it will accept

##operator overloading
#let say 

#let say
print(int.__add__(2,3))## u se this will add to give 5 but there is way to overide it to give u your predfined operator
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __add__(self,other):
        return Calculator(self.num1 + other.num1,self.num2 + other.num2)
    def __str__(self):
        return f"Calculator({self.num1}, {self.num2})"

cal1=Calculator(2,4)
cal2=Calculator(4,5)
sum=cal1+cal2
# print(cal2.__add__(4))
print(cal2.__str__())