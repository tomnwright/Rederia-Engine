from math import *
from copy import deepcopy as copy

class NumberArray(list):
    '''
    
    '''
    def __setitem__(self, key, value):
        
        if type(value) in (int, float,):
            super().__setitem__(key, value)
        else:
            raise TypeError(
                'MatrixData modification: MatrixData can only contain int and float; not {}.'.format(type(value))
            )
        return
    def dot(self, a):
        return NumberArray.Dot(self, a)

    @staticmethod
    def Dot(a, b):
        '''
        Caluculates the dot product of two number arrays, a and b.
        '''
        bA, bB = isinstance(a, NumberArray), isinstance(b, NumberArray)
        if not (bA and bB):
            raise TypeError("Cannot calculate dot product of {} and {}".format(type(a), type(b)))
        
        L = len(a)
        if L != len(b):
            raise ValueError("Cannot multiply NumberArrays of different lengths.")

        return sum(
            [ ( a[i]* b[i] ) for i in range(L) ]
        )
class Matrix:
    '''
    2D number matrix,
    stored as lists of NumberArray lists,
    in column form [[column1], [column2], ...]
    eg. 3x1 : [[1, 2, 3]]

    Using NumberArray allows validation of individualy set matrix values.
    eg. matrix[0][0] = 5.
    '''
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        #CheckMatrixData will run once for every new instance. Considering removing for performance
        validate = Matrix.Tools.CheckData(value)

        if validate:
            raise validate
        else:
            self._data = Matrix.Tools.HomoNest([NumberArray(c) for c in value])
            return
    @data.deleter
    def data(self):
        '''Delete self.data'''
        del self._data


    def __init__(self, data = []):
        self.data = data     
    def __getitem__(self, key):
        return self.data[key]
    def __str__(self):
        return str(self.data)

    def __add__(self, m):
        if not isinstance(m, Matrix):
            raise TypeError("unsupported operand type(s) for +:  '{}' and '{}'".format(type(self).__name__, type(m).__name__))
        
        l = m.width == self.width
        h = m.height == self.height

        if not (l and h):
            raise ValueError("Uncompatible matrix dimensions: {}x{} + {}x{}".format(self.height, self.width, m.height, m.width))
        
        
        out = copy(self.data)
        for i, column in enumerate(out):
            for j, n in enumerate(column):

                out[i][j] += m[i][j]
        
        #makes sure function works for inherited
        outInst = type(self)()
        outInst.data = out
        return outInst
    def __sub__(self, m):
        if not isinstance(m, Matrix):
            raise TypeError("unsupported operand type(s) for +:  '{}' and '{}'".format(type(self).__name__, type(m).__name__))
        
        return self + (-1 * m)
    def __mul__(self, a):
        if type(a) in (float, int):
            out = copy(self.data)
            for i, column in enumerate(out):
                for j, n in enumerate(column):

                    out[i][j] *= a
            
            #makes sure function works for inherited classes
            outInst = type(self)()
            outInst.data = out
            return outInst
        elif isinstance(a, Matrix):
            #MATRIX MULTIPLICATION
            return Matrix.Tools.Multiply(self, a)
        else:
            raise TypeError("unsupported operand type(s) for *: {} and {}.".format(type(self).__name__, type(a).__name__))
    __rmul__ = __mul__
    def __truediv__(self, s):
        if type(s) in (float, int):
            out = copy(self.data)
            for i, column in enumerate(out):
                for j, n in enumerate(column):

                    out[i][j] /= s
            
            #makes sure function works for inherited classes
            outInst = type(self)()
            outInst.data = out
            return outInst
        else:
            raise TypeError("Cannot divide Matrix by type {}".format(type(s)))

    
    @property
    def width(self):
        '''Number of columns'''
        return len(self.data)
    @property
    def height(self):
        '''Number of rows'''
        out = 0
        for c in self.data:
            if len(c) > out:
                out = len(c)
        return out
        
    @property
    def columns(self):
        '''
        Returns a list of columns (class: NumberArray)
        '''
        return Matrix.Tools.HomoNest(self.data)
    @property
    def rows(self):
        '''
        Returns a list of rows (class: NumberArray)
        '''
        h = self.height
        out = [NumberArray() for i in range(h)]

        for i, col in enumerate(self.data):
            for j, element in enumerate(col):
                out[j].append(element)

        return Matrix.Tools.HomoNest(out)

    def Print(self):
        print("\n".join([str(i) for i in self.rows]))

    class Tools:
        @staticmethod
        def CheckData(data):
            '''
            Validates potential data set structure.
            Returns False if data ok.
            Returns Exception object if found.
            ''' 
            if not isinstance(data, list):
                return TypeError(
                    'Matrix data must be list; not {}.'.format(type(data))
                )

            for i, column in enumerate(data):
                
                if not isinstance(column, list):
                    return TypeError(
                        'Matrix column at position {} must be list; not {}.'.format(i, type(column))
                    )

                for j, n in enumerate(column):

                    if type(n) not in (int, float,):
                        return TypeError(
                            'Matrix data at position {},{} - Matrix can only contain int and float; not {}.'.format(i, j, type(n))
                        )      
            
            return False

        @staticmethod
        def HomoNest(nest):
            '''
            (Nest Homogeniser)
            Takes list of NumberArrays (copy),
            adds 0 to make them the same length,
            '''
            nList = copy(nest)

            L = 0
            homo = True

            for array in nList:
                if len(array) < L:
                    homo = False
                else:
                    L = len(array)

            if homo:
                return nList
            
            for array in nList:
                array += [0] * (L - len(array))
            return nList

        @staticmethod
        def Multiply(b,a):

            '''
            Takes two Matrix instances,
            multiplies b by a:
            performs b(a)
            '''

            if b.width != a.height:
                raise ValueError("Wrong Matrix dimensions for multiplication.")

            nH, nW = b.height, a.width

            data = []

            for i in range(nW):
                col = NumberArray()

                for j in range(nH):

                    val = NumberArray.Dot(
                        b.rows[j],
                        a.columns[i]
                    )
                    col.append(val)
                
                data.append(col)
            
            out = type(a)()
            out.data = data
            return out          
