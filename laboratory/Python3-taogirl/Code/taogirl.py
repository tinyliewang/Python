import os
import threading
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

browserPath = 'C:\\Users\\user\\Desktop\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
homePage = 'https://www.taobao.com/markets/mm/mmku?'
outputDir = 'photo/'
parser = 'html5lib'

driver = webdriver.PhantomJS(executable_path=browserPath)
driver.get(homePage)
bsObj = BeautifulSoup(driver.page_source, parser)
girlsList = driver.find_elements_by_class_name('cons_li') #获得主页上所有妹子的姓名、所在城市、身高、体重等信息
#print(girlsList[0].text.split('\n'))
#girlsUrl = bsObj.find_all("a",{"href": re.compile("\/.*\/.*\/homepage\?(userId=)[0-9]")})  #解析出妹子的个人主页地址等信息
imgs = bsObj.find_all("img", {"src": re.compile(".*\.jpg")})
print(imgs)

#//da.taobao.com/n/author/homepage?spm=5679.126511.640858.37.MtXHaM&amp;userId=728310618