# # -*- coding=utf-8 -*-
# import os
# import string
# import time
# import urllib.request
# from urllib.parse import quote
#
# import xlrd
# from bs4 import BeautifulSoup
# ## 引入WebDriver的包
# from selenium import webdriver
#
#
# def fafangyuan58(url):
#     filters = ['抢购', '不可多得', '稀缺', '定制', '至尊', '楼王', '黄金', '钻石', 'zui', 'ZUI']
#
#     ## 创建浏览器对象
#     browser = webdriver.Firefox()
#     browser.maximize_window()
#     browser.implicitly_wait(5)
#     browser.set_page_load_timeout(5)
#
#     ## 打开58经纪人网站
#     try:
#         browser.get('http://vip.anjuke.com/')
#     except:
#         browser.execute_script("window.stop()")
#
#         xlsfile = r".\data.xls"  # 打开指定路径中的xls文件
#         book = xlrd.open_workbook(xlsfile)  # 得到Excel文件的book对象，实例化对象
#
#         sheet2 = book.sheet_by_index(0)  # 通过sheet索引获得sheet对象
#         loginName = sheet2.cell_value(0, 1)
#         loginPwd = sheet2.cell_value(1, 1)
#         keyWord = sheet2.cell_value(2, 1)
#
#         print("before click")
#
#         # time.sleep(0.5)
#         js = "$('.login-switch.bar-code.iconfont').click();"
#         browser.execute_script(js)
#
#         print("after click")
#
#         # time.sleep(0.5)
#         browser.find_element_by_id('loginName').send_keys(str(loginName).split('.')[0])
#         browser.find_element_by_id('loginPwd').send_keys(loginPwd)
#         browser.find_element_by_id('loginSubmit').click()
#         # time.sleep(0.5)
#
#         set_bianhao = set()
#         set_biaoti = set()
#         start = 1
#         url_real = url + str(keyWord)
#         print(url_real)
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64"
#         }
#         req = urllib.request.Request(quote(url_real, safe=string.printable), headers=headers)
#         response = urllib.request.urlopen(req)
#         html = response.read()
#         soup = BeautifulSoup(html, 'html.parser')
#         page_box = soup.find('div', class_="paging-box page-box house-lst-page-box")
#         if len(page_box) == 0:
#             end = 0
#         else:
#             soup = BeautifulSoup(str(page_box), 'html.parser')
#             all = soup.find_all('a')
#             soup = BeautifulSoup(str(all[-2]), 'html.parser')
#             end = soup.find('a').text.strip()
#         end = int(end) + 1
#
#         for i in range(start, end + 1):
#             url_real = url + str(keyWord) + "&page=" + str(i)
#             print(quote(url_real, safe=string.printable))
#             req = urllib.request.Request(quote(url_real, safe=string.printable), headers=headers)
#             response = urllib.request.urlopen(req)
#             html = response.read()
#             soup = BeautifulSoup(html, 'html.parser')
#             house_list_wrap = soup.find('div', class_="list-wrap")
#             soup = BeautifulSoup(str(house_list_wrap), 'html.parser')
#             all = soup.find_all('li')
#
#             for a in all:
#                 try:
#                     a_soup = BeautifulSoup(str(a), 'html.parser')
#                     info_panel = a_soup.find('div', class_="info-panel")
#                     a_soup = BeautifulSoup(str(info_panel), 'html.parser')
#                     href = a_soup.find('a').attrs['href'].strip()
#                     bianhao = href.strip("/").strip("/esf")
#                     if bianhao not in set_bianhao:
#                         set_bianhao.add(bianhao)
#                         house_url = "http://www.yongxinjia.com" + href
#                         shoujia = a_soup.find('span', class_="num").text.strip()  # 售价
#
#                         req = urllib.request.Request(quote(house_url, safe=string.printable), headers=headers)
#                         response = urllib.request.urlopen(req)
#                         html = response.read()
#                         soup = BeautifulSoup(html, 'html.parser')
#                         room = soup.find('div', class_="room").text.strip().strip("厅").split("室")
#                         shi = room[0]  # 室
#                         ting = room[1]  # 厅
#                         if int(shi) < 1:
#                             shi = '1'
#                         if int(ting) < 1:
#                             ting = '1'
#                         wei = 1
#                         if int(shi) > 2:
#                             wei = '2'
#                         html = html.decode("utf-8")
#                         n = html.find('楼层：')
#                         louceng = html[n + 24:n + 35].split("/")[0]
#                         zongceng = html[n + 24:n + 35].split("/")[1].split("层")[0]
#                         mianji = soup.find('div', class_="area").text.strip().strip("平")
#                         n = html.find('年代：')
#                         niandai = html[n + 24:n + 30].split("年")[0]
#                         shoujia = soup.find('div', class_="mainInfo bold").text.strip().strip("万")
#                         biaoti = soup.find('h1', class_="main").text.strip()
#                         if biaoti not in set_biaoti:
#                             set_biaoti.add(biaoti)
#                             xiangqing = soup.find('div', class_="feature").text.strip().replace("?", "")
#                             if len(xiangqing) >= 300:
#                                 xiangqing = xiangqing[0:299]
#                             xintai = xiangqing
#                             peitao = xiangqing
#                             jieshao = xiangqing
#
#                             browser.get('http://vip.anjuke.com/house/publish/ershou/?from=manage')
#                             browser.find_elements_by_xpath(
#                                 "//input[@class='ui-button ui-button-positive ui-button-medium']")[
#                                 0].click()
#                             browser.find_element_by_name('user_defined').send_keys(bianhao)  # 房源编号
#
#                             browser.find_element_by_name('room').send_keys(shi)
#                             browser.find_element_by_name('hall').send_keys(ting)
#                             browser.find_element_by_name('bathroom').send_keys(wei)
#                             browser.find_element_by_name('floor').send_keys(louceng)
#                             browser.find_element_by_name('allFloor').send_keys(zongceng)
#                             browser.find_element_by_name('allArea').send_keys(mianji)
#
#                             browser.find_element_by_name('community58').send_keys(keyWord)  # 小区地址
#                             time.sleep(0.5)
#                             browser.find_element_by_class_name('auto-wrap').click()
#
#                             browser.find_elements_by_class_name("ui-select-box")[2].click()  # 房屋情况
#                             # time.sleep(0.3)
#                             browser.find_element_by_xpath("//li[@data-val='8']").click()  # 普通住宅
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[3].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='4']")[1].click()  # 精装
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[4].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='2']")[2].click()  # 朝南
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[5].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='3']")[1].click()  # 塔楼
#
#                             browser.find_element_by_name('age').send_keys(niandai)
#                             browser.find_element_by_name('price').send_keys(shoujia)
#                             browser.find_element_by_name('allArea').send_keys(mianji)
#                             browser.find_element_by_name('unitArea').click()
#                             # browser.find_element_by_name('unitArea').send_keys(mianji - 1)#套内面积
#
#                             target = browser.find_elements_by_class_name("ui-select-box")[8]
#                             browser.execute_script("arguments[0].scrollIntoView();", target)
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[8].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='1']")[5].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[9].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='1']")[6].click()
#
#                             browser.find_elements_by_class_name("ui-radio")[0].click()  # 满五年
#                             browser.find_elements_by_class_name("ui-radio")[3].click()  # 唯一住房
#
#                             tag = browser.find_element_by_name('title')
#                             for filter in filters:
#                                 biaoti = biaoti.replace(filter, "")
#                             tag.send_keys(biaoti)
#                             browser.execute_script("arguments[0].scrollIntoView();", target)
#                             # time.sleep(0.3)
#                             browser.find_element_by_id('txt_1').send_keys(xiangqing)
#                             browser.find_element_by_id('txt_2').send_keys(xintai)
#                             browser.find_element_by_id('txt_3').send_keys(peitao)
#                             browser.find_element_by_id('txt_4').send_keys(jieshao)
#
#                             tupian = soup.find('div', id="album-view-wrap")
#                             soup = BeautifulSoup(str(tupian), 'html.parser')
#                             all = soup.find_all('li')
#                             n = 0
#                             for a in all:
#                                 a_soup = BeautifulSoup(str(a), 'html.parser')
#                                 img = a_soup.find('img')['data-large']
#                                 n = n + 1
#                                 import requests
#                                 r = requests.get(img)
#                                 with open('./imgs/' + str(n) + ".jpg", 'wb') as f:
#                                     f.write(r.content)
#                                 time.sleep(1)
#                                 # import cv2
#                                 # import numpy as np
#                                 #
#                                 # path = "imgs/" + n + ".jpg"
#                                 #
#                                 # img = cv2.imread(path)
#                                 # hight, width, depth = img.shape[0:3]
#                                 #
#                                 # # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
#                                 # thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
#                                 #
#                                 # # 创建形状和尺寸的结构元素
#                                 # kernel = np.ones((3, 3), np.uint8)
#                                 #
#                                 # # 扩张待修复区域
#                                 # hi_mask = cv2.dilate(thresh, kernel, iterations=1)
#                                 # specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)
#                                 #
#                                 # cv2.namedWindow("Image", 0)
#                                 # cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
#                                 # cv2.imshow("Image", img)
#                                 #
#                                 # cv2.namedWindow("newImage", 0)
#                                 # cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
#                                 # cv2.imshow("newImage", specular)
#                                 # cv2.waitKey(0)
#                                 # cv2.destroyAllWindows()
#                                 browser.find_element_by_id('room_fileupload').send_keys(
#                                     os.getcwd() + "\imgs\\" + str(n) + ".jpg")
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("set-main")[0].click()
#                             time.sleep(0.3)
#                             target = browser.find_element_by_id("publish-ershou-add")
#                             browser.execute_script("arguments[0].scrollIntoView();", target)
#                             # time.sleep(0.3)
#                             target.click()
#                             time.sleep(25)
#                 except:
#                     continue
#
#
# url = "http://www.yongxinjia.com/esf?keyWord="
# fafangyuan58(url)

# # -*- coding=utf-8 -*-
# import os
# import string
# import time
# import urllib.request
# from urllib.parse import quote
#
# import xlrd
# from bs4 import BeautifulSoup
# ## 引入WebDriver的包
# from selenium import webdriver
#
#
# def fafangyuan58andanjuke(url):
#     filters = ['抢购', '不可多得', '稀缺', '定制', '至尊', '楼王', '黄金', '钻石', 'zui', 'ZUI']
#
#     ## 创建浏览器对象
#     browser = webdriver.Firefox()
#     browser.maximize_window()
#     browser.implicitly_wait(3)
#     browser.set_page_load_timeout(3)
#
#     ## 打开58经纪人网站
#     try:
#         browser.get('http://vip.anjuke.com/')
#     except:
#         browser.execute_script("window.stop()")
#
#         xlsfile = r".\data.xls"  # 打开指定路径中的xls文件
#         book = xlrd.open_workbook(xlsfile)  # 得到Excel文件的book对象，实例化对象
#
#         sheet2 = book.sheet_by_index(0)  # 通过sheet索引获得sheet对象
#         loginName = sheet2.cell_value(0, 1)
#         loginPwd = sheet2.cell_value(1, 1)
#         keyWord = sheet2.cell_value(2, 1)
#
#         print("before click")
#
#         # time.sleep(0.5)
#         js = "$('.login-switch.bar-code.iconfont').click();"
#         browser.execute_script(js)
#
#         print("after click")
#
#         # time.sleep(0.5)
#         browser.find_element_by_id('loginName').send_keys(str(loginName).split('.')[0])
#         browser.find_element_by_id('loginPwd').send_keys(str(loginPwd).split('.')[0])
#         browser.find_element_by_id('loginSubmit').click()
#         # time.sleep(0.5)
#
#         set_bianhao = set()
#         set_biaoti = set()
#         start = 1
#         url_real = url + str(keyWord)
#         print(url_real)
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64"
#         }
#         req = urllib.request.Request(quote(url_real, safe=string.printable), headers=headers)
#         response = urllib.request.urlopen(req)
#         html = response.read()
#         soup = BeautifulSoup(html, 'html.parser')
#         page_box = soup.find('div', class_="paging-box page-box house-lst-page-box")
#         if len(page_box) == 0:
#             end = 0
#         else:
#             soup = BeautifulSoup(str(page_box), 'html.parser')
#             all = soup.find_all('a')
#             # print(all)
#             soup = BeautifulSoup(str(all[-1]), 'html.parser')
#             end = soup.find('a').text.strip()
#             if end == "下一页":
#                 end = all[-2].text.strip()
#             # print("end = ", end)
#         end = int(end) + 1
#
#         for i in range(start, end + 1):
#             url_real = url + str(keyWord) + "&page=" + str(i)
#             print(quote(url_real, safe=string.printable))
#             req = urllib.request.Request(quote(url_real, safe=string.printable), headers=headers)
#             response = urllib.request.urlopen(req)
#             html = response.read()
#             soup = BeautifulSoup(html, 'html.parser')
#             house_list_wrap = soup.find('div', class_="list-wrap")
#             soup = BeautifulSoup(str(house_list_wrap), 'html.parser')
#             all = soup.find_all('li')
#
#             for a in all:
#                 try:
#                     a_soup = BeautifulSoup(str(a), 'html.parser')
#                     info_panel = a_soup.find('div', class_="info-panel")
#                     a_soup = BeautifulSoup(str(info_panel), 'html.parser')
#                     href = a_soup.find('a').attrs['href'].strip()
#                     bianhao = href.strip("/").strip("/esf")
#                     if bianhao not in set_bianhao:
#                         set_bianhao.add(bianhao)
#                         house_url = "http://www.yongxinjia.com" + href
#                         shoujia = a_soup.find('span', class_="num").text.strip()  # 售价
#
#                         req = urllib.request.Request(quote(house_url, safe=string.printable), headers=headers)
#                         response = urllib.request.urlopen(req)
#                         html = response.read()
#                         soup = BeautifulSoup(html, 'html.parser')
#                         room = soup.find('div', class_="room").text.strip().strip("厅").split("室")
#                         shi = room[0]  # 室
#                         ting = room[1]  # 厅
#                         if int(shi) < 1:
#                             shi = '1'
#                         if int(ting) < 1:
#                             ting = '1'
#                         wei = 1
#                         if int(shi) > 2:
#                             wei = '2'
#                         html = html.decode("utf-8")
#                         n = html.find('楼层：')
#                         louceng = html[n + 24:n + 35].split("/")[0]
#                         zongceng = html[n + 24:n + 35].split("/")[1].split("层")[0]
#                         mianji = soup.find('div', class_="area").text.strip().strip("平")
#                         n = html.find('年代：')
#                         niandai = html[n + 24:n + 30].split("年")[0]
#                         shoujia = soup.find('div', class_="mainInfo bold").text.strip().strip("万")
#                         biaoti = soup.find('h1', class_="main").text.strip()
#                         if biaoti not in set_biaoti:
#                             set_biaoti.add(biaoti)
#                             xiangqing = soup.find('div', class_="feature").text.strip().replace("?", "")
#                             if len(xiangqing) >= 300:
#                                 xiangqing = xiangqing[0:299]
#                             xintai = xiangqing
#                             peitao = xiangqing
#                             jieshao = xiangqing
#
#                             browser.get('http://vip.anjuke.com/house/publish/ershou/?from=manage')
#                             browser.find_element_by_id('chooseWeb_1').click()
#                             browser.find_elements_by_xpath(
#                                 "//input[@class='ui-button ui-button-positive ui-button-medium']")[
#                                 0].click()
#                             browser.find_element_by_name('user_defined').click()
#                             browser.find_element_by_name('user_defined').clear()
#                             browser.find_element_by_name('user_defined').send_keys(bianhao)  # 房源编号
#
#                             browser.find_element_by_name('room').send_keys(shi)
#                             browser.find_element_by_name('hall').send_keys(ting)
#                             browser.find_element_by_name('bathroom').send_keys(wei)
#                             browser.find_element_by_name('floor').send_keys(louceng)
#                             browser.find_element_by_name('allFloor').send_keys(zongceng)
#                             browser.find_element_by_name('allArea').send_keys(mianji)
#
#                             browser.find_element_by_name('communityauto').send_keys(keyWord)  # 小区地址
#                             time.sleep(1)
#                             browser.find_elements_by_class_name('auto-wrap')[0].click()
#
#                             # browser.find_element_by_name('communityAJK').send_keys(keyWord)  # 小区地址
#                             # time.sleep(0.5)
#                             # browser.find_elements_by_class_name('auto-wrap')[1].click()
#
#                             browser.find_element_by_name('community58').click()
#                             browser.find_element_by_name('community58').clear()
#                             browser.find_element_by_name('community58').send_keys(keyWord)  # 小区地址
#                             time.sleep(0.5)
#                             browser.find_elements_by_class_name('auto-wrap')[2].click()
#
#                             browser.find_elements_by_class_name("ui-select-box")[2].click()  # 房屋情况
#                             # time.sleep(0.3)
#                             browser.find_element_by_xpath("//li[@data-val='8']").click()  # 普通住宅
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[3].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='4']")[1].click()  # 精装
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[4].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='2']")[2].click()  # 朝南
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[5].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='3']")[1].click()  # 塔楼
#
#                             browser.find_element_by_name('age').send_keys(niandai)
#                             browser.find_element_by_name('price').send_keys(shoujia)
#                             browser.find_element_by_name('allArea').send_keys(mianji)
#                             browser.find_element_by_name('unitArea').click()
#                             # browser.find_element_by_name('unitArea').send_keys(mianji - 1)#套内面积
#
#                             target = browser.find_elements_by_class_name("ui-select-box")[8]
#                             browser.execute_script("arguments[0].scrollIntoView();", target)
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[8].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='1']")[5].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("ui-select-box")[9].click()
#                             # time.sleep(0.3)
#                             browser.find_elements_by_xpath("//li[@data-val='1']")[6].click()
#
#                             browser.find_elements_by_class_name("ui-radio")[0].click()  # 满五年
#                             browser.find_elements_by_class_name("ui-radio")[3].click()  # 唯一住房
#
#                             tag = browser.find_element_by_name('title')
#                             for filter in filters:
#                                 biaoti = biaoti.replace(filter, "")
#                             tag.send_keys(biaoti)
#                             browser.execute_script("arguments[0].scrollIntoView();", target)
#                             # time.sleep(0.3)
#                             browser.find_element_by_id('txt_1').send_keys(xiangqing)
#                             browser.find_element_by_id('txt_2').send_keys(xintai)
#                             browser.find_element_by_id('txt_3').send_keys(peitao)
#                             browser.find_element_by_id('txt_4').send_keys(jieshao)
#
#                             browser.find_element_by_link_text("品质小区").click()
#                             browser.find_element_by_link_text("繁华地段").click()
#                             browser.find_element_by_link_text("配套成熟").click()
#
#                             tupian = soup.find('div', id="album-view-wrap")
#                             soup = BeautifulSoup(str(tupian), 'html.parser')
#                             all = soup.find_all('li')
#
#                             n = 0
#                             for a in all:
#                                 a_soup = BeautifulSoup(str(a), 'html.parser')
#                                 img = a_soup.find('img')['data-large']
#                                 n = n + 1
#                                 if n > 10:
#                                     continue
#                                 import requests
#                                 r = requests.get(img)
#                                 with open('./imgs/' + str(n) + ".jpg", 'wb') as f:
#                                     f.write(r.content)
#                                 time.sleep(1)
#                                 # import cv2
#                                 # import numpy as np
#                                 #
#                                 # path = "imgs/" + n + ".jpg"
#                                 #
#                                 # img = cv2.imread(path)
#                                 # hight, width, depth = img.shape[0:3]
#                                 #
#                                 # # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
#                                 # thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))
#                                 #
#                                 # # 创建形状和尺寸的结构元素
#                                 # kernel = np.ones((3, 3), np.uint8)
#                                 #
#                                 # # 扩张待修复区域
#                                 # hi_mask = cv2.dilate(thresh, kernel, iterations=1)
#                                 # specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)
#                                 #
#                                 # cv2.namedWindow("Image", 0)
#                                 # cv2.resizeWindow("Image", int(width / 2), int(hight / 2))
#                                 # cv2.imshow("Image", img)
#                                 #
#                                 # cv2.namedWindow("newImage", 0)
#                                 # cv2.resizeWindow("newImage", int(width / 2), int(hight / 2))
#                                 # cv2.imshow("newImage", specular)
#                                 # cv2.waitKey(0)
#                                 # cv2.destroyAllWindows()
#                                 browser.find_element_by_id('room_fileupload').send_keys(
#                                     os.getcwd() + "\imgs\\" + str(n) + ".jpg")
#                             # time.sleep(0.3)
#                             browser.find_elements_by_class_name("set-main")[0].click()
#                             time.sleep(0.3)
#                             target = browser.find_element_by_id("publish-ershou-add")
#                             browser.execute_script("arguments[0].scrollIntoView();", target)
#                             # time.sleep(0.3)
#                             target.click()
#                             time.sleep(25)
#                 except:
#                     continue
#
#
# url = "http://www.yongxinjia.com/esf?keyWord="
# fafangyuan58andanjuke(url)

# -*- coding=utf-8 -*-
import os
import string
import time
import urllib.request
import win32clipboard
from urllib.parse import quote

import xlrd
from bs4 import BeautifulSoup
## 引入WebDriver的包
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def ffy58ajkgj(url):
    filters = ['抢购', '不可多得', '稀缺', '定制', '至尊', '楼王', '黄金', '钻石', 'zui', 'ZUI', '超级', '顶级', '优质', '首选', '首府', '孩子', '第一',
               '精品']
    ## 创建浏览器对象
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.set_page_load_timeout(10)
    ## 打开58经纪人网站
    try:
        browser.get('http://vip.anjuke.com/')
    except:
        browser.execute_script("window.stop()")
        xlsfile = r".\data.xls"  # 打开指定路径中的xls文件
        book = xlrd.open_workbook(xlsfile)  # 得到Excel文件的book对象，实例化对象
        sheet2 = book.sheet_by_index(0)  # 通过sheet索引获得sheet对象
        loginName = sheet2.cell_value(0, 1)
        loginPwd = sheet2.cell_value(1, 1)
        keyWord = sheet2.cell_value(2, 1)
        js = "$('.login-switch.bar-code.iconfont').click();"
        browser.execute_script(js)
        browser.find_element_by_id('loginName').send_keys(str(loginName).split('.')[0])
        browser.find_element_by_id('loginPwd').send_keys(str(loginPwd).split('.')[0])
        browser.find_element_by_id('loginSubmit').click()
        set_bianhao = set()
        set_biaoti = set()
        start = 1
        url_real = url + str(keyWord)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64"
        }
        req = urllib.request.Request(quote(url_real, safe=string.printable), headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        page_box = soup.find('div', class_="paging-box page-box house-lst-page-box")
        if len(page_box) == 0:
            end = 0
        else:
            soup = BeautifulSoup(str(page_box), 'html.parser')
            all = soup.find_all('a')
            soup = BeautifulSoup(str(all[-1]), 'html.parser')
            end = soup.find('a').text.strip()
            if end == "下一页":
                end = all[-2].text.strip()
        end = int(end) + 1
        for i in range(start, end + 1):
            url_real = url + str(keyWord) + "&page=" + str(i)
            req = urllib.request.Request(quote(url_real, safe=string.printable), headers=headers)
            response = urllib.request.urlopen(req)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            house_list_wrap = soup.find('div', class_="list-wrap")
            soup = BeautifulSoup(str(house_list_wrap), 'html.parser')
            all = soup.find_all('li')
            for a in all:
                try:
                    a_soup = BeautifulSoup(str(a), 'html.parser')
                    info_panel = a_soup.find('div', class_="info-panel")
                    a_soup = BeautifulSoup(str(info_panel), 'html.parser')
                    href = a_soup.find('a').attrs['href'].strip()
                    bianhao = href.strip("/").strip("/esf")
                    if bianhao not in set_bianhao:
                        set_bianhao.add(bianhao)
                        house_url = "http://www.yongxinjia.com" + href
                        shoujia = a_soup.find('span', class_="num").text.strip()  # 售价
                        req = urllib.request.Request(quote(house_url, safe=string.printable), headers=headers)
                        response = urllib.request.urlopen(req)
                        html = response.read()
                        soup = BeautifulSoup(html, 'html.parser')
                        room = soup.find('div', class_="room").text.strip().strip("厅").split("室")
                        shi = room[0]  # 室
                        ting = room[1]  # 厅
                        if int(shi) < 1:
                            shi = '1'
                        if int(ting) < 1:
                            ting = '1'
                        wei = 1
                        if int(shi) > 2:
                            wei = '2'
                        html = html.decode("utf-8")
                        n = html.find('楼层：')
                        louceng = html[n + 24:n + 35].split("/")[0]
                        zongceng = html[n + 24:n + 35].split("/")[1].split("层")[0]
                        mianji = soup.find('div', class_="area").text.strip().strip("平")
                        n = html.find('年代：')
                        niandai = html[n + 24:n + 30].split("年")[0]
                        shoujia = soup.find('div', class_="mainInfo bold").text.strip().strip("万")
                        biaoti = soup.find('h1', class_="main").text.strip()
                        if biaoti not in set_biaoti:
                            set_biaoti.add(biaoti)
                            xiangqing = soup.find('div', class_="feature").text.strip().replace("?", "")
                            if len(xiangqing) >= 300:
                                xiangqing = xiangqing[0:299]
                            xintai = xiangqing
                            peitao = xiangqing
                            jieshao = xiangqing
                            browser.get('http://vip.anjuke.com/house/publish/ershou/?from=manage')
                            # browser.find_element_by_id('chooseWeb_1').click()
                            browser.find_elements_by_xpath(
                                "//input[@class='ui-button ui-button-positive ui-button-medium']")[
                                0].click()

                            tags = browser.find_elements_by_id('formcache-refuse')
                            if (len(tags) > 0):
                                tags[0].click()

                            browser.find_element_by_name('user_defined').click()
                            browser.find_element_by_name('user_defined').clear()
                            browser.find_element_by_name('user_defined').send_keys(bianhao)  # 房源编号
                            browser.find_element_by_name('room').send_keys(shi)
                            browser.find_element_by_name('hall').send_keys(ting)
                            browser.find_element_by_name('bathroom').send_keys(wei)
                            browser.find_element_by_name('floor').click()
                            browser.find_element_by_name('floor').clear()
                            browser.find_element_by_name('floor').send_keys(louceng)
                            browser.find_element_by_name('allFloor').click()
                            browser.find_element_by_name('allFloor').clear()
                            browser.find_element_by_name('allFloor').send_keys(zongceng)
                            browser.find_element_by_name('allArea').send_keys(mianji)
                            browser.find_element_by_name('communityauto').send_keys(keyWord)  # 小区地址
                            # time.sleep(0.5)
                            browser.find_elements_by_class_name('auto-wrap')[0].click()
                            # browser.find_element_by_name('communityAJK').send_keys(keyWord)  # 小区地址
                            # time.sleep(0.5)
                            # browser.find_elements_by_class_name('auto-wrap')[1].click()
                            browser.find_element_by_name('community58').click()
                            browser.find_element_by_name('community58').clear()
                            browser.find_element_by_name('community58').send_keys(keyWord)  # 小区地址
                            # time.sleep(0.5)
                            browser.find_elements_by_class_name('auto-wrap')[2].click()
                            browser.find_element_by_name('address58').click()
                            browser.find_element_by_name('address58').clear()
                            browser.find_element_by_name('address58').send_keys(keyWord)
                            #
                            # browser.find_element_by_name('communityGJ').click()
                            # browser.find_element_by_name('communityGJ').clear()
                            # browser.find_element_by_name('communityGJ').send_keys(keyWord)  # 小区地址
                            # browser.find_element_by_name('addressGJ').click()
                            # time.sleep(0.5)
                            # browser.find_elements_by_class_name('auto-wrap')[3].click()
                            browser.find_elements_by_class_name("ui-select-box")[2].click()  # 房屋情况
                            # browser.find_elements_by_xpath("//li[@data-val='0']")[0].click()
                            # # browser.find_element_by_name('addressGJ').send_keys(keyWord)
                            # browser.find_elements_by_class_name("ui-select-box")[4].click()
                            browser.find_element_by_xpath("//li[@data-val='8']").click()  # 普通住宅
                            browser.find_elements_by_class_name("ui-select-box")[3].click()
                            browser.find_elements_by_xpath("//li[@data-val='4']")[1].click()  # 精装
                            browser.find_elements_by_class_name("ui-select-box")[4].click()
                            browser.find_elements_by_xpath("//li[@data-val='2']")[2].click()  # 朝南
                            # browser.find_elements_by_class_name("ui-select-box")[5].click()
                            # browser.find_elements_by_xpath("//li[@data-val='3']")[2].click()  # 塔楼
                            browser.find_element_by_name('age').send_keys(niandai)
                            browser.find_element_by_name('price').click()
                            browser.find_element_by_name('price').clear()
                            browser.find_element_by_name('price').send_keys(shoujia)
                            browser.find_element_by_name('allArea').send_keys(mianji)
                            browser.find_element_by_name('unitArea').click()
                            # browser.find_element_by_name('unitArea').send_keys(mianji - 1)#套内面积
                            target = browser.find_elements_by_class_name("ui-select-box")[8]
                            browser.execute_script("arguments[0].scrollIntoView();", target)
                            browser.find_elements_by_class_name("ui-select-box")[8].click()
                            browser.find_elements_by_xpath("//li[@data-val='1']")[5].click()
                            browser.find_elements_by_class_name("ui-select-box")[9].click()
                            browser.find_elements_by_xpath("//li[@data-val='1']")[6].click()
                            browser.find_elements_by_class_name("ui-radio")[0].click()  # 满五年
                            browser.find_elements_by_class_name("ui-radio")[3].click()  # 唯一住房
                            tag = browser.find_element_by_name('title')
                            for filter in filters:
                                biaoti = biaoti.replace(filter, "")
                            tag.send_keys(biaoti)
                            browser.execute_script("arguments[0].scrollIntoView();", target)
                            findAndPaste(browser, 'txt_1', xiangqing)
                            findAndPaste(browser, 'txt_2', xintai)
                            findAndPaste(browser, 'txt_3', peitao)
                            findAndPaste(browser, 'txt_4', jieshao)

                            target = browser.find_element_by_link_text('品质小区')
                            ActionChains(browser).move_to_element(target).perform()
                            # time.sleep(0.5)
                            browser.find_element_by_link_text("品质小区").click()
                            browser.find_element_by_link_text("繁华地段").click()
                            browser.find_element_by_link_text("配套成熟").click()
                            tupian = soup.find('div', id="album-view-wrap")
                            soup = BeautifulSoup(str(tupian), 'html.parser')
                            all = soup.find_all('li')
                            n = 0
                            # browser.find_element_by_id('room_fileupload').clear()
                            for a in all:
                                a_soup = BeautifulSoup(str(a), 'html.parser')
                                img = a_soup.find('img')['data-large']
                                n = n + 1
                                if n > 10:
                                    continue
                                import requests
                                r = requests.get(img)
                                with open('./imgs/' + str(n) + ".jpg", 'wb') as f:
                                    f.write(r.content)
                                browser.find_element_by_id('room_fileupload').send_keys(
                                    os.getcwd() + "\imgs\\" + str(n) + ".jpg")
                            browser.find_elements_by_class_name("set-main")[0].click()
                            time.sleep(1)
                            target = browser.find_element_by_id("publish-ershou-add")
                            browser.execute_script("arguments[0].scrollIntoView();", target)
                            target.click()
                            time.sleep(25)
                except:
                    continue


def findAndPaste(browser, id, str):
    browser.find_element_by_id(id).click()
    browser.find_element_by_id(id).clear()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(str, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    browser.find_element_by_id(id).send_keys(Keys.CONTROL + "v")


url = "http://www.yongxinjia.com/esf?keyWord="
ffy58ajkgj(url)