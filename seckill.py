
#  https://chromedriver.storage.googleapis.com/index.html 打开Google 驱动地址， 要和 本地Google 浏览器版本基本一致。 
import datetime

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

import win32com.client

speaker = win32com.client.Dispatch('SAPI.SpVoice')


browser = webdriver.Chrome()


browser.get('https://www.taobao.com/')

time.sleep(5)


browser.find_element(By.LINK_TEXT, '亲，请登录').click()  


print(f"请尽快扫码登陆")
time.sleep(10)

# browser.find_element(By.CLASS_NAME, 'icon-qrcode').click()


browser.get("https://cart.taobao.com/cart.htm")
# browser.get("https://buy.tmall.com/order/confirm_order.htm")


time.sleep(7)

while True: 
    if browser.find_element(By.CLASS_NAME,'J_SelectAll'):
        browser.find_element(By.CLASS_NAME, 'J_SelectAll').click()
        break

while True:

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    print(now)

    if now >= '2023-04-29 20:23:00.000001':
        while True:
            try:
                if browser.find_element(By.ID, 'J_SmallSubmit'):
                    print('here')

                    browser.find_element(By.ID, 'J_SmallSubmit').click()
                    print(f'老板， 你的茅台我帮你抢到了，快点去结算')
                    speaker.Speak(f'老板， 商品我帮你抢到了，快点去结算')
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