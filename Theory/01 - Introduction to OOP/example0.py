# Система управления магазином

# Проблема отслежиания товаров

# называем переменные item1 подразумевая что это один товар
# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity 

# в языке программирования Python каждый тип данных это объект, 
# который был создан ранее на основе какого-либо класса
# print(type(item1))

# В Python с помощью классов мы можем создавать собственные типы данных

# как создать класс и как создать на его основе объект?
# когда говорят объект или эксземпляр класса имеют в виду одно и тоже 

class Item:
    pass

item1 = Item()

# random_str = str("4") 
# тоже самое что
# random_str = "4"


# каждый из атрибутов присвается одному экземпляру класса
item1.name = "Phone"
item1.price = 100
item1.quantity = 5


print(item1)
print(item1.name)
print(item1.price)


some_str = "ab"
# метод строк
print(some_str.upper())


# Создадим класс с методами

class SuperItem:
    # метод это функция которая находиться внутри класса
    #  который вычисляет общую тему 
    def calculate_total_price(self, x, y):
        return x * y




item1 = SuperItem()
item1.name = "Телефон "
item1.price = 100
item1.quantity = 5
item1.calculate_total_price(item1.price, item1.quantity)

item2 = SuperItem()
item2.name = "Ноутбук"
item2.price = 1000
item2.quantity = 3
item2.calculate_total_price(item2.price, item2.quantity)