#
# Reference :
# - https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window
#

# coding: utf-8

try:
    import tkinter as tk
    from tkinter import scrolledtext
except: # Python2 compatible
    import Tkinter as tk
    from Tkinter import scrolledtext

def main():
    master_window = tk.Tk()

    # Parent widget for the buttons
    buttons_frame = tk.Frame(master_window)
    buttons_frame.grid(row=0, column=0, sticky=tk.W+tk.E)    

    btn_Image = tk.Button(buttons_frame, text='Image')
    btn_Image.grid(row=0, column=0, padx=(10), pady=10)

    btn_File = tk.Button(buttons_frame, text='File')
    btn_File.grid(row=0, column=1, padx=(10), pady=10)

    btn_Folder = tk.Button(buttons_frame, text='Folder')
    btn_Folder.grid(row=0, column=2, padx=(10), pady=10)

    # Group1 Frame ----------------------------------------------------
    group1 = tk.LabelFrame(master_window, text="Text Box", padx=5, pady=5)
    group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.E+tk.W+tk.N+tk.S)

    master_window.columnconfigure(0, weight=2)
    master_window.rowconfigure(1, weight=2)

    group1.rowconfigure(0, weight=1)
    group1.columnconfigure(0, weight=1)

    # Create the textbox
    txtbox = scrolledtext.ScrolledText(group1, width=40, height=10)
    txtbox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
    txtbox2 = scrolledtext.ScrolledText(group1, width=40, height=10)
    txtbox2.grid(row=0, column=1, sticky=tk.E+tk.W+tk.N+tk.S)

    # Added by Q&A from stackoverflow
    # https://stackoverflow.com/questions/72713209/how-to-keep-two-textboxes-the-same-size-when-resizing-window-with-python-tkinter
    group1.columnconfigure((0,1), weight=1)

    master_window.mainloop()

if __name__ == '__main__':
    main()