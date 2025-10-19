3. #Write a program that prompts the user for their age. If the age is 18 or older, print "You are eligible to vote." If it is under 18, print "You are not eligible to vote
# class Age:
#     def __init__(self,age):
#          self.age=age
#     def lk(self):
#         if self.age<=18:
#             return "you are not eligible to vote"
#         else:
#             return "you are eligible to vote"
# Bio=Age(28)
# print(Bio.lk())
# class Age:
#     def eligib(self,age):
#         if age>=18:
#             return " you are eligible"
#         else:
#             return "you are not eligible"
#     def divisible(self,num):
#         if num%3==0 and num%5==0:
#             return "divisble by both"
#         if num%3==0:
#             return "the number is divisible by 3"
#         if num%5==0:
#             return "the number is divisble ny 5"
#         else:
#             return "not divisible by any"
# bio=Age()
# print(bio.eligib(12))
# print(bio.divisible(9))
##come here again
# class task:
#     def negativechecker(self):
#         lisa=[1,2,3,4]
#         for i in lisa:
#             if i <0:
#                 return i
#             else: 
#                 return "No negative "

# liaa=task()
# print(liaa.negativechecker())
class Task:
    task=[]
    def __init__(self,lisa):
    #     self.item=item
        self.lisa=lisa
        
    def adding(self):
        self.task.append(self.lisa)
        return self.task
    def remove(self):
        self.task.append(self.lisa)
        return self.task


        

    # def removing
bio=Task(2)
print(bio.adding())

