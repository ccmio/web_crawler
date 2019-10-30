import requests
import re
from requests import Request, Session
from lxml import etree
from bs4 import BeautifulSoup
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
#

# files = {
#     'file': open('favicon.ico', 'rb')
# }
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key + '=' + value)

# s = requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# url = 'http://httpbin.org/post'
# data = {
#     'name': 'cc'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0'
# }
# s = Session()
# req = Request('POST', url=url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)

# content = '''asdlfjals;dfjl;djf Hello 13
#           4 5678 World_This is a
#           Regex Demodla;fd f'''
# content = re.sub('\d+', '', content)
# print(content)

# text = '''
# <div>
# <ul>
# <li class="item-O"><a href="link1.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </ul>
# </div>
# '''
# html = etree.HTML(text)
# print(type(html))
# result = etree.tostring(html)
# print(type(result))
# print(result.decode('utf8'))
#
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//@href')
# print(result)

# html = """
# <html><head><title>The Dormouse’ s story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse’s story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><! -- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> ;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html, 'lxml')
# # print(soup.prettify())
# print(soup.find_all(attrs={'class': 'sister'}))

# db = pymysql.connect(host='localhost', user='root', password='4651708', port=3306, db='spiders')
# cursor = db.cursor()
# data = {
#     'id': '0589',
#     'name': '张涛',
#     'age': 19
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s']*len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
# try:
#     cursor.execute(sql, tuple(data.values()))
#     db.commit()
#     print('success')
# except:
#     db.rollback()
#     print('failed')
# db.close()

# db = pymysql.connect(host='localhost', user='root', password='4651708', port=3306, db='spiders')
# cursor = db.cursor()
# try:
#     cursor.execute('UPDATE students SET age = %s WHERE name = %s', 28, '张涛')
#     db.commit()
#     print('ok')
# except:
#     db.rollback()
#     print('fail')
# db.close()
#
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url, browser.get_cookie(name=''), browser.page_source)
# finally:
#     browser.close()

browser = webdriver.PhantomJS()
browser.get('https://www.baidu.com')
WebDriverWait(browser, 5)
print(browser.current_url)
browser.close()