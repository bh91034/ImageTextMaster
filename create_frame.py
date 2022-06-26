from ITM.Frame.FrameManager import FrameManager
from ITM.Data.DataManager import DataManager
from ITM.Control.ControlManager import ControlManager

data = DataManager()
control = ControlManager()
root = FrameManager.init()
root.mainloop()
