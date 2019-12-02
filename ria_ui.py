import tkinter,ria,string

class ObjectFrame(tkinter.Frame):
    def __init__(self,master,obj3d,icon,**kwargs):
        super().__init__(master,**kwargs)
    
        #Component widgets should be mastered by self not self.master (!!)
        self.master = master
        self.config(background = Style.colour.bw[0])
        #linked to actual object
        self.obj = obj3d
        #tell frame to not let chilren control size
        #self.pack_propagate(0)
        self.symbols = Style.images()

        #defining buttons
        self.del_btn = tkinter.Button(
            self,
            command = self.obj.delete,
            **Style.button.delete(self.symbols),
            )
        self.tnf_btn = tkinter.Button(
            self,
            command = lambda: self.obj.master.transform_objects([self.obj,]),
            **Style.button.transform(self.symbols))
        self.ppt_btn = tkinter.Button(
            self,
            command = self.obj.properties_temp,
            **Style.button.properties(self.symbols))
        #packing buttons
        self.del_btn.pack(side='right',fill='y',padx=(2,4,),pady=4)
        self.ppt_btn.pack(side='right',fill='y',padx=2,pady=4)
        self.tnf_btn.pack(side='right',fill='y',padx=(4,2,),pady=4)  
        
        self.tog = tkinter.Label(
            self,
            image = self.symbols.tg1,
            bg=Style.colour.bw[2])
        self.tog.pack(side= 'left', fill='y')

        self.symb = tkinter.Label(
            self,
            image = icon,
            bg=Style.colour.bw[0]
            )
        self.symb.pack(side= 'left', fill='y')

        self.text_container = tkinter.Frame(
            self,
            bg = Style.colour.bw[0])
        
        self.name = tkinter.Label(
            self.text_container,
            background = Style.colour.bw[0],
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
            selectbackground = Style.colour.bw[0],
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
        self.symb.config(bg = Style.colour.orange[0])
        self.tog.config(image = self.symbols.tg2)
    def set_selected(self):
        self.symb.config(bg = Style.colour.orange[1])
        self.tog.config(image = self.symbols.tg2)
    def set_deselected(self):
        self.symb.config(bg = Style.colour.bw[0])
        self.tog.config(image = self.symbols.tg1)
    def select_passOver(self,event):
        self.obj.toggle_select()
    def update(self):
        self.name.configure(text=self.obj.name)
class input_ui:
    class DisplayFrame(tkinter.LabelFrame):
        def __init__(self,master, *args, x=0, y=0, z=0,**kwargs):
            super().__init__(master, *args,**kwargs,
                bg = Style.colour.bw[0],
                fg = 'white',
                padx = 2, pady=2)
            
            self.x = input_ui.ValueDisplay(self, 'X:',x)
            self.x.pack(fill='both',padx = 2, pady=2)

            self.y = input_ui.ValueDisplay(self, 'Y:',y)
            self.y.pack(fill='both',padx = 2, pady=2)

            self.z = input_ui.ValueDisplay(self, 'Z:',z)
            self.z.pack(fill='both',padx = 2, pady=2)

        def get_x(self):
            return float(self.x.value)
        def get_y(self):
            return float(self.y.value)
        def get_z(self):
            return float(self.z.value)
        def get_v3(self):
            return ria.Vector3(
                x = self.get_x(),
                y = self.get_y(),
                z = self.get_z())
    class ValueDisplay(tkinter.Label):
        def __init__(self, master,  label, value, *args, **kwargs):
            self.value = ria.misctools.get_intDisplay(value,6)
            super().__init__(
                master, *args, **kwargs,
                text=self.value,
                bg = Style.colour.bw[2],fg='white',
                anchor = 'e',
                padx = 0, pady = 0
                )

            x_label = tkinter.Label(self,
                text=label,
                bg = Style.colour.bw[2],
                fg='white',
                anchor = 'w'
                )
            x_label.pack(side = 'left')

            self.bind('<Button-1>',self.edit_init)

        def edit_init(self, event):
            widget = event.widget
            entry_widget = tkinter.Entry(
                widget,
                bg = 'gray',
                selectbackground = Style.colour.bw[0],
                relief = 'flat',
                fg = 'white',
                #insertbackground = 'lightblue'
                justify = 'right',
                )

            entry_widget.insert(0,self.value)
            entry_widget.select_range(0, 'end')
            entry_widget.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0)
            entry_widget.bind("<Return>", self.edit_lock)
            entry_widget.bind("<Escape>", self.edit_cancel)
            entry_widget.bind("<FocusOut>", self.edit_lock)
            entry_widget.focus_set()

        def edit_lock(self, event):
            entry = event.widget
            i = entry.get()
            try:
                if i and i != self.value:
                    if ria.misctools.contains_except(i, '01234567.'):
                        i = eval(i)
                    self.value = ria.misctools.get_intDisplay(i,6)
                    self.configure(text=self.value)

                entry.destroy()
            except Exception as e:
                print(e)
                entry.destroy()
        def edit_cancel(self, event):
            entry = event.widget
            entry.destroy()
    
    class GenericDisplay(tkinter.Label):
        def __init__(self, master,validate = None, *args, **kwargs):
            super().__init__(
                master, *args, **kwargs,
                bg = Style.colour.bw[2],fg='white',
                )
            self.validate = validate
            self.bind('<Button-1>',self.edit_init)

        def edit_init(self, event):
            widget = event.widget
            entry_widget = tkinter.Entry(
                widget,
                bg = 'gray',
                selectbackground = Style.colour.bw[0],
                relief = 'flat',
                fg = 'white',
                #insertbackground = 'lightblue'
                justify = 'left',
                )

            entry_widget.insert(0,self.cget('text'))
            entry_widget.select_range(0, 'end')
            entry_widget.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0)
            entry_widget.bind("<Return>", self.edit_lock)
            entry_widget.bind("<Escape>", self.edit_cancel)
            entry_widget.bind("<FocusOut>", self.edit_lock)
            entry_widget.focus_set()

        def edit_lock(self, event):
            entry = event.widget
            i = entry.get()
            if i != self.cget('text'):
                if self.validate:
                    i = self.validate(i)
                self.config(text=i)
            entry = event.widget
            entry.destroy()
        def edit_cancel(self, event):
            entry = event.widget
            entry.destroy()

class LabeledWidget:
    class Label(tkinter.Label):
        def __init__(self,label,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.label = label
class Properties_Frames:
    @staticmethod
    def get_frame(i,imgs):
        out = {
            'object':(Properties_Frames.Object_Generic, imgs.obj),
        }
        return out[i]

    class Object_Generic(tkinter.Frame):
        def __init__(self, master, obj=None, *args, **kwargs):
            self.main_bg = Style.colour.bw[0]
            super().__init__(master,*args,**kwargs,
                bg = self.main_bg
                )
            self.master = master
            self.obj = obj

            self.title = tkinter.Label(self, text = 'Object Properties', bg = Style.colour.bw[1], fg = 'white',padx=3,pady=3)
            self.title.pack(side = 'top', fill = 'both')

            self.name_frame = tkinter.LabelFrame(self,text = 'Name',bg = self.main_bg,fg='white',padx=4,pady=4)
            self.name_input = input_ui.GenericDisplay(
                self.name_frame,
                text = self.obj.name,
                anchor = 'w',
                validate=self.check_newname,
                padx=2,pady=2
                )
            self.name_input.pack(fill='both')
            self.name_frame.pack(side = 'top', fill = 'both', padx = 5)

            self.loc_input = input_ui.DisplayFrame(
                self,
                text = 'Location',
                x = self.obj.location.x,
                y = self.obj.location.y,
                z = self.obj.location.z
            )
            self.loc_input.pack(side='top',fill='both',padx=5,pady=5)

            self.rot_input = input_ui.DisplayFrame(
                self,
                text = 'Rotation',
                x = self.obj.rotation.x,
                y = self.obj.rotation.y,
                z = self.obj.rotation.z
            )
            self.rot_input.pack(side='top',fill='both',padx=5,pady=5)

            self.size_input = input_ui.DisplayFrame(
                self,
                text = 'Scale',
                x = self.obj.size.x,
                y = self.obj.size.y,
                z = self.obj.size.z
            )
            self.size_input.pack(side='top',fill='both',padx=5,pady=5)
        def apply_all(self):
            self.obj.location = self.loc_input.get_v3()
            self.obj.rotation = self.rot_input.get_v3()
            self.obj.size = self.size_input.get_v3()
            self.obj.name = self.name_input.cget('text')
            #update object display frame
            self.obj.frame_instance.update()
        def check_newname(self,name):
            names = [k.name for k in self.obj.master.objects]
            while name in names:
                name = ria.misctools.increment(name)
            return name

class Style:
    class colour:
        bw = [
            '#232323',
            '#313131',
            '#404040',
            '#575757',
            '#656565',
            '#7e7e7e',
            '#a0a0a0',
            '#bcbcbc',
            '#cacaca',
            '#e5e5e5',
            '#ffffff',
            ]     
        orange = ['#ff7200',
            '#ff9c4d',
            '#dd6a0c']

        delete_button = [
            '#8b0000',
            '#bf1313'
            ]

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
            self.tor = tkinter.PhotoImage(file = 'graphics/symbols/torus.png')
            self.mon = tkinter.PhotoImage(file = 'graphics/symbols/monkey.png')
            self.kle = tkinter.PhotoImage(file = 'graphics/symbols/klein.png')
            

            self.translate = tkinter.PhotoImage(file = 'graphics/transformations/translate.png')
            self.rotate = tkinter.PhotoImage(file = 'graphics/transformations/rotate.png')
            self.scale = tkinter.PhotoImage(file = 'graphics/transformations/scale.png')
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
                ria.Torus : self.tor,
                ria.Monkey: self.mon,
                ria.Klein : self.kle,
            }
            return class_to_img[obj_class]
    class button:
        @staticmethod
        def delete(img_ls):
            out = {
            'relief' : 'flat',
            'bg' : Style.colour.delete_button[0],
            'activebackground' : Style.colour.delete_button[1],
            'image' : img_ls.dee}
            return out
        @staticmethod
        def properties(img_ls):
            out = {
                'relief' : 'flat',
                'bg' : Style.colour.bw[3],
                'activebackground' : Style.colour.bw[4],
                'image' : img_ls.pro}
            return out
        @staticmethod
        def transform(img_ls):
            out = {
                'relief' : 'flat',
                'bg' : Style.colour.orange[2],
                'activebackground' : Style.colour.orange[1],
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
        obj_frame.pack(side = 'top',fill='both',padx=(0,5,),pady=2)

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
        object_menu.add_command(label = 'Transform',command = lambda: root.handler.transform_objects(root.handler.selected))
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
        add_menu.add_command(label = 'Torus',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Torus))
        add_menu.add_command(label = 'Klein Bottle',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Klein))
        add_menu.add_command(label = 'Monkey',command = lambda: add_funcs.generic(root, root.obj_frame, ria.Monkey))

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
    root = tkinter.Tk()
    x = input_ui.DisplayFrame(root, text = 'Location', x=1,y = 3, z = 4)
    x.pack(fill='both')
    root.mainloop()
    
    