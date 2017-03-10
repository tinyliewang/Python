#coding=utf-8
import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'http://.+\.jpg{1}'
    imgre = re.compile(reg)
    imgre,html = imgre,html.decode('utf-8')
    imglist = re.findall(imgre,html)
    return imglist

html = getHtml("http://tieba.baidu.com/p/4911397526")

print (getImg(html))
