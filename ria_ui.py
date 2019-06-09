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
            command = self.delete,
            **Style.button.delete(self.symbols))
        self.tnf_btn = tkinter.Button(
            self,
            **Style.button.transform(self.symbols))
        self.ppt_btn = tkinter.Button(
            self,
            command = self.properties_temp,
            **Style.button.properties(self.symbols))
        #packing buttons
        self.del_btn.pack(side='right',fill='y')
        self.ppt_btn.pack(side='right',fill='y')
        self.tnf_btn.pack(side='right',fill='y')  
        
        self.nonbtn_container = tkinter.Label(self,bd=0)
        self.symb = tkinter.Label(
            self.nonbtn_container,
            image = icon,
            bg=Style.colors('grey_01'))
        self.symb.pack(side= 'left', fill='y')
        text_container = tkinter.Frame(
            self.nonbtn_container,
            bg = Style.colors('grey_01'))
        
        self.name = tkinter.Label(
            text_container,
            background = Style.colors('grey_01'),
            text=self.obj.name,
            justify='left' ,
            padx = 1 ,
            pady= 1,
            fg = 'white'
            )
        self.name.bind('<Double-Button-1>',self.rename)
        self.name.pack(side = 'left')
        
        text_container.pack(side = 'left', fill = 'both', expand=1)
        self.nonbtn_container.pack(side = 'left', fill = 'both', expand=1)
        self.nonbtn_container.bind('<Button-1>',lambda: self.obj.toggle_select(self))
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
    def delete(self):
        self.obj.delete()
        self.destroy()
    def properties_temp(self):
        print("___OBJ___\nName : {}\nType : {}\nLocation : {}\nRotation : {}\nScale : {}\n_______".format(self.obj.name,type(self.obj),self.obj.location,self.obj.rotation,self.obj.size))
    def set_active(self):
        pass
    def set_selected(self):
        pass
    def set_deselected(self):
        pass
class Style:
    obj_pad = 5

    @staticmethod
    def colors(index):
        pallete = {'grey_01' : '#232323'}
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
    def cube(master,obj_container):
        new_obj = ria.Cube(master.handler,'Cube')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.cub)
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
    @staticmethod
    def empty(master,obj_container):
        new_obj = ria.Empty(master.handler,'Empty')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.axi,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
    
    @staticmethod
    def curve(master,obj_container):
        new_obj = ria.Curve(master.handler,'Curve')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.cur,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
    @staticmethod
    def cylinder(master,obj_container):
        new_obj = ria.Cylinder(master.handler,'Cylinder')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.cyl,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
    @staticmethod
    def directional(master,obj_container):
        new_obj = ria.Directional(master.handler,'Directional')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.dir,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
    @staticmethod
    def plane(master,obj_container):
        new_obj = ria.Plane(master.handler,'Plane')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.pla,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
    @staticmethod
    def point(master,obj_container):
        new_obj = ria.Point(master.handler,'Point')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.poi,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
    @staticmethod
    def poly(master,obj_container):
        new_obj = ria.Poly(master.handler,'Poly')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.pol,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
    @staticmethod
    def ico(master,obj_container):
        new_obj = ria.Icosphere(master.handler,'Icosphere')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.ico,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
    @staticmethod
    def uvs(master,obj_container):
        new_obj = ria.Sphere(master.handler,'Sphere')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.uvs,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
    
    @staticmethod
    def camera(master,obj_container):
        new_obj = ria.Camera(master.handler,'Camera')
        master.handler.add_object(new_obj)

        obj_frame = ObjectFrame(
            obj_container,
            new_obj,
            icon = master.images.cam,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)
        master.update_scroll(master.obj_canvas)
 
if __name__ == '__main__':
    pass