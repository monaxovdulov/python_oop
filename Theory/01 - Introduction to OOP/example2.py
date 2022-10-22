# магазин который продает телефоны и ноутбуки одной модели

storage = [
    {
        "name_item":"Laptop",
        "price":"30000",
        "count":1
    },
    {
        "name_item":"Phone",
        "price":"10000",
        "count":1
    }
]



while True:
    user_choice = input("""Программа МАГАЗИНУС-ТОВАРУС 1.0 
ГЛАВНОЕ МЕНЮ
1 - Посмотеть содержимое склада
2 - Посчитать общую стоимость товаров
3 - Добавить товары
4 - Выход
Вводить сюда $>""")
    if user_choice == "1":
        for i in storage:
            print(f'Товар:{i["name_item"]}\nЦена за штуку:{i["price"]}\nКоличество:{i["count"]}')

    elif user_choice == "2":
        pass
    elif user_choice == "3":
        user_choice = input("""МЕНЮ ДОБАВЛЕНИЯ ТОВАРОВ\nВыберите что хотите добавить\n1 - ноутбук\n2 - телефон""")
        if user_choice == "1":
            pass
        elif user_choice == "2":
            pass
    elif user_choice == "4":
        print("Хороших выходных!")
        break
    else:
        print("Ошибка выбора")
        
        




