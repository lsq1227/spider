import re
import time
import requests
import random
import json



user = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11Opera 11.11",
    "User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11 ",
    "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
]

def get_comm(id,page):
    head = {
        'Host': 'sclub.jd.com',
        'Referer': 'https://item.jd.com/555561.html',
        'User-Agent': random.choice(user),
        'Connection': 'keep-alive',
        'TE': 'Trailers'
    }
    url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={id}&score=0&sortType=6&page={page}&pageSize=10&isShadowSku=0&rid=0&fold=1'
    #默认按时间排序
    res = requests.get(url, headers=head).text
    temp = re.findall('fetchJSON_.*?\((.*?)\);',res)[0]
    temp = temp.replace('None',"'None'").replace('True',"'True'").replace('False',"'False'")
    json_info = json.loads(temp)
    return json_info












