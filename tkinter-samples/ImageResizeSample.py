#
# Reference :
# - https://www.codegrepper.com/code-examples/python/how+to+resize+image+in+python+tkinter
#

# How to resize an image in Tkinter to exactly half of the original size
from tkinter import *
from PIL import Image, ImageTk

# Function to resize an image
def resize_image():
    global img_info
    global img
    global c
    global new_width
    global new_height

    # They are int
    print("Width type: ", type(new_width), "Height type: ", type(new_height))

    # Divide the original width by 2
    resized_width = new_width / int(2)
    resized_height = new_height / int(2)

    # They are float
    print("Width type: ", type(resized_width), "Height type: ", type(resized_height))

    # Convert float to int
    resized_width = int(resized_width)
    resized_height = int(resized_height)

    # They are int
    print("Width type: ", type(resized_width), "Height type: ", type(resized_height))

    # Declare new size to the image
    img_info = img_info.resize((resized_width, resized_height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_info)
    c.create_image(0, 0, image=img, anchor=NW)

    # New size of image
    print("Size of image: " + str(resized_width) + "x" + str(resized_height))

# Setting up the window
root = Tk()

# Resize image button
Button(root, text='resize image', command=lambda:resize_image()).pack()

# Display image
img_info = Image.open("images/1.jpg")
new_width, new_height = img_info.size

# Size of image
print("Size of image: " + str(new_width) + "x" + str(new_height))

c = Canvas(root, width=new_width, height=new_height, bg="black")
c.pack()

img = ImageTk.PhotoImage(Image.open(r"images/1.jpg"))
c.create_image(2, 2, image=img, anchor=NW)

# Main loop
root.mainloop()