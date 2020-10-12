#4. Пользователь вводит целое положительное число. 
#Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
user_number = input("Введите целое положительное число")
length = len(user_number)
icount = 0
max_number = int(user_number[0])
while icount < length:
    current_number = int(user_number[icount])

    if current_number > max_number:
        max_number = current_number
    icount += 1
print("Цифра с самым высоким числовым значением в вашем числе: " + str(max_number))