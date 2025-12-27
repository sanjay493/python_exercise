class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        if price <= 0:
            raise ValueError("Price must be greater than zero")
        if quantity <0:
            raise ValueError("Quantity cannot be negative")
        self.price = price
        self.quantity = quantity
    def update_stock(self,qty):
        if qty < 0:
            raise ValueError("Quantity to add cannot be negative")
        self.quantity += qty
        return self.quantity
    def invetory_value(self):
        return self.price * self.quantity
    
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "inventory_value": self.invetory_value()
        }
    
#  use __str__ method to return string representation of object
    def __str__(self):
        return (f"Product[ID: {self.product_id} | "
                f"Name: {self.name} | "
                 f"Price: {self.price} | "
                 f"Quantity: {self.quantity}]")
    
    #how to use it

orange = Product(101, "Orange", 50, 200)
print(orange)
    # Output: Product ID: 101, Name: Orange, Price: 50,

orange.update_stock(10)

print(orange.invetory_value())
print(orange.to_dict())

