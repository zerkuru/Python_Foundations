#6. * Реализовать структуру данных «Товары».
#Она должна представлять собой список кортежей.
#Каждый кортеж хранит информацию об отдельном товаре.
#В кортеже должно быть два элемента — номер товара и словарь с параметрами
#(характеристиками товара: название, цена, количество, единица измерения).
#Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

storagelist = []
i = 1
icount = 1
while i > 0:
    print("Введите данные о товаре:")
    name = input("название: ")
    price = (input("цена: "))
    try:
        price = float(price)
        price = round(price, 2)
    except Exception:
        print("Введите целое число или с дробной частью через точку")
        price = (input("цена: "))
        price = float(price)
        price = round(price, 2)
    quantity = input("количество: ")

    try:
        quantity = round(float(quantity),3)
    except Exception:
        print("Введите целое число или с дробной частью через точку")
        quantity = input("количество: ")
        quantity = round(float(quantity), 3)

    measure = input("единица измерения: ")

    itemdata = {"название":name, "цена":price, "количество":quantity, "единица измерения":measure}
    new_item = (icount, itemdata)
    storagelist.append(new_item)
    icount +=1
    prolong_list = input("""Продолжить заполнение списка? Ответьте "да" если хотите продолжить: """)
    if prolong_list == "да":
        continue
    else:
        break
print(str(storagelist))

