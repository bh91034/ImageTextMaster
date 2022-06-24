import tkinter as tk
from tkinter import ttk

#------------------------------------------------------------------------------
# Top frame : top side buttons layout and command handlers
#------------------------------------------------------------------------------
class TopFrame:
    global top_frm
    def __init__(self, root):
        # top buttons frame
        top_frm = tk.Frame(root)
        top_frm.pack(padx=2, pady=2, fill='both', side='top')

        # top buttons : '이전 이미지'
        top_frm_btn_prv_img = ttk.Button(
            top_frm,
            text='이전 이미지'
        )

        # top buttons : '다음 이미지'
        top_frm_btn_nxt_img = ttk.Button(
            top_frm,
            text='다음 이미지'
        )

        # top buttons : '목록에서 선택'
        top_frm_btn_search_img = ttk.Button(
            top_frm,
            text='목록에서 선택'
        )

        # top buttons : '결과 저장'
        top_frm_btn_save_img = ttk.Button(
            top_frm,
            text='결과 저장'
        )

        top_frm_btn_prv_img.pack(side='left')
        top_frm_btn_nxt_img.pack(side='left')
        top_frm_btn_search_img.pack(side='left')
        top_frm_btn_save_img.pack(side='right')