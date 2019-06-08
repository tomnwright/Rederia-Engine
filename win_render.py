import tkinter
from PIL import Image, ImageTk

class main(tkinter.Frame):

    def __init__(self, master=None,resolution=(100,100,)):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.init_win()

    def init_win(self):
        self.master.iconbitmap("graphics/icon/icon_03w.ico")
        self.master.title("Render.IA")


if __name__=='__main__':
    app = main(tkinter.Tk())
    app.mainloop()