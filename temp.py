import bpy
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
    bl_options = {"DEFAULT_CLOSED"}
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

    for cls in classes:
        register_class(cls)

    bpy.types.Scene.renderiasettings = bpy.props.PointerProperty(type=RenderiaProperties)
    return
def unregister():
    from bpy.utils import unregister_class

    del bpy.types.Scene.renderia

    for cls in reversed(classes):
        unregister_class(cls)
    return
if __name__ == '__main__':
    register()