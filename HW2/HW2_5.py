#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#У пользователя необходимо запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

from random import randint
length_list:int = int(input("Введите длину рейтинга:"))
max_value:int = int(input("Введите максимальное значение рейтинга:"))
icount:int = 0
total_list = []
while icount < length_list:
    total_list.insert(icount, randint(0,max_value))
    icount+=1
total_list = sorted(total_list, reverse = True)
print(str(total_list))

new_value:int = int(input("Введите новое значение (положительное число):"))

for i in total_list:
    if new_value >= i:
        new_ind = total_list.index(i)
        total_list.insert(new_ind, new_value)
        break
print(str(total_list))
