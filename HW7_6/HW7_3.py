class Cell():
    pieces = 0
    def __init__(self, pieces):
        self.pieces = pieces
    def __add__(self, other):
        newcell = Cell(self.pieces + other.pieces)
        return newcell
    def __sub__(self, other):
        if self.pieces - other.pieces >= 2:
            newcell = Cell(self.pieces - other.pieces)
            return newcell
        else:
            print("Вычесть можно только клетку на 2 ячейки и более меньшую, чем та, из которой вычитают")
    def __mul__(self, other):
        newcell = Cell(self.pieces * other.pieces)
        return  newcell
    def __truediv__(self, other):
        newcell = Cell(self.pieces//other.pieces)
    def make_order(self, number_in_lines):
        newstring = ""
        totalnum  = self.pieces
        linenum = totalnum//number_in_lines
        rest_pieces = totalnum%number_in_lines
        icount = 1
        while icount <= linenum:
            jcount = 1
            currentstring = ""
            while jcount <= number_in_lines:
                currentstring += "*"
                jcount +=1
            newstring += currentstring + "\n"
            icount += 1
        currentstring = ""
        kcount = 1
        while kcount <= rest_pieces:
            currentstring +="*"
            kcount +=1
        newstring += currentstring + "\n"
        print(newstring)
        return newstring


Cell1 = Cell(10)
Cell1.make_order(3)
Cell2 = Cell(30)
Cell2.make_order(4)
Cell3 = Cell(31)
Cell3.make_order(34)

Cell4 = Cell3 - Cell2
try:
    Cell4.make_order(5)
except AttributeError:
    print(AttributeError)
Cell5 = Cell2 - Cell1
Cell5.make_order(2)
Cell6 = Cell1+ Cell2 + Cell3
Cell6.make_order(5)
