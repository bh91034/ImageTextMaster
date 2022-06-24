import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

#------------------------------------------------------------------------------
# Middle frame : middle side canvases
#------------------------------------------------------------------------------
class MiddleFrame:
    global mid_frm
    def __init__(self, root):
        # middle canvases frame
        mid_frm = tk.Frame(root)
        mid_frm.pack(padx=2, pady=2, fill='both', expand=True)

        bg = ImageTk.PhotoImage(file='./images/a.png')
        left_canvas = tk.Canvas(mid_frm, bg='lightgray')
        left_canvas.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
        #left_canvas.create_image(0,0, image=bg, anchor="nw")
        right_canvas = tk.Canvas(mid_frm, bg='lightgray')
        right_canvas.grid(row=0, column=1, sticky=tk.E+tk.W+tk.N+tk.S)
        #right_canvas.create_image(0,0, image=bg, anchor="nw")

        def resizer_size_calculate(img_w, img_h, canvas_w, canvas_h):
            print ('########> w1=', img_w, ', h1=', img_h, ', w2=', canvas_w, ', h2=', canvas_h)
            w_ratio = img_h/img_w
            h_ratio = img_w/img_h
            print ('########> ratio=', w_ratio, ', img_w=', img_w, ', img_h=', img_w*w_ratio)
            # step 1
            if canvas_w*w_ratio <= canvas_h:
                return int(canvas_w), int(canvas_w*w_ratio)
            else:
                return int(canvas_h*h_ratio), int(canvas_h)

        # Reference :
        # - https://www.youtube.com/watch?v=xiGQD2J47nA
        # - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/image_bg_resize.py
        # - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/
        def resizer(e):
            global bg_resize, bg_left, new_bg_left, bg_right, new_bg_right
            left_canvas.delete("all")
            right_canvas.delete("all")
            if e.width >= bg.width() and e.height >= bg.height():
                left_canvas.create_image(0,0, image=bg, anchor="nw")
                right_canvas.create_image(0,0, image=bg, anchor="nw")
            else:
                bg_resize = Image.open('./images/a.png')
                w1, h1 = bg_resize.size
                w, h = resizer_size_calculate(w1, h1, e.width, e.height)
                bg_left = bg_resize.resize((w, h), Image.ANTIALIAS)
                new_bg_left = ImageTk.PhotoImage(bg_left)
                left_canvas.create_image(0,0, image=new_bg_left, anchor="nw")
                bg_right = bg_resize.resize((w, h), Image.ANTIALIAS)
                new_bg_right = ImageTk.PhotoImage(bg_right)
                right_canvas.create_image(0,0, image=new_bg_right, anchor="nw")

        left_canvas.bind('<Configure>', resizer)


        # Added by Q&A from stackoverflow
        # https://stackoverflow.com/questions/72713209/how-to-keep-two-textboxes-the-same-size-when-resizing-window-with-python-tkinter
        mid_frm.columnconfigure((0,1), weight=1)
        mid_frm.rowconfigure(0, weight=1)