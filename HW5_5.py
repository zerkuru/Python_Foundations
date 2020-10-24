# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

lenlist = int(input("Введите длину списка чисел: "))
icount = 0
number_list = []
while icount <= lenlist:
    number_list.append(randint(1, 100))
    icount += 1

with open("new_file5.txt", 'a', encoding='utf-8') as f_obj_new:
    f_obj_new.write(" ".join(map(str,number_list)))

with open("new_file5.txt", 'r') as f_obj:
    newlist = []
    for line in f_obj:
        newlist.append(line)

newnumlist = []
for line in newlist:
    currentlist = line.split(" ")
    for i in currentlist:
        newnumlist.append(int(i))
numbersum = 0
for i in newnumlist:
    numbersum += i

print(f"Сумма случайных чисел из файла new_file5.txt: {numbersum}")
