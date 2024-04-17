class Category:
    name: str
    description: str
    __goods: list
    total_number = 0
    unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.total_number += len(self.__goods)
        Category.unique_products += 1


    def goods_addition(self, product):
        self.__goods.append(product)
        Category.unique_products += 1

    @property
    def goods(self):
        goods_list = []
        for item in self.__goods:
            goods_list.append(f'{item.name}, {item.price} руб. Остаток: {item.quantity} шт.')
        return goods_list


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def goods_addition(cls, dict_product):
        name = dict_product['name']
        description = dict_product['description']
        price = dict_product['price']
        quantity = dict_product['quantity']
        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, check_price):
        if check_price <= 0:
            print("Цена введена некорректная")
            return None
        self.__price = check_price