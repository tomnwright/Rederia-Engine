import tkinter,ria
from ria_ui import *
from tkinter import messagebox
import win_render,win_properties

class main(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        self.init_ria()
        self.init_win()
        menus.init_menubar(self)    
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

        self.obj_canvas = tkinter.Canvas(self.right_frame,width=1,highlightthickness=0)#,bg='green')
        self.obj_canvas.pack(side='left',fill='both',expand=1)
        #scrollbar
        self.obj_scroll = tkinter.Scrollbar(self.right_frame, orient="vertical", command=self.obj_canvas.yview)
        self.obj_canvas.config(yscrollcommand=self.obj_scroll.set)
        self.obj_scroll.pack(side='right',fill='y')
        
        self.obj_frame = tkinter.Frame(self.obj_canvas)
        self.obj_frameCANV = self.obj_canvas.create_window((0, 0), window=self.obj_frame, anchor="nw")

        self.init_objlist(self.obj_frame)

        self.obj_canvas.bind('<Configure>',self.objcanvas_width)
        self.obj_frame.bind('<Configure>',self.update_objscroll)
    def init_ria(self):
        self.handler = ria.ObjectMaster()
        self.images = Style.images()
    
    def init_objlist(self,root):
        btn1 = tkinter.Menubutton(
            root,
            text='Add Object',
            bg = 'darkgray',
            activebackground = 'gray')
        a_men = menus.init_addmenu(btn1,self)
        btn1['menu'] = a_men
        btn1.pack(side = 'top',fill='both',padx= 5,pady= 5)
    
    def objcanvas_width(self, event):
        canvas_width = event.width
        self.obj_canvas.itemconfig(self.obj_frameCANV, width = canvas_width)
        self.update_objscroll()
    def update_objscroll(self,*args):
        scrollable = self.obj_canvas
        scrollable.configure(scrollregion=scrollable.bbox("all"))
    def properties_temp(self):
        if self.handler.active:
            self.handler.active.properties_temp()

            props_win = win_properties.main(tkinter.Toplevel())
            #props_win.grab_set()
            props_win.mainloop()
        else:
            messagebox.showerror('No Active Object','should this error happen...')






if __name__=='__main__':
    app = main(tkinter.Tk())
    app.mainloop()