import tkinter as tk
from tkinter import ttk
from ITM.Control.TopFrameControl import clickedChangeFolder, clickedNextImage, clickedPrevImage, clickedSaveOutput
from ITM.Data.DataManager import DataManager

#------------------------------------------------------------------------------
# Top frame : top side buttons layout and command handlers
#------------------------------------------------------------------------------
class TopFrame:
    root = None
    label_curr_file_name = None
    def __init__(self, root):
        # top buttons frame
        top_frm = tk.Frame(root)
        top_frm.pack(padx=2, pady=2, fill='both', side='top')

        # top buttons : '이전 이미지', '다음 이미지', '폴더 변경'
        btn_prv_img = ttk.Button(top_frm, text='이전 이미지', command=clickedPrevImage)
        btn_nxt_img = ttk.Button(top_frm, text='다음 이미지', command=clickedNextImage)
        btn_change_folder = ttk.Button(top_frm, text='폴더 변경', command=clickedChangeFolder)

        # label : 현재 작업 파일
        from ITM.Control.ControlManager import ControlManager
        label_curr_file_title = ttk.Label(top_frm, text='작업 파일:')
        label_curr_file_name = ttk.Label(top_frm, text=ControlManager.work_file)

        TopFrame.label_curr_file_name = label_curr_file_name

        # top buttons : '결과 저장'
        btn_save_img = ttk.Button(top_frm, text='결과 저장', command=clickedSaveOutput)

        btn_prv_img.pack(side='left')
        btn_nxt_img.pack(side='left')
        btn_change_folder.pack(side='left')
        label_curr_file_title.pack(side='left')
        label_curr_file_name.pack(side='left')
        btn_save_img.pack(side='right')

        TopFrame.root = top_frm
    
    @classmethod
    def changeWorkFile(cls, work_file):
        cls.label_curr_file_name.config(text=work_file)