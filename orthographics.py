from ria import *
import numpy

class Orthographic(Object3D):
    def __init__(self, name, location, rotation, scale, orthoscale, **kwargs):

        super().__init__(name, location, rotation, scale, **kwargs)

        self.orthoscale = orthoscale

    def projectvertex_old(self, vertex):
            
            a = self.location # SET TO POSITION!!!
            b = Vector3.right()
            c = Vector3.down() #y axis on canvas is inverted!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111

            self.size = 1

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
            
            print(mesh.vertices[edge[0]])
            start_v = self.projectvertex_old(
                mesh.vertex_local_to_global(
                    mesh.vertices[edge[0]],
                    meshobject)
            )

            end_v   = self.projectvertex_old(
                mesh.vertex_local_to_global(
                    mesh.vertices[edge[1]],
                    meshobject)
            )
            
            yield (start_v, end_v,)

        return
    
    def getpixelscale(self, resolution):
        '''returns pixel length of 1 scene unit'''

        return resolution.max() /  self.orthoscale