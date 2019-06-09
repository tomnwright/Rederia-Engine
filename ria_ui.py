import tkinter

class ObjectList(tkinter.Frame):
    def __init__(self,master,bg_color='pink',index=0,**kwargs):
        super().__init__(master,**kwargs)
    
        #Component widgets should be mastered by self not self.master (!!)
        self.master = master
        self.bg_color = bg_color
        #tell frame to not let chilren control size
        #self.pack_propagate(0)
        self.symbols = (
            tkinter.PhotoImage(file = 'graphics/symbols/axis.png'),
            tkinter.PhotoImage(file = 'graphics/symbols/cube.png'),
            tkinter.PhotoImage(file = 'graphics/symbols/cylinder.png'),
            tkinter.PhotoImage(file = 'graphics/symbols/graph.png'),
            tkinter.PhotoImage(file = 'graphics/symbols/plane.png'),
            tkinter.PhotoImage(file = 'graphics/symbols/point.png'),
            tkinter.PhotoImage(file = 'graphics/symbols/sphere_ico.png'),
            tkinter.PhotoImage(file = 'graphics/symbols/sphere_uv.png'),
            tkinter.PhotoImage(file = 'graphics/delete.png'),
            tkinter.PhotoImage(file = 'graphics/transform.png'),
            tkinter.PhotoImage(file = 'graphics/properties.png')
        )

        self.symb = tkinter.Label(
            self,
            image = self.symbols[index],
            bg=self.bg_color)
        self.symb.pack(side= 'left', fill='y')
        self.del_btn = tkinter.Button(
            self,
            image = self.symbols[6],
            bg='darkred',
            relief = 'flat')
        self.tnf_btn = tkinter.Button(
            self,
            image = self.symbols[7],
            bg='darkgreen',
            relief = 'flat')
        self.ppt_btn = tkinter.Button(
            self,
            image = self.symbols[8],
            bg='darkgray',
            relief = 'flat')
        self.del_btn.pack(side='right',fill='y')
        self.ppt_btn.pack(side='right',fill='y')
        self.tnf_btn.pack(side='right',fill='y')  
        
        

        text_container = tkinter.Frame(
            self,
            bg = self.bg_color)
        self.name = tkinter.Label(
            text_container,
            background = self.bg_color,
            text="Object_01",
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
            justify = 'left'
            )

        entry_widget.insert(0,self.name['text'])
        entry_widget.select_range(0, 'end')
        entry_widget.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0)
        entry_widget.bind("<Return>", self.rename_lock)
        entry_widget.bind("<Escape>", self.rename_cancel)
        entry_widget.focus_set()
    def rename_lock(self, event):
        entry = event.widget
        i = entry.get()
        if i:
            self.name.configure(text=i)
        entry.destroy()
    def rename_cancel(self, event):
        entry = event.widget
        entry.destroy()

if __name__ == '__main__':
    app = tkinter.Tk()
    obj = ObjectList(app,height=50)
    obj.pack(fill='both')
    app.mainloop()