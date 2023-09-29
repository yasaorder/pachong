import os
import random
import time

import requests
from lxml import etree
from docx import Document
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

load_wait_short = 2
load_wait_middle = 4
load_wait_long = 6


def getChromeBrowser():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = r"D:\SoftwarePackage\Programming\Python\chromedriver_win32_96_0_4664\chromedriver.exe"
    browser = webdriver.Chrome(chrome_driver, options=chrome_options)
    return browser


def openBrowserWebsite(url):
    browser = getChromeBrowser()
    browser.get(url)
    browser.implicitly_wait(load_wait_short)
    print('web title:', end='')
    print(browser.title)

if __name__ == '__main__':
    # 右键谷歌浏览器图标，目标后面添加如下，确定，重启浏览器。
    # --args --disable-web-security --user-data-dir = D:\pycharmprogram\pachong
    # os.system("cd C:\Program Files\Google\Chrome\Application")
    # dir_path = os.getcwd()
    # user-data-dir 如果是其他盘或者c 盘已有的文件，chrome 会报错，无法对其进行读写操作
    # os.system('C:\Program Files\Google\Chrome\Application>chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')
    # --remote --debugging - port值，可以指定任何打开的端口。
    # --user-data-dir标记，指定创建新Chrome配置文件的目录。它是为了确保在单独的配置文件中启动chrome，不会污染你的默认配置文件。

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(chrome_options)
    document = Document('safety.docx')

    for i in range(321):
        elements = driver.find_elements(By.CLASS_NAME,'quesBox')
        text = elements[0].text

        text = text.replace('答案解析：\n上一题\n下一题', '')
        text = text.replace('隐藏答案', '')
        document.add_paragraph(text)

        # 点击下一题按钮
        ran_time = random.random()*3
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div[2]/div[2]').click()
        time.sleep(ran_time)
        """
        上一次爬报错，可能是元素不可交互，以下为gpt给出的方案
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        # 等待元素可交互
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[2]/div[2]')))
        # 点击元素
        element.click()
        """

        document.save('safety.docx')
