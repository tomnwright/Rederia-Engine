import argparse
import ria
import datatransfer
import tkinter
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser(description= "Parse the render-request file.")
parser.add_argument('filepath', help= "Path of the render-request file.")
args = parser.parse_args()

filepath = args.filepath

requestData = datatransfer.load(filepath)
camera = requestData.cam

x,y, percentage = requestData.res

resolution = ria.Vector2(int(x * (percentage / 100)), int(y * (percentage/100)))
centre = ria.Vector2(*(resolution / 2.).toInt())

objects = requestData.objs

image = Image.new('RGB', resolution.toInt(), (200, 200, 200))
draw = ImageDraw.Draw(image)

for obj in objects:
    if type(obj) != ria.MeshObject:
        continue
    print(obj.name)

    for projectdEdge in camera.projectedges(obj):

        start, end = projectdEdge

        scale =  camera.getpixelscale(resolution)
        start = centre + (start * scale)
        end   = centre + (end * scale)
        
        draw.line(start.toInt() + end.toInt(), fill = (0,0,0,), width = 2)

image.show()