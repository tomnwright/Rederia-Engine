import bpy
from objtypes import *
#renderia.objects contains from mathematics import *, not needed again

def ConvertObjects(scene): #scene = bpy.context.scene
    '''
    Finds all objects (mesh, point, sun) excluding cameras, and converts them to Renderia form
    '''

    objects = []

    for obj in scene.objects:

        transform = ConvertObjectTransform(obj) #name, location, rotation, scale

        if obj.type == "LIGHT":

            energy = obj.data.energy #strength or power
            specular = obj.data.specular_factor #specular
            
            colour = tuple(obj.data.color)
            
            if obj.data.type == "POINT":

                radius = obj.data.shadow_soft_size #radius (point)

                riaObj = Point(*transform, colour, energy, specular, radius)
                objects.append(riaObj)

            if obj.data.type == "SUN":

                angle = obj.data.angle #angle in radians (sun)

                riaObj = Directional(*transform , colour, energy, specular, angle)
                objects.append(riaObj)



        if obj.type == "MESH":

            vertices = []
            
            for vertex in obj.data.vertices:

                coords = tuple(vertex.co)

                vertices.append(
                    Vector3 (*coords)
                )

            edges = []

            for edge in obj.data.edges:

                edges.append(
                    list(edge.vertices)
                )

            faces = []

            for poly in obj.data.polygons:

                faces.append(
                    list(poly.vertices)
                )

            mesh = Mesh(vertices, edges, faces)
        
            riaObj = MeshObject(*transform, mesh)
            objects.append(riaObj)
    return objects
            
def ConvertCamera(cam):

    transform = ConvertObjectTransform(cam) #name, location, rotation, scale

    if cam.data.type == "ORTHO":
        
        orthoscale = cam.data.ortho_scale
        
        riaCam = Orthographic(*transform, orthoscale)
        return riaCam

    elif cam.data.type == "PERSP":

        focallength = cam.data.lens #mm
        fov = cam.data.angle # field of view (radians)

        riaCam = Perspective(*transform, fov, focallength)
        return riaCam

    else:
        raise Exception("Wrong camera type.")
    
    return

def ConvertObjectTransform(obj):
    name = obj.name

    location = Vector3(
        *tuple(
            obj.location
        )
    )

    rotation = Vector3(
        *tuple(
            obj.rotation_euler
        )
    )

    scale = Vector3(
        *tuple(
            obj.scale
        )
    )

    return name, location, rotation, scale