# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
def getdigitfrom(currenline):
    numstring = ''
    icount = 0
    while icount < len(currenline):
        current_symbol = currenline[icount]
        if current_symbol.isdigit():
            numstring += current_symbol
        icount += 1
    return numstring


def get_number_hours(userlist):
    currentnum = 0
    numberstring = ''
    for subline in userlist:
        current_symbol = subline[0]
        if current_symbol.isdigit():
            numberstring = getdigitfrom(subline)
            currentnum += int(numberstring)
    return currentnum

with open("try6.txt", 'r', encoding='utf-8') as f_obj:
    linelist = []
    for line in f_obj:
        linelist.append(line)
subjects_study = {}
for newline in linelist:
    newlist = newline.split(" ")
    totalnum = get_number_hours(newlist)
    subj = newlist[0]
    subjects_study[subj] = totalnum
print("Итоговый словарь:")
for i in subjects_study:
    print(f"{i} {subjects_study[i]}")
