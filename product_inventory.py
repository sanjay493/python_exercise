class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    def update_stock(self,qty):
        self.quantity += qty
        return self.quantity
    def invetory_value(self):
        return self.price * self.quantity
    
#  use __str__ method to return string representation of object
    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    #how to use it

Orange = Product(101, "Orange", 50, 200)
print(Orange)
    # Output: Product ID: 101, Name: Orange, Price: 50,