import glob

from ITM.Data.DataManager import DataManager
from ITM.Frame.LowFrame import LowFrame
from ITM.Frame.MiddleFrame import MiddleFrame
from ITM.Frame.TopFrame import TopFrame

class ControlManager:
    def __init__(self, data_manager):
        pass

    @classmethod
    def changedWorkFolder(cls, work_dir):
        print ('[ControlManager.changedWorkFolder] work_dir=', work_dir)

        # set new dir to 'DataManager' and make DataManager to reload image list
        DataManager.reset(work_dir)

        # set new dir to 'TopFrame' at the label displaying work dir
        TopFrame.changeWorkFolder(work_dir)
        
        # clear all data in 'remove tab' of 'LowFrame'
        LowFrame.resetRemoveTabData()

        # clear all data in 'write tab' of 'LowFrame'
        LowFrame.resetWriteTabData()

        # TODO: change images in cavases of 'MiddleFrame' with the 1st image of new dir
        work_file = DataManager.target_files[0]
        MiddleFrame.resetCanvasImages(work_file)
            