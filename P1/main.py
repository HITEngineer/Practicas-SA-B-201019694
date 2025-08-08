# main.py

from inventory.services.inventory_service import InventoryService
from inventory.ui.cli import InventoryCLI

if __name__ == "__main__":
    inventory_service = InventoryService()
    cli = InventoryCLI(inventory_service)
    cli.prompt_user()
