#引入selenium库中的 webdriver 模块
from selenium import webdriver
#引入time库
import time
from selenium.webdriver.common.by import By

#打开谷歌浏览器
driver = webdriver.Edge()
#打开智慧树学习平台
driver.get('http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fappswh.chaoxing.com%2Fres%2Fpc%2FquizTestWeb%2Fviews%2Fpractice.html%3FcategoryId%3D5B8654FA7C8E9063%26questionConfigId%3D8719%26name%3D%25E5%259F%25BA%25E7%25A1%2580%25E5%25AE%2589%25E5%2585%25A8%25E7%259F%25A5%25E8%25AF%2586%25E6%25A8%25A1%25E6%258B%259F%25E8%2587%25AA%25E6%25B5%258B')
'''
考虑到网页打开的速度取决于每个人的电脑和网速，
使用time库sleep()方法，让程序睡眠5秒
'''
time.sleep(5)
#在主页面点击登录按钮，进入登录页面
# driver.find_element(By.XPATH, '//*[@id="notLogin"]/span/a[1]').click()
#输入账号和密码
driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys('18707106536')
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys('486932SHKT')
time.sleep(3)
#点击登录按钮
driver.find_element(By.XPATH, '//*[@id="leftdiv"]/div[1]/a[2]').click()
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[1]/span[2]').click()
time.sleep(2)
get = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]')
print(get)

