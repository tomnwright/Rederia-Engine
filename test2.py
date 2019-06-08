from tkinter import *
import os

root = Tk()
termf = Frame(root, width = 400, height = 200)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 80x20 -sb -e python &' % wid)

root.mainloop()