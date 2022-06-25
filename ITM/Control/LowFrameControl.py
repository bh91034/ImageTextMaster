

from ITM.Data.DataManager import DataManager

def clickedTextSearchInRemoveTab():
    from ITM.Control.ControlManager import ControlManager
    print ('[LowFrameControl] clickedTextSearchInRemoveTab() called!!...')
    easyocr_reader = ControlManager.easyocr_reader
    work_img = ControlManager.work_file
    result = easyocr_reader.readtext(work_img)
    texts = [t[1] for t in result]
    print (texts)
    DataManager.setTargetTexts(work_img, result)
    from ITM.Frame.LowFrame import LowFrame
    print ('[LowFrameControl] clickedTextSearchInRemoveTab() texts=', texts)
    LowFrame.resetRemoveTabData(texts)
