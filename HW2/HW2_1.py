#Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. 
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list_test = ['с', '132', 132, [1,4,4], {1: 2, 2: 4, 3: 9, 4: 16}, 143.3]
for element in list_test:
	datatype_element = type(element)
	print(f"Элемент {element} - тип данных: {datatype_element}.")
