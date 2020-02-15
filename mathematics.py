from math import *

class MatrixData(list):
    '''
    Storing matrix using MatrixData
    allows validation of individualy set matrix values.
    eg. matrix[0][0] = 5.
    '''
    def __setitem__(self, key, value):
        
        if type(value) in (int, float,):
            super().__setitem__(key, value)
        else:
            raise TypeError(
                'MatrixData modification: MatrixData can only contain int and float; not {}.'.format(type(value))
            )
        return

class Matrix:
    '''
    2D number matrix,
    stored as lists of MatrixData lists,
    in column form [[column1], [column2], ...]
    '''
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self):
        return str(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        '''Set self.data value'''
        #validate structure
        validate = Matrix.check_data(value)

        if validate:
            raise validate
        else:
            self._data = [MatrixData(c) for c in value]
            return

    @data.deleter
    def data(self):
        '''Delete self.data'''
        del self._data

    @property
    def width(self):
        out = 0
        for c in self.data:
            if len(c) > out:
                out = len(c)
        return out

    @property
    def height(self):
        return len(self.data)
        
    @classmethod
    def check_data(cls, data):
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
    
class Vector3(Matrix):

    def __init__(self, x, y, z):
        super().__init__([[x, y, z]])
    
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

if __name__ == '__main__':
    #testing
    m = Vector3(1,2,3)
    print(m.up)