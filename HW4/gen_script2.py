from random import randint
from sys import argv
script_name, list_len = argv
numberlen = int(list_len)

icount = 0
numbers=[]
while icount <= numberlen:
    newnum = randint(1, 20)
    numbers.append(newnum)
    icount +=1

generator = (i for i in numbers)

for el in generator:
    print(el)