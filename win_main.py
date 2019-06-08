import tkinter
import win_render

class main(tkinter.Frame):

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.init_win()
    def init_win(self):

        self.master.iconbitmap("graphics/icon/icon_03.ico")
        self.master.title("render.ia")
        self.master.geometry("1000x500")
        self.master.minsize(500,250)
        self.init_menu(self.master)
        #self.testimg = tkinter.BitmapImage(file = 'graphics/interface/add.bmp')
        panes = tkinter.PanedWindow(self.master,orient='horizontal')
        panes.pack(side='bottom',fill='both',expand=1)

        left = tkinter.Frame(panes,bg='blue')
        panes.add(left,minsize=250)
        right = tkinter.Frame(panes,bg='red')
        panes.add(right,minsize=250)

        #add button on right
        """btn_add = tkinter.Button(right, text='New Object',relief = 'flat')
        btn_add.pack(side='bottom',fill='both',padx=10,pady=10)

        btn_edit = tkinter.Button(right, text='Edit',relief = 'flat')
        btn_edit.pack(side='bottom',fill='both',padx=10,pady=10,expand=1)"""

        #self.init_editmenu(right)
    def init_menu(self,root):

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

        object_menu = tkinter.Menu(menubar,tearoff=1)
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
        new_menu = tkinter.Menu(object_menu,tearoff=0)
        new_menu.add_command(label = 'Plane')
        new_menu.add_command(label = 'Cube')
        new_menu.add_command(label = 'UV Sphere')
        new_menu.add_command(label = 'Ico Sphere')
        new_menu.add_separator()
        new_menu.add_command(label = 'Graph')
        object_menu.add_cascade(label = 'Insert',menu = new_menu)
        #Import
        import_menu = tkinter.Menu(object_menu,tearoff=0)
        import_menu.add_command(label = 'Wavefront (OBJ)')
        object_menu.add_cascade(label='Import',menu = import_menu)
        #Export
        export_menu = tkinter.Menu(object_menu,tearoff=0)
        export_menu.add_command(label = 'Wavefront (OBJ)')
        object_menu.add_cascade(label='Export',menu = export_menu)
        #~
        menubar.add_cascade(label = 'Object', menu=object_menu)

        menubar.add_separator()
        menubar.add_command(label = 'Render Image')

        root.config(menu=menubar)

        
if __name__=='__main__':
    app = main(tkinter.Tk())
    app.mainloop()