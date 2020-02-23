import bpy
import sys
bpy.app.debug_wm = False
#allows importing
codepath = "C:/Users/Tom/Documents/GitHub/Renderia-Engine"
#add script directory to path
if not codepath in sys.path:
    sys.path.append(codepath)
import mathematics as maths

active = bpy.context.view_layer.objects.active

if active.type != "MESH":
    raise TypeError("I want MESH")

mesh = active.data

rb = active.rotation_euler
rot = maths.Vector3(
    rb.x, rb.y, rb.z
)

rotMatrix = maths.Vector3.Rotation.rotZYX(
    -rot.z, -rot.y, -rot.x
)

for v in mesh.vertices:
    loc = maths.Vector3(
        v.co.x,
        v.co.y,
        v.co.z
    )
    newLoc = maths.Vector3.FromMatrix(rotMatrix * loc)
    v.co = tuple(newLoc)