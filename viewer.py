from ria import *
import ctypes
import numpy,tkinter
class ViewCam:
    class Ortho:
        '''Orthographic only, for now'''
        def __init__(self):
            
            self.b = Vector3.right()
            self.c = Vector3.down() #y axis on canvas is inverted!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111


            self.normal = self.b.cross_product(self.c)
        def project_verts(self, vertices):
            gVs = []
            a = Vector3.zero() # SET TO POSITION!!!
            for vertex in vertices:
                # b.{xyz}[l] + c.{xyz}[m] + normal.{xyz}[alpha] = k where: k = (P.{xyz} - location.{xyz})
                
                #x coefficients
                x_co = [self.b.x, self.c.x, self.normal.x]
                y_co = [self.b.y, self.c.y, self.normal.y]
                z_co = [self.b.z, self.c.z, self.normal.z]
            
                all_co = numpy.array([x_co, y_co, z_co])
                all_k = numpy.array([
                    vertex.x - a.x,
                    vertex.y - a.y,
                    vertex.z - a.z])
                
                sol = numpy.linalg.solve(all_co, all_k) #solution
                gVs.append(Vector2(sol[0],sol[1]))
            return gVs
        def rotate(self, rB, rC):
            self.b = self.b.rotate(Vector3.up() * rB).normalise()
            self.c = self.c.rotate(Vector3.right() * rC).normalise()
            self.normal = self.b.cross_product(self.c)



class ViewMaster(tkinter.Canvas):
    def __init__(self, *args, obj_master = None, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.rotSpeed = .01

        self.obj_master = obj_master
        self.viewer = ViewCam.Ortho()
        self.view_objects = []
        self.bind("<Configure>",self.onResize)

        self.bind("<2>", self.dragStart)
        self.bind("<B2-Motion>", self.dragMove)
    def update(self,*args):
        self.delete('all'); self.view_objects = []
        for obj in self.obj_master.objects:
            self.view_objects.append(Mesh_View(self, obj.mesh, self.viewer,obj))
    def onResize(self, event):
        self.update()
    
    
    def dragStart(self, event):
        self.lastPos =  Vector2(event.x, event.y)
    def dragMove(self, event):
        newPos = Vector2(event.x, event.y)
        delta = newPos - self.lastPos
        delta *= self.rotSpeed
        self.viewer.rotate(delta.x, delta.y)
        self.update()

        self.lastPos = newPos
        

class Mesh_View:
    def __init__(self,canvas, mesh, cam,obj):
        self.cam_verts = cam.project_verts(mesh.local_to_global(obj))
        self.cam_edges = []
        for face in mesh.faces:
            for e,v in enumerate(face):
                #when e = 0, [e-1] < 0
                new_e = [v, face[e-1]]
                if new_e not in self.cam_edges:
                    self.cam_edges.append(new_e)
        centre = Vector2(canvas.winfo_width()*0.5, canvas.winfo_height()*0.5)
        self.lines = []
        for edge in self.cam_edges:
            start_v = centre+ (self.cam_verts[edge[0]]* 50)
            end_v = centre+ (self.cam_verts[edge[1]]* 50)
            self.lines.append(canvas.create_line(start_v.x,start_v.y,end_v.x,end_v.y))


            
