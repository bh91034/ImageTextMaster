
Introduction
========================================
This application is a sample demo which is to guide how 'easy-ocr' can be used for manipulating texts in images.
In the demo, 'easy-ocr' will be used to detect all texts(e.g. Chinese texts) in the target image(e.g. 'a.png').
After that, 'cv2' will be used to get rid of the text area seamlessly in the image using 'cv2.inpaint()' method, the area info of each text was achieved by 'easy-ocr'.
In the interim output image, there's no texts in it meaning no Chinese texts in the image any more.
All texts detected by 'easy-ocr' will be translated by using 'googletrans' liberary which is a tranlation library by 'Google', and then the translated text will be written in the image instead of original text(e.g. Chinese text).
In case the translated text is too long not to fit in the area acupied by the original text, we should make the text shorter not to write text outside of the original text area.


How to run this demo
========================================
Before running this demo, you should install runnalbe environment in your PC.
 - install Anaconda (Anaconda3 2022.05 (Python 3.9.12 64-bit))
 - create an environment(e.g. 'easyocr-01') with 'Python 3.6.13' using Anaconda Navigator
 - install 'Jupiter Notebook' using Anaconda Navigator
 - Open Terminal(e.g. 'easyocr-01') from Anaconda
 - install EasyOCR (refer : https://github.com/JaidedAI/EasyOCR)
 - install googletrans (pip install googletrans==4.0.0-rc1)
   > NOTE : DO NOT install googletrans with only 'pip install googletrans'!!
   > That will install lower version (e.g. 3.x), and it'll not compatible with this demo.
   > Refer : https://blockdmask.tistory.com/540
 - go to the folder where this demo is located on your Terminal
 - run this demo with the following command
   > python easy_ocr_text_translator.py


Result
===================================================
This demo will use './images/a.png' as a source image file.
If you run this demo without errors, you can see 2 result files like below.
 - ./images/output-imterim/a.png
 - ./images/output-final/a.png

'./images/output-imterim/a.png' is the interim output file. In this file, you can see all Chinese texts were removed seamlessly.
'./images/output-final/a.png' is the final output file. In this file, you can see some of Chinese texts in the original file are tranlated in Korean.

