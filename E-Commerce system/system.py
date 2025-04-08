class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            self.items[product] = self.items.get(product, 0) + quantity
            return True
        return False

    def remove_product(self, product):
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]
            return True
        return False

    def apply_discount(self, percentage):
        return sum(product.price * qty * (1 - percentage / 100) for product, qty in self.items.items())


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        return self.cart.add_product(product, quantity)

    def remove_from_cart(self, product):
        return self.cart.remove_product(product)


class Order:
    def __init__(self, customer):
        self.customer = customer 
