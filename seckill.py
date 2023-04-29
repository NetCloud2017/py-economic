
#  https://chromedriver.storage.googleapis.com/index.html 打开Google 驱动地址， 要和 本地Google 浏览器版本基本一致。 
import datetime

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

import win32com.client

speaker = win32com.client.Dispatch('SAPI.SpVoice')


browser = webdriver.Chrome()


browser.get('https://www.jd.com/')

time.sleep(5)


browser.find_element(By.LINK_TEXT, '你好，请登录').click()


print(f"请扫码")
time.sleep(10)



browser.get("https://cart.jd.com/cart_index")

time.sleep(5)

while True: 
    if browser.find_element(By.CLASS_NAME,'jdcheckbox'):
        browser.find_element(By.CLASS_NAME, 'jdcheckbox').click()
        break

while True:

    now = datetime.datetime.now().strftime('%Y-%m-$d %H:%M:%S.%f')

    print(now)

    if now >= '2023-04-29 16:45:00':
        while 1==1:
            try:
                if browser.find_element(By.LINK_TEXT, '去结算'):
                    print('here')

                    browser.find_element(By.LINK_TEXT, '去结算').click()
                    print(f'老板， 你的茅台我帮你抢到了，快点去结算')
                    speaker.Speak(f'老板， 你的茅台我帮你抢到了，快点去结算')
                    break
            except:
                pass
        
        while True:
            try: 
                if browser.find_element(By.LINK_TEXT, '提交订单'):
                    browser.find_element(By.LINK_TEXT, '提交订单').click()
                    print(f'抢单成功， 尽快付款')
            except: 
                print(f'老板，付钱， 不然下次不帮你抢了')
                break
            time.sleep(0.01)