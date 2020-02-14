import numpy
from math import *

def sq(x):
    return x**2

##########################################
#############   BASICS   #################
##########################################

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
        if type(sA) not in (float,int,):
            raise Exception('Affector must be scalar')
        return Vector3(
            self.x*sA,
            self.y*sA,
            self.z*sA)    
    __rmul__ = __mul__

    def __truediv__(self, sA):
        if type(sA) not in (float,int,):
            raise Exception('Affector must be scalar')
        return Vector3(
            self.x / sA,
            self.y / sA,
            self.z / sA) 

    def straight_product(self,vA):
        return Vector3(
            self.x*vA.x,
            self.y*vA.y,
            self.z*vA.z)

    def dot_product(self, vA):
        '''Returns scalar (float) value'''
        return float((self.x*vA.x)+(self.y*vA.y)+(self.y*vA.y))

    def cross_product(self, vA):
        '''Returns Vector3D value'''
        return Vector3(
            self.y*vA.z - self.z*vA.y,
            self.z*vA.x - self.x*vA.z,
            self.x*vA.y - self.y*vA.x
            )

    def magnitude(self):
        return sqrt((self.x ** 2)+(self.y ** 2)+(self.z ** 2))

    def normalise(self):
        return self / self.magnitude()

    def rotate(self, rot):
        rotX = numpy.array([
            [1, 0, 0,],
            [0, cos(rot.x), -1 * sin(rot.x)],
            [0, sin(rot.x), cos(rot.x)],
            ])
        rotY = numpy.array([
            [cos(rot.y), 0, sin(rot.y),],
            [0, 1, 0,],
            [-1* sin(rot.y), 0, cos(rot.y),],
            ])
        rotZ = numpy.array([
            [cos(rot.z), -1 * sin(rot.z), 0,],
            [sin(rot.z), cos(rot.z), 0,],
            [0, 0, 1,],
        ])

        out = numpy.reshape([self.x, self.y, self.z], (1,3)).dot(rotX).dot(rotY).dot(rotZ)
        return Vector3(out[0][0], out[0][1], out[0][2])

    def rotateAround(self, nA, theta):
        u,v,w = nA.x, nA.y, nA.z
        x,y,z = self.x, self.y, self.z
        out = Vector3 (
            (u)*(u*x + v*y + w*z)*(1-cos(theta)) + (x * cos(theta)) + ((v*z - w*y)*sin(theta)),
            (v)*(u*x + v*y + w*z)*(1-cos(theta)) + (y * cos(theta)) + ((w*x - u*z)*sin(theta)),
            (w)*(u*x + v*y + w*z)*(1-cos(theta)) + (z * cos(theta)) + ((u*y - v*x)*sin(theta)),
        )
        #print(out)
        return out

    @staticmethod
    def unit():
        return Vector3(1,1,1)
    @staticmethod
    def zero():
        return Vector3()
    @staticmethod
    def left():
        return Vector3(-1,0,0)
    @staticmethod
    def right():
        return Vector3(1,0,0)
    @staticmethod
    def forward():
        return Vector3(0,1,0)
    @staticmethod
    def backward():
        return Vector3(0,-1,0)
    @staticmethod
    def up():
        return Vector3(0,0,1)
    @staticmethod
    def down():
        return Vector3(0,0,-1)
    
class Vector2:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("({}, {})".format(self.x,self.y))

    def __add__(self, vA):
        return Vector2(
            self.x + vA.x,
            self.y + vA.y)

    def __sub__(self, vA):
        return Vector2(
            self.x - vA.x,
            self.y - vA.y)

    def __mul__(self,sA):
        return Vector2(
            self.x*sA,
            self.y*sA)
        __rmul__ = __mul__

    def __truediv__(self, sA):
        if type(sA) not in (float,int,):
            raise Exception('Affector must be scalar')
        return Vector2(
            self.x / sA,
            self.y / sA,
        )

    def __iter__(self):
        yield self.x
        yield self.y

    def toInt(self):
        return (int(self.x), int(self.y),)

    def max(self):
        return max(self.x, self.y)
            
    @staticmethod
    def unit():
        return Vector2(1,1)
    @staticmethod
    def zero():
        return Vector2()
    

