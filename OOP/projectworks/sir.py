class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:

    def __init__(self):
        self.cart_item = {}
        self.total = 0

    def find_product(self, product):
        if product.name in self.cart_item:
            return True
        else:
            return False

    def add_product(self, product, quantity):
        # check quantity
        product_exists = self.find_product(product)
        if product_exists:
            qty_left = (product.quantity - self.cart_item[product.name])
            # check quantity
            if quantity <= qty_left:
                self.cart_item[product.name] += quantity
                # self.cart_item[product.price] += (quantity * product.price)
                self.total += (quantity * product.price)
                print(f'Product {product.name} added to the cart')
            else:
                print(f'quantity exceed the available product quantity')
        else:
            if quantity <= product.quantity:
                self.cart_item[product.name] = quantity
                self.total += product.price * quantity
                print(f'Product {product.name} added to the cart')
            else:
                print(f'quantity exceed the available product quantity')

    def remove_product(self, product):
        if product.name in self.cart_item:

            self.total -= (self.cart_item[product.name] * product.price)
            self.cart_item.pop(product.name)
        else:
            print(f'Product is not in there')

    def calculate_total(self):
        print(f'total: {self.total}')


class Customer:
    def __init__(self, name, cart = {}):
        self.name = name
        self.cart = cart

    def display(self):
        print(f'Customer {self.name} cart: {self.cart.cart_item}')


banana = Product('Banana', 200, 5)
orange = Product('Orange', 100, 2)
pawpaw = Product('Pawpaw', 50, 10)

cart1 = Cart()
cart2 = Cart()

cart1.add_product(banana, 3)
cart1.add_product(banana, 2)
cart1.add_product(orange, 2)
cart1.add_product(pawpaw, 4)
cart2.add_product(banana, 3)
cart1.remove_product(banana)

cart1.calculate_total()

philip = Customer('Philip', cart1)
philip1 = Customer('Philip1', cart2)
philip.display()
philip1.display()
cart2.calculate_total()
