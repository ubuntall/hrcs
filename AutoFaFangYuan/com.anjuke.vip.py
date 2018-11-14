## 引入WebDriver的包
import time

from selenium import webdriver

## 创建浏览器对象

browser = webdriver.Firefox()
browser.maximize_window()
## 打开58经纪人网站
browser.get('http://vip.anjuke.com/')

# tag = browser.find_element_by_class_name("login-switch")
# print(tag)
# tag.click()

loginName = browser.find_element_by_id('loginName')
loginName.send_keys("15860197003")

loginPwd = browser.find_element_by_id('loginPwd')
loginPwd.send_keys("l123456")
time.sleep(1)
loginSubmit = browser.find_element_by_id('loginSubmit')
loginSubmit.click()
