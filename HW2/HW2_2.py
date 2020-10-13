#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
list_test = list(input("Введите список элементов, разделенных пробелом"))
userList = str(list_test).split()
print("Ваш список:" + str(userList))
incount = 0

while incount < len(list_test):
    el1 = list_test[incount]
    new_inc = incount + 1;
    if new_inc < len(list_test):
        el2 = list_test[new_inc]
        list_test.insert(new_inc, el1)
        del list_test[incount]
        list_test.insert(incount, el2)
    incount +=2
userList = list_test.split()
print("Итоговый список:" + str(userList))