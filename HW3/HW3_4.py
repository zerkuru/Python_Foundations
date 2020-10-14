#4. Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y.
#Задание необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x,y):
    x = float(x)
    x = 1/x
    y = abs(y)
    resultnum = float(0)
    if y == 1:
        resultnum = x
    elif y == 0:
        resultnum = 1
    else:
        icount = 2
        resultnum = x
        while icount <=y:
            resultnum = resultnum * x
            icount +=1
    return resultnum

x = input("Введите действительное положительное число: ")

icount = 0
while icount < 1:
    try:
        x = float(x)
        icount = 1
    except Exception:
        print("Вы ввели не действительное положительное число ")
        x = input("Введите действительное положительное число: ")
        continue

y = input("Введите целое отрицательное число: -")
icount = 0
while icount < 1:
    if y.isdigit():
        y = int(y)
        y = 0 - y
        if y > 0:
            print("Вы ввели не отрицательное число")
            y = input("Введите целое отрицательное число: -")
        else:
            icount = 1
    else:
        print("Вы ввели не число ")
        y = input("Введите целое отрицательное число: -")

resultnum = my_func(x,y)
print("Результат %f"%resultnum)