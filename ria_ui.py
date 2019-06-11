import tkinter,ria

class ObjectFrame(tkinter.Frame):
    def __init__(self,master,obj3d,icon,**kwargs):
        super().__init__(master,**kwargs)
    
        #Component widgets should be mastered by self not self.master (!!)
        self.master = master
        #linked to actual object
        self.obj = obj3d
        #tell frame to not let chilren control size
        #self.pack_propagate(0)
        self.symbols = Style.images()

        #defining buttons
        self.del_btn = tkinter.Button(
            self,
            command = self.obj.delete,
            **Style.button.delete(self.symbols))
        self.tnf_btn = tkinter.Button(
            self,
            **Style.button.transform(self.symbols))
        self.ppt_btn = tkinter.Button(
            self,
            command = self.obj.properties_temp,
            **Style.button.properties(self.symbols))
        #packing buttons
        self.del_btn.pack(side='right',fill='y')
        self.ppt_btn.pack(side='right',fill='y')
        self.tnf_btn.pack(side='right',fill='y')  
        
        self.tog = tkinter.Label(
            self,
            image = self.symbols.tg1)
        self.tog.pack(side= 'left', fill='y')

        self.symb = tkinter.Label(
            self,
            image = icon,
            bg=Style.colors('grey_01'))
        self.symb.pack(side= 'left', fill='y')

        self.text_container = tkinter.Frame(
            self,
            bg = Style.colors('grey_01'))
        
        self.name = tkinter.Label(
            self.text_container,
            background = Style.colors('grey_01'),
            text=self.obj.name,
            justify='left' ,
            padx = 1 ,
            pady= 1,
            fg = 'white'
            )
        self.name.bind('<Double-Button-1>',self.rename)
        self.name.pack(side = 'left')
        
        self.text_container.pack(side = 'left', fill = 'both', expand=1)

        self.text_container.bind('<Button-3>',self.select_passOver)
        self.symb.bind('<Button-3>',self.select_passOver)
        self.name.bind('<Button-3>',self.select_passOver)
    def rename(self, event):
        widget = event.widget.master
        entry_widget = tkinter.Entry(
            widget,
            bg = 'gray',
            selectbackground = Style.colors('grey_01'),
            relief = 'flat',
            fg = 'white',
            #insertbackground = 'lightblue'
            justify = 'left',
            )

        entry_widget.insert(0,self.name['text'])
        entry_widget.select_range(0, 'end')
        entry_widget.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0)
        entry_widget.bind("<Return>", self.rename_lock)
        entry_widget.bind("<Escape>", self.rename_cancel)
        entry_widget.bind("<FocusOut>", self.rename_lock)
        entry_widget.focus_set()
    def rename_lock(self, event):
        entry = event.widget
        i = entry.get()
        if i and i != self.name['text']:
            new_name = self.obj.set_name(i)
            self.name.configure(text=new_name)

        entry.destroy()
    def rename_cancel(self, event):
        entry = event.widget
        entry.destroy()
    def set_active(self):
        self.symb.config(bg = Style.colors('active'))
        self.tog.config(image = self.symbols.tg2)
    def set_selected(self):
        self.symb.config(bg = Style.colors('selected'))
        self.tog.config(image = self.symbols.tg2)
    def set_deselected(self):
        self.symb.config(bg = Style.colors('grey_01'))
        self.tog.config(image = self.symbols.tg1)
    def select_passOver(self,event):
        self.obj.toggle_select()

class Style:
    obj_pady = 1
    obj_padx = 5
    @staticmethod
    def colors(index):
        pallete = {'grey_01' : '#232323','active':'#E66A1F','selected':'#E6A882'}
        return pallete[index]
    class images:
        def __init__(self):
            self.axi = tkinter.PhotoImage(file = 'graphics/symbols/axis.png')
            self.cub = tkinter.PhotoImage(file = 'graphics/symbols/cube.png')
            self.cyl = tkinter.PhotoImage(file = 'graphics/symbols/cylinder.png')
            self.cur = tkinter.PhotoImage(file = 'graphics/symbols/curve.png')
            self.pla = tkinter.PhotoImage(file = 'graphics/symbols/plane.png')
            self.poi = tkinter.PhotoImage(file = 'graphics/symbols/point.png')
            self.ico = tkinter.PhotoImage(file = 'graphics/symbols/sphere_ico.png')
            self.uvs = tkinter.PhotoImage(file = 'graphics/symbols/sphere_uv.png')
            self.dee = tkinter.PhotoImage(file = 'graphics/delete.png')
            self.tra = tkinter.PhotoImage(file = 'graphics/transform.png')
            self.pro = tkinter.PhotoImage(file = 'graphics/properties.png')
            self.dir = tkinter.PhotoImage(file = 'graphics/symbols/directional.png')
            self.pol = tkinter.PhotoImage(file = 'graphics/symbols/poly.png')
            self.cam = tkinter.PhotoImage(file = 'graphics/symbols/camera.png')
            self.tg1 = tkinter.PhotoImage(file = 'graphics/symbols/toggle_deselected.png')
            self.tg2 = tkinter.PhotoImage(file = 'graphics/symbols/toggle_selected.png')
            self.obj = tkinter.PhotoImage(file = 'graphics/symbols/object.png')
        def get_by_class(self,obj_class):
            class_to_img = {
                ria.Empty : self.axi,
                ria.Cube : self.cub,
                ria.Cylinder : self.cyl,
                ria.Curve : self.cur,
                ria.Plane : self.pla,
                ria.Point : self.poi,
                ria.Icosphere : self.ico,
                ria.Sphere : self.uvs,
                ria.Directional : self.dir,
                ria.Poly : self.pol,
                ria.Camera : self.cam,
            }
            return class_to_img[obj_class]
    class button:
        @staticmethod
        def delete(img_ls):
            out = {
            'relief' : 'flat',
            'bg' : 'darkred',
            'image' : img_ls.dee}
            return out
        @staticmethod
        def properties(img_ls):
            out = {
                'relief' : 'flat',
                'bg' : 'darkgray',
                'image' : img_ls.pro}
            return out
        @staticmethod
        def transform(img_ls):
            out = {
                'relief' : 'flat',
                'bg' : 'darkgreen',
                'image' : img_ls.tra}
            return out
    @staticmethod
    def ObjectFrame():
        out = {
        }
        return out

class add_funcs:
    @staticmethod
    def generic(master,obj_container,obj_type):
        new_obj = obj_type(master.handler)
        master.handler.add_object(new_obj)
        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.get_by_class(obj_type)
        )
        new_obj.frame_instance = obj_frame
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_padx,pady=Style.obj_pady)

class menus:
    @staticmethod
    def init_menubar(root):

        menubar = tkinter.Menu(root.master)

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
        edit_menu.add_command(label = 'Undo',state='disabled')
        edit_menu.add_command(label = 'Redo',state='disabled')
        edit_menu.add_separator()
        edit_menu.add_command(label = 'Select All', command = root.handler.select_all)
        menubar.add_cascade(label = 'Edit', menu=edit_menu)

        view_menu = tkinter.Menu(menubar, tearoff=0)
        view_menu.add_checkbutton(label = 'Axis')
        view_menu.add_checkbutton(label = 'Grid')
        menubar.add_cascade(label = 'View', menu=view_menu)

        object_menu = menus.init_objmenu(menubar,root)
        menubar.add_cascade(label = 'Object', menu=object_menu)

        debug_menu = menus.init_debugmenu(menubar,root)
        menubar.add_cascade(label='Debug',menu=debug_menu)

        menubar.add_separator()
        menubar.add_command(label = 'Render Image')

        root.master.config(menu=menubar)
    @staticmethod
    def init_objmenu(parent,root):
        object_menu = tkinter.Menu(parent,tearoff=0)
        #Translation
        object_menu.add_command(label = 'Transform',state='disabled')
        #Clear menu
        clear_menu = tkinter.Menu(object_menu,tearoff=0)
        clear_menu.add_command(label = 'Location')
        clear_menu.add_command(label = 'Rotation')
        clear_menu.add_command(label = 'Scale')
        object_menu.add_cascade(label='Clear',menu=clear_menu,state='disabled')
        object_menu.add_separator()
        #Misc
        object_menu.add_command(label = 'Properties',command = root.properties_temp)
        object_menu.add_command(label = 'Duplicate',state='disabled')
        object_menu.add_command(label = 'Delete', command = root.handler.delete_selection)
        object_menu.add_separator()
        #New section
        object_menu.add_cascade(label = 'Add',menu = menus.init_addmenu(object_menu,root))
        #Import
        import_menu = tkinter.Menu(object_menu,tearoff=0)
        import_menu.add_command(label = 'Wavefront (OBJ)',command = lambda: add_funcs.generic(root,root.obj_frame,ria.Poly))
        object_menu.add_cascade(label='Import',menu = import_menu)
        #Export
        export_menu = tkinter.Menu(object_menu,tearoff=0)
        export_menu.add_command(label = 'Wavefront (OBJ)')
        object_menu.add_cascade(label='Export',menu = export_menu)
        
        return object_menu
    @staticmethod
    def init_addmenu(parent,root):
        add_menu = tkinter.Menu(parent,tearoff=0)
        add_menu.add_command(label = 'Camera',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Camera))
        #lights
        light_menu = tkinter.Menu(add_menu, tearoff=0)
        light_menu.add_command(label = 'Point',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Point))
        light_menu.add_command(label = 'Directional',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Directional))
        add_menu.add_cascade(label = 'Light',menu =light_menu)
        add_menu.add_command(label = 'Plain Axis',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Empty))
        add_menu.add_separator()

        add_menu.add_command(label = 'Plane',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Plane))
        add_menu.add_command(label = 'Cube',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Cube))
        add_menu.add_command(label = 'UV Sphere',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Sphere))
        add_menu.add_command(label = 'Ico Sphere',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Icosphere))
        add_menu.add_command(label = 'Cylinder',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Cylinder))
        add_menu.add_separator()
        add_menu.add_command(label = 'Curve',command = lambda: add_funcs.generic(root,root.obj_frame,ria.Curve))
        return add_menu
    @staticmethod
    def init_debugmenu(parent,root):
        debug = tkinter.Menu(parent,tearoff=0)
        debug.add_command(label='List objects', command = root.handler.ls_objs)
        debug.add_command(label='List selected', command = root.handler.debug_selection)
        return debug

if __name__ == '__main__':
    pass