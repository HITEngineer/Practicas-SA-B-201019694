# main.py

from Inventory.Services.Inventory_service import InventoryService
from Inventory.UI.cli import InventoryCLI

if __name__ == "__main__":
    inventory_service = InventoryService()
    cli = InventoryCLI(inventory_service)
    cli.prompt_user()
