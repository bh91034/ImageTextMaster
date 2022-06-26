from ITM.Frame.FrameManager import FrameManager
from ITM.Data.DataManager import DataManager
from ITM.Control.ControlManager import ControlManager

#
data = DataManager()
control = ControlManager(data)
root = FrameManager.init(control)
root.mainloop()