##########################################
#############   OBJECT   #################
##########################################

class Object3D:
    def __init__(self, name, location = Vector3.zero(), rotation = Vector3.zero(), scale = Vector3.unit()):
        
        self.name = name
        self.location = location
        self.rotation = rotation
        self.scale = scale

        #properties window
        self.data = ['object']

    def translate(self, tA):
        self.location += tA
    def rotate(self, rA):
        self.rotation += rA
    def scale(self,sA):
        self.scale = self.scale.straight_product(sA)

    def __str__(self):
        return "{} ({})\nLocation : {}\nRotation : {}\nScale : {}\n_______".format(self.name,type(self),self.location,self.rotation,self.scale)


class MeshObject(Object3D):
    #restructure to include mesh
    def __init__(self,name, location, rotation, scale, mesh, **kwargs):
        super().__init__(name, location, rotation, scale, **kwargs)
        self.mesh = mesh

class Mesh:
    def __init__(self, vertices, edges, faces):
        self.vertices = vertices
        self.edges = edges
        self.faces = faces

    def vertex_local_to_global(self, vertex, parentObj):
        '''Converts vertex to global'''
        n = (vertex.straight_product(parentObj.scale)).rotate(parentObj.rotation)
        n += parentObj.location
        return n


##########################################
#############  CAMERAS   #################
##########################################

class Orthographic(Object3D):
    def __init__(self, name, location, rotation, scale, orthoscale, **kwargs):

        super().__init__(name, location, rotation, scale, **kwargs)

        self.orthoscale = orthoscale

    def projectvertex_old(self, vertex):
            
            a = self.location # SET TO POSITION!!!
            b = (Vector3.left().rotate(self.rotation)).normalise()
            c = (Vector3.backward().rotate(self.rotation)).normalise() #y axis on canvas is inverted!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111

            print(a,b,c)
            print(self.rotation)
            normal = b.cross_product(c) #should the normal be normalised?
            
            # b.{xyz}[l] + c.{xyz}[m] + normal.{xyz}[alpha] = k where: k = (P.{xyz} - location.{xyz})
            
            #x coefficients
            x_co = [b.x, c.x, normal.x]
            y_co = [b.y, c.y, normal.y]
            z_co = [b.z, c.z, normal.z]
        
            all_co = numpy.array([x_co, y_co, z_co])
            all_k = numpy.array([
                vertex.x - a.x,
                vertex.y - a.y,
                vertex.z - a.z])
            
            sol = numpy.linalg.solve(all_co, all_k) #solution
            return Vector2(sol[0],sol[1])

        
    def projectedges(self, meshobject):

        mesh = meshobject.mesh
        

        self.lines = []
        for edge in mesh.edges:

            start_v = self.projectvertex_old(
                mesh.vertex_local_to_global(
                    mesh.vertices[edge[0]],
                    meshobject)
            )

            end_v   = self.projectvertex_old(
                mesh.vertex_local_to_global(
                    mesh.vertices[edge[1]],
                    meshobject
                )
            )
            
            yield (start_v, end_v,)

        return
    
    def getpixelscale(self, resolution):
        '''returns pixel length of 1 scene unit'''

        return resolution.max() /  self.orthoscale

class Perspective(Object3D):
    def __init__(self, name, location, rotation, scale, fov, focal, **kwargs):

        super().__init__(name, location, rotation, scale, **kwargs)

        self.fov = fov #field of view
        self.focal = focal #focal length
 

##########################################
##########   LIGHT SOURCES   #############
##########################################

class Directional(Object3D):
    def __init__(self, name, location, rotation, scale, colour, strength, specular, angle, **kwargs):

        super().__init__(name, location, rotation, scale, **kwargs)

        self.colour = colour
        self.strength = strength
        self.specular = specular
        self.angle = angle


class Point(Object3D):
    def __init__(self, name, location, rotation, scale, colour, power, specular, radius, **kwargs):

        super().__init__(name, location, rotation, scale, **kwargs)

        self.colour = colour
        self.power = power
        self.specular = specular
        self.radius = radius

if __name__ == '__main__':
    v2 = Vector2(3,5)
    print(tuple(v2))