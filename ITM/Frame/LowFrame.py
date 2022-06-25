import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import END, scrolledtext
from ITM.Control.LowFrameControl import clickedTextSearchInRemoveTab

#------------------------------------------------------------------------------
# Low frame : low side tabbed pane (tools)
#------------------------------------------------------------------------------
class ScrollableChecklist(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root

        self.vsb = ttk.Scrollbar(self, orient="vertical")
        self.text = tk.Text(self, width=40, height=20, 
                            yscrollcommand=self.vsb.set)
        self.vsb.config(command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

    def reset(self, text_list=None):
        self.text.delete('1.0', END)
        print ('[LowFrame.ScrollableChecklist] reset() called!!...')
        print ('[LowFrame.ScrollableChecklist] reset() : text_list=', text_list)
        if text_list is not None:
            for t in text_list:
                cb = tk.Checkbutton(self, text=t)
                self.text.window_create("end", window=cb)
                self.text.insert("end", "\n") # to force one checkbox per line

class ScrollableCombobox(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root

        self.vsb = ttk.Scrollbar(self, orient="vertical")
        self.text = tk.Text(self, width=40, height=20, 
                            yscrollcommand=self.vsb.set)
        self.vsb.config(command=self.text.yview)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

    def reset(self, text_list=None):
        self.text.delete('1.0', END)

        if text_list is not None:
            for i in range(20):
                #cb = ttk.Combobox(self, text="checkbutton #%s" % i)
                cb = ttk.Radiobutton(self, text="checkbutton #%s" % i)
                self.text.window_create("end", window=cb)
                self.text.insert("end", "\n") # to force one checkbox per line

class LowFrame:
    remove_tab_text_list = None
    write_tab_text_list = None
    write_tab_text_org = None
    write_tab_text_google = None
    write_tab_text_final = None
    global low_frm
    def __init__(self, root):
        # create a notebook
        low_frm = ttk.Notebook(root)
        low_frm.pack(pady=10, fill='both')
        low_frm.config(height=220)

        # create frames
        low_frm_remove_tab = ttk.Frame(low_frm, height=50)
        low_frm_write_tab = ttk.Frame(low_frm, height=50)

        low_frm_remove_tab.pack(fill='both', expand=True)
        low_frm_write_tab.pack(fill='both', expand=True)

        # add frames to notebook
        low_frm.add(low_frm_remove_tab, text='지우기 도구')
        low_frm.add(low_frm_write_tab, text='쓰기 도구')

        #------------------------------------------------------------------------------
        # Low frame - remove tab : low frame remove tab controls
        #------------------------------------------------------------------------------
        remove_tab_up_frm = ttk.Frame(low_frm_remove_tab)
        remove_tab_up_frm.pack(padx=2, pady=2, fill='both', side='top')
        
        #from ITM.Control.LowFrameControl import clickedTextSearchInRemoveTab
        remove_tab_btn_search_img = ttk.Button(remove_tab_up_frm, text='텍스트 찾기', command=clickedTextSearchInRemoveTab)
        remove_tab_btn_remove_img = ttk.Button(remove_tab_up_frm, text='선택 지우기')
        remove_tab_btn_revoke_img = ttk.Button(remove_tab_up_frm, text='원상태 복원')

        remove_tab_btn_search_img.pack(side='left')
        remove_tab_btn_remove_img.pack(side='left')
        remove_tab_btn_revoke_img.pack(side='left')

        remove_tab_down_frm = ttk.Frame(low_frm_remove_tab)
        remove_tab_down_frm.pack(padx=2, pady=2, fill='both', expand=True)

        remove_tab_text_list = ScrollableChecklist(remove_tab_down_frm)

        remove_tab_text_list.pack(side="top", fill="both", expand=True)
        remove_tab_text_list.reset()
        LowFrame.remove_tab_text_list = remove_tab_text_list

        #------------------------------------------------------------------------------
        # Low frame - write tab : low frame write tab controls
        #------------------------------------------------------------------------------
        # low frame write tab - [LEFT] text list
        write_tab_text_list = ScrollableCombobox(low_frm_write_tab)
        write_tab_text_list.pack(padx=2, pady=2, side="left", fill="y")
        write_tab_text_list.reset(1)

        LowFrame.write_tab_text_list = write_tab_text_list

        # low frame write tab - [RIGHT] style tool and buttons
        a = ttk.Frame(low_frm_write_tab)
        a.pack(side='right', fill='both')

        b = ttk.LabelFrame(a, text='스타일 도구')
        b.pack(fill='both', side='top')
        b.columnconfigure(0, weight=1)
        b.rowconfigure(0, weight=1)
        c = ttk.Frame(a)
        c.pack(side='bottom')

        write_tab_right_label_font_style = ttk.Label(b, text='폰트 스타일 :')
        write_tab_right_label_font_style.grid(column=0, row=0, columnspan=2, sticky=tk.W)

        combo_box = ttk.Combobox(b)
        combo_box.grid(column=0, row=1, columnspan=4, sticky=tk.W+tk.E)

        write_tab_right_label_font_size = ttk.Label(b, text='폰트 사이즈 :')
        write_tab_right_label_font_size.grid(column=0, row=2, columnspan=2, sticky=tk.W)

        combo_box2 = ttk.Combobox(b)
        combo_box2.grid(column=0, row=3, columnspan=2, sticky=tk.W+tk.E)

        write_tab_right_label_font_color = ttk.Label(b, text='폰트 색상 :')
        write_tab_right_label_font_color.grid(column=0, row=4, columnspan=2, sticky=tk.W)

        button_color = tk.Button(b, text='...', bg='yellow')
        button_color.grid(column=0, row=5, columnspan=1, sticky=tk.W+tk.E)

        write_tab_right_btn_apply = ttk.Button(c, text='적용')
        write_tab_right_btn_apply.pack(side='left')
        write_tab_right_btn_cancel = ttk.Button(c, text='취소')
        write_tab_right_btn_cancel.pack(side='left')

        # low frame write tab - [CENTER] translation tool
        write_tab_trans_frm = ttk.LabelFrame(low_frm_write_tab, text="번역 도구")
        write_tab_trans_frm.pack(padx=2, pady=2, fill='both', side='top', expand=True)
        write_tab_trans_frm.columnconfigure(0, weight=1)

        write_tab_label_org = ttk.Label(write_tab_trans_frm, text='원본 텍스트 :')
        write_tab_label_org.grid(column=0, row=0, sticky=tk.W)
        write_tab_text_org = tk.Text(write_tab_trans_frm, height=3)
        write_tab_text_org.grid(column=0, row=1, sticky=tk.W+tk.E+tk.N+tk.S)

        write_tab_label_google = ttk.Label(write_tab_trans_frm, text='구글 번역 결과 :')
        write_tab_label_google.grid(column=0, row=2, sticky=tk.W)
        write_tab_text_google = tk.Text(write_tab_trans_frm, height=3)
        write_tab_text_google.grid(column=0, row=3, sticky=tk.W+tk.E+tk.N+tk.S)

        write_tab_label_final = ttk.Label(write_tab_trans_frm, text='적용할 텍스트 :')
        write_tab_label_final.grid(column=0, row=4, sticky=tk.W)
        write_tab_text_final = tk.Text(write_tab_trans_frm, height=3)
        write_tab_text_final.grid(column=0, row=5, sticky=tk.W+tk.E+tk.N+tk.S)

        LowFrame.write_tab_text_org = write_tab_text_org
        LowFrame.write_tab_text_google = write_tab_text_google
        LowFrame.write_tab_text_final = write_tab_text_final

    @classmethod
    def resetRemoveTabData(cls, texts=None):
        print ('[LowFrame] resetRemoveTabData() called...')
        print ('[LowFrame] resetRemoveTabData() : texts=', texts)
        cls.remove_tab_text_list.reset(texts)

    @classmethod
    def resetWriteTabData(cls):
        print ('[LowFrame.resetWriteTabData] called...')

        # clear test list found in the image
        cls.write_tab_text_list.reset(None)

        # clear 'translation tool' area
        cls.write_tab_text_org.delete('1.0', END)
        cls.write_tab_text_google.delete('1.0', END)
        cls.write_tab_text_final.delete('1.0', END)

        # TODO: clear 'style tool' area
