class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.quantity=0
    def __str__(self):
        return (f"{self.name} price:{self.price} quantity :{self.quantity}")
class Cart:
    def __init__(self):
        self.products={}
        
    def add_product(self,product,quantity):
        if quantity<=0:
            return "negative or zero not accepted "
        
        self.products[product]=quantity
        return self.products        
    def remove_One_product(self,product):
        if product in self.products:
            self.products[product]-=1
            if self.products[product]==0:
                self.products.pop(product)
                return "product"
            return "successfully removed on product"
        else:
            return "does not exist"
        
    #     for i in self.products:
    #         if i.name==product.name and i.quantity>0:
    #             i.quantity-=1
    #             if i.quantity==0:
    #                 self.products.remove(i)
    #                 return "product removed"
    #             return "successfully removed one quantity of the product"
        
#         return "Product does not exist"
    def remove_per_quantity(self,product,quantity):
        if product in self.products:
            self.products[product]-=quantity
            if self.products[product]==0:
                self.products.pop(product)
                return "success"
        else:
            return "does not exist"


#         for i in self.products:
#             if i.name==product.name and i.quantity>0:
#                 if quantity>i.quantity:
#                     return " product in cart is less than quantity entered"
#                 i.quantity-=quantity
#                 if i.quantity==0:
#                     self.products.remove(i)
#                     return "product removed"
#                 return "successfully removed quantity entered by user"
        
#         return "Product does not exist"
        
    def remove_product(self,product):
        if product in self.products:
            self.products.pop(product)
            return "success"
        else:
            return "does not exist"

    def calculate_total(self):
        total=0
        for i,a in self.products.items():
            total += i.price*a
        return (total)

class Customer:
    def __init__(self,name,cart):
        self.cart=cart
        self.name=name
        
    


# dell=Product("dell laptop",200)

iphone11=Product("iphone 11",200)
dell=Product("laptop",200)

cart1=Cart()
Osei=Customer("Yaw",cart1)
cart2=Cart()
Rabby=Customer("Kofi",cart2)

# cart1.add_product(dell,20)
# print(cart1.remove_per_quantity(iphone11,1))
# print(cart1.calculate_total())

Rabby.cart.add_product(dell,2)
print(Rabby.cart.calculate_total())
Osei.cart.add_product(iphone11,99)
Osei.cart.add_product(iphone11,48)
print(Osei.cart.calculate_total())

# Osei.show_products(cart2)
# print(cart2.calculate_total())

# Osei=Customer("Osei Bio",cart2)

# Jandra=Customer("Jandra",cart1)
# print(Jandra.cart.add_product(iphone11,45))
# # print(Jandra.cart.add_product(iphone11,12))
# print(Jandra.cart.add_product(dell,12))
# print(Jandra.cart.calculate_total())
# Osei=Customer("Osei Bio",cart2)
# print(Osei.cart.add_product(iphone11,1))
# print(Osei.cart.add_product(iphone11,1))
# print(Osei.cart.add_product(dell,12))
# Osei.cart.calculate_total()


# print(Jandra.cart.add_product(dell,20))
# print(Jandra.cart.add_product(dell,20))
# print(Jandra.cart.add_product(iphone11,20))
# # print(Jandra.cart.remove_One_product(dell))
# print(Jandra.cart.remove_per_quantity(dell,20))
# print(Jandra.cart.remove_product(iphone11))
# print(Jandra.cart.calculate_total())
# cart2=Cart()
# 
# Osei.cart.add_product(dell,1)
# print(Osei.cart.calculate_total())