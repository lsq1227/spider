import hashlib
import json
import time
import requests
from selenium import webdriver

def get_sign():
    t = int(time.time())
    e = str('%X' % t)
    m1 = hashlib.md5()
    m1.update(str(t).encode(encoding='utf-8'))
    i = str(m1.hexdigest()).upper()
    o = i[0:5]
    n = i[-5:]
    a = ''
    r = ''
    for s in range(0, 5):
        a += o[s] + e[s]
        r += e[s + 3] + n[s]
    eas = 'A1' + a + e[-3:]
    ecp = e[0:3] + r + 'E1'
    return {'as': eas, 'cp': ecp}




class selenium_nign():
    def __init__(self,url):
        self.url = url
        driver = webdriver.FirefoxOptions()
        # driver.add_argument('-headless')
        self.driver = webdriver.Firefox(firefox_options=driver)
        self.driver.get(self.url)
    def nign(self,time=0):
        nign = self.driver.execute_script('''return utils.tacSign("/c/user/article/");''')
         #通过这里来获取，第一个参数为作者id，第二个参数就是前面讲的max_behot_time参数
        return nign
    def cookie(self,blok=0):
         #这里获取cookie，头条对id也有加密，正常的session获取的会话似乎没办法通过
        if blok:
            self.driver.get(self.url)
        cookies = self.driver.get_cookies()
        cookie = [item['name'] + "=" + item['value'] for item in cookies]
        cookiestr = '; '.join(item for item in cookie)
        return cookiestr
    def sclock(self):
        self.driver.close()
se = selenium_nign(url='https://www.toutiao.com/c/user/102107972930/#mid=1607559076471816')

while True:
    ascp = get_sign()
    print(se.cookie())
    print(se.nign())
    print(ascp['as'])
    print(ascp['cp'])

    url = f'https://www.toutiao.com/c/user/article/?page_type=1&user_id=102107972930&max_behot_time=0&count=20&as={ascp["as"]}&cp={ascp["cp"]}&_signature={se.nign()}'
    print(url)

    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'referer': 'https://www.toutiao.com/c/user/102107972930/',
        'cookie': se.cookie(),
    }
    res = requests.get(url,headers=head).text
    js = json.loads(res)
    if js['data'] != []:
        break
    print(res)
    time.sleep(5)








