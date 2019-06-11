import tkinter
from tkinter import ttk
from ria_ui import *


class main_old(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.config(bg = 'gray')
        self.imgs = Style.images()

        '''tab_frame = tkinter.Frame(self.master,bg = 'darkgray')
    
        tab_obj = tkinter.Label(tab_frame,image = self.imgs.obj,bg='black')
        tab_obj.pack(side='left')
        tkinter.Separtor
        tab_obj = tkinter.Label(tab_frame,image = self.imgs.obj,bg='black')
        tab_obj.pack(side='left')

        tab_obj = tkinter.Label(tab_frame,image = self.imgs.obj,bg='black')
        tab_obj.pack(side='left')

        tab_frame.pack(side = 'top', fill = 'x',padx = 5,pady=5)'''

class main(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.config(bg = 'gray')
        self.master.grab_set()
        self.imgs = Style.images()

        self.notebook = ttk.Notebook(self.master)

        self.f1 = tkinter.Frame(self.notebook)
        self.f2 = tkinter.Frame(self.notebook)

        loc = tkinter.LabelFrame(self.f1,text='Location',padx =2,pady=2)
        x = tkinter.Label(loc,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        x_label = tkinter.Label(x,text='X:',bg = 'black',fg='white',anchor = 'w')
        x_label.pack(side = 'left')
        x.pack(side = 'top',fill='both', padx = 2, pady=2)

        y = tkinter.Label(loc,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        y_label = tkinter.Label(y,text='Y:',bg = 'black',fg='white',anchor = 'w')
        y_label.pack(side = 'left')
        y.pack(side = 'top',fill='both', padx = 2, pady=2)
        
        z = tkinter.Label(loc,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        z_label = tkinter.Label(z,text='Z:',bg = 'black',fg='white',anchor = 'w')
        z_label.pack(side = 'left')
        z.pack(side = 'top',fill='both', padx = 2, pady=2)

        loc.pack(fill='both',padx=5,pady=5,expand=1)
        
        rot = tkinter.LabelFrame(self.f1,text='Rotation',padx =2,pady=2)
        x = tkinter.Label(rot,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        x_label = tkinter.Label(x,text='X:',bg = 'black',fg='white',anchor = 'w')
        x_label.pack(side = 'left')
        x.pack(side = 'top',fill='both', padx = 2, pady=2)

        y = tkinter.Label(rot,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        y_label = tkinter.Label(y,text='Y:',bg = 'black',fg='white',anchor = 'w')
        y_label.pack(side = 'left')
        y.pack(side = 'top',fill='both', padx = 2, pady=2)
        
        z = tkinter.Label(rot,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        z_label = tkinter.Label(z,text='Z:',bg = 'black',fg='white',anchor = 'w')
        z_label.pack(side = 'left')
        z.pack(side = 'top',fill='both', padx = 2, pady=2)

        rot.pack(fill='both',padx=5,pady=5,expand=1)
        
        scale = tkinter.LabelFrame(self.f1,text='Scale',padx =2,pady=2)
        x = tkinter.Label(scale,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        x_label = tkinter.Label(x,text='X:',bg = 'black',fg='white',anchor = 'w')
        x_label.pack(side = 'left')
        x.pack(side = 'top',fill='both', padx = 2, pady=2)

        y = tkinter.Label(scale,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        y_label = tkinter.Label(y,text='Y:',bg = 'black',fg='white',anchor = 'w')
        y_label.pack(side = 'left')
        y.pack(side = 'top',fill='both', padx = 2, pady=2)
        
        z = tkinter.Label(scale,text='12.5000',bg = 'black',fg='white',anchor = 'e')
        z_label = tkinter.Label(z,text='Z:',bg = 'black',fg='white',anchor = 'w')
        z_label.pack(side = 'left')
        z.pack(side = 'top',fill='both', padx = 2, pady=2)

        scale.pack(fill='both',padx=5,pady=5,expand=1)



        rot = tkinter.LabelFrame(self.f2,text='Rotation')
        btn = tkinter.Button(rot, text='Change')
        btn.pack()
        rot.pack()

        self.notebook.add(self.f1, image = self.imgs.obj)
        self.notebook.add(self.f2, image = self.imgs.obj)

        self.notebook.pack(fill='both',expand=1)
        

        


if __name__ == '__main__':
    top = main(tkinter.Toplevel())
    top.mainloop()