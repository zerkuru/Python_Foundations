#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.

def translate_from_english(newword):
    englishdict = {}
    englishdict["One"] = "Один"
    englishdict["Two"] = "Два"
    englishdict["Three"] = "Три"
    englishdict["Four"] = "Четыре"
    translation = englishdict[newword]
    return translation

with open("try4.txt", 'r', encoding='utf-8') as f_obj:
    totallist = []
    for line in f_obj:
        linelist = line.split(" ")
        totallist.append(linelist)

with open("new_file4.txt", 'a', encoding='utf-8') as f_obj_new:
    for newline in totallist:
        numeral = newline[0]
        newline.remove(numeral)
        numeral = translate_from_english(numeral)
        newline.insert(0,numeral)
        f_obj_new.write(" ".join(newline))
