import tkinter as tk
from tkinter import END, scrolledtext
from tkinter import ttk
from turtle import bgcolor
from PIL import ImageTk, Image

# root window
root = tk.Tk()
root.geometry('1200x600+20+20')
#root.resizable(False, False)
root.title('Button Demo')

#------------------------------------------------------------------------------
# Top frame : top side buttons layout and command handlers
#------------------------------------------------------------------------------
from ITM.Frame.TopFrame import TopFrame
top_frm = TopFrame(root)

#------------------------------------------------------------------------------
# Middle frame : middle side canvases
#------------------------------------------------------------------------------
from ITM.Frame.MiddleFrame import MiddleFrame
mid_frm = MiddleFrame(root)

#------------------------------------------------------------------------------
# Low frame : low side tabbed pane (tools)
#------------------------------------------------------------------------------
from ITM.Frame.LowFrame import LowFrame
low_frm = LowFrame(root)



root.mainloop()