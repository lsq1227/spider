## jd系的爬虫：

评论抓取：定义ua，找到接口，获取响应，解析结果。

销量搜索：定义ua，找到接口，获取响应，解析结果。



## tb系的爬虫：

和jd不一样的，淘宝必须获取到cookie才返回数据。且数据在返回的html里面夹杂了响应数据。

请求前获取cookie，可以在redis写入cookie池，过期周期为一日。

找到搜索接口，获取响应，正则解析。



问大家sign参数解析：

首先贴上一个问大家的接口：[接口连接](https://h5api.m.taobao.com/h5/mtop.taobao.social.feed.aggregate/1.0/?jsv=2.4.1&appKey=12574478&t=1585878352000&sign=7dcea76df402496ed30e082f46faa6dc&api=mtop.taobao.social.feed.aggregate&v=1.0&ecode=0&timeout=300000&timer=300000&AntiCreep=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22cursor%22:%221%22,%22pageNum%22:%221%22,%22pageId%22:24501,%22env%22:1,%22bizVersion%22:0,%22params%22:%22%7B%5C%22refId%5C%22:%5C%22540672068569%5C%22,%5C%22namespace%5C%22:1,%5C%22pageNum%5C%22:1,%5C%22pageSize%5C%22:10%7D%22%7D](https://h5api.m.taobao.com/h5/mtop.taobao.social.feed.aggregate/1.0/?jsv=2.4.1&appKey=12574478&t=1585878352000&sign=7dcea76df402496ed30e082f46faa6dc&api=mtop.taobao.social.feed.aggregate&v=1.0&ecode=0&timeout=300000&timer=300000&AntiCreep=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data={"cursor":"1","pageNum":"1","pageId":24501,"env":1,"bizVersion":0,"params":"{\"refId\":\"540672068569\",\"namespace\":1,\"pageNum\":1,\"pageSize\":10}"}))

然后来看他的参数

1. jsv: 2.4.1
2. appKey: 12574478
3. t: 1585878500662
4. sign: a83167bed53b46c924d9cf06e73fd1a3
5. api: mtop.taobao.social.feed.aggregate
6. v: 1.0
7. ecode: 0
8. timeout: 300000
9. timer: 300000
10. AntiCreep: true
11. type: jsonp
12. dataType: jsonp
13. callback: mtopjsonp1
14. data：{"cursor":"1","pageNum":"1","pageId":24501,"env":1,"bizVersion":0,"params":"{\"refId\":\"540672068569\",\"namespace\":1,\"pageNum\":1,\"pageSize\":10}"}



其中只有sign和t是每次改变的。

就得出 sign为参数加密   t 为时间戳。

打开调试后找到加密方式

 j = h(d.token + "&" + i + "&" + g + "&" + c.data)

j  =  sign

h = function()

d.token = 返回结果里面cookie的 _m_h5_tk值

i = 时间戳

g = 12574478 固定值

c.data = 页码以及商品id的参数



将这些拼接起来后 就可以得到sign   h函数在我的test.js里面有源码。

第一次请求还是请求https://h5api.m.taobao.com/h5/mtop.taobao.social.feed.aggregate/1.0/这个接口，什么也不用带直接会返回一个_m_h5_tk，拿到之后开始拼接cookie进行一系列的参数拼接。

拼接完成之后的url参数，最好去比对一下，参数很容易出错。







## 知乎爬虫

知乎的接口是一个经典的伪加密。

在请返回结果里面带有一串加密参数session_token字段

本来以为是一个js加密，反复测试后，他竟然是个伪加密。只要带一个就可以一直访问。目前观察到的周期为一天。所以在请求之前只要请求了知乎官网就可以直接无限请求（知乎是有cookie验证的，每次必须提前登陆才能拿到数据，cookie验证同理tb的cookie验证。）



## 头条爬虫

先贴一个链接[链接](https://www.toutiao.com/c/user/article/?page_type=1&user_id=102107972930&max_behot_time=0&count=20&as=A185BED8CA9A847&cp=5E8ABA080457EE1&_signature=WVIiDgAgEBDJraClGUiBAFlTYxAAAfZvsjcdJBrm3BQ5Lcwwi8.485qNftHd93ZpKQiE-zfWyXzY-3k1VxciWZv2slFIaf19YHOr6jP2GTAoBlcbAo.-dAZze4KrO3ZIvGI)

1. page_type: 1
2. user_id: 102107972930
3. max_behot_time: 0
4. count: 20
5. as: A185BED8CA9A847
6. cp: 5E8ABA080457EE1
7. _signature: WVIiDgAgEBDJraClGUiBAFlTYxAAAfZvsjcdJBrm3BQ5Lcwwi8.485qNftHd93ZpKQiE-zfWyXzY-3k1VxciWZv2slFIaf19YHOr6jP2GTAoBlcbAo.-dAZze4KrO3ZIvGI

这些是参数 首先确定  变化的是 as ，cp ， _signature。这三个参数。

首先破解as，cp的参数：

找到他对应的js加密文件，尝试使用node环境去调用js。遇到了找不到md5加密的问题。所以使用python去翻译他的js代码。在头条文件夹里面get_sign函数仿写头条的js加密方式。

as，cp参数破解成功！

接下来就是对signture的破解，因为他的js里面带有window对象和local对象。这些都是浏览器自带的对象用nodejs没法模拟这些对象，所以用无头浏览器进行调用js获得他的结果。执行的js代码为window.byted_acrawler.sign(）。在我的头条爬虫里面，有代码。

大概代码思路已经整理出来了，接下来就是解析，他的返回是json格式，非常好解析。