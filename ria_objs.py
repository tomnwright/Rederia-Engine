from ria import *

class cube(PolyOBJ):
    def __init__(self, position = Vector3.zero, rotation = Vector3.zero, size = Vector3.unit):
        Vs = [
            Vector3(-1.0, -1.0, 1.0),
            Vector3(-1.0, 1.0, 1.0),
            Vector3(-1.0, -1.0, -1.0),
            Vector3(-1.0, 1.0, -1.0),
            Vector3(1.0, -1.0, 1.0),
            Vector3(1.0, 1.0, 1.0),
            Vector3(1.0, -1.0, -1.0),
            Vector3(1.0, 1.0, -1.0)]
        Fs = [
            [1, 2, 4, 3],
            [3, 4, 8, 7],
            [7, 8, 6, 5],
            [5, 6, 2, 1],
            [3, 7, 5, 1],
            [8, 4, 2, 6]]
        super().__init__(Vs,Fs,position,rotation,size)