# Inventario de Productos - Software Avanzado

## Funcionalidades
- Agregar, eliminar, listar, ordenar y buscar productos
- Validación de errores
- Código modular y limpio

## Principios SOLID aplicados

### 1. SRP - Single Responsibility
Cada clase tiene una única responsabilidad:
- `Product` representa el producto
- `InventoryService` gestiona el inventario
- `InventoryCLI` maneja la interacción con el usuario

### 2. OCP - Open/Closed Principle
El sistema permite ordenar por diferentes criterios (`price` y `quantity`) sin modificar el código base.

### 3. LSP - Liskov Substitution
Los métodos en `InventoryService` no rompen comportamiento esperado si son usados con diferentes entradas.

### 4. ISP - Interface Segregation
`CLI` solo accede a métodos de `InventoryService` necesarios para la UI, manteniendo las dependencias al mínimo.

### 5. DIP - Dependency Inversion
`InventoryCLI` depende de una abstracción (`InventoryService`), no de una implementación rígida.

## Ejemplo
```python
inventory_service = InventoryService()
inventory_service.add_product("Azúcar", 10, 5.50)
