'''
This script is opened in the blender file and registered (by running).
The UI then allows a render to be executed, which ports the data to a separate Python process using an intermediary file.
'''
import sys
import os
import threading
import bpy

from bpy_extras.io_utils import ExportHelper

bl_info = {
    "name": "Renderia",
    "description": "Calls Renderia to render scene (requires active camera).",
    "author": "Tom Wright",
    "version": (1, 0),
    "blender": (2, 81, 0),
    "location": "Properties > Render > Renderia",
    "category": "Render"
}

class RenderiaProperties (bpy.types.PropertyGroup):

    shading: bpy.props.EnumProperty(
        name="",
        description="Determines the mode in which the image is rendered.",
        items=[ ('WIREFRAME','Wireframe','Wireframe shading', 'SHADING_WIRE', 1),
                ('SOLID','Solid','Solid shading','SHADING_SOLID', 2),
                ('RENDERED','Rendered','Rendered (lit) shading', 'SHADING_RENDERED', 3)
               ]
        )

    codepath: bpy.props.StringProperty(
        default = "C:/",
        description = "Path containing Renderia code"
    )

    requestfile: bpy.props.StringProperty(
        default = "../",
        description = "File that request is written to."
    )

class RenderiaPanelSettings:
    bl_space_type = 'PROPERTIES'
    bl_region_type = "WINDOW"
    bl_category = "Tools"
    bl_context = "render"
    bl_options = {"DEFAULT_CLOSED"}
class RenderiaPanel(RenderiaPanelSettings, bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Renderia"
    bl_idname = "RENDER_PT_renderia"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        renderia = scene.renderia

        layout.prop(renderia, "shading")
        
        #layout.prop_search(scene, "RenderCam", scene, "objects")
        
        row = layout.row()
        row.scale_y = 2.0
        row.operator("wm.renderia", text = "Render")

class RenderiaSubPanel(RenderiaPanelSettings, bpy.types.Panel):
    """Contains settings for Renderia Panel"""
    bl_label = "Settings"
    bl_parent_id = "RENDER_PT_renderia"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        renderia = scene.renderia

        
        layout.label(text ="Code Path:")

        col = layout.column()
        row = col.row(align=True)
        row.operator("wm.selectdir", icon="FILE_FOLDER", text="")
        row.prop(renderia, "codepath", text="")

        
        layout.label(text ="Request File Output:")

        col = layout.column()
        row = col.row(align=True)
        row.operator("wm.selectrequestfile", icon="FILE_FOLDER", text="")
        row.prop(renderia, "requestfile", text="")

class RenderiaSelectDir(bpy.types.Operator, ExportHelper):
    
    bl_idname = 'wm.selectdir'
    bl_label = 'Select Path'
    
    filename_ext = ""

    filter_glob: bpy.props.StringProperty(
        default="",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    def invoke(self, context, event):
        self.filepath = ""
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    def execute(self, context):
        filedir = self.filepath
        context.scene.renderia.codepath = os.path.dirname(self.filepath)
        return {'FINISHED'}
    
class RenderiaSelectRequestFile(bpy.types.Operator, ExportHelper):
    
    bl_idname = 'wm.selectrequestfile'
    bl_label = 'Accept'
    
    filename_ext = ""

    filter_glob: bpy.props.StringProperty(
        default="",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )
    def invoke(self, context, event):
        self.filepath = "request00"
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    def execute(self, context):
        filedir = self.filepath
        context.scene.renderia.requestfile = self.filepath
        return {'FINISHED'}



class Render(bpy.types.Operator):
    bl_idname = 'wm.renderia'
    bl_label = 'Render'
    bl_description = 'Call Renderia to render scene.'

    def execute(self, context):
        
        
        codepath = context.scene.renderia.codepath
        requestfilepath = context.scene.renderia.requestfile


        #add script directory to path
        if not codepath in sys.path:
            sys.path.append(codepath)

        import datatransfer, blenderconvert
        
        objects = blenderconvert.ConvertObjects(context.scene)
        camera = blenderconvert.ConvertCamera(context.scene)

        bpyRender = context.scene.render
        resolution = (bpyRender.resolution_x, bpyRender.resolution_y, bpyRender.resolution_percentage)

        shading = context.scene.renderia.shading

        data = datatransfer.RenderRequest(objects, camera, resolution, shading)
        data.dump(requestfilepath)

        command = 'python {}\\ria-client.py "{}"'.format(codepath, requestfilepath)

        renderThread = threading.Thread(target = lambda: os.system(command))
        print("Starting new Renderia thread. ({} active)".format(threading.activeCount()+1))
        renderThread.start()

        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.scene.camera is not None


classes  = (
    Render,
    RenderiaSelectDir,
    RenderiaSelectRequestFile,
    RenderiaProperties,
    RenderiaPanel,
    RenderiaSubPanel,
)

def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)

    bpy.types.Scene.renderia = bpy.props.PointerProperty(type=RenderiaProperties)
    return
def unregister():
    from bpy.utils import unregister_class

    del bpy.types.Scene.renderia

    for cls in reversed(classes):
        unregister_class(cls)
    return
if __name__ == '__main__':
    register()