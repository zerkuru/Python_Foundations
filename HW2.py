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