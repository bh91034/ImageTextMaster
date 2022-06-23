import tkinter as tk
from tkinter import END, scrolledtext
from tkinter import ttk
from turtle import bgcolor

# root window
root = tk.Tk()
root.geometry('1200x600+20+20')
#root.resizable(False, False)
root.title('Button Demo')

#------------------------------------------------------------------------------
# Top frame : top side buttons layout and command handlers
#------------------------------------------------------------------------------
# command hander : 'top_frm_btn_prv_img'
def cb_top_frm_btn_prv_img():
    print ('top_frm_btn_prv_img pressed...')

# command hander : 'top_frm_btn_nxt_img'
def cb_top_frm_btn_nxt_img():
    print ('top_frm_btn_nxt_img pressed...')

# command hander : 'top_frm_btn_search_img'
def cb_top_frm_btn_search_img():
    print ('top_frm_btn_search_img pressed...')

# command hander : 'top_frm_btn_save_img'
def cb_top_frm_btn_save_img():
    print ('top_frm_btn_save_img pressed...')

# top buttons frame
top_frm = tk.Frame(root)
top_frm.pack(padx=2, pady=2, fill='both', side='top')

# top buttons : '이전 이미지'
top_frm_btn_prv_img = ttk.Button(
    top_frm,
    text='이전 이미지',
    command=cb_top_frm_btn_prv_img
)

# top buttons : '다음 이미지'
top_frm_btn_nxt_img = ttk.Button(
    top_frm,
    text='다음 이미지',
    command=cb_top_frm_btn_nxt_img
)

# top buttons : '목록에서 선택'
top_frm_btn_search_img = ttk.Button(
    top_frm,
    text='목록에서 선택',
    command=cb_top_frm_btn_search_img
)

# top buttons : '결과 저장'
top_frm_btn_save_img = ttk.Button(
    top_frm,
    text='결과 저장',
    command=cb_top_frm_btn_save_img
)

top_frm_btn_prv_img.pack(side='left')
top_frm_btn_nxt_img.pack(side='left')
top_frm_btn_search_img.pack(side='left')
top_frm_btn_save_img.pack(side='right')

#------------------------------------------------------------------------------
# Middle frame : middle side canvases
#------------------------------------------------------------------------------
# middle canvases frame
mid_frm = tk.Frame(root)
mid_frm.pack(padx=2, pady=2, fill='both', expand=True)

txtbox = scrolledtext.ScrolledText(mid_frm, width=40, height=10)
txtbox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
txtbox2 = scrolledtext.ScrolledText(mid_frm, width=40, height=10)
txtbox2.grid(row=0, column=1, sticky=tk.E+tk.W+tk.N+tk.S)

# Added by Q&A from stackoverflow
# https://stackoverflow.com/questions/72713209/how-to-keep-two-textboxes-the-same-size-when-resizing-window-with-python-tkinter
mid_frm.columnconfigure((0,1), weight=1)
mid_frm.rowconfigure(0, weight=1)

#------------------------------------------------------------------------------
# Low frame : low side tabbed pane (tools)
#------------------------------------------------------------------------------
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

remove_tab_btn_search_img = ttk.Button(remove_tab_up_frm, text='텍스트 찾기')
remove_tab_btn_remove_img = ttk.Button(remove_tab_up_frm, text='선택 지우기')
remove_tab_btn_revoke_img = ttk.Button(remove_tab_up_frm, text='원상태 복원')

remove_tab_btn_search_img.pack(side='left')
remove_tab_btn_remove_img.pack(side='left')
remove_tab_btn_revoke_img.pack(side='left')

remove_tab_down_frm = ttk.Frame(low_frm_remove_tab)
remove_tab_down_frm.pack(padx=2, pady=2, fill='both', expand=True)

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

        # for i in range(4):
        #     cb = tk.Checkbutton(self, text="checkbutton #%s" % i)
        #     self.text.window_create("end", window=cb)
        #     self.text.insert("end", "\n") # to force one checkbox per line

    def reset(self, text_list=None):
        self.text.delete('1.0', END)

        if text_list is not None:
            for i in range(20):
                cb = tk.Checkbutton(self, text="checkbutton #%s" % i)
                
                self.text.window_create("end", window=cb)
                self.text.insert("end", "\n") # to force one checkbox per line

remove_tab_text_list = ScrollableChecklist(remove_tab_down_frm)
remove_tab_text_list.pack(side="top", fill="both", expand=True)
remove_tab_text_list.reset(1)

#------------------------------------------------------------------------------
# Low frame - write tab : low frame write tab controls
#------------------------------------------------------------------------------
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

        # for i in range(4):
        #     cb = tk.Checkbutton(self, text="checkbutton #%s" % i)
        #     self.text.window_create("end", window=cb)
        #     self.text.insert("end", "\n") # to force one checkbox per line

    def reset(self, text_list=None):
        self.text.delete('1.0', END)

        if text_list is not None:
            for i in range(20):
                #cb = ttk.Combobox(self, text="checkbutton #%s" % i)
                cb = ttk.Radiobutton(self, text="checkbutton #%s" % i)
                self.text.window_create("end", window=cb)
                self.text.insert("end", "\n") # to force one checkbox per line

# low frame write tab - [LEFT] text list
write_tab_text_list = ScrollableCombobox(low_frm_write_tab)
write_tab_text_list.pack(padx=2, pady=2, side="left", fill="y")
write_tab_text_list.reset(1)

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

# low frame write tab - translation tool
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

root.mainloop()