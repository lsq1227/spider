import requests
import re
import base64
import io
from lxml import etree
from fontTools.ttLib import TTFont
url = 'https://ph0101.cn.china.cn/contact-information/'
res = requests.get(url).text
print(res)
base64_str = re.search("base64,(.*?)'\)",res).group(1)
b = base64.b64decode(base64_str)
font = TTFont(io.BytesIO(b))
test = {
    '12663173': '0',
    '126983':'1',
    '12610656': '2',
    '14012694': '3',
    '1269460': '4',
    '12698156': '5',
    '126111181': '6',
    '12611177': '7',
    '1265483': '8',
    '12615-1': '9'
}
font.saveXML('ts.xml')
bestcmap = font.getGlyphOrder()[1:]
with open('ts.xml','r') as f:
    t = f.read()
t = t.replace('<?xml version="1.0" encoding="UTF-8"?>','')
print(t)
root = etree.XML(t)
dic = {}
s = root.xpath('//CharString')[1:]

for i in s:
    temp = i.xpath('./text()')[0].split()
    name = i.xpath('./@name')[0].replace('uni','')
    fon = temp[0] + temp[1] + temp[2]
    dic[name] = fon
r = etree.HTML(res)
tel = r.xpath('string(//span[@class="rrdh secret"])')
c = tel.encode('utf-8')
dc = {}
for ka,va in test.items():
    for ka1, va1 in dic.items():
        if ka == va1:
            # &#x100c4;
            ka1 = f'&#x{ka1};'
            dc[ka1] = va
for k,v in dc.items():
    print(k,v)
response_ = res
# 循环处理后的字体映射表
for k, v in dc.items():
    # 拼接页面中完整的乱码字符
    uni_font = k
    # 判断乱码字符是否存在抓取下来的网页内容中
    if uni_font in response_:
        # 如果存在，将其替换为解码后的汉字
        response_ = response_.replace(uni_font, dc[k])
r = etree.HTML(response_)
tel = r.xpath('string(//span[@class="rrdh secret"])')
print(tel)



