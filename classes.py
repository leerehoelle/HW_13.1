class Category:
    name: str
    description: str
    goods: list
    total_number = 0
    unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_number += len(self.goods)
        Category.unique_products += 1


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
