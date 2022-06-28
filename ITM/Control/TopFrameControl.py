import glob
import tkinter
from tkinter import messagebox as mb
from tkinter import filedialog
from ITM.Data.DataManager import DataManager
from ITM.Frame.MiddleFrame import MiddleFrame

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

def clickedSaveOutput():
    print ('[TopFrameControl] clickedSaveOutput() called!!...')
    from ITM.Control.ControlManager import ControlManager
    result = DataManager.saveOutputFile(ControlManager.work_file, MiddleFrame.out_image)
    if result == True:
        mb.showinfo("성공", "저장되었습니다")
    else:
        mb.showerror("에러", "저장에 실패했습니다")

def clickedPrevImage():
    print ('[TopFrameControl] clickedPrevImage() called!!...')
    from ITM.Control.ControlManager import ControlManager
    work_file = ControlManager.work_file
    if work_file == None:
        mb.showerror("에러", "현재 작업중인 이미지 파일이 없습니다")
        return
    prev_img = DataManager.getPrevImageFile(work_file)
    print ('[TopFrameControl] clickedPrevImage() : prev image = ', prev_img)
    if prev_img == None:
        mb.showerror("에러", "현재 이미지 파일이 첫번째 이미지 파일입니다")
        return
    ControlManager.changedWorkImage(prev_img)
    

def clickedNextImage():
    print ('[TopFrameControl] clickedNextImage() called!!...')
    from ITM.Control.ControlManager import ControlManager
    work_file = ControlManager.work_file
    if work_file == None:
        mb.showerror("에러", "현재 작업중인 이미지 파일이 없습니다")
        return
    next_img = DataManager.getNextImageFile(work_file)
    print ('[TopFrameControl] clickedNextImage() : next image = ', next_img)
    if next_img == None:
        mb.showerror("에러", "더이상 이미지 파일이 없습니다")
        return
    ControlManager.changedWorkImage(next_img)


def clickedChangeFolder():
    print ('[TopFrameControl] clickedChangeFolder() called!!...')
    from ITM.Frame.TopFrame import TopFrame
    dir_path = filedialog.askdirectory(parent=TopFrame.root, title='작업할 폴더를 선택하세요', initialdir=DataManager.target_folder)
    print("##> dir_path : ", dir_path)
    from ITM.Control.ControlManager import ControlManager
    if __checkWorkFolder(dir_path):
            ControlManager.changedWorkFolder(dir_path)
    

