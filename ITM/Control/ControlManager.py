import glob
import os

from ITM.Data.DataManager import DataManager
from ITM.Frame.LowFrame import LowFrame
from ITM.Frame.MiddleFrame import MiddleFrame
from ITM.Frame.TopFrame import TopFrame

class ControlManager:
    work_file = None
    def __init__(self, data_manager):
        ControlManager.work_file = DataManager.target_files[0]

    @classmethod
    def changedWorkImage(cls, work_file):
        print ('[ControlManager.changedWorkImage] work_img=', work_file)
        # clear all data in 'remove tab' of 'LowFrame'
        LowFrame.resetRemoveTabData()

        # clear all data in 'write tab' of 'LowFrame'
        LowFrame.resetWriteTabData()

        # change images in cavases of 'MiddleFrame' with the 1st image of new dir
        MiddleFrame.resetCanvasImages(work_file)
        cls.work_file = work_file

        # set new dir to 'TopFrame' at the label displaying work dir
        TopFrame.changeWorkFile(work_file)

        # set texts to remove tab in 'LowFrame'
        texts = DataManager.getExistingTextsInImage(work_file)
        LowFrame.resetRemoveTabData(texts)

    @classmethod
    def changedWorkFolder(cls, work_dir):
        print ('[ControlManager.changedWorkFolder] work_dir=', work_dir)

        # set new dir to 'DataManager' and make DataManager to reload image list
        DataManager.reset(work_dir)

        # set current work file
        work_file = DataManager.target_files[0]
        
        # change image in frames
        cls.changedWorkImage(work_file)
