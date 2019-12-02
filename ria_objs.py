import ria
import mesh
from tkinter.filedialog import askopenfilename
#__Mesh Objects____________________
class Cube(ria.MeshObject):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master,name='Cube',*args,mesh = mesh.cube(),**kwargs)


class Plane(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Plane',*args,mesh = mesh.plane(),**kwargs)
    
class Cylinder(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Cylinder',*args,mesh = mesh.from_obj('shapes/cylinder.obj'),**kwargs)


class Sphere(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='UV Sphere',*args,mesh = mesh.from_obj('shapes/uv.obj'),**kwargs)


class Icosphere(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Icosphere',*args,mesh = mesh.from_obj('shapes/ico.obj'),**kwargs)

class Torus(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Torus',*args,mesh = mesh.from_obj('shapes/torus.obj'),**kwargs)

class Monkey(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Monkey',*args,mesh = mesh.from_obj('shapes/monkey.obj'),**kwargs)

class Klein(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Klein Bottle',*args,mesh = mesh.from_obj('shapes/klein.obj'),**kwargs)

class Poly(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        fname = askopenfilename(filetypes=(("Wavefront (.obj)", "*.obj"),))
        objname = fname.split('/')[-1]
        super().__init__(master,name=objname,mesh = mesh.from_obj(fname),*args,**kwargs)


#__Other__________________________
class Empty(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Empty',*args,**kwargs)
class Curve(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Curve',*args,**kwargs)
class Directional(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Directional',*args,**kwargs)
class Point(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Point',*args,**kwargs)

class Camera(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Camera',*args,**kwargs)