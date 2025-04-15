# Product class represents each item for sale
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

    def __str__(self):
        return f"{self.name} - Rs {self.price} (Stock: {self.stock})"

# ShoppingCart class manages items user wants to buy
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

    def total_price(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def view_cart(self):
        for product, qty in self.items.items():
            print(f"{product.name} x {qty} = Rs {product.price * qty}")
        print(f"Total: Rs {self.total_price()}")

# Customer class with their own cart
class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        return self.cart.add_product(product, quantity)

    def remove_from_cart(self, product):
        return self.cart.remove_product(product)

# Order class finalizes customer purchases
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.total = self.customer.cart.total_price()

    def summary(self):
        print(f"Order Summary for {self.customer.name}:")
        self.customer.cart.view_cart()
        print(f"Grand Total: Rs {self.total}")

# Example usage
if __name__ == "__main__":
    # Create some products
    p1 = Product("T-Shirt", 800, 10)
    p2 = Product("Jeans", 1500, 5)

    # Create customer
    customer1 = Customer("Sania")

    # Add items to cart
    customer1.add_to_cart(p1, 2)
    customer1.add_to_cart(p2, 1)

    # View cart
    customer1.cart.view_cart()

    # Finalize order
    order = Order(customer1)
    order.summary()
