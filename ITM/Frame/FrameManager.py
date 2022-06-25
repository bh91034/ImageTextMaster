import tkinter as tk

class FrameManager:
    global control_manager
    @staticmethod
    def init(control_manager):
        control_manager = control_manager
        # root window
        root = tk.Tk()
        root.geometry('1200x600+20+20')
        root.title('Image Text Master')

        # Top frame : top side buttons layout and command handlers
        from ITM.Frame.TopFrame import TopFrame
        top_frm = TopFrame(root)

        # Middle frame : middle side canvases
        from ITM.Frame.MiddleFrame import MiddleFrame
        mid_frm = MiddleFrame(root)

        # Low frame : low side tabbed pane (tools)
        from ITM.Frame.LowFrame import LowFrame
        low_frm = LowFrame(root)
        return root
