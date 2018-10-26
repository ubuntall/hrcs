# -*- coding=utf-8 -*-
import json
import re
import string
import urllib.request
from urllib.parse import quote

import xlrd
from bs4 import BeautifulSoup
from xlutils.copy import copy


def downloadhtml(url_str, start, end):
    for i in range(start, end + 1):
        url = url_str + str(i)
        # print(url)
        html = getHtml(url)
        saveHtml(str(i), html)
        print(str(i) + " 下载成功")


def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


def saveHtml(file_name, file_content):
    # 注意windows文件命名的禁用符，比如 /
    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        # 写文件用bytes而不是str，所以要转码
        f.write(file_content)


# downloadhtml("http://www.yongxinjia.com/jjr/?page=", 1, 34)
def pachong(houzui, start, end):
    xlsfile = 'zhongjie_longyan.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()
    print(sheet_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    print(ncols)
    j = -1
    for i in range(start, end + 1):
        url = str(i) + houzui
        html = open(url, 'rb')
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.find('div', class_="list-wrap"))
        # print(soup.find('ul', id="house-lst"))
        context_html = soup.find('ul', id="house-lst")
        context_soup = BeautifulSoup(str(context_html), 'html.parser')
        all = context_soup.find_all('li')
        # print(all)

        for a in all:
            a_soup = BeautifulSoup(str(a), 'html.parser')
            # print(a_soup.find('a', name="selectDetail").text)
            print(a_soup.find('h2').text.strip() + "绿色")
            name = a_soup.find('h2').text.strip() + "绿色"
            print(a_soup.find('div', class_="contact").text.strip())
            contact = a_soup.find('div', class_="contact").text.strip()
            j = j + 1
            sheet.put_cell(j, 0, 1, name, 0)
            sheet.put_cell(j, 1, 1, contact, 0)
            print(j)
    wb = copy(book)
    wb.save(xlsfile)


# pachong(".html", 1, 34)


def downloadhtmlwherefrom(url_str, wherefrom):
    html = getHtml(url_str)
    saveHtml(wherefrom, html)
    print(wherefrom + " 下载成功")


# downloadhtmlwherefrom("https://m.anjuke.com/long/tycoon/xinluo/","anjuke")
def pachong_anjuke(html_filename):
    xlsfile = 'anjuke.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()
    print(sheet_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    print(ncols)
    j = -1

    html = open(html_filename, 'rb')
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.find('div', class_="list-wrap"))
    # print(soup.find('ul', id="house-lst"))
    # context_html = soup.find('ul', id="house-lst")
    # context_soup = BeautifulSoup(str(html), 'html.parser')
    all = soup.find_all('div', class_="broker-info")
    # print(all)

    for a in all:
        a_soup = BeautifulSoup(str(a), 'html.parser')
        # print(a_soup.find('a', name="selectDetail").text)

        if a_soup.find('a', class_="campany text-over"):
            print(a_soup.find('span', class_="name text-over").text.strip() + "_" + a_soup.find('a',
                                                                                                class_="campany text-over").text.strip())
            name = a_soup.find('span', class_="name text-over").text.strip() + "_" + a_soup.find('a',
                                                                                                 class_="campany text-over").text.strip()
        else:
            print(a_soup.find('span', class_="name text-over").text.strip() + "_")
            name = a_soup.find('span', class_="name text-over").text.strip() + "_"
        print(a_soup.find('a').attrs['href'].strip()[4:])
        contact = a_soup.find('a').attrs['href'].strip()[4:]
        j = j + 1
        sheet.put_cell(j, 0, 1, name, 0)
        sheet.put_cell(j, 1, 1, contact, 0)
        print(j)

        wb = copy(book)
        wb.save(xlsfile)


# pachong_anjuke("anjuke.html")

def pachong_ganji(url, start, end):
    xlsfile = 'ganji.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()
    print(sheet_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    print(ncols)
    j = -1
    for i in range(start, end + 1):
        url_real = url + str(i)
        html = urllib.request.urlopen(url_real).read()
        soup = BeautifulSoup(html, 'html.parser')
        all = soup.find_all('a', class_="f-list-item")
        # print(all)

        for a in all:
            a_soup = BeautifulSoup(str(a), 'html.parser')
            name = a_soup.find('span', class_="name").text.strip() + "_" + a_soup.find('div',
                                                                                       class_="bc-name").text.strip()
            print(name)
            contact_url = a_soup.find('a').attrs['href'].strip()
            contact_pre_url = "http://longyan.ganji.com"
            contact_url = contact_pre_url + contact_url
            html = urllib.request.urlopen(contact_url).read()
            soup = BeautifulSoup(html, 'html.parser')
            contact = soup.find('title').text.strip()
            contact = re.findall(r'([0-9]+)', contact)[0]
            print(contact)
            j = j + 1
            sheet.put_cell(j, 0, 1, name, 0)
            sheet.put_cell(j, 1, 1, contact, 0)
            print(j)
    wb = copy(book)
    wb.save(xlsfile)


# ganji_url = "http://longyan.ganji.com/fang/agent/o"
# pachong_ganji(ganji_url, 1, 15)

def pachong_58(url, start, end):
    xlsfile = '58.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()
    print(sheet_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    print(ncols)
    j = -1
    for i in range(start, end + 1):
        url_real = url + str(i)
        html = urllib.request.urlopen(url_real).read()
        soup = BeautifulSoup(html, 'html.parser')
        house_list_wrap = soup.find('ul', class_="house-list-wrap")
        soup = BeautifulSoup(str(house_list_wrap), 'html.parser')
        all = soup.find_all('li')
        # print(all)

        for a in all:
            a_soup = BeautifulSoup(str(a), 'html.parser')
            link = a_soup.find('a', class_="link").attrs['href'].strip()
            name = a_soup.find('span', class_="name").text.strip() + "_" + a_soup.find('p',
                                                                                       class_="compony").text.strip()
            print(name)
            # print(link)
            html = urllib.request.urlopen("https:" + link).read()
            soup = BeautifulSoup(html, 'html.parser')
            index = str(html).find("brokerId = ")
            brokerId = str(html)[index + 12:index + 19]
            broker_url = "https://broker.58.com/api/encphone?cityId=6752&brokerId=" + brokerId
            contact = json.loads(urllib.request.urlopen(broker_url).read())["data"]
            # print(contact)

            j = j + 1
            sheet.put_cell(j, 0, 1, name, 0)
            sheet.put_cell(j, 1, 1, contact, 0)
            print(j)
    wb = copy(book)
    wb.save(xlsfile)


# url = "https://broker.58.com/ly/list/pn"
# pachong_58(url, 1, 23)

def pachong_0597ok(url, start, end):
    xlsfile = '0597OK.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()
    print(sheet_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    print(ncols)
    j = -1
    for i in range(start, end + 1):
        url_real = url + str(i)
        print(url_real)
        html = urllib.request.urlopen(url_real).read()
        soup = BeautifulSoup(html, 'html.parser')
        house_list_wrap = soup.find('div', class_="list_mk")
        soup = BeautifulSoup(str(house_list_wrap), 'html.parser')
        all = soup.find_all('li')
        # print(all)

        for a in all:
            a_soup = BeautifulSoup(str(a), 'html.parser')
            if a_soup.find('h3', ):
                name = a_soup.find('h3', ).text.strip()
                name_array = name.split('-')
                # print(name_array)
                name = name_array[-1] + "_" + name_array[0]
                print(name)
                contact = a_soup.find('p').text.strip().replace("热线：", "").split(",")
                print(contact)

                j = j + 1
                sheet.put_cell(j, 0, 1, name, 0)
                sheet.put_cell(j, 1, 1, contact[0], 0)
                if len(contact) > 1:
                    sheet.put_cell(j, 2, 1, contact[1], 0)

                print(j)
    wb = copy(book)
    wb.save(xlsfile)


# url = "http://www.0597ok.com//companym.asp?t=2&PageNo="
# pachong_0597ok(url, 1, 291)

def pachong_loupanzidian(url, start, end):
    global set
    xlsfile = 'loupanzidian.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()
    print(sheet_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    print(ncols)
    j = -1
    set = set()
    for i in range(start, end + 1):
        url_real = url + str(i)
        print(url_real)
        html = urllib.request.urlopen(url_real).read()
        soup = BeautifulSoup(html, 'html.parser')
        house_list_wrap = soup.find('div', class_="list-wrap")
        soup = BeautifulSoup(str(house_list_wrap), 'html.parser')
        all = soup.find_all('li')
        # print(all)

        for a in all:
            a_soup = BeautifulSoup(str(a), 'html.parser')
            if a_soup.find('span', class_="nameEllipsis"):
                name = a_soup.find('span', class_="nameEllipsis").text.strip()
                set.add(name)
                print(name)

    for a in set:
        j = j + 1
        sheet.put_cell(j, 0, 1, a, 0)
        print(j)
    wb = copy(book)
    wb.save(xlsfile)


# url = "http://www.yongxinjia.com/esf/?page="
# pachong_loupanzidian(url, 1, 568)

def pachong_zongjia_min(url, keyWord):
    global set
    xlsfile = 'data.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()
    print(sheet_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    print(ncols)
    j = -1
    set = set()
    start = 1
    url_real = url + str(keyWord)
    print(url_real)
    html = urllib.request.urlopen(quote(url_real, string.printable)).read()
    html = html.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    page_box = soup.find('div', class_="paging-box page-box house-lst-page-box")
    # print(page_box)
    soup = BeautifulSoup(str(page_box), 'html.parser')
    all = soup.find_all('a')
    soup = BeautifulSoup(str(all[-2]), 'html.parser')
    end = soup.find('a').text.strip()
    print(end)
    end = int(end) + 1
    # print(end)

    for i in range(start, end + 1):
        url_real = url + str(keyWord) + "&page=" + str(i)
        print(url_real)
        html = urllib.request.urlopen(quote(url_real, string.printable)).read()
        soup = BeautifulSoup(html, 'html.parser')
        house_list_wrap = soup.find('div', class_="list-wrap")
        soup = BeautifulSoup(str(house_list_wrap), 'html.parser')
        all = soup.find_all('li')
        # print(all)

        for a in all:
            # print(a)
            a_soup = BeautifulSoup(str(a), 'html.parser')
            info_panel = a_soup.find('div', class_="info-panel")
            # print(info_panel)
            a_soup = BeautifulSoup(str(info_panel), 'html.parser')
            href = a_soup.find('a').attrs['href'].strip()
            house_url = "http://www.yongxinjia.com" + href
            # print(house_url)
            num = a_soup.find('span', class_="num").text.strip()
            print(str(num) + "万")
            price_pre = a_soup.find('div', class_="price-pre").text.strip()
            print(price_pre)
            j = j + 1
            sheet.put_cell(j, 0, 1, num, 0)
            sheet.put_cell(j, 1, 1, price_pre, 0)
            sheet.put_cell(j, 2, 1, house_url, 0)

    wb = copy(book)
    wb.save(xlsfile)


# url = "http://www.yongxinjia.com/esf?keyWord="
# pachong_zongjia_min(url, "")

def pachong_fjlyfdc(url, start, end):
    global set
    xlsfile = 'fjlyfdc.xls'
    book = xlrd.open_workbook(xlsfile)
    sheet_name = book.sheet_names()
    print(sheet_name)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print(nrows)
    print(ncols)
    j = -1
    for i in range(start, end + 1):
        url_real = url + str(i)
        print(url_real)
        html = urllib.request.urlopen(url_real).read()
        soup = BeautifulSoup(html, 'html.parser')
        table_responsive = soup.find('div', class_="table-responsive")
        soup = BeautifulSoup(str(table_responsive), 'html.parser')
        all = soup.find_all('tr')
        del all[0]
        # print(all)

        for a in all:
            a_soup = BeautifulSoup(str(a), 'html.parser')
            td_all = a_soup.find_all('td')
            name = td_all[0].text.strip()
            num = td_all[1].text.strip()
            j = j + 1
            sheet.put_cell(j, 0, 1, name, 0)
            sheet.put_cell(j, 1, 1, num, 0)

    wb = copy(book)
    wb.save(xlsfile)


url = "http://www.fjlyfdc.com.cn/Html/CYZT/index/employee?pagenumber="
pachong_fjlyfdc(url, 1, 114)
