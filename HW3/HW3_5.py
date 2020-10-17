#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
#Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введен после нескольких чисел,
#то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def check_for_exit(userlist, special):
    laststr = userlist[-1]
    lastlit = laststr[-1]
    if lastlit == special:
        return True
    else:
        return False

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def add_to_sum(current_sum, userlist, special):
    laststr = userlist[-1]
    lastlit = laststr[-1]
    if lastlit == special:
        laststr = laststr[:-1]
        userlist.insert(-1,laststr)
    notnum = False
    newlist = []
    for i in userlist:
        if is_digit(i):
            newlist.append(float(i))
        else:
            newlist.append(i)
            notnum = True
    for i in newlist:
        if notnum:
            current_sum = str(current_sum) + str(i)
        else:
            current_sum = current_sum + i
    return current_sum



special = input("Введите спец символ, по которому будет происходить завершение программы: ")
need_exit = False
first_time = True
current_sum = 0
while need_exit==False:
    if first_time:
        userline = input("Вводите числа, разделенные пробелом. \n При продолжении ввода числа будут приплюсованы к предыдущей сумме. \n При вводе %s программа завершит работу \n: "%special)
        first_time = False
    else:
        userline = input(": ")
    userlist = userline.split()
    need_exit = check_for_exit(userlist, special)
    current_sum = add_to_sum(current_sum, userlist, special)
    print("Сумма всех введенных слагаемых: " + str(current_sum))



