#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
#но с прописной первой буквой.
#Например, print(int_func(‘text’)) -> Text


def int_func(userstring):
    #userstring = capitalize(userstring)
    leftsign = userstring[0]
    leftsign = leftsign.upper()
    userstring = leftsign + userstring[1:]
    return userstring

userstring = input("Введите слово: ")
print(int_func(userstring))

userstring1 = input("Вводите слова, разделенные пробелом: ")
userlist = userstring1.split()
newlist = []
for i in userlist:
    newlist.append(int_func(i))

print(" ".join(newlist))