import misctools

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
    def __init__(
        self,
        master,
        name,
        location = Vector3.zero,
        rotation = Vector3.zero,
        size = Vector3.unit):
        #___________________
        self.master = master
        self.set_name(name)
        self.location = location
        self.rotation = rotation
        self.size = size
    def translate(self):#, tA):
        #self.location += tA
        print('{} will be translated'.format(self.name))
    def rotate(self):#, rA):
        #self.rotation += rA
        print('{} will be rotated'.format(self.name))
    def scale(self):#,sA):
        #self.size *= sA
        print('{} will be scaled'.format(self.name))
    def set_name(self,new_name):
        names = [i.name for i in self.master.objects]
        while new_name in names:
            new_name = misctools.increment(new_name)
        self.name = new_name
        return self.name
    def delete(self):
        self.master.remove_object(self)
    def toggle_select(self, display_inst):
        print('select')
        
class MeshObject(Object3D):
    #restructure to include mesh
    def __init__(self,*args,mesh,**kwargs):
        super().__init__(*args,**kwargs)
        self.mesh = mesh

class Mesh:
    #restructure to include mesh
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
    def global_space(self,master):
        gVs = []
        for vertex in self.vertices:
            n = vertex.vector_scale(master.size)
            n += master.location
            gVs.append(n)
        return gVs



class ObjectMaster:
    def __init__(self):
        self.objects = []
        self.active = None
        self.selected = []
    def add_object(self, new_obj):
        self.objects.append(new_obj)
        return new_obj
    def remove_object(self,object_instance):
        self.objects.remove(object_instance)
    def ls_objs(self):
        print([i.name for i in self.objects])


from ria_objs import *
if __name__ == '__main__':
    handlers = []
    handler = ObjectMaster()
    print(handler)
    handlers.append(handler)
    print(handlers[0])