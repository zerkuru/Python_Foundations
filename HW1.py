#1 Поработайте с переменными, создайте несколько, выведите на экран, 
#запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

building_name = input('Введите название здания')
building_height = int(input('Введите высоту здания'))
building_apart_per_floor = int(input('Введите количество квартир на этаже'))
apartments = building_height * building_apart_per_floor
print("В здании " + building_name + " " + str(building_height) + " этажей и " + str(apartments) + " квартир")

#2 Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк. 

time_in_seconds = int(input('Введите время в секундах'))
days = time_in_seconds // (3600*24)
left_from_days = time_in_seconds % (3600*24)
hours = left_from_days // 3600
left_time = time_in_seconds % 3600
minutes = left_time // 60
seconds = left_time % 60

time_in_string = '%02d:%02d:%02d' % (hours, minutes, seconds)
if days != 0:
	answ_time = "Всего " + str(days) + " дней и " + time_in_string
else:
    answ_time = "Итого: " + time_in_string
print(answ_time)

#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_string = input("Введите положительное число")
answer_number = int(number_string) + int(number_string + number_string) + int(number_string + number_string + number_string)
print("Итоговый результат: " + str(answer_number))

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

#5. Запросите у пользователя значения выручки и издержек фирмы. 
#Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
 #Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

total_income = int(input("Введите общую выручку компании: "))
total_cost = int(input("Введите общие издержки компании: "))
profit = total_income - total_cost
if profit > 0:
	print("Компания отработала с прибылью " + str(profit))
	percent_profit = float(profit/total_income) * 100 
	print("Рентабельность выручки составила: " + str(percent_profit) + " процентов")
	employees = int(input("Введите количество сотрудников фирмы: "))
	profit_per_person = profit/employees
	print("На одного сотрудника приходится " + str(profit_per_person) + " части прибыли")
elif profit == 0: 
	print("Компания отработала в ноль, издержки равны доходам")
elif profit < 0:
	print("Компания оотработала в убыток " + str(profit))

#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
#Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
#Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

initial_run = float(input("Сколько километров пробежал спортсмен в первый день? "))
final_run = float(input("Сколько в итоге он должен пробежать километров? "))
number_days = 0
while initial_run < final_run:
	initial_run += (initial_run / 10)
	number_days +=1
print("Всего спортсмену понадобится " + str(number_days) + " полных дней для достижения результата ")


