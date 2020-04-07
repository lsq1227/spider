import re
import time

import chardet
import requests



index_url = 'https://www.zhihu.com/'
cookie = ''
head = {
"authority":"www.zhihu.com",
"method":"GET",
"path":"/",
"scheme":"https",
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.9",
"cache-control":"max-age=0",
"cookie":cookie,
"sec-fetch-dest":"document",
"sec-fetch-mode":"navigate",
"sec-fetch-site":"none",
"sec-fetch-user":"?1",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
#
# index_res = requests.get(index_url,headers= head)
# session_token = re.findall('\?session_token=(.*?)&',index_res.text)[0]
#
# print(session_token)

i = 1
while True:
    api_url = f'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=292a04924d7f522e816068842491b48&desktop=true&page_number={i}&limit=6&action=down&after_id=5&ad_interval=-1'
    res = requests.get(api_url,headers=head)
    print(res.text)
    i = i + 1
    time.sleep(2)












