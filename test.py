import urllib.request
import re
import json

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getFinance(html):
    reg = r'href="(.*(finance).*\.html)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist  
  
html = getHtml("http://www.sina.com.cn/")
html = html.decode('gbk')
data=getFinance(html)
jdata=json.dumps(data)
f = open('sinadata.txt','w+')
f.write(jdata)
f.close()



print (jdata)