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
        g_result_text = translator.translate(text, dest='ko')
        p_result_text = __translate_by_papago(text)
        if p_result_text is not None:
            result_text = "===> 구글 번역 결과 <===\n" + g_result_text.text + "\n\n===> 파파고 번역 결과 <===\n" + p_result_text
            LowFrame.low_frm_text_right.reset([result_text])
        else:
            LowFrame.low_frm_text_right.reset([g_result_text.text])
    return

# Reference : Papago API (pypapago API)
# - https://wikidocs.net/35983
# - https://www.dbility.com/560
# - https://ansan-survivor.tistory.com/75
# - https://developers.naver.com/apps/#/myapps/fV9b7SkB6EST_pBANjIB/overview
# - https://developers.naver.com/docs/papago/papago-detectlangs-overview.md#%EC%96%B8%EC%96%B4-%EA%B0%90%EC%A7%80-%EA%B0%9C%EC%9A%94
def __translate_by_papago(text):
    import os
    import sys
    import urllib.request
    import json
    client_id = "fV9b7SkB6EST_pBANjIB" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "gUlhZt5TWd" # 개발자센터에서 발급받은 Client Secret 값
    #encText = urllib.parse.quote("번역할내용")
    encText = urllib.parse.quote(text)
    data = "source=zh-CN&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        res = json.loads(response_body.decode('utf-8'))
        #from pprint import pprint
        #pprint(res)
        result = res['message']['result']['translatedText']
        return result
    else:
        print("Error Code:" + rescode)
        return None

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
