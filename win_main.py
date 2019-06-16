import tkinter,ria
from ria_ui import *
from tkinter import messagebox
import win_render,win_properties,win_transform

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
        self.init_left_frame(panes)

        #right
        self.init_right_frame(panes)
    def init_ria(self):
        self.handler = ria.ObjectMaster()
        self.images = Style.images()
    
    def init_right_frame(self,panes):
        self.right_frame = tkinter.Frame(panes,bg = Style.colour.bw[2])
        panes.add(self.right_frame,minsize=250)
        
        title = tkinter.Label(self.right_frame, text = 'Object Outline',bg = Style.colour.bw[3],fg = 'white',padx=3,pady=3)
        title.pack(side = 'top', fill='both')
        

        self.obj_canvas = tkinter.Canvas(self.right_frame,width=1,highlightthickness=0,bg=Style.colour.bw[2])
        self.obj_canvas.pack(side='left',fill='both',expand=1)
        #scrollbar
        self.obj_scroll = tkinter.Scrollbar(self.right_frame, orient="vertical", command=self.obj_canvas.yview)
        self.obj_canvas.config(yscrollcommand=self.obj_scroll.set)
        self.obj_scroll.pack(side='right',fill='y')
        
        self.obj_frame = tkinter.Frame(self.obj_canvas,bg=Style.colour.bw[2],padx = 5, pady = 10)
        self.obj_frameCANV = self.obj_canvas.create_window((0, 0), window=self.obj_frame, anchor="nw")

        

        self.obj_canvas.bind('<Configure>',self.objcanvas_width)
        self.obj_frame.bind('<Configure>',self.update_objscroll)
    def init_left_frame(self,panes):
        left = tkinter.Frame(panes,bg='red')#Style.colour.bw[5])
        panes.add(left,minsize=250)
        
        title = tkinter.Label(left, text = '3D Viewport',bg = Style.colour.bw[3],fg = 'white',padx=3,pady=3)#,anchor = 'w')
        title.pack(side = 'top', fill='both')

        self.canvas_master = ria.viewer.ViewMaster(left,obj_master = self.handler, bg = Style.colour.bw[5],highlightthickness=0)# grey border caused by highlightthickness
        self.canvas_master.pack(side = 'top', fill='both',expand = 1,padx= 0, pady=0)
        self.canvas_master.bind('<Button-1>', self.canvas_master.update)
        
    def init_listbtns(self,root):
        btn_frame = tkinter.Frame(root,bg = Style.colour.bw[2])

        add_btn = tkinter.Menubutton(
            btn_frame,
            text='Add Object',
            bg = 'darkgray',
            activebackground = 'gray')
        a_men = menus.init_addmenu(add_btn,self)
        add_btn['menu'] = a_men
        add_btn.pack(side = 'top',padx=5,pady= 5)

        btn_frame.pack(side = 'top', fill='x')
    
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

            props_win = win_properties.main(tkinter.Toplevel(),self.handler.active)
            #props_win.grab_set()
            props_win.mainloop()
        else:
            messagebox.showerror('No Active Object','should this error happen...')






if __name__=='__main__':
    app = main(tkinter.Tk())
    app.mainloop()