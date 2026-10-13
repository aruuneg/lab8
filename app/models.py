"""Simple domain models used by the CI lab."""


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"User {self.name}"


class Product:
    def __init__(self, name: str, price: float, description: str):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price
        self.description = description
