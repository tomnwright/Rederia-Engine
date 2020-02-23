'''
Renderia Engine, for use within Blender.
'''
bl_info = {
    "name": "Renderia",
    "description": "Renderia Rendering Engine (Maths IA).",
    "author": "Tom Wright",
    "version": (1, 0),
    "blender": (2, 81, 0),
    "location": "Properties > Render > Renderia",
    "category": "Render"
}


#Add code path to file, to allow importing modules
import sys
codepath = "C:/Users/Tom/Documents/GitHub/Renderia-Engine"
#add script directory to path
if not codepath in sys.path:
    sys.path.append(codepath)

from mathematics import *
import objtypes
import bpyconvert

import bpy
import bgl
import bresenham


class RenderiaEngine(bpy.types.RenderEngine):
    # These three members are used by blender to set up the
    # RenderEngine; define its internal name, visible name and capabilities.
    bl_idname = "RENDERIA"
    bl_label = "Renderia"
    bl_use_preview = False

    # Init is called whenever a new render engine instance is created. Multiple
    # instances may exist at the same time, for example for a viewport and final
    # render.
    def __init__(self):
        self.scene_data = None
        self.draw_data = None

    # When the render engine instance is destroy, this is called. Clean up any
    # render engine data here, for example stopping running render threads.
    def __del__(self):
        pass

    # This is the method called by Blender for both final renders (F12) and
    # small preview for materials, world and lights.
    def render(self, depsgraph):
        
        scene = depsgraph.scene
        scale = scene.render.resolution_percentage / 100.0
        self.size_x = int(scene.render.resolution_x * scale)
        self.size_y = int(scene.render.resolution_y * scale)
        self.is_rendering = True
        centre = Vector2(
            int(self.size_x / 2),
            int(self.size_y / 2)
            )


        # has to be called to update the frame on exporting animations
        scene.frame_set(scene.frame_current)

        #convert to renderia format
        objects = bpyconvert.ConvertObjects(scene)
        camera = bpyconvert.ConvertCamera(scene.camera)

        pixelscale = camera.getpixelscale((self.size_x, self.size_y,))
        # Fill the render result with a flat color. The framebuffer is
        # defined as a list of pixels, each pixel itself being a list of
        # R,G,B,A values.
        bgcolor = [0.05,0.05,0.05, 1.0]
        linecolor = [1,1,1,1]

        pixel_count = self.size_x * self.size_y
        rect = [bgcolor] * pixel_count

        
        #calculate total vertices
        #this is to accurately update render progress
        totalEdges = 0
        for obj in objects:
            if isinstance(obj, objtypes.MeshObject):
                totalEdges += len(obj.mesh.edges)
        

        progress = 0
        for obj in objects:
            if isinstance(obj, objtypes.MeshObject):
                mesh = obj.mesh
                for edge in mesh.edges:
                    self.update_progress(progress / totalEdges)

                    #get start and end vertices (Vector3)
                    v1, v2 = mesh.vertices[edge[0]], mesh.vertices[edge[1]]
                    #get global vertex positions
                    v1 = mesh.vertex_local_to_global(v1, obj)
                    v2 = mesh.vertex_local_to_global(v2, obj)

                    #project vertex points (now Vector2)
                    p1 = camera.project(v1) * pixelscale + centre
                    p2 = camera.project(v2) * pixelscale + centre

                    #draw line between points
                    
                    for x,y in bresenham.bresenham(*p1.ToInt(), *p2.ToInt()):
                        if (0 <= x <= self.size_x) and (0 <= y <= self.size_y):
                            try:
                                rect[y * self.size_x + x] = linecolor
                            except:
                                continue
                    
                    progress += 1


        # Here we write the pixel values to the RenderResult
        result = self.begin_result(0, 0, self.size_x, self.size_y)
        layer = result.layers[0].passes["Combined"]
        layer.rect = rect
        self.end_result(result)


# RenderEngines also need to tell UI Panels that they are compatible with.
# We recommend to enable all panels marked as BLENDER_RENDER, and then
# exclude any panels that are replaced by custom panels registered by the
# render engine, or that are not supported.
def get_panels():
    exclude_panels = {
        'VIEWLAYER_PT_filter',
        'VIEWLAYER_PT_layer_passes',
    }

    panels = []
    for panel in bpy.types.Panel.__subclasses__():
        if hasattr(panel, 'COMPAT_ENGINES') and 'BLENDER_RENDER' in panel.COMPAT_ENGINES:
            if panel.__name__ not in exclude_panels:
                panels.append(panel)

    return panels



'''
#######################################
##########   UI  ######################
#######################################
'''


class RenderiaProperties (bpy.types.PropertyGroup):

    shading: bpy.props.EnumProperty(
        name="",
        description="Determines the mode in which the image is rendered.",
        items=[ ('WIREFRAME','Wireframe','Wireframe shading', 'SHADING_WIRE', 1),
                ('SOLID','Solid','Solid shading','SHADING_SOLID', 2),
                ('RENDERED','Rendered','Rendered (lit) shading', 'SHADING_RENDERED', 3)
               ]
        )

class RenderiaPanelSettings:
    bl_space_type = 'PROPERTIES'
    bl_region_type = "WINDOW"
    bl_category = "Tools"
    bl_context = "render"
    bl_options =  {"HIDE_HEADER"}
class RenderiaPanel(RenderiaPanelSettings, bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Renderia"
    bl_idname = "RENDER_PT_renderia"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        renderiasettings = scene.renderiasettings

        layout.prop(renderiasettings, "shading")
        
        #layout.prop_search(scene, "RenderCam", scene, "objects")
    
        row = layout.row()
        row.scale_y = 2.0
        row.operator("render.render")
    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == "RENDERIA"


class RenderiaSubPanel(RenderiaPanelSettings, bpy.types.Panel):
    """Contains settings for Renderia Panel"""
    bl_label = "Settings"
    bl_parent_id = "RENDER_PT_renderia"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        renderiasettings = scene.renderiasettings


classes  = (
    RenderiaProperties,
    RenderiaPanel,
    RenderiaSubPanel,
)


def register():
    from bpy.utils import register_class

    # Register the RenderEngine
    register_class(RenderiaEngine)

    for panel in get_panels():
        panel.COMPAT_ENGINES.add('RENDERIA')


    for cls in classes:
        register_class(cls)

    bpy.types.Scene.renderiasettings = bpy.props.PointerProperty(type=RenderiaProperties)
    return


def unregister():
    from bpy.utils import unregister_class

    unregister_class(RenderiaEngine)

    for panel in get_panels():
        if 'RENDERIA' in panel.COMPAT_ENGINES:
            panel.COMPAT_ENGINES.remove('RENDERIA')

    del bpy.types.Scene.renderia

    for cls in reversed(classes):
        unregister_class(cls)
    

if __name__ == "__main__":
    register()