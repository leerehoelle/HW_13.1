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
        if not isinstance(self, Product):
            raise ValueError('Мы не можем добавлять то, что не является экземпляром класса Product')
        self.__goods.append(product)
        Category.unique_products += 1

    @property
    def goods(self):
        goods_list = []
        for item in self.__goods:
            goods_list.append(f'{item.name}, {item.price} руб. Остаток: {item.quantity} шт.')
        return goods_list

    def __len__(self):
        return len(self.__goods)

    def __str__(self):
        goods_list = []
        for item in self.__goods:
            goods_list.append(len(item))
        return f"{self.name}, количество продуктов: {sum(goods_list)} шт."


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


    def sum_price(self):
        return self.quantity * self.price


    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только между экземплярами одного класса')
        return self.sum_price() + other.sum_price()


    def __len__(self):
        return self.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color



class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germin_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germin_period = germin_period
        self.color = color
