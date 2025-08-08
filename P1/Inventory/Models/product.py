# inventory/models/product.py

class Product:
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} | Cantidad: {self.quantity} | Precio: Q{self.price:.2f}"
