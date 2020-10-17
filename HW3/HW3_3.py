#3. Реализовать функцию my_func(),
#которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def max_sum(a, b, c):
    listnum = []
    listnum.append(a)
    listnum.append(b)
    listnum.append(c)
    listnum.sort()
    if is_digit(listnum[1]):
        if is_digit(listnum[2]):
            newsum = float(listnum[1]) + float(listnum[2])
        else:
            newsum = listnum[1]+listnum[2]
    else:
        newsum = listnum[1] + listnum[2]
    return newsum

a = input("Введите первый аргумент: ")
b = input("Введите второй аргумент: ")
c = input("Введите третий аргумент: ")
newsum = max_sum(a, b, c)
print("Сумма максимальных двух аргументов: %s"%newsum)