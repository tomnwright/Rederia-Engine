import tkinter,ria

class ObjectFrame(tkinter.Frame):
    def __init__(self,master,obj3d,bg_color='pink',**kwargs):
        super().__init__(master,**kwargs)
    
        #Component widgets should be mastered by self not self.master (!!)
        self.master = master
        #linked to actual object
        self.obj = obj3d
        self.bg_color = bg_color
        #tell frame to not let chilren control size
        #self.pack_propagate(0)
        self.symbols = Style.images()

        self.symb = tkinter.Label(
            self,
            image = self.symbols.axi,
            bg=self.bg_color)
        self.symb.pack(side= 'left', fill='y')
        #defining buttons
        self.del_btn = tkinter.Button(
            self,
            command = self.destroy,#DO NOT LEAVE, make destroy function
            **Style.button.delete(self.symbols))
        self.tnf_btn = tkinter.Button(
            self,
            **Style.button.transform(self.symbols))
        self.ppt_btn = tkinter.Button(
            self,
            **Style.button.properties(self.symbols))
        #packing buttons
        self.del_btn.pack(side='right',fill='y')
        self.ppt_btn.pack(side='right',fill='y')
        self.tnf_btn.pack(side='right',fill='y')  
        

        text_container = tkinter.Frame(
            self,
            bg = self.bg_color)
        self.name = tkinter.Label(
            text_container,
            background = self.bg_color,
            text=self.obj.name,
            justify='left' ,
            padx = 1 ,
            pady= 1,
            fg = 'white'
            )
        self.name.bind('<Double-Button-1>',self.rename)
        self.name.pack(side = 'left')
        
        text_container.pack(side = 'left', fill = 'both', expand=1)

    def rename(self, event):
        widget = event.widget.master
        entry_widget = tkinter.Entry(
            widget,
            bg = 'gray',
            selectbackground=self.bg_color,
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
        
class Style:
    obj_pad = 5
    class images:
        def __init__(self):
            self.axi = tkinter.PhotoImage(file = 'graphics/symbols/axis.png')
            self.cub = tkinter.PhotoImage(file = 'graphics/symbols/cube.png')
            self.cyl = tkinter.PhotoImage(file = 'graphics/symbols/cylinder.png')
            self.gra = tkinter.PhotoImage(file = 'graphics/symbols/graph.png')
            self.pla = tkinter.PhotoImage(file = 'graphics/symbols/plane.png')
            self.poi = tkinter.PhotoImage(file = 'graphics/symbols/point.png')
            self.ico = tkinter.PhotoImage(file = 'graphics/symbols/sphere_ico.png')
            self.uvs = tkinter.PhotoImage(file = 'graphics/symbols/sphere_uv.png')
            self.dee = tkinter.PhotoImage(file = 'graphics/delete.png')
            self.tra = tkinter.PhotoImage(file = 'graphics/transform.png')
            self.pro = tkinter.PhotoImage(file = 'graphics/properties.png')

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
            'bg_color':'#232323'
        }
        return out
class Add:
    @staticmethod
    def cube(obj_master,obj_container):
        new_obj = obj_master.add_object('cube')
        obj_frame = ObjectFrame(
            obj_container
            ,new_obj,
            **Style.ObjectFrame())
        obj_frame.pack(side = 'top',fill='both',padx=Style.obj_pad,pady=Style.obj_pad)

if __name__ == '__main__':
    pass