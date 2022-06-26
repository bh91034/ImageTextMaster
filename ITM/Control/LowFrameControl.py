from ITM.Data.DataManager import DataManager
from tkinter import messagebox as mb

def selectedCheckListInRemoveTab(text):
    print ('[LowFrameControl] selectedCheckListInRemoveTab() called!!...')
    print ('[LowFrameControl] selectedCheckListInRemoveTab() : text=', text)


def clickedTextSearchInRemoveTab():
    print ('[LowFrameControl] clickedTextSearchInRemoveTab() called!!...')

    # check error case
    from ITM.Control.ControlManager import ControlManager
    if ControlManager.work_file == None:
        mb.showerror("에러", "아직 선택된 이미지가 없습니다")
        return
    
    # check if text search has been done already
    i = DataManager.getImageIndex(ControlManager.work_file)

    # read texts in image
    texts = DataManager.readTextsInImage(ControlManager.work_file)
    if texts == None:
        return

    # set texts in data area of LowFrame's remove tab
    from ITM.Frame.LowFrame import LowFrame
    LowFrame.resetRemoveTabData(texts)
