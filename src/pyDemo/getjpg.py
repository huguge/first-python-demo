#coding=utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    
#     uniCodehtml = html.decode("gbk")
#     utf8html = uniCodehtml.encode("UTF-8")
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imgList = re.findall(imgre,html)
    x = 0
    for imgurl in imgList:
        urllib.urlretrieve(imgurl, 'C:\Users\80s\Desktop\File\python-file\%s.jpg' % x)
        x+=1

html = getHtml("http://tieba.baidu.com/p/3936526825")

print getImg(html)
