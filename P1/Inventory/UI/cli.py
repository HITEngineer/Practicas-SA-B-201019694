# inventory/ui/cli.py

class InventoryCLI:
    def __init__(self, inventory_service):
        self.service = inventory_service

    def display_menu(self):
        print("\n==== INVENTARIO ====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar lista de productos")
        print("4. Ordenar productos")
        print("5. Buscar producto")
        print("6. Salir")

    def prompt_user(self):
        while True:
            self.display_menu()
            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.delete_product()
            elif choice == "3":
                self.show_products()
            elif choice == "4":
                self.sort_products()
            elif choice == "5":
                self.search_product()
            elif choice == "6":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")

    def add_product(self):
        try:
            name = input("Nombre: ")
            quantity = int(input("Cantidad: "))
            price = float(input("Precio: "))
            self.service.add_product(name, quantity, price)
            print("Producto agregado.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_product(self):
        name = input("Nombre del producto a eliminar: ")
        if self.service.remove_product(name):
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def show_products(self):
        products = self.service.list_products()
        if not products:
            print("No hay productos.")
        for p in products:
            print(p)

    def sort_products(self):
        by = input("Ordenar por 'price' o 'quantity': ")
        products = self.service.sort_products(by)
        for p in products:
            print(p)

    def search_product(self):
        name = input("Nombre del producto a buscar: ")
        product = self.service.search_product(name)
        if product:
            print(product)
        else:
            print("Producto no encontrado.")
