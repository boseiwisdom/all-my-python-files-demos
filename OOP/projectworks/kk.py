class Product:
    def __init__(self,name,price,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity
    def _str_(self):
        return (f"{self.name} price:{self.price} quantity :{self.quantity}")
class Cart:
    def __init__(self):
        self.products=[]
    def add_product(self,product,quantity):
        if quantity<=0:
                return "negative or zero not accepted "
        for i in self.products:
            if i.name==product.name :
                i.quantity+=quantity
                return "success"
          
        self.products.append(product)
        product.quantity+=quantity
        return "successfully done"
        
    def remove_One_product(self,product):
        for i in self.products:
            if i.name==product.name and i.quantity>0:
                i.quantity-=1
                if i.quantity==0:
                    self.products.remove(i)
                    return "product removed"
                return "successfully removed one quantity of the product"
        
        return "Product does not exist"
    def remove_per_quantity(self,product,quantity):
        for i in self.products:
            if i.name==product.name and i.quantity>0:
                if quantity>i.quantity:
                    return " product in cart is less than quantity entered"
                i.quantity-=quantity
                if i.quantity==0:
                    self.products.remove(i)
                    return "product removed"
                return "successfully removed quantity entered by user"
        
        return "Product does not exist"
        
    def remove_product(self,product):
        for i in self.products:
            if i.name==product.name:
                self.products.remove(i)
                return "successfully removed"
        return "Product does not exist"
    def calculate_total(self):
        total=0
        for product in self.products:
            total+= product.price*product.quantity
        return (f"total amount :${total}")
class Customer:
    def __init__(self,name,cart):
        self.name=name
        self.cart=cart

dell=Product("dell laptop",200)
print(dell)
iphone11=Product("iphone 11",200)
cart1=Cart()
cart2=Cart()
cart1.calculate_total()
# Jandra=Customer("Jandra",cart1)
# print(Jandra.cart.add_product(dell,20))
# print(Jandra.cart.add_product(dell,20))
# print(Jandra.cart.add_product(iphone11,20))
# print(Jandra.cart.remove_One_product(dell))
# print(Jandra.cart.remove_per_quantity(dell,20))
# print(Jandra.cart.remove_product(iphone11))
# print(Jandra.cart.calculate_total())
# Rabby=Customer("Kofi",cart2)
# print(Rabby.cart.add_product(iphone11,1))
# print(Rabby.cart.calculate_total())
cart1.add_product(iphone11,2)
print(cart1.calculate_total())
cart2.add_product(iphone11,1)
print(cart2.calculate_total())
