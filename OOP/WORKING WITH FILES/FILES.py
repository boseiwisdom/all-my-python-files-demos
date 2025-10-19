# file="data.txt"
# content= open(file,"r")
# print(content.read())
# content.close()###alway remember to close or it will lead to memeory high usge which will lead to crushes
# or 
# file="data.txt"
file1=None
try:
    # file="data.txt" this one should not be i the try excepet 
    content= open(file1,"r")
    print(content.read())
    # content.close() so here let say we forget to bring the close.()
except Exception as a:
    print ("something is wrong" "or file not found")
finally:
    if file1:
        content.close()

###let see how to prevent memory leak if we fail to bring close() with try execpt 
file1="data.txt"
try:
    # file="data.txt"
    content= open(file1,r)
    print(content.read())
    # content.close() so here let say we forget to bring the close.()
except Exception as a:
    print ("something is wrong",a)


#BEST OPTION TO PREVENT MEMORY LEAK. WITH WITH OPEN U DONT NEED TRY EXCEPT BUT 
# AS A DEVELOPER ANYTHING CAN HAPPEN SO TRY YOUR BEST TO HANDE EVERY ERROR YOURSELF
 
with open(file1,"r") as file:
    print(file.read())
#TO WRITE TO A file
with open("information.txt","w") as file:
    file.write("Take care")
