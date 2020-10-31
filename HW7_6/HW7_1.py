#1. Реализовать класс Matrix (матрица).
#Обеспечить перегрузку конструктора класса (метод __init__()),
#который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
#Результатом сложения должна быть новая матрица.
#Подсказка:
#сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
#с первым элементом первой строки второй матрицы и т.д.
from random import randint

def MatGenerate(length, width):
  list1 = []
  max_list = []
  i = 0
  j = 0
  while i < length:
      while j < width:
          newint = randint(0, 50)
          list1.append(newint)
          j +=1
      max_list.append(list1)
      list1 = []
      j = 0
      i +=1
  return max_list



class Matrix():
    matrix_list = []
    def __init__(self, total_list):
        self.matrix_list = total_list

    def __str__(self):
        strrline = ""
        for i in self.matrix_list:
            strlist = " ".join(map(str, i))
            strrline += f"\n {strlist}"
        return strrline

    def __add__(self, *args):
        oldselfmatrix = self.matrix_list
        for next_matrix in args:
            newmatrix = []
            for linelist in next_matrix.matrix_list:
                newlist = []
                for linelist_original in self.matrix_list:
                    if next_matrix.matrix_list.index(linelist) == self.matrix_list.index(linelist_original):
                        for i in linelist:
                            for j in linelist_original:
                                if linelist.index(i) == linelist_original.index(j):
                                    k = i + j
                                    newlist.append(k)
                newmatrix.append(newlist)
            self.matrix_list = newmatrix
        result_matrix = self.matrix_list
        self.matrix_list = oldselfmatrix
        return Matrix(result_matrix)

length = int(input("Введите длину матрицы: "))
width = int(input("Введите ширину матрицы: "))


mat_list = MatGenerate(length, width)
mat_list1 = MatGenerate(length, width)
mat_list2 = MatGenerate(length, width)


Mymatrix = Matrix(mat_list)
Mymatrix1 = Matrix(mat_list1)
Mymatrix2 = Matrix(mat_list2)

print(Mymatrix)
print(Mymatrix1)
print(Mymatrix2)
NewMatrix = Mymatrix1 + Mymatrix2 + Mymatrix
print(NewMatrix)