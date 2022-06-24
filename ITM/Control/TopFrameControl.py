import tkinter
from tkinter import filedialog
from ITM.Data.DataManager import DataManager

def clickedChangeFolder():
    print ('[TopFrameControl] clickedChangeFolder() called!!...')
    from ITM.Frame.TopFrame import TopFrame
    dir_path = filedialog.askdirectory(parent=TopFrame.root, title='Please select a directory', initialdir=DataManager.target_folder)
    print("##> dir_path : ", dir_path)
    print("##> TopFrame.root : ", TopFrame.root)
