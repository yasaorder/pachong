import random
import time
from docx import Document
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # 因为用selenium进行登录会遇到验证码的问题，不会搞，就直接控制已经打开的浏览器，看readme
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(chrome_options)
    document = Document('safety.docx')

    for i in range(321):
        elements = driver.find_elements(By.CLASS_NAME,'quesBox')
        text = elements[0].text

        # 删一些没用的字符
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
