#2. Создать текстовый файл (не программно),
#сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open("try2.txt", 'r', encoding='utf-8') as f_obj:
    numberlines = 0
    lineinfo = []
    print('Данные файла: ')
    for line in f_obj:
        numberlines +=1
        lineinfo.append(len(line))
        print(line)
    print(f'Итого строк:{numberlines}')
    countline = 1
    for i in lineinfo:
        print(f"В {countline} строке - {i} символов")
        countline +=1

