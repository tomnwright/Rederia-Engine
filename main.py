import tkinter
import renderwin
def donothing():
    print("HI")
class main(tkinter.Frame):

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.init_win()
    def init_win(self):

        root = self.master
        root.iconbitmap("graphics/icon/icon_03.ico")
        root.title("Render.IA")
        root.geometry("1000x500")

        panel = tkinter.Frame(root,height = 40,bg = 'green')
        panel.pack(side = 'top',fill='x')

        menubar = tkinter.Menu(root)
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = tkinter.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = tkinter.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu = menubar)


        

        panes = tkinter.PanedWindow(root,orient='horizontal')
        panes.pack(side='bottom',fill='both',expand=1)

        
        left = tkinter.Frame(panes,bg='blue')
        panes.add(left,minsize=250)
        right = tkinter.Frame(panes,bg='red')
        panes.add(right,minsize=250)


if __name__=='__main__':
    app = main(tkinter.Tk())
    app.mainloop()