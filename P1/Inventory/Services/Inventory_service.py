# inventory/services/inventory_service.py

from Inventory.Models.product import Product
from Inventory.Utils.error_handling import validate_positive_number

class InventoryService:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity, price):
        validate_positive_number(quantity, "Cantidad")
        validate_positive_number(price, "Precio")
        self.products.append(Product(name, quantity, price))

    def remove_product(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                self.products.remove(p)
                return True
        return False

    def list_products(self):
        return self.products

    def sort_products(self, by="price"):
        if by == "price":
            return sorted(self.products, key=lambda p: p.price)
        elif by == "quantity":
            return sorted(self.products, key=lambda p: p.quantity)
        else:
            return self.products

    def search_product(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None
