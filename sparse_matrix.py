import sys
sys.path.append('B:\courses\The Complete Data Structures and Algorithms Course in Python\DSA\slinkedlist.py')
from slinkedlist import Slinkedlist

class matrixEntry:
    def __init__(self, col_num, value):
        self.col_num = col_num
        self.value = value


class SparseMatrix:

    def __init__(self, nrows, ncols, defaultvalue):
        self.nrows = nrows
        self.ncols = ncols
        self.defaultvalue = defaultvalue
        self.top_list = list()
        #this is the primary list contatining the major node for the matrix

        for i in range(nrows):
            self.top_list.append(Slinkedlist())

    def set(self, row, col, value):
        for i, j in enumerate(self.top_list[row]):
            if j.col_num == col:
                if value == self.defaultvalue:
                    self.top_list[row].remove(self.top_list[row].__getitem__(i))
                    return
                else:
                    self.top_list[row].__getitem__(i).value = value
                    return
        
        new_value = matrixEntry(col, value)
        self.check_row(row)
        self.check_row(col)
        self.top_list[row].add_to_head(new_value)

    
    def get(self, row, col):
        self.check_row(row)
        self.check_row(col)

        for i, j in enumerate(self.top_list[row]):
            if j.col_num == col:
                matrixEntry = self.top_list[row].__getitem(i)
                return matrixEntry.value

        return self.defaultvalue

    def clear_value(self):
        for k in self.top_list:
            for i in k:
                self.top_list[k].remove(i)

    
    def check_row(self, row):
        if type(row) is not int:
            raise TypeError('row should be int')
        if row < 0 or row >= self.nrows:
            raise TypeError('row number is invalid')
    


    def check_col(self, col):
        if type(col) is not int:
            raise TypeError('col should be int')

        if col < 0 or col  >= self.ncols:
            raise TypeError('col number is invalid')


    def __str__(self, starting_row=0, starting_col=0, nrows=None, ncols=None):
        self.check_col(starting_col)
        self.check_row(starting_row)
        
        if nrows == None:
            nrows = self.nrows
        if ncols == None:
            ncols = self.ncols

        # starting row+row-col size should not exceed matrix size
        self.check_col(starting_col+ncols-1)
        self.check_row(starting_row+nrows-1)

        for i, j in enumerate(self.top_list):
            if i>= starting_row and i <= starting_row+nrows:
                k = 0
                while starting_col+k < starting_col+ncols:
                    current_col = starting_col+k
                    print(self.get(i, current_col), " ", end = "")
                    k+=1
                    print(" ")