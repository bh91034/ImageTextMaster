import glob
import tkinter
from tkinter import messagebox as mb
from tkinter import filedialog
from ITM.Data.DataManager import DataManager

def __checkWorkFolder(work_dir):
    # check if image exists
    ext = ['png', 'jpg', 'gif']
    target_files = []
    [target_files.extend(glob.glob(work_dir + '/' + '*.' + e)) for e in ext]
    if len(target_files) == 0:
        mb.showerror("에러", "해당 폴더에는 이미지 파일이 없습니다")
        return False
    else:
        return True

def clickedChangeFolder():
    print ('[TopFrameControl] clickedChangeFolder() called!!...')
    from ITM.Frame.TopFrame import TopFrame
    dir_path = filedialog.askdirectory(parent=TopFrame.root, title='작업할 폴더를 선택하세요', initialdir=DataManager.target_folder)
    print("##> dir_path : ", dir_path)
    print("##> TopFrame.root : ", TopFrame.root)
    from ITM.Control.ControlManager import ControlManager
    if __checkWorkFolder(dir_path):\
            ControlManager.changedWorkFolder(dir_path)
    

