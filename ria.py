class Vector3:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return ("({}, {}, {})".format(self.x,self.y,self.z))
    def __add__(self, vA):
        return Vector3(
            self.x+vA.x,
            self.y+vA.y,
            self.z+vA.z)
    def __mul__(self,sA):
        if type(sA) not in (float,str,):
            raise Exception('Affector must be scalar')
        return Vector3(
            self.x*sA,
            self.y*sA,
            self.z*sA)
    def vector_scale(self, vA):
        nx,ny,nz = vA * self.x , vA * self.y, vA * self.z
        return Vector3(nx,ny,nz)

    __rmul__ = __mul__
Vector3.unit = Vector3(1,1,1)
Vector3.zero = Vector3()

class Vector2:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return ("({}, {})".format(self.x,self.y))
    def __add__(self, vA):
        return Vector2(
            self.x+vA.x,
            self.y+vA.y)
    def __mul__(self,sA):
        if type(sA) not in (float,str,):
            raise Exception('Affector must be scalar')
        return Vector2(
            self.x*sA,
            self.y*sA)
    __rmul__ = __mul__
Vector2.unit = Vector2(1,1)
Vector2.zero = Vector2()

class Object3D:
    def __init__(self, position = Vector3.zero, rotation = Vector3.zero, size = Vector3.unit):
        self.position = position
        self.rotation = rotation
        self.size = size
    def translate(self, tA):
        self.position += tA
    def rotate(self, rA):
        self.rotation += rA
    def scale(self,sA):
        self.size *= sA
class PolyOBJ(Object3D):
    def __init__(self, vertices, faces, position = Vector3.zero, rotation = Vector3.zero, size = Vector3.unit):
        super().__init__(position,rotation,size)
        self.vertices = vertices
        self.faces = faces
    def global_space(self):
        gVs = []
        for vertex in self.vertices:
            n = vertex.vector_scale(self.size)
            n += self.position
            gVs.append(n)
        return gVs


import ria_objs
objects = []