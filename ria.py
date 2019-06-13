import misctools,tkinter
import win_transform

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
        if type(sA) in (float,str,):
            raise Exception('Affector must be scalar')
        return Vector3(
            self.x*sA,
            self.y*sA,
            self.z*sA)
    def straight_product(self,vA):
        return Vector3(
            self.x*vA.z,
            self.y*vA.y,
            self.z*vA.z)
    def vector_scale(self, vA):
        nx,ny,nz = vA * self.x , vA * self.y, vA * self.z
        return Vector3(nx,ny,nz)
    @staticmethod
    def unit():
        return Vector3(1,1,1)
    @staticmethod
    def zero():
        return Vector3()
    __rmul__ = __mul__

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
    @staticmethod
    def unit():
        return Vector2(1,1)
    @staticmethod
    def zero():
        return Vector2()
    __rmul__ = __mul__

class Object3D:
    def __init__(
        self,
        master,
        name,
        location = Vector3.zero(),
        rotation = Vector3.zero(),
        size = Vector3.unit(),
        frame_instance = None):
        #___________________
        self.master = master
        self.set_name(name)
        self.location = location
        self.rotation = rotation
        self.size = size
        self.frame_instance = frame_instance
    def translate(self, tA):
        self.location += tA
    def rotate(self, rA):
        self.rotation += rA
    def scale(self,sA):
        self.size = self.size.straight_product(sA)
    def set_name(self,new_name):
        names = [i.name for i in self.master.objects]
        while new_name in names:
            new_name = misctools.increment(new_name)
        self.name = new_name
        return self.name
    def delete(self):
        self.frame_instance.destroy()
        if self in self.master.selected:
            self.master.selected.remove(self)
            if self.master.active is self:
                self.master.active = None
        self.master.objects.remove(self)
    def toggle_select(self):
        if self.master.active == self:
            self.master.active = None
            self.master.selected.remove(self)
            self.frame_instance.set_deselected()
        else:
            ria.misctools.select(self.master.selected,self)
            self.frame_instance.set_active()
            if self.master.active:
                self.master.active.frame_instance.set_selected()
            self.master.active = self
    def properties_temp(self):
        print("___OBJ___\nName : {}\nType : {}\nLocation : {}\nRotation : {}\nScale : {}\n_______".format(self.name,type(self),self.location,self.rotation,self.size))
    

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
    def ls_objs(self):
        print([i.name for i in self.objects])
    def debug_selection(self):
        print('Active: {}\n Selected: {}\n'.format(self.active,[i.name for i in self.selected]))
    def delete_selection(self):
        while self.selected:
            target = self.selected.pop(0)
            #note that Object3D.delete() removes ITSELF from [selected] and from [active]
            target.delete()
        self.selected = []
        self.active = None


    def select_all(self):
        if self.selected:
            for i in self.selected:
                i.frame_instance.set_deselected()
            self.selected = []
            self.active = None
        else:
            for i in self.objects:
                self.selected.append(i)
                i.frame_instance.set_selected()
    def transform_objects(self,obj_list):
        trans_win = win_transform.main(tkinter.Toplevel(),obj_list)
        trans_win.mainloop()
from ria_objs import *
if __name__ == '__main__':
    handlers = []
    handler = ObjectMaster()
    print(handler)
    handlers.append(handler)
    print(handlers[0])