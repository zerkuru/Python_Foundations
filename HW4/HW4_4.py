#4. Представлен список чисел.
#Определить элементы списка, не имеющие повторений.
#Сформировать итоговый массив чисел, соответствующих требованию.
#Элементы вывести в порядке их следования в исходном списке.
#Для выполнения задания обязательно использовать генератор.
#Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#Результат: [23, 1, 3, 10, 4, 11]
from random import randint
numberlen = int(input("Введите длину исходного списка: "))
icount = 0
numbers=[]
while icount <= numberlen:
    newnum = randint(1, 20)
    numbers.append(newnum)
    icount +=1
print (*numbers, sep = ', ')
result = []
for number in numbers:
    if numbers.count(number) == 1:
        result.append(number)
print("Итоговый список: ")
print(*result, sep = ', ')