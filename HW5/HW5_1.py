#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.
linelist = []
print("Вводите данные для записи в файлю Ввод данных будет закончен, как только будет введена пустая строка");
while True:
    newline = input(": ")
    if newline == "":
        break
    else:
        linelist.append(newline)
try:
    user_new_file = open("new_file.txt", "a")
    user_new_file.writelines(linelist)
    user_new_file.close()
except IOError:
    user_new_file = open("new_file.txt", "w+")
    user_new_file.seek(0)
    user_new_file.writelines(linelist)
    user_new_file.close()
