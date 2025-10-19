is_active = True
name= 'kofi'
print(name)
print(type(name))

###comparisim operators include(==,<=,>=,!=) and logical operators include(and,or,not)
print(not(3>9) or 3>8)

##assignment operator eg(x+=10) which can be expand as x=x+10
x=1
x+=2
x=x+2
x//=2   ###// is called floor . let take  a float 2.6 . it will give the number infont which is 2.
print(x)

### identity operation is used to check if two object are the same . that is same memory location  .give true and false 
ama= 6
Yaa= 4
print(id(ama))
print(id(Yaa))
print(ama is Yaa)
print(ama is not Yaa)
kk=2**5
print(kk)

##membership operations  include "in " is used if value is found is in the sequence  and "in not" is used if value is not 