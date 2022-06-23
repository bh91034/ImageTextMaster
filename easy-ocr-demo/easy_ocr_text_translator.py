#!/usr/bin/env python
# coding: utf-8

# In[2]:


import easyocr
import os
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
#result = reader.readtext('a.png')
target_file = 'a.png'
source_folder = 'images'
output_interim_folder = 'output-interim'
output_final_folder = 'output-final'


# In[4]:


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def getSourceFilePath(file_name):
    return './' + source_folder + '/' + file_name

def getOutputInterimPath(file_name):
    return './' + source_folder + '/' + output_interim_folder + '/' + file_name

def getOutputFinalPath(file_name):
    return './' + source_folder + '/' + output_final_folder + '/' + file_name

createFolder('./' + source_folder + '/' + output_interim_folder)
createFolder('./' + source_folder + '/' + output_final_folder)

source_file = getSourceFilePath(target_file)
interim_output_file = getOutputInterimPath(target_file)
final_output_file = getOutputFinalPath(target_file)
print (source_file)
print (interim_output_file)
print (final_output_file)


# In[5]:


result = reader.readtext(source_file)
print (result)
from IPython.display import Image
Image(filename=source_file) 


# In[6]:


texts = [t[1] for t in result]
print (texts)


# In[7]:


import googletrans
from googletrans import Translator


# In[8]:


translator = Translator()
for t in texts:
    r = translator.translate(t,dest='ko')
    print (r)


# In[9]:


import math
import numpy as np
import cv2


# In[10]:


def midpoint(x1, y1, x2, y2):
    x_mid = int((x1 + x2)/2)
    y_mid = int((y1 + y2)/2)
    return (x_mid, y_mid)


# In[11]:


#example of a line mask for the word "Tuesday"
box = result[0]

x0, y0 = box[0][0]
x1, y1 = box[0][1] 
x2, y2 = box[0][2]
x3, y3 = box[0][3] 
x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
thickness = int(math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))


# In[13]:


#img = Image('a.png')
i = cv2.imread(source_file)
img = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255, thickness)


# In[14]:


import matplotlib.pyplot as plt
masked = cv2.bitwise_and(img, img, mask=mask)
plt.imshow(masked)


# In[15]:


img_inpainted = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
plt.imshow(img_inpainted)


# In[16]:


def inpaint_text(img_path):
    # read image
    reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    texts = reader.readtext(img_path)
    # generate (word, box) tuples 
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
    #img = cv2.cvtColor(cv2.imread(img_path))
    mask = np.zeros(img.shape[:2], dtype="uint8")
    for t in texts:
        #if (len(box[0]) <= 1):
        #    continue
        x0, y0 = t[0][0]
        x1, y1 = t[0][1] 
        x2, y2 = t[0][2]
        x3, y3 = t[0][3] 
        
        x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
        x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
        
        thickness = int(math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 ))
        
        cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255, thickness)
        img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
        
        print (t[0])
    return(img)


# In[17]:


img_inpainted = inpaint_text(source_file)
plt.imshow(img_inpainted)


# In[18]:


print (type(img_inpainted))


# In[19]:


img_inpainted_converted = cv2.cvtColor(img_inpainted, cv2.COLOR_RGB2BGR)
cv2.imwrite(interim_output_file, img_inpainted_converted)


# In[20]:


print (result)
print (texts)


# In[21]:


from PIL import Image, ImageFont, ImageDraw 
my_image = Image.open(interim_output_file)
draw = ImageDraw.Draw(my_image)
font = ImageFont.truetype("./fonts/동그라미재단M.ttf", 16)
#draw.text((0, 0),"(중국어 번역 예제)",(255,255,255),font=font)
for t in result:
    x0, y0 = t[0][0]
    x1, y1 = t[0][1] 
    x2, y2 = t[0][2]
    x3, y3 = t[0][3] 
    print (x0, y0, x1, y1, x2, y2, x3, y3)
    r = translator.translate(t[1],dest='ko')
    print ('Font Size=', y3-y0, r.text)
    if x0 == 24 and y0==48:
        font = ImageFont.truetype("./fonts/TMONBlack.ttf", y3-y0-25)
        draw.text((x0, y0),"Tmall앱 다운로드",(255,255,255),font=font)
#my_image.save('sample-out.jpg')


# In[22]:


my_image.save(final_output_file)


# In[23]:


from IPython.display import Image
saved_image_url = final_output_file
Image(filename=saved_image_url)


# In[ ]:




