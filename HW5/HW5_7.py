#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
#название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
#а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список.
#Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json
with open("try7.txt", 'r', encoding='utf-8') as f_obj:
    linelist = []
    for line in f_obj:
        linelist.append(line)
companydict = {}
average_profit = {}

number_of_companies = 0
totalprofit = 0
for line in linelist:
    newlist = line.split(" ")
    company = newlist[0]
    income = int(newlist[2])
    cost = int(newlist[3])
    profit = income - cost
    companydict[company] = profit
    if profit > 0:
        totalprofit +=profit
        number_of_companies +=1
if number_of_companies == 0:
    average_profit["average_profit"] = 0
else:
    average_profit["average_profit"] = totalprofit/number_of_companies
finallist = []
finallist.append(companydict)
finallist.append(average_profit)

with open("new_file_7.json", "a", encoding='utf-8') as write_f:
    json.dump(finallist, write_f, ensure_ascii=False)