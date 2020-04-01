

import json
import os
import re
import time
import requests, random

#输入自己的cookie
cookie = ''





head = {
    "authority":"s.taobao.com",
    "Connection":"close",
    "method":"GET",
    "path":"/search?q=%E5%9C%B    0%E6%BC%8F&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc",
    "scheme":"https",
    "accept":"ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9",
    "cache-control":"max-age=0",
    "cookie":cookie,
    "referer":"https://www.taobao.com/",
    "sec-fetch-dest":"document",
    "sec-fetch-mode":"navigate",
    "sec-fetch-site":"same-origin",
    "sec-fetch-user":"?1",
    "upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}

def get_info(key,i):
    if i == '1':
        url = f'https://s.taobao.com/search?q={key}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&s=0'
    else:
        url = f'https://s.taobao.com/search?q={key}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&s={(int(i)-1)*44}'
    res = requests.get(url, headers=head).text
    try:
        img = re.findall('"pic_url":"(.*?)",', res)
        shop_name = re.findall('"nick":"(.*?)",', res)
        id = re.findall('"nid":"(.*?)",', res)
        test = re.findall('"nid":"(.*?)",', res)[0]
    except:
        input('cookie验证过期，请重新验证cookie！\n')
        res = requests.get(url, headers=head).text
        img = re.findall('"pic_url":"(.*?)",', res)
        shop_name = re.findall('"nick":"(.*?)",', res)
        id = re.findall('"nid":"(.*?)",', res)
    res_lsit = []
    for i in range(0, len(img)):
        res_lsit.append({'shop_name':shop_name,'id':id,'img':img})
    return res_lsit






