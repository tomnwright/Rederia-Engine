import tkinter
from ria_ui import *


class main(tkinter.Frame):

    def __init__(self, master=None,object_list = []):
        super().__init__(master)
        self.master = master
        self.object_list = object_list
        self.master.resizable(1,0)
        self.master.grab_set()

        self.master.update()
        self.master.geometry('250x175')

        self.master.title('Transform')
        self.imgs = Style.images()
        
        self.choice_frame = tkinter.Frame(self.master, bg = 'red')
        self.init_top(self.choice_frame)
        self.choice_frame.pack(side = 'top', fill= 'both')

        self.v3_input = Vector3_ui.DisplayFrame(self.master, text = 'Translate')
        self.v3_input.pack(fill='both',padx = 5,pady=5)

        self.btn_frame = tkinter.Frame(self.master, bg = 'green')
        self.init_bottom(self.btn_frame)
        self.btn_frame.pack(side = 'bottom', fill = 'x')#,expand=1)

    def init_bottom(self, frame):
        self.apply = tkinter.Button(frame, text = 'Apply', relief = 'flat', bg = 'darkgray',command = self.apply_transform)
        self.cancel = tkinter.Button(frame, text = 'Cancel', relief = 'flat', bg = 'darkred',command = self.master.destroy)
        self.apply.pack(side = 'left',fill = 'both',expand = 1)
        self.cancel.pack(side = 'left',fill = 'both',expand = 1)
    def init_top(self, frame):
        self.btn_tra = LabeledWidget.Label(0,frame, image = self.imgs.translate)
        self.btn_rot = LabeledWidget.Label(1,frame, image = self.imgs.rotate)
        self.btn_sca = LabeledWidget.Label(2,frame, image = self.imgs.scale)

        self.btn_tra.bind('<Button-1>',self.select_btn)
        self.btn_rot.bind('<Button-1>',self.select_btn)
        self.btn_sca.bind('<Button-1>',self.select_btn)

        self.btn_tra.pack(side = 'left', fill = 'both')
        self.btn_rot.pack(side = 'left', fill = 'both')
        self.btn_sca.pack(side = 'left', fill = 'both')

        self.active = self.btn_tra
    def select_btn(self, event):
        widget = event.widget

        self.active.config(bg = 'gray')
        self.active = widget
        self.active.config(bg = 'orange')
        print(['Translate','Rotate','Scale'][widget.label])

        self.v3_input.config(text = ['Translate','Rotate','Scale'][widget.label])
    def apply_transform(self):
        a_n = self.active.label
        affector = self.v3_input.get_v3()
        for obj in self.object_list:
           [obj.translate,obj.rotate,obj.scale][a_n](affector)
        self.master.destroy()
        

        
if __name__ == '__main__':
    top = main(tkinter.Toplevel())
    top.mainloop()