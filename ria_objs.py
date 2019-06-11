import ria
import mesh
#__Mesh Objects____________________
class Cube(ria.MeshObject):
    def __init__(self, master,*args,**kwargs):
        super().__init__(master,name='Cube',*args,mesh = mesh.cube(),**kwargs)


class Plane(ria.MeshObject):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Plane',*args,mesh = mesh.plane(),**kwargs)
    #REQUIRE UPDATING
class Cylinder(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Cylinder',*args,**kwargs)
class Sphere(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='UVSphere',*args,**kwargs)
class Icosphere(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Icosphere',*args,**kwargs)
class Poly(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Poly',*args,**kwargs)


#__Other__________________________
class Empty(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Empty',*args,**kwargs)
class Curve(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Curve',*args,**kwargs)
class Camera(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Camera',*args,**kwargs)
class Directional(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Directional',*args,**kwargs)
class Point(ria.Object3D):
    def __init__(self, master, *args,**kwargs):
        super().__init__(master,name='Point',*args,**kwargs)