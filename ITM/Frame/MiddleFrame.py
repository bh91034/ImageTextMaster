import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from ITM.Data.DataManager import DataManager

class CanvasWorkier:
    def __init__(self, img_file, canvas):
        self.img_file = img_file
        self.canvas = canvas
        self.image = Image.open(img_file)
        self.photoimage = None
    
    def drawImage(self):
        self.photoimage = ImageTk.PhotoImage(file=self.img_file)
        
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        # sometimes at the very first draw, the canvas size was (1,1) and it makes error
        if canvas_w <= 1 or canvas_h <= 1:
            return

        self.canvas.cnvs.delete("all")

        self.scale_ratio = 1.0
        self.canvas.cnvs.create_image(0,0, image=self.photoimage, anchor="nw")
        # Reference : 
        # - https://stackoverflow.com/questions/56043767/show-large-image-using-scrollbar-in-python
        self.canvas.cnvs.config(scrollregion=self.canvas.cnvs.bbox(tk.ALL))

        from ITM.Frame.LowFrame import LowFrame
        from ITM.Control.ControlManager import ControlManager
        # draw lines for selected text in check list of remove tab in LowFrame
        idx = 0
        list_values = LowFrame.low_frm_text_list.list_values
        if list_values == None or len(list_values) == 0:
            return
        for item in LowFrame.low_frm_text_list.list_values:
            if item.get() == True:
                start_pos, end_pos = DataManager.getBorderInfoOfText(ControlManager.work_file, idx)
                self.canvas.cnvs.create_rectangle(
                    int(self.scale_ratio*start_pos[0]),  # start x 
                    int(self.scale_ratio*start_pos[1]),  # start y
                    int(self.scale_ratio*end_pos[0]),    # end x
                    int(self.scale_ratio*end_pos[1]),    # end y
                    #outline='green'
                    outline='#00ff00'
                )
            idx = idx + 1
    
    def changeImageFile(self, img_file):
        self.img_file = img_file
        self.image = Image.open(img_file)

    def setImage(self, image):
        if image is not None:
            self.image = image
    
    def getImage(self):
        return self.image
    
    @classmethod
    def getAdaptedImageSize(cls, img_w, img_h, canvas_w, canvas_h):
        w_ratio = img_h/img_w
        h_ratio = img_w/img_h
        if canvas_w*w_ratio <= canvas_h:
            return int(canvas_w), int(canvas_w*w_ratio)
        else:
            return int(canvas_h*h_ratio), int(canvas_h)
    
#------------------------------------------------------------------------------
# Middle frame : middle side canvases
#------------------------------------------------------------------------------
class MiddleFrame:
    mid_frm = None
    src_canvas_worker = None
    out_canvas_worker = None

    def __init__(self, root):
        from ITM.Control.ControlManager import ControlManager
        # middle canvases frame
        mid_frm = tk.Frame(root)
        MiddleFrame.mid_frm = mid_frm
        mid_frm.pack(padx=2, pady=2, fill='both', expand=True)

        left_canvas = ScrollableImage(mid_frm)
        left_canvas.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

        # Reference :
        # - https://www.youtube.com/watch?v=xiGQD2J47nA
        # - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/image_bg_resize.py
        # - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/
        def resizer(e):
            MiddleFrame.redrawCanvasImages()
 
        left_canvas.bind('<Configure>', resizer)
        # Added by Q&A from stackoverflow
        # https://stackoverflow.com/questions/72713209/how-to-keep-two-textboxes-the-same-size-when-resizing-window-with-python-tkinter
        mid_frm.columnconfigure(0, weight=1)
        mid_frm.rowconfigure(0, weight=1)

        MiddleFrame.src_canvas_worker = CanvasWorkier(ControlManager.work_file, left_canvas)

    # TODO: why those variables could not be inside the method? (canvas doesn't display)
    bg_left = None
    new_bg_left = None
    bg_right = None
    new_bg_right = None
    @classmethod
    def redrawCanvasImages(cls):
        print ('[MiddleFrame.resizeCanvasImages] called...')
        cls.src_canvas_worker.drawImage()

    @classmethod
    def getAdaptedImageSize(cls, img_w, img_h, canvas_w, canvas_h):
        w_ratio = img_h/img_w
        h_ratio = img_w/img_h
        if canvas_w*w_ratio <= canvas_h:
            return int(canvas_w), int(canvas_w*w_ratio)
        else:
            return int(canvas_h*h_ratio), int(canvas_h)

    @classmethod
    def resetCanvasImages(cls, work_file):
        from ITM.Control.ControlManager import ControlManager
        print ('[MiddleFrame] resetCanvasImages() called...')

        src_file = work_file
        cls.src_canvas_worker.changeImageFile(src_file)
        cls.src_canvas_worker.drawImage()

# Reference : 
# - https://stackoverflow.com/questions/56043767/show-large-image-using-scrollbar-in-python
class ScrollableImage(tk.Frame):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        sw = kw.pop('scrollbarwidth', 10)
        super(ScrollableImage, self).__init__(master=master, **kw)
        self.cnvs = tk.Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image(0, 0, anchor='nw', image=self.image)
        # Vertical and Horizontal scrollbars
        self.v_scroll = tk.Scrollbar(self, orient='vertical', width=sw)
        self.h_scroll = tk.Scrollbar(self, orient='horizontal', width=sw)
        # Grid and configure weight.
        self.cnvs.grid(row=0, column=0,  sticky='nsew')
        self.h_scroll.grid(row=1, column=0, sticky='ew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # Set the scrollbars to the canvas
        self.cnvs.config(xscrollcommand=self.h_scroll.set, 
                           yscrollcommand=self.v_scroll.set)
        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.cnvs.yview)
        self.h_scroll.config(command=self.cnvs.xview)
        # Assign the region to be scrolled 
        self.cnvs.config(scrollregion=self.cnvs.bbox('all'))
        self.cnvs.bind_class(self.cnvs, "<MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, evt):
        if evt.state == 0 :
            self.cnvs.yview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)), 'units') # For windows
        if evt.state == 1:
            self.cnvs.xview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.xview_scroll(int(-1*(evt.delta/120)), 'units') # For windows
