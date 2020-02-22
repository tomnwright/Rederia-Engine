from mathematics import *


class Object3D:
    '''
    Parent object class.
    Rotation must be XYZ order.
    '''
    def __init__(self, name, location = Vector3.zero, rotation = Vector3.zero, scale = Vector3.unit):
        
        self.name = name
        self.location = location
        self.rotation = rotation
        self.scale = scale
        
    def translate(self, tA):
        self.location += tA
    def rotate(self, rA):
        self.rotation += rA
    def scale(self,v):
        self.scale = self.scale.straight(v)

    def __str__(self):
        return "{} ({})\nLocation : {}\nRotation : {}\nScale : {}\n_______".format(self.name,type(self),self.location,self.rotation,self.scale)


class MeshObject(Object3D):
    '''
    Mesh object, inheriting from Object3D
    '''
    def __init__(self,name, location, rotation, scale, mesh, **kwargs):
        super().__init__(name, location, rotation, scale, **kwargs)
        self.mesh = mesh

class Mesh:
    def __init__(self, vertices, edges, faces):
        self.vertices = vertices
        self.edges = edges
        self.faces = faces

    def vertex_local_to_global(self, vCoord, parentObj):
        '''Converts vertex to global'''
        scale = Vector3.Transform.scaleXYZ(
            *tuple(parentObj.scale)
        )
        rot = Vector3.Transform.rotXYZ(
            *tuple(parentObj.rotation)
        )
        
        out = (rot * scale * vCoord) + parentObj.location
        return out



##########################################
#############  CAMERAS   #################
##########################################

class Orthographic(Object3D):
    def __init__(self, name, location, rotation, scale, orthoscale, **kwargs):

        super().__init__(name, location, rotation, scale, **kwargs)

        self.orthoscale = orthoscale

    def project(self, vertex):
        '''
        Project vertex position onto camera plane.
        Returns 2D position of projected point.
        '''
        v = copy(vertex)
        
        rot = Vector3.Transform.rotZYX(
            -self.rotation.z,
            -self.rotation.y,
            -self.rotation.x
        )

        v = rot * (v - self.location)

        return (v.x, v.y,)
        
    def getpixelscale(self, resolution):
        '''returns pixel length of 1 scene unit'''

        return max(resolution) /  self.orthoscale

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