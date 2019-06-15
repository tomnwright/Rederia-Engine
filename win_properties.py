import tkinter,ria
from tkinter import ttk
from ria_ui import *

class main(tkinter.Frame):

    def __init__(self, master, obj):
        super().__init__(master)
        self.obj = obj
        self.master = master
        self.imgs = Style.images()

        self.master.overrideredirect(True)
        self.master.config(bg = Style.colour.bw[0],borderwidth=1)
        self.master.resizable(1,0)
        self.master.grab_set()
        self.master.title('Properties')

        win_x = int(0.5 * self.master.winfo_screenwidth())
        win_y = int(0.5 * self.master.winfo_screenheight())
        self.master.geometry('200x500+{}+{}'.format(win_x-100, win_y-250))

        self.choice_frame = tkinter.Frame(self.master, bg = Style.colour.bw[3])
        self.choice_frame.pack(side = 'top', fill= 'both')
        self.choice_frame.bind('<B1-Motion>', self.OnMotion)
        self.choice_frame.bind('<ButtonPress-1>', self.StartMotion)
        self.choice_frame.bind('<ButtonRelease-1>', self.EndMotion)


        self.frame_selectors = []
        self.frames = []

        for i in (self.obj.data):
            frame_class, icon = Properties_Frames.get_frame(i, self.imgs)

            frame = frame_class(self.master, obj = self.obj)
            self.frames.append(frame)

            selector = tkinter.Label(self.choice_frame, image = icon, bg = Style.colour.bw[2])
            selector.pack(side = 'left', fill = 'both',pady = (3,0,),padx=1)
            selector.bind('<Button-1>', self.select_btn)
            self.frame_selectors.append(selector)
        self.frames[0].pack(side = 'top',fill='both')
        self.active = self.frame_selectors[0]  
        self.active.pack_configure(padx = (3,0,)) 
        self.active.config(bg = Style.colour.bw[0])
        
        self.btn_frame = tkinter.Frame(self.master, bg = Style.colour.bw[0])
        self.init_bottom(self.btn_frame)
        self.btn_frame.pack(side = 'bottom', fill = 'x',expand=1)

        
    def init_bottom(self, frame):
        self.apply = tkinter.Button(
            frame,
            text = 'Apply',
            relief = 'flat',
            bg = Style.colour.bw[5],
            activebackground = Style.colour.bw[5],
            command = self.apply_properties
            )
        self.cancel = tkinter.Button(
            frame,
            text = 'Cancel',
            relief = 'flat',
            bg = Style.colour.delete_button[0],
            activebackground = Style.colour.delete_button[1],
            command = self.master.destroy
            )
        self.apply.pack(side = 'left',fill = 'both',expand = 1,padx = (4,2,),pady = 4)
        self.cancel.pack(side = 'left',fill = 'both',expand = 1,padx = (2,4,),pady = 4)

    def select_btn(self, event):
        widget = event.widget

        self.active.config(bg = Style.colour.bw[2])
        self.active = widget
        self.active.config(bg = Style.colour.bw[0])

        #print

    def apply_properties(self):
        for i in self.frames:
            i.apply_all()
        self.master.destroy()
    def StartMotion(self,event):
        self.x1 = event.x
        self.y1 = event.y
    def EndMotion(self,event):
        self.x1 = None
        self.y1 = None
    def OnMotion(self, event):
        deltax = event.x - self.x1
        deltay = event.y - self.y1
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry('+%d+%d' % (x,y))
        

if __name__ == '__main__':
    test_handler = ria.ObjectMaster()
    test_handler.add_object(ria.Object3D(test_handler,'test'))
    test_obj = ria.Object3D(test_handler, 'test1')
    test_handler.add_object(test_obj)
    top = main(tkinter.Toplevel(),obj = test_obj)
    top.mainloop()