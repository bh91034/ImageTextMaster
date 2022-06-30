import tkinter as tk
from tkinter import ttk

from ITM.Frame.LowFrame import ScrollableList, ScrollableListType, ScrollableText

class LowFrameTransTab:
    @classmethod
    def init(cls, frm_trtab):
        # low frame trans tab : [UP] buttons
        cls.__initTransTabUpFrame(frm_trtab)

        # low frame trans tab : [DOWN] texts areas
        cls.__initTransTabDownFrame(frm_trtab)
        return
    
    # low frame -> trans tab -> up -> buttons
    @classmethod
    def __initTransTabUpFrame(cls, frm_trtab):
        frm_trtab_up = ttk.Frame(frm_trtab)
        frm_trtab_up.pack(padx=2, pady=2, fill='both', side='top')
        
        btn_trtab_text_search = ttk.Button(frm_trtab_up, text='텍스트 찾기')
        btn_trtab_check_all = ttk.Button(frm_trtab_up, text='전체 선택')
        btn_trtab_uncheck_all = ttk.Button(frm_trtab_up, text='전체 해제')
        btn_trtab_translate = ttk.Button(frm_trtab_up, text='번역 실행')
        btn_trtab_text_search.pack(side='left')
        btn_trtab_check_all.pack(side='left')
        btn_trtab_uncheck_all.pack(side='left')
        btn_trtab_translate.pack(side='left')
    
    # low frame -> trans tab -> down -> text areas
    @classmethod
    def __initTransTabDownFrame(cls, frm_trtab):
        frm_trtab_down = ttk.Frame(frm_trtab)
        frm_trtab_down.pack(padx=2, pady=2, fill='both', side='top')
        
        txt_trtab_translate = ScrollableList(frm_trtab_down, ScrollableListType.CHECK_BUTTON, width=20)
        txt_trtab_translate.pack(padx=2, pady=2, side="left", fill="y")

        txt_trtab_edit = ScrollableText(frm_trtab_down)
        txt_trtab_edit.pack(padx=2, pady=2, side="left", fill="both", expand=True)

        txt_trtab_result = ScrollableText(frm_trtab_down)
        txt_trtab_result.pack(padx=2, pady=2, side="left", fill="both", expand=True)