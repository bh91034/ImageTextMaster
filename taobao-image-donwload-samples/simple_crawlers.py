# Reference :
# - https://private.tistory.com/126
# How to run :
# - pip install selenium
# - pip install fake_useragent
# - download 'chromedriver.exe' to the same folder where your program run
from random import random
from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from urllib.parse import quote
import time, random

from selenium import webdriver
import sys, os

# if  getattr(sys, 'frozen', False): 
#     chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
#     driver = webdriver.Chrome(chromedriver_path)
# else:
#     driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
user_ag = UserAgent().random
options.add_argument('user-agent=%s'%user_ag)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
driver = webdriver.Chrome('chromedriver.exe', options=options)

# 크롤링 방지 설정을 undefined로 변경
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
            """
})

wait = WebDriverWait(driver, 5)

url = 'https://login.taobao.com/member/login.jhtml'
driver.get(url=url)
time.sleep(2)

id_input = wait.until(EC.presence_of_element_located((By.ID, "fm-login-id")))
id_input.send_keys('gkgk_yutong')

pw_input = wait.until(EC.presence_of_element_located((By.ID, "fm-login-password")))
pw_input.send_keys('hyja1837!')

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fm-button"))).click()

#로그인대기
time.sleep(random.randint(5, 10))

taobao_name_tag = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "site-nav-login-info-nick ")))
print(f" >>>> 접속자:{taobao_name_tag.text}")

url = 'https://item.taobao.com/item.htm?spm=a1z09.2.0.0.17b92e8dovzb3u&id=622011217822&_u=t20crpi8cdd984&mt='
driver.get(url)
time.sleep(2)
img_search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_DivItemDesc"]')))

search_link = driver.current_url

try:
    image_load_done = False
    while image_load_done == False:
        for i in range(100):
            image_url = driver.find_element_by_xpath('//*[@id="J_DivItemDesc"]/p/img['+str(i+1)+']').get_attribute('src')
            print ('###>    img=', image_url)
            if '85-85.gif' in image_url or '!!' not in image_url:
                print ('###>        [',i,']not loaded image found, image_url=', image_url)
                break
        print ('###> loop again')
        time.sleep(2)
except selenium.common.exceptions.NoSuchElementException:
    print ('###> done!')

# <div id="J_DivItemDesc" class="content">
#     <p>
#     <img src="https://img.alicdn.com/imgextra/i4/720419782/O1CN01aMNGfn2M8CvIOzPsc_!!720419782.jpg" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i2/720419782/O1CN01ZGmAVh2M8CvIOxTMV_!!720419782.jpg" style="max-width: 750.0px;" data-spm-anchor-id="2013.1.0.i1.36f02facYxuqSN">
#     <img src="https://img.alicdn.com/imgextra/i1/720419782/O1CN01jRpLd42M8CvNznaQ1_!!720419782.jpg" style="max-width: 750.0px;" data-spm-anchor-id="2013.1.0.i3.36f02facYxuqSN">
#     <img align="absmiddle" src="https://img.alicdn.com/imgextra/i3/720419782/O1CN013mgI7Y2M8Cw1n2N9d_!!720419782.jpg" style="max-width: 750.0px;">
#     <img align="absmiddle" src="https://img.alicdn.com/imgextra/i3/720419782/O1CN01ujorbb2M8CvQphBO4_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i4/720419782/O1CN01ANhjMj2M8CvLo9RDD_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i1/720419782/O1CN01z1TFn12M8CvLnOFfp_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i4/720419782/O1CN01oJdA4C2M8CvLo9N3t_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i2/720419782/O1CN01EEFp3O2M8CvDgYuCP_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i4/720419782/O1CN01MZmCBk2M8CvLnOinQ_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i1/720419782/O1CN010TxMsw2M8CvDgaz6d_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i2/720419782/O1CN01HsmX9r2M8CvMOyxtu_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i4/720419782/O1CN01AribBr2M8CvJnJmRW_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i1/720419782/O1CN01IdgRHw2M8CvP5sKpZ_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i2/720419782/O1CN01wngFZ92M8CvNzmVuz_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i3/720419782/O1CN01bcOGcj2M8CvDgYlti_!!720419782.jpg" class="" style="max-width: 750.0px;">
#     <img src="https://img.alicdn.com/imgextra/i4/720419782/O1CN01Qe5KU72M8CvLnOJqW_!!720419782.jpg" class="" style="max-width: 750.0px;"></p>
# </div>