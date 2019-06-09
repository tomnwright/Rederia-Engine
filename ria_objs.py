import ria
import mesh
#__Mesh Objects____________________
class Cube(ria.MeshObject):
    def __init__(self, master,name,*args,**kwargs):
        super().__init__(master,name,*args,mesh = mesh.cube(),**kwargs)

class Plane(ria.MeshObject):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,mesh = mesh.plane(),**kwargs)
    #REQUIRE UPDATING
class Cylinder(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)
class Sphere(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)
class Icosphere(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)
class Poly(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)


#__Other__________________________
class Empty(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)
class Curve(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)
class Camera(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)
class Directional(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)
class Point(ria.Object3D):
    def __init__(self, master, name, *args,**kwargs):
        super().__init__(master,name,*args,**kwargs)