# class Animal:

#    # name = "Buddy"  ##attribute
    
#     def __init__(self,name):###init is standard name here(here u cant right anyname u want) 
#         self.name=name
     
    
#     ##method
#     def speak(self,sound):###for this speak it can chane per the question .but here the speak is method
#         print (f" {self.name} says {sound}")
# animal1=Animal("buddy")
# print(animal1.name)
# animal1.name="husky"
# animal1.speak("meoo")
# ###define a class call car, the car should have an attribute called (model and year) and methods of drive
# class car:
#     def __init__(self,model,year):
#         self.model=model
#         self.year=year
#     def drive(self):
#         print("it can  move")
# car1=car("Toyota",2025)
# print(car1.model)
# print(car1.year)
# car1.drive()

# # ###new assignment  ###this one have limitation
# # class calculator():
# #     def __init__(self,num1,num2):
# #         self.num1=num1
# #         self.num2=num2
# #     def add(self,num1,num2):
# #         print(num1 + num2)
# #     def subtraction(self,num1,num2):
# #         print(num1-num2)
# #     def division(self,num1,num2):
# #         print(num1/num2)
# #     def multiplication(self,num1,num2):
# #         print(num1*num2)
# # cal1=calculator(2,3)
# # cal1.add(2,3)
# # cal1.subtraction(5,2)
# # cal1.division(5,6)
# # cal1.multiplication(2,5)
# class calculator():
#     def add(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(num1 + num2)
#     def subtraction(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(num1-num2)
#     def division(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(num1/num2)
#     def multiplication(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(num1*num2)
# cal1=calculator()
# cal1.add(2,3)
# cal1.subtraction(5,2)
# cal1.division(5,6)
# cal1.multiplication(2,5)
# class Car:
#     def __init__(self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
# Toyota=Car("A-50","GREEN","2025")
# print(Toyota.model)
# print(Toyota.year)
# Kia=Car("A-30","RED","2025")
# benz=Car("A-20","RED","2025")
###write calulator where each method takes the operators
# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         return (self.num1 + self.num2)
#     def update(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
# add=Calculator(2,3)
# print(add.add())
# add.update(2,6)
# print(add.add())



class Age:
    def __init__(self,age):
        self.age=age
    
        if age<18:
            return "you are not eligible to vote"
        else:
            return "you are eligible to vote"
Bio=Age(28)
print(Bio.age)