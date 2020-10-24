#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("try3.txt", 'r', encoding='utf-8') as f_obj:
    salary = {}
    for line in f_obj:
        linelist = line.split(" ")
        salary[linelist[0]] = linelist[1]
    print("Оклад меньше 20000 имеют: ")
    totalsalary = 0
    for employee in salary:
        less20 = False
        current_salary = int(salary[employee])
        totalsalary += current_salary
        if current_salary < 20000:
            print(employee)
            less20 = True
    if less20 == False:
        print("никто из сотрудников")
    avr_salary = totalsalary/ len(salary)
    print(f"Средняя зарплата: {avr_salary}")
