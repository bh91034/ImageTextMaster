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

        self.scale_ratio = 1.0
        if canvas_w >= self.photoimage.width() and canvas_h >= self.photoimage.height():
            self.canvas.create_image(0,0, image=self.photoimage, anchor="nw")
        else:
            w1, h1 = self.image.size
            w, h = CanvasWorkier.getAdaptedImageSize(w1, h1, canvas_w, canvas_h)
            image_resized = self.image.resize((w, h), Image.ANTIALIAS)
            self.photoimage = ImageTk.PhotoImage(image_resized)
            self.canvas.create_image(0,0, image=self.photoimage, anchor="nw")
            self.scale_ratio = w/w1
        
        from ITM.Frame.LowFrame import LowFrame
        from ITM.Control.ControlManager import ControlManager
        tab_idx = LowFrame.notebook.index(LowFrame.notebook.select())
        if tab_idx == 0:
            # draw lines for selected text in check list of remove tab in LowFrame
            idx = 0
            list_values = LowFrame.remove_tab_text_list.list_values
            if list_values == None or len(list_values) == 0:
                return
            for item in LowFrame.remove_tab_text_list.list_values:
                if item.get() == True:
                    start_pos, end_pos = DataManager.getBorderInfoOfText(ControlManager.work_file, idx)
                    self.canvas.create_rectangle(
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

        left_canvas = tk.Canvas(mid_frm, bg='lightgray')
        left_canvas.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
        right_canvas = tk.Canvas(mid_frm, bg='lightgray')
        right_canvas.grid(row=0, column=1, sticky=tk.E+tk.W+tk.N+tk.S)

        src_file = ControlManager.work_file
        out_file = DataManager.getOutputFile(ControlManager.work_file)

        # Reference :
        # - https://www.youtube.com/watch?v=xiGQD2J47nA
        # - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/image_bg_resize.py
        # - https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/
        def resizer(e):
            MiddleFrame.redrawCanvasImages()
 
        left_canvas.bind('<Configure>', resizer)
        # Added by Q&A from stackoverflow
        # https://stackoverflow.com/questions/72713209/how-to-keep-two-textboxes-the-same-size-when-resizing-window-with-python-tkinter
        mid_frm.columnconfigure((0,1), weight=1)
        mid_frm.rowconfigure(0, weight=1)

        MiddleFrame.src_canvas_worker = CanvasWorkier(src_file, left_canvas)
        MiddleFrame.out_canvas_worker = CanvasWorkier(out_file, right_canvas)

    # TODO: why those variables could not be inside the method? (canvas doesn't display)
    bg_left = None
    new_bg_left = None
    bg_right = None
    new_bg_right = None
    @classmethod
    def redrawCanvasImages(cls):
        global bg_left, new_bg_left, bg_right, new_bg_right
        print ('[MiddleFrame.resizeCanvasImages] called...')
        cls.src_canvas_worker.drawImage()
        cls.out_canvas_worker.drawImage()

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
        out_file = DataManager.getOutputFile(work_file)

        cls.src_canvas_worker.changeImageFile(src_file)
        cls.out_canvas_worker.changeImageFile(out_file)

        cls.src_canvas_worker.drawImage()
        cls.out_canvas_worker.drawImage()

    @classmethod
    def removeSelectedTexts(cls):
        from ITM.Control.ControlManager import ControlManager
        print ('[MiddleFrame] removeSelectedTexts() called...')

        texts = DataManager.target_texts[DataManager.getImageIndex(ControlManager.work_file)]
        if texts == None:
            print ('[MiddleFrame] removeSelectedTexts() : no texts were selected!')
            return None
        
        # Reference : Image conversion from cv2 to PhotoImage (PIL)
        # - https://m.blog.naver.com/heennavi1004/222028305376
        import cv2
        out_file = DataManager.getOutputFile(ControlManager.work_file)
        img_cv2 = cls.__inpaintForSelectedTexts(out_file, texts)
        if img_cv2 is None:
            print ('[MiddleFrame] removeSelectedTexts() : no need to redraw image!')
            return
        
        img_conv = Image.fromarray(img_cv2)

        # reset (redraw) output canvas with image which selected texts were removed in
        cls.out_canvas_worker.setImage(img_conv)
        cls.redrawCanvasImages()

    @classmethod
    def __inpaintForSelectedTexts(cls, img_path, texts):
        import math
        import numpy as np
        import cv2
        import easyocr
        from ITM.Frame.LowFrame import LowFrame

        print ('[MiddleFrame] __inpaint_text() called...')
        
        # generate (word, box) tuples 
        img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
        mask = np.zeros(img.shape[:2], dtype="uint8")

        img_return = None
        idx = 0
        for t in texts:
            list_status = LowFrame.remove_tab_text_list.list_values
            if list_status[idx].get() == True:
                x0, y0 = t[0][0]
                x1, y1 = t[0][1] 
                x2, y2 = t[0][2]
                x3, y3 = t[0][3] 

                x_mid0, y_mid0 = cls.__midpoint(x1, y1, x2, y2)
                x_mid1, y_mi1 = cls.__midpoint(x0, y0, x3, y3)
                thickness = int(math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))
                
                cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255, thickness)
                img_return = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
            idx = idx+1
        return img_return

    @classmethod
    def __midpoint(cls, x1, y1, x2, y2):
        x_mid = int((x1 + x2)/2)
        y_mid = int((y1 + y2)/2)
        return (x_mid, y_mid)