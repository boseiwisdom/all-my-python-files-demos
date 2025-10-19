if task["task_name"] in task not in tasks:
        tasks.append(task)
        return task
# #print(3/0)#This will give error
# ### how to handle errors
# #python uses try except plugs o handle exceptions addtional clauses like else and finally add more control
# # try to test for error and except to handle the errors 
# try:
#     print(3/0)
# except Exception:
#     print("cant divide by zero")
# ##make a variable named num and accept input for user to enter to enter a number
# try:
#     num=float(input("enter the number"))
#     print(num)
# except Exception:##bad way to handle error
#     print("wrong input")
# try:
#     num=float(input("enter the number"))
#     print(num)
# except Exception as ex:##bad way a little to handle error . Exception is broad thing to handle error
#     print("wrong input",ex)
# try:
#     num=float(input("enter the number"))
#     print(num)
# except ValueError as ex:## best way to handle error  valueERROR IS under Exception 
    # print("wrong input",ex)##this ex becareful when u finish coding remove it before u publish your app or it wll be used against u
try:
    num=float(input("enter the number"))
    print(10/num)
except Exception as ex:##bad way a little to handle error . Exception is broad thing to handle error
    print("wrong input",ex)
except ZeroDivisionError as ex:
    print("cant divide by zero ",ex)
# else:
#    print(10/num)# #else runs only if no exception occurs in the try block but not that important to bring
finally:
    print("finallasaa")##finally always execute whether an exception occured or not . it is using for cleaing u resources
