from ITM.Frame.FrameManager import FrameManager
from ITM.Data.DataManager import DataManager
from ITM.Control.ControlManager import ControlManager

data = DataManager('C:/Users/javaes/workspace/easy-ocr/ImageTextMagician/images/')
control = ControlManager(data)
root = FrameManager.init(control)
root.mainloop()