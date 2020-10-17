# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_information(name, surname, birthyear, city, email, phone):
    string_info = "Пользователь: %s %s, год рождения: %i, город проживания: %s, адрес электронной почты: %s, телефон: %s" % (
    name, surname, birthyear, city, email, phone)
    print(string_info)
    return string_info


name = ""
surname = ""
birthyear = 0
city = ""
email = ""
phone = ""

user_input = input("""Введите через запятую (", "): имя, фамилию, год рождения, город проживания, e-mail, номер телефона """)
list_user_input = user_input.split(',')
for i in list_user_input:
    if list_user_input.index(i) == 0:
        name = i
    elif list_user_input.index(i) == 1:
        surname = i
    elif list_user_input.index(i) == 2:
        birthyear = int(i)
    elif list_user_input.index(i) == 3:
        city = i
    elif list_user_input.index(i) == 4:
        email = i
    elif list_user_input.index(i) == 5:
        phone = i

user_information(name, surname, birthyear, city, email, phone)

