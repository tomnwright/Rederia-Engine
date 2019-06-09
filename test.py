import tkinter
from tkinter import ttk
from ria_ui import *
from tkinter import messagebox as msg
import win_render
global obj_pad
obj_pad = 5
class main(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.init_win()
        self.init_menubar(self.master)
        
    def init_objlist(self,root):
        #currently called from self.init_win
        obj2 = ObjectList(root,bg_color='#232323',index = 4)
        obj2.pack(side = 'top',fill='both',padx=obj_pad,pady=obj_pad)
        obj2.symb.config(bg = 'orange')
        for i in range(25):
            obj = ObjectList(root,bg_color='#232323')
            obj.pack(side = 'top',fill='both',padx=obj_pad,pady=obj_pad)
        #add button
        btn1 = tkinter.Menubutton(
            root,
            text='Add Object',
            height = 30)
        a_men = self.init_addmenu(btn1)
        btn1['menu'] = a_men
        btn1.pack(side = 'top',fill='both',padx=obj_pad,pady=obj_pad)
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
        
        
        
        
        #from file
        self.tasks=[]
        self.tasks_canvas = tkinter.Canvas(panes,bg='red',highlightthickness=0)

        self.tasks_frame = tkinter.Frame(self.tasks_canvas)
        self.text_frame = tkinter.Frame(self)

        self.scrollbar = tkinter.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)


        self.task_create = tkinter.Text(self.text_frame, height=3, bg="white", fg="black")

        panes.add(self.tasks_canvas,minsize=250)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.text_frame.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.task_create.focus_set()

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

        current_tasks = ['a','b','c','d','e','f','g','h','i','j','k']
        for task in current_tasks:
            task_text = task[0]
            self.add_task(None, task_text, True)

        self.master.bind("<Configure>", self.on_frame_configure)
        self.tasks_canvas.bind("<Configure>", self.task_width)

    def add_task(self, event=None, task_text=None, from_db=False):
        if not task_text:
            task_text = self.task_create.get(1.0, tkinter.END).strip()

        if len(task_text) > 0:
            new_task = tkinter.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-1>", self.remove_task)
            new_task.pack(side=tkinter.TOP, fill=tkinter.X)

            self.tasks.append(new_task)

            if not from_db:
                self.save_task(task_text)

        self.task_create.delete(1.0, tkinter.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)

            event.widget.destroy()

            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)
        #self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))
    def canvasframe_width(self, event):
        canvas_width = event.width
        self.R_super_canvas.itemconfig(self.objlist_win, width = canvas_width)
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

        menubar.add_separator()
        menubar.add_command(label = 'Render Image')

        root.config(menu=menubar)
    def init_addmenu(self,root):
        add_menu = tkinter.Menu(root,tearoff=0)
        add_menu.add_command(label = 'Camera')
        #lights
        light_menu = tkinter.Menu(add_menu, tearoff=0)
        light_menu.add_command(label = 'Point')
        light_menu.add_command(label = 'Directional')
        add_menu.add_cascade(label = 'Light',menu =light_menu)
        add_menu.add_separator()

        add_menu.add_command(label = 'Plane')
        add_menu.add_command(label = 'Cube')
        add_menu.add_command(label = 'UV Sphere')
        add_menu.add_command(label = 'Ico Sphere')
        add_menu.add_separator()
        add_menu.add_command(label = 'Graph')
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
        import_menu.add_command(label = 'Wavefront (OBJ)')
        object_menu.add_cascade(label='Import',menu = import_menu)
        #Export
        export_menu = tkinter.Menu(object_menu,tearoff=0)
        export_menu.add_command(label = 'Wavefront (OBJ)')
        object_menu.add_cascade(label='Export',menu = export_menu)
        
        return object_menu
if __name__=='__main__':
    app = main(tkinter.Tk())
    app.mainloop()