from sys import argv

script_name, hourly_rate, hours, premium = argv
salary = (int(hours)*int(hourly_rate)+int(premium))

print("Имя скрипта: ", script_name)
print("Ставка в час: ", hourly_rate)
print("Часы: ", hours)
print("Премия: ", premium)
print("Итого зарплата: ", salary)