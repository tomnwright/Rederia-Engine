import ria, bpy

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

                riaObj = ria.Point(*transform, colour, energy, specular, radius)
                objects.append(riaObj)

            if obj.data.type == "SUN":

                angle = obj.data.angle #angle in radians (sun)

                riaObj = ria.Directional(*transform , colour, energy, specular, angle)
                objects.append(riaObj)



        if obj.type == "MESH":

            vertices = []
            
            for vertex in obj.data.vertices:

                coords = tuple(vertex.co)

                vertices.append(
                    ria.Vector3 (*coords)
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

            mesh = ria.Mesh(vertices, edges, faces)
        
            riaObj = ria.MeshObject(*transform, mesh)
            objects.append(riaObj)
    return objects
            
def ConvertCamera(scene):
    
    cam = scene.camera
    transform = ConvertObjectTransform(cam) #name, location, rotation, scale

    if cam.data.type == "ORTHO":
        
        orthoscale = cam.data.ortho_scale
        
        riaCam = ria.Orthographic(*transform, orthoscale)
        return riaCam

    elif cam.data.type == "PERSP":

        focallength = cam.data.lens #mm
        fov = cam.data.angle # field of view (radians)

        riaCam = ria.Perspective(*transform, fov, focallength)
        return riaCam

    else:
        raise Exception("Wrong camera type.")
    
    return

def ConvertObjectTransform(obj):
    name = obj.name

    location = ria.Vector3(
        *tuple(
            obj.location
        )
    )

    rotation = ria.Vector3(
        *tuple(
            obj.rotation_euler
        )
    )

    scale = ria.Vector3(
        *tuple(
            obj.scale
        )
    )

    return name, location, rotation, scale