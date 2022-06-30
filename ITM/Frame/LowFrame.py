from msilib.schema import Control
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import END, scrolledtext
from ITM.Control.LowFrameControl import clickedTextSearch, selectedCheckList
from ITM.Data.DataManager import DataManager
from ITM.Frame.MiddleFrame import MiddleFrame

#------------------------------------------------------------------------------
# Low frame : low side tabbed pane (tools)
#------------------------------------------------------------------------------
class LowFrame:
    low_frm_text_list = None

    def __init__(self, root):
        from ITM.Frame.MiddleFrame import MiddleFrame

        # create frames
        low_frm = ttk.Frame(root, height=50)
        low_frm.pack(fill='both')

        low_frm_up = ttk.Frame(low_frm, height=50)
        low_frm_up.pack(padx=2, pady=2, fill='both', side='top')
        
        btn_low_frm_search = ttk.Button(low_frm_up, text='텍스트 찾기', command=clickedTextSearch)
        btn_low_frm_check_all = ttk.Button(low_frm_up, text='전체 선택')
        btn_low_frm_uncheck_all = ttk.Button(low_frm_up, text='전체 해제')
        #remove_tab_btn_revoke_img = ttk.Button(low_frm_up, text='선택 번역')

        btn_low_frm_search.pack(side='left')
        btn_low_frm_check_all.pack(side='left')
        btn_low_frm_uncheck_all.pack(side='left')

        low_frm_down = ttk.Frame(low_frm)
        low_frm_down.pack(padx=2, pady=2, fill='both', expand=True)

        txt_low_frm_left = ScrollableList(low_frm_down, ScrollableListType.CHECK_BUTTON)

        txt_low_frm_left.pack(side="top", fill="both", expand=True)
        txt_low_frm_left.reset()
        LowFrame.low_frm_text_list = txt_low_frm_left

    @classmethod
    def getStatusOfCheckListInRemoveTab(cls, idx):
        print ('[LowFrame] getStatusOfCheckListInRemoveTab() called...')
        return cls.low_frm_text_list.list_values[idx]
    
    @classmethod
    def resetRemoveTabData(cls, texts=None):
        print ('[LowFrame] resetRemoveTabData() called...')
        print ('[LowFrame] resetRemoveTabData() : texts=', texts)
        cls.low_frm_text_list.reset(texts)

from enum import Enum, auto
class ScrollableListType(Enum):
    CHECK_BUTTON = auto()
    RADIO_BUTTON = auto()

class ScrollableList(tk.Frame):
    # note : the following 2 variables should be reset when image changes
    #        - list_values
    #        - text
    def __init__(self, root, list_type, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.list_type = list_type
        self.vsb = ttk.Scrollbar(self, orient="vertical")
        self.text = tk.Text(self, width=40, height=20, 
                            yscrollcommand=self.vsb.set)
        self.vsb.config(command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        self.list_values = []

    def __getIndexedText(self, idx, text):
        return str(idx) + '|' + text
    
    def reset(self, text_list=None):
        self.text.delete('1.0', END)
        self.list_values = []
        print ('[LowFrame.ScrollableList] reset() called!!...')
        print ('[LowFrame.ScrollableList] reset() : text_list=', text_list)
        
        if text_list is not None:
            idx = 0
            self.list_values = [None] * len(text_list)
            for i in range(len(text_list)):
                self.list_values[i] = tk.BooleanVar()
            
            for t in text_list:
                if self.list_type == ScrollableListType.CHECK_BUTTON:
                    # Reference : checkbutton example getting value in callback
                    # - https://arstechnica.com/civis/viewtopic.php?t=69728
                    cb = tk.Checkbutton(self, text=t, command=lambda i=self.__getIndexedText(idx,t): selectedCheckList(i), var=self.list_values[idx])
                elif self.list_type == ScrollableListType.RADIO_BUTTON:
                    cb = tk.Radiobutton(self, text=t)
                else:
                    cb = tk.Checkbutton(self, text=t)
                self.text.window_create("end", window=cb)
                self.text.insert("end", "\n") # to force one checkbox per line
                idx = idx + 1