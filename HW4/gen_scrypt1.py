from sys import argv

script_name, startcount, finishcount = argv
generator = (param for param in range(int(startcount), int(finishcount)+1))

for el in generator:
    print(el)


