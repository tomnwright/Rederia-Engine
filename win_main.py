import tkinter
from tkinter import ttk
from ria_ui import *
import win_render
global obj_pad
obj_pad = 5
class main(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.init_ria()
        self.init_win()
        self.init_menubar(self.master)    
    def init_win(self):

        self.master.iconbitmap("graphics/icon/icon_03.ico")
        self.master.title("render.ia")
        self.master.geometry("1000x500")
        self.master.minsize(500,250)
        panes = tkinter.PanedWindow(self.master,orient='horizontal')
        panes.pack(side='bottom',fill='both',expand=1)
        #left
        left = tkinter.Frame(panes,bg='blue')
        panes.add(left,minsize=250)
        tkinter.Label(left,text='3D Viewer').place(x=100,y=100)

        #right
        self.right_frame = tkinter.Frame(panes,bg='red')
        panes.add(self.right_frame,minsize=250)

        self.obj_canvas = tkinter.Canvas(self.right_frame,width=1,highlightthickness=0,bg='green')
        self.obj_canvas.pack(side='left',fill='both',expand=1)
        #scrollbar
        self.obj_scroll = tkinter.Scrollbar(self.right_frame, orient="vertical", command=self.obj_canvas.yview)
        self.obj_canvas.config(yscrollcommand=self.obj_scroll.set)
        self.obj_scroll.pack(side='right',fill='y')
        
        self.obj_frame = tkinter.Frame(self.obj_canvas)
        self.obj_frameCANV = self.obj_canvas.create_window((0, 0), window=self.obj_frame, anchor="nw")

        self.init_objlist(self.obj_frame)

        self.obj_canvas.bind('<Configure>',self.objcanvas_width)
    def init_ria(self):
        self.handler = ria.ObjectMaster()
        self.images = Style.images()

    def init_menubar(self,root):

        menubar = tkinter.Menu(root)

        #File menu
        file_menu = tkinter.Menu(menubar,tearoff=0)
        #New/open functions
        file_menu.add_command(label='New',command = lambda: print("File; New"))
        file_menu.add_command(label='Open',command = lambda: print("File; Open"))
        file_menu.add_separator()
        #Save functions
        file_menu.add_command(label='Save',command = lambda: print("File; Save"))
        file_menu.add_command(label='Save As',command = lambda: print("File; Save As"))
        file_menu.add_command(label='Save Copy',command = lambda: print("File; Save Copy"))
        file_menu.add_separator()
        #Preferences
        file_menu.add_command(label='Preferences',command = lambda: print("File; Preferences"))
        menubar.add_cascade(label = 'File', menu=file_menu)

        edit_menu = tkinter.Menu(menubar, tearoff=0)
        edit_menu.add_command(label = 'Undo')
        edit_menu.add_command(label = 'Redo')
        menubar.add_cascade(label = 'Edit', menu=edit_menu)

        view_menu = tkinter.Menu(menubar, tearoff=0)
        view_menu.add_checkbutton(label = 'Axis')
        view_menu.add_checkbutton(label = 'Grid')
        menubar.add_cascade(label = 'View', menu=view_menu)

        object_menu = self.init_objmenu(menubar)
        menubar.add_cascade(label = 'Object', menu=object_menu)

        debug_menu = self.init_debugmenu(menubar)
        menubar.add_cascade(label='Debug',menu=debug_menu)

        menubar.add_separator()
        menubar.add_command(label = 'Render Image')

        root.config(menu=menubar)
    def init_objlist(self,root):
        btn1 = tkinter.Menubutton(
            root,
            text='Add Object',)
        a_men = self.init_addmenu(btn1)
        btn1['menu'] = a_men
        btn1.pack(side = 'top',fill='both',padx=obj_pad,pady=obj_pad)
    def init_addmenu(self,root):
        add_menu = tkinter.Menu(root,tearoff=0)
        add_menu.add_command(label = 'Camera',command = lambda: add_funcs.camera(self,self.obj_frame))
        #lights
        light_menu = tkinter.Menu(add_menu, tearoff=0)
        light_menu.add_command(label = 'Point',command = lambda: add_funcs.point(self,self.obj_frame))
        light_menu.add_command(label = 'Directional',command = lambda: add_funcs.directional(self,self.obj_frame))
        add_menu.add_cascade(label = 'Light',menu =light_menu)
        add_menu.add_command(label = 'Plain Axis',command = lambda: add_funcs.empty(self,self.obj_frame))
        add_menu.add_separator()

        add_menu.add_command(label = 'Plane',command = lambda: add_funcs.plane(self,self.obj_frame))
        add_menu.add_command(label = 'Cube',command = lambda: add_funcs.cube(self,self.obj_frame))
        add_menu.add_command(label = 'UV Sphere',command = lambda: add_funcs.uvs(self,self.obj_frame))
        add_menu.add_command(label = 'Ico Sphere',command = lambda: add_funcs.ico(self,self.obj_frame))
        add_menu.add_command(label = 'Cylinder',command = lambda: add_funcs.cylinder(self,self.obj_frame))
        add_menu.add_separator()
        add_menu.add_command(label = 'Curve',command = lambda: add_funcs.curve(self,self.obj_frame))
        return add_menu
    def init_objmenu(self,root):
        object_menu = tkinter.Menu(root,tearoff=0)
        #Translation
        object_menu.add_command(label = 'Transform')
        #Clear menu
        clear_menu = tkinter.Menu(object_menu,tearoff=0)
        clear_menu.add_command(label = 'Location')
        clear_menu.add_command(label = 'Rotation')
        clear_menu.add_command(label = 'Scale')
        object_menu.add_cascade(label='Clear',menu=clear_menu)
        object_menu.add_separator()
        #Misc
        object_menu.add_command(label = 'Properties')
        object_menu.add_command(label = 'Duplicate')
        object_menu.add_command(label = 'Delete')
        object_menu.add_separator()
        #New section
        object_menu.add_cascade(label = 'Add',menu = self.init_addmenu(object_menu))
        #Import
        import_menu = tkinter.Menu(object_menu,tearoff=0)
        import_menu.add_command(label = 'Wavefront (OBJ)',command = lambda: add_funcs.poly(self,self.obj_frame))
        object_menu.add_cascade(label='Import',menu = import_menu)
        #Export
        export_menu = tkinter.Menu(object_menu,tearoff=0)
        export_menu.add_command(label = 'Wavefront (OBJ)')
        object_menu.add_cascade(label='Export',menu = export_menu)
        
        return object_menu
    def init_debugmenu(self,root):
        debug = tkinter.Menu(root,tearoff=0)
        debug.add_command(label='List objects', command = self.handler.ls_objs)
        return debug

    def objcanvas_width(self, event):
        canvas_width = event.width
        self.obj_canvas.itemconfig(self.obj_frameCANV, width = canvas_width)
        self.update_scroll(self.obj_canvas)
    def update_scroll(self,scrollable):
        scrollable.configure(scrollregion=scrollable.bbox("all"))
if __name__=='__main__':
    app = main(tkinter.Tk())
    app.mainloop()