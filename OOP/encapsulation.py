#encapsulation means buddlind data (the atrributes) and methods 
# that operates on the data within one unit/class and restricting direct access 
# to some component
class Car:
    def __init__(self):
        self.__color="red"
    ##setter
    def set_color(self,name):##the set_color can be anyname
        self.__color=name
    ##getter
    def get_color(self):
        return self.__color
    ## or u can use decorated method
    @property
    def color(self):
        return self.__color
    @color.setter#the color is the one at the top i mean the def color(self) and the color under @property and under colour>setter can be change
    def color(self,name):
        self.__color=name
ca1=Car()
ca1.set_color="red"
print(ca1.get_color())
##how to access using the decorated method
ca1.color="Pink"
print(ca1.color)

