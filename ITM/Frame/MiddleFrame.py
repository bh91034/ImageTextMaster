import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from ITM.Data.DataManager import DataManager

#------------------------------------------------------------------------------
# Middle frame : middle side canvases
#------------------------------------------------------------------------------
class MiddleFrame:
    global mid_frm
    left_canvas = None
    right_canvas = None
    src_photoimage = None
    out_photoimage = None
    src_image = None

    def __init__(self, root):
        from ITM.Control.ControlManager import ControlManager
        # middle canvases frame
        mid_frm = tk.Frame(root)
        mid_frm.pack(padx=2, pady=2, fill='both', expand=True)

        left_canvas = tk.Canvas(mid_frm, bg='lightgray')
        left_canvas.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
        right_canvas = tk.Canvas(mid_frm, bg='lightgray')
        right_canvas.grid(row=0, column=1, sticky=tk.E+tk.W+tk.N+tk.S)
        MiddleFrame.src_image = Image.open(ControlManager.work_file)
        MiddleFrame.left_canvas = left_canvas
        MiddleFrame.right_canvas = right_canvas
        MiddleFrame.src_photoimage = ImageTk.PhotoImage(file=ControlManager.work_file)
        MiddleFrame.out_photoimage = ImageTk.PhotoImage(file=ControlManager.work_file)

        # Reference :
        # - https://www.youtube.com/watch?v=xiGQD2J47nA
        # - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/image_bg_resize.py
        # - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/
        def resizer(e):
            MiddleFrame.resizeCanvasImages()
 
        left_canvas.bind('<Configure>', resizer)
        # Added by Q&A from stackoverflow
        # https://stackoverflow.com/questions/72713209/how-to-keep-two-textboxes-the-same-size-when-resizing-window-with-python-tkinter
        mid_frm.columnconfigure((0,1), weight=1)
        mid_frm.rowconfigure(0, weight=1)

    # TODO: why those variables could not be inside the method? (canvas doesn't display)
    bg_left = None
    new_bg_left = None
    bg_right = None
    new_bg_right = None
    @classmethod
    def resizeCanvasImages(cls):
        global bg_left, new_bg_left, bg_right, new_bg_right
        print ('[MiddleFrame.resizeCanvasImages] called...')
        canvas_w = cls.left_canvas.winfo_width()
        canvas_h = cls.left_canvas.winfo_height()

        # variables
        left_canvas = cls.left_canvas
        right_canvas = cls.right_canvas
        left_image = cls.src_photoimage
        right_image = cls.out_photoimage
        bg_left = cls.bg_left
        new_bg_left = cls.new_bg_left
        bg_right = cls.bg_right
        new_bg_right = cls.new_bg_right

        # clear canvases
        left_canvas.delete("all")
        right_canvas.delete("all")

        # check if a image to be drawn exists
        if left_image == None:
            return

        # draw image
        scale_ratio = 1.0
        if canvas_w >= left_image.width() and canvas_h >= left_image.height():
            left_canvas.create_image(0,0, image=left_image, anchor="nw")
            right_canvas.create_image(0,0, image=right_image, anchor="nw")
        else:
            left_image_resize = MiddleFrame.src_image
            right_image_resize = MiddleFrame.src_image

            w1, h1 = left_image_resize.size
            w, h = cls.getAdaptedImageSize(w1, h1, canvas_w, canvas_h)
            bg_left = left_image_resize.resize((w, h), Image.ANTIALIAS)
            new_bg_left = ImageTk.PhotoImage(bg_left)
            left_canvas.create_image(0,0, image=new_bg_left, anchor="nw")
            bg_right = right_image_resize.resize((w, h), Image.ANTIALIAS)
            new_bg_right = ImageTk.PhotoImage(bg_right)
            right_canvas.create_image(0,0, image=new_bg_right, anchor="nw")
            scale_ratio = w/w1
        
        # draw lines for selected text in check list of remove tab in LowFrame
        idx = 0
        from ITM.Frame.LowFrame import LowFrame
        from ITM.Control.ControlManager import ControlManager
        list_values = LowFrame.remove_tab_text_list.list_values
        if list_values == None or len(list_values) == 0:
            return
        for item in LowFrame.remove_tab_text_list.list_values:
            if item.get() == True:
                start_pos, end_pos = DataManager.getBorderInfoOfText(ControlManager.work_file, idx)
                left_canvas.create_rectangle(
                    int(scale_ratio*start_pos[0]),  # start x 
                    int(scale_ratio*start_pos[1]),  # start y
                    int(scale_ratio*end_pos[0]),    # end x
                    int(scale_ratio*end_pos[1]),    # end y
                    outline='red'
                )
            idx = idx + 1

    @classmethod
    def getAdaptedImageSize(cls, img_w, img_h, canvas_w, canvas_h):
        w_ratio = img_h/img_w
        h_ratio = img_w/img_h
        if canvas_w*w_ratio <= canvas_h:
            return int(canvas_w), int(canvas_w*w_ratio)
        else:
            return int(canvas_h*h_ratio), int(canvas_h)

    @classmethod
    def resetCanvasImages(cls, work_image):
        print ('[MiddleFrame.resetCanvasImages] called...')
        
        # clear canvases
        cls.left_canvas.delete("all")
        cls.right_canvas.delete("all")
        cls.src_photoimage = None
        cls.out_photoimage = None

        # load new images and draw them to canvases
        cls.src_image = Image.open(work_image)
        cls.src_photoimage = ImageTk.PhotoImage(file=work_image)
        cls.out_photoimage = ImageTk.PhotoImage(file=work_image)
        cls.resizeCanvasImages()
