from tkinter import messagebox as mb

from ITM.Frame.MiddleFrame import MiddleFrame

def selectedCheckList(text):
    from ITM.Frame.LowFrame import LowFrame
    print ('[LowFrameControl] selectedCheckListInRemoveTab() called!!...')
    text_info = text.split('|', 1)

    # get selected item's info (id, text, status)
    selected_item_id = int(text_info[0])
    selected_item_text = text_info[1]
    selected_item_status = LowFrame.getStatusOfCheckListInRemoveTab(selected_item_id)
    print ('[LowFrameControl] selectedCheckListInRemoveTab() : id = ', selected_item_id)
    print ('[LowFrameControl] selectedCheckListInRemoveTab() : text = ', selected_item_text)
    print ('[LowFrameControl] selectedCheckListInRemoveTab() : status = ', selected_item_status.get())
    from ITM.Control.ControlManager import ControlManager
    MiddleFrame.resetCanvasImages(ControlManager.work_file)

    text_list = LowFrame.low_frm_text_left.getCheckedTexts()
    LowFrame.low_frm_text_center.reset(text_list)
    LowFrame.low_frm_text_right.reset()

def clickedTranslate():
    from ITM.Frame.LowFrame import LowFrame
    import googletrans
    from googletrans import Translator

    # get text
    text = LowFrame.low_frm_text_center.text.get('1.0', 'end')

    # check availability
    if text is not None and len(text) > 0:
        translator = Translator()
        result_text = translator.translate(text, dest='ko')
        LowFrame.low_frm_text_right.reset([result_text.text])
    return

def clickedCheckAll():
    from ITM.Frame.LowFrame import LowFrame
    LowFrame.low_frm_text_left.checkAll()
    LowFrame.low_frm_text_center.reset(LowFrame.low_frm_text_left.text_list)
    LowFrame.low_frm_text_right.reset()
    MiddleFrame.redrawCanvasImages()

def clickedUncheckAll():
    from ITM.Frame.LowFrame import LowFrame
    LowFrame.low_frm_text_left.uncheckAll()
    LowFrame.low_frm_text_center.reset()
    LowFrame.low_frm_text_right.reset()
    MiddleFrame.redrawCanvasImages()

def clickedTextSearch():
    print ('[LowFrameControl] clickedTextSearch() called!!...')

    # check error case
    from ITM.Control.ControlManager import ControlManager
    if ControlManager.work_file == None:
        mb.showerror("에러", "아직 선택된 이미지가 없습니다")
        return
    
    # check if text search has been done already
    from ITM.Data.DataManager import DataManager
    i = DataManager.getImageIndex(ControlManager.work_file)
    if DataManager.target_texts[i] != None:
        mb.showwarning("Warning", "이미 text를 읽었습니다")
        return

    # read texts in image
    texts = DataManager.readTextsInImageAgain(ControlManager.work_file)
    if texts == None:
        return

    # set texts in data area of LowFrame's remove tab
    from ITM.Frame.LowFrame import LowFrame
    LowFrame.resetRemoveTabData(texts)
