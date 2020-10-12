#3 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_string = input("Введите положительное число")
answer_number = int(number_string) + int(number_string + number_string) + int(number_string + number_string + number_string)
print("Итоговый результат: " + str(answer_number))