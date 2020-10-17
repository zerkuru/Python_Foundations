#2. Представлен список чисел.
#Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
#Для формирования списка использовать генератор.
#Пример исходного списка: [300, 2, 1, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#Результат: [12, 44, 4, 10, 78, 123].
#исходный список:
from random import randint
numberlen = int(input("Введите длину исходного списка: "))
icount = 0
numbers=[]
while icount <= numberlen-1:
    newnum = randint(1, 100)
    numbers.append(newnum)
    icount +=1
print (*numbers, sep = ', ')
result = []

#обработка списка
for icount in range(numberlen-2):
    number = numbers[icount]
    number1 = numbers[icount + 1]
    if number1 > number:
        result.append(number1)

print("Итоговый список: ")
print(*result, sep = ', ')