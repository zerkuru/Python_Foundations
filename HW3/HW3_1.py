#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_function(a,b):
    answer = ""
    try:
        a = float(a)
    except Exception:
        answer = "Делимое не является числом."
    try:
        b = float(b)
    except Exception:
        answer = answer + "Делитель не является числом."
    if b == 0:
        answer = answer+ "Ошибка деления на ноль."
    elif answer == "":
        answer = str(float(a/b))
    else:
        return answer
    return answer

a = input("Введите делимое: ")
b = input("Введите делитель: ")
print("Результат деления: " + division_function(a,b))