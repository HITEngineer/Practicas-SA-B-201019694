# inventory/utils/error_handling.py

def validate_positive_number(value, field_name):
    if value < 0:
        raise ValueError(f"{field_name} debe ser un número positivo.")