class Vector3(Matrix):

    def __init__(self, x = 0, y = 0, z = 0):
        super().__init__([[x, y, z]])
    def __str__(self):
        return "v({}, {}, {})".format(self.x, self.y, self.z)

    @property
    def x(self):
        return self.data[0][0]
    @x.setter
    def x(self, value):
        self.data[0][0] = value
        return

    @property
    def y(self):
        return self.data[0][1]
    @y.setter
    def y(self, value):
        self.data[0][1] = value
        return
        
    @property
    def z(self):
        return self.data[0][2]
    @z.setter
    def z(self, value):
        self.data[0][2] = value
        return

    @property
    def magnitude(self):
        return sqrt((self.x ** 2)+(self.y ** 2)+(self.z ** 2))
    @magnitude.setter
    def magnitude(self, value):
        scale = value / magnitude
        #self *= scale
        return

    #standard vectors
    @property
    def unit(self):
        return Vector3(1,1,1)
    @property
    def zero(self):
        return Vector3(self)
    @property
    def left(self):
        return Vector3(-1,0,0)
    @property
    def right(self):
        return Vector3(1,0,0)
    @property
    def forward(self):
        return Vector3(0,1,0)
    @property
    def backward(self):
        return Vector3(0,-1,0)
    @property
    def up(self):
        return Vector3(0,0,1)
    @property
    def down(self):
        return Vector3(0,0,-1)
    
    def ToMatrix(self):
        return Matrix(self.data)
    @staticmethod
    def FromMatrix(matrix):
        out = Vector3()
        out.data = matrix.data
        return out

if __name__ == '__main__':
    pass