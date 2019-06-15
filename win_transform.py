import tkinter
from ria_ui import *


class main(tkinter.Frame):

    def __init__(self, master=None,object_list = []):
        super().__init__(master)
        self.object_list = object_list
        self.master = master
        self.imgs = Style.images()

        self.master.overrideredirect(True)
        self.master.config(bg = Style.colour.bw[0],borderwidth=1)
        self.master.resizable(1,0)
        self.master.grab_set()
        self.master.title('Transform')

        win_x = int(0.5 * self.master.winfo_screenwidth())
        win_y = int(0.5 * self.master.winfo_screenheight())
        self.master.geometry('200x175+{}+{}'.format(win_x-100, win_y-90))
    

        self.choice_frame = tkinter.Frame(self.master, bg = Style.colour.bw[3])
        self.init_top(self.choice_frame)
        self.choice_frame.pack(side = 'top', fill= 'both')
        self.choice_frame.bind('<B1-Motion>', self.OnMotion)
        self.choice_frame.bind('<ButtonPress-1>', self.StartMotion)
        self.choice_frame.bind('<ButtonRelease-1>', self.EndMotion)

        self.v3_input = input_ui.DisplayFrame(self.master, text = 'Translate')
        self.v3_input.pack(fill='both',padx = 5,pady=(2,2,))

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
            command = self.apply_transform
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
    def init_top(self, frame):
        self.btn_tra = LabeledWidget.Label(0,frame, image = self.imgs.translate, bg = Style.colour.bw[0])
        self.btn_rot = LabeledWidget.Label(1,frame, image = self.imgs.rotate, bg = Style.colour.bw[2])
        self.btn_sca = LabeledWidget.Label(2,frame, image = self.imgs.scale, bg = Style.colour.bw[2])

        self.btn_tra.bind('<Button-1>',self.select_btn)
        self.btn_rot.bind('<Button-1>',self.select_btn)
        self.btn_sca.bind('<Button-1>',self.select_btn)

        self.btn_tra.pack(side = 'left', fill = 'both',pady = (3,0,),padx = (3,1,))
        self.btn_rot.pack(side = 'left', fill = 'both',pady = (3,0,),padx=1)
        self.btn_sca.pack(side = 'left', fill = 'both',pady = (3,0,),padx=1)

        self.active = self.btn_tra
    def select_btn(self, event):
        widget = event.widget

        self.active.config(bg = Style.colour.bw[2])
        self.active = widget
        self.active.config(bg = Style.colour.bw[0])

        self.v3_input.config(text = ['Translate','Rotate','Scale'][widget.label])
    def apply_transform(self):
        a_n = self.active.label
        affector = self.v3_input.get_v3()
        for obj in self.object_list:
           [obj.translate,obj.rotate,obj.scale][a_n](affector)
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
    top = main(tkinter.Toplevel())
    top.mainloop()