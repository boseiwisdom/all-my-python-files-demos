# ##functions is a block of *reusable* code that performs a specific tasks
# ##functions help you organise your code and avoid repetition and make it more readabe
# #syntax
# # def function_name():
#     # "doctrine--a commentofwhat is for"
#     # block of code here 
# def great():
#     print('welcome Osei')
# ###calling or invoking 
# great()

# def sum():
#     print(1+2)
# ###calling or invoking
# sum()
# ##function can takes inputs called parameters
# def great(name):##here the name is parameter
#     print(f'welcome {name}')
# great('Bio')##here the Bio is argument
# great('Bio')##here the Bio is argument
# def sum(num1,num2):
#     print(num1+num2)
# sum(2,5)
# ###settting defalut name
# def great(name="GUEST"):
#     print(f'welcome {name}')
# great()  ###though u cant still place an argument here in the ( ) to replace the default GUEST
# def divi(name=10):
#     print(name/2)
# divi()  ###though u cant still place an argument here in the ( ) to replace the default GUEST
# def divi(du,name=10):##if there are more parameters the default paramater which here is name should be last as showed
#     print(name/2+du)
# divi(4)  ###though u cant still place an argument here in the ( ) to replace the default GUEST
# divi(4,8)###here i change the defalut value which was 10 to 8

# ###write a function which takes a list of numbers and print out the sum if those numbers

# #ef sum(lisa):
#    #v=0
#    #for i in lisa:
#    #    v+=i
#    #print(v)
# #um([1,2,3,4,5])
#  #*anyname(def function(*args)) so let use the official *args aloow s yout pass postional argument to a function.
# #the argument pass through *args are corrected into a tuple 
# #example
# #ef total_sum(*args):
#     #otal=sum(args)
#    #print(total)
# #otal_sum(2,3,4,5,6)
# # def averag(*args):#worng for a reason
# #    v=sum([args])/len(args)
# #    print(v)
# # averag(2,3,4)
# #**kwargs allows you toy pass a variable number to keyword argument to a function
# ##they are collected into a dictionary
# def person_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# person_info(name="Alice",age=25,gender="F")
# def add(num1,num2):
#     return num1 + num2
# print(add)

# def su(num1,num2):
#     print(num1 +num2)

# print(su(1,2))

# ##write an application which the user can use to deposit , withdraw and checkbalance
# # def deposit(balance,amount):
# #     balance+=amount
# #     return balance

# # def withdrawal(balance,amount):
# #     if balance<amount:
# #         return "insufficient"
# #     else:
# #         return balance- amount

# # def checkbalance(balance):
# #     return balance
# # balance=0
# # balance=deposit(balance,200)
# # print(balance)
# # balance=deposit(balance, 20)
# # print(balance)
# ##now create a function but this time name and balance kinda it should be dictionary

# def creating_account(acounts):
#     return {
#         "name" :acounts["name"],
#         "balance" : acounts["balance"]
#     }
    
# acounts=creating_account({"name":"osei" ,"balance":0})
# def depo(acounts,amount):
#     acounts["balance"]+= amount
#     return acounts

# acounts=depo(acounts,20)
# def withdrawal(acounts,amount):
#     if acounts["balance"]<amount:
#         return "insufficient"
#     else:
#         acounts["balance"]-=amount
#         return amount
# print(withdrawal(acounts,200))

##now create a function but this time name and balance kinda it should be dictionary
##creating a account
def accountcreator(name,amount):
    return {
        "name":name,
        "balance":amount
    }
account1=accountcreator("kofi",0)
##depositing 
def deposit(account1,amount):
    account1["balance"]+=amount
    return account1
deposit(account1,20)
##withdrawing
def withdraw(account1,amount):
    if account1["balance"]<amount:
        print("insufficent")
    account1["balance"]-=amount
    return account1
print(withdraw(account1,12))


