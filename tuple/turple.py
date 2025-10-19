my_tuple=(1,2,3,4,5,6)
my_tuple2=(6,7,8)
##unpacking tuple
(one,kka,any)=my_tuple2
print(one)
print("for loop")
for i in my_tuple2:
    print(i)

print("now we are on sets")
##sets are unoredered mutable and contain only unique element
my_set={1,1,2,2,3,4,6,5}
print(my_set)
my_set2={"hello","hey",False,0}
print(my_set2)
my_set3={"hello","hey",1,True}
print("1" in my_set3)
##looping through
print("looping through")
for i in my_set3:
    print(i)

print('adding to a set')
my_set3.add("Kofi")
print(my_set3)
####to remove
print('removing from a set')
my_set.remove(2)
print(my_set)

print("we are now going to set operation")

#| for unioon
#& for intercession
#- is the differecne
a={1,2,3}
b={2,3,4}
print("this for union")
print(a|b)
##intercession symbol == &
print(a&b)
print("difference")
print(a-b)
print("symmetric diifernce")
print(a^b)
###DICTIONARY are key value pair and are are unordered
print("we are now on dictionary")
##Dictionaries are unordered  collection of data. They are store in key-value pair . The keys are unqiue and mutable(cant be change) but the value can be any type
person_one={"name" : "kofi" ,"age" : 26}#a way to create dictionary
person_two=dict(name= "yaw" , age = 56,gender="Male")#another way to create dictionary
print("accessing dctionary")
print(person_one["name"])
###some methods
print(person_one.get("kslas","unknown"))###the get takes two aguments first is the key and second is the value it should returun if error
print(person_two.keys())
print(person_two.values())
print(person_two.items())
##assigning values to dictiionary
print("assigning in dictionary")
person_two["name"]='Abena'
print(person_two)
person_two.update({"age":25})
print(person_two)
##removing from dictionary
print('removing in dictionary')
#print(person_two.pop("age"))
print(person_one.popitem()) ##remove last item
print(person_one)
# print("loops in dictionary")
# for key,vale in person_one.items():
#     print(f"{key}:{vale}")
# print("worked examples")
# for key in person_one:
#     print(person_one[key])
#    ###tuple cant be cahnage after created because it immutable but there is a way around fist change itt to list then convert it back
# tuple_1=(1,2,3,4,5,6,7)
# mylis=list(tuple_1)
# print(mylis)
# mylis[0]="kofi"
# print(mylis)
# mylis=tuple(mylis)
# print(type(mylis))


# print("worked example")
# cat ={
#     "name":"mayhem",
#     "action": ["speaks",'walks'],
#     "breed":("African","Asian")
# }
# print(cat["breed"][0])
# #print(cat["action"][1])