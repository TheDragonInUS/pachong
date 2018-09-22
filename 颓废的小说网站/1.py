import requests
from lxml import etree

url = "http://www.555x.org/"


def qingqiu(url):
    """
    获取第一链接
    :param url:
    :return:
    """

    message = {}
    response = requests.get(url=url)
    content = response.content.decode()
    content = etree.HTML(content)

    # classify = content.xpath("/html/body/div[2]/div[6]/div[1]/div[1]/ul[1]/li[1]/a[1]")
    for i in range(1, 11):
        details = {}
        cla = '''//div[@class="fenlei"]/ul[1]/li[%s]/a[2]/text()''' % i
        name = content.xpath(cla)[0]

        hr = '''//div[@class="fenlei"]/ul[1]/li[%s]/a[2]/@href''' % i
        href = content.xpath(hr)[0]

        da = '''//div[@class="fenlei"]/ul[1]/li[%s]/span[@class="rr3"]/font[1]/text()''' % i
        date = content.xpath(da)[0]

        au = '''//div[@class="fenlei"]/ul[1]/li[%s]/span[@class="rr5"]/text()''' % i
        author = content.xpath(au)[0]

        details["name"] = name
        details["author"] = author
        details["date"] = date
        details["url"] = href

        message[str(i)] = details

    print(message)

    return message


message = qingqiu(url)


import json
with open("data.json", "w") as f:
    json.dump(message, f)


print(len(message))


def down_0():
    """
    提取第一次url
    :return:
    """
    a = []
    for i in range(1, 11):
        url1 = message[str(i)]["url"]
        # print(url)
        response1 = requests.get(url=url1)
        content1 = response1.content.decode()
        content1 = etree.HTML(content1)
        # print(content1)
        url_down1 = content1.xpath('''//div[@class="downbox"]/a[1]/@href''')
        # print(url_down1[0])
        print("获取第一层，第%s链接" % str(i))
        a.append(url_down1[0])

    print(a)
    return a


url_0_list = down_0()


def down_1(url_list):
    a = []
    for i in range(0, len(url_list)):
        response2 = requests.get(url_list[i])
        content2 = response2.content.decode()
        content2 = etree.HTML(content2)
        url_down2 = content2.xpath('''//div[@class="shuji"]/ul[1]/li[2]/a[1]/@href''')
        print("获取第二层，第%s链接" % str(i+1))
        a.append(url_down2[0])

    print(a)
    return a


url_1_list = down_1(url_0_list)


import multiprocessing


def down_2(url_1_list,nu=0,):
    response2 = requests.get(url_1_list[nu])
    with open(str(nu)+".txt", "wb") as f:
        f.write(response2.content)


p0 = multiprocessing.Process(target=down_2, args=(url_1_list, 0))
p1 = multiprocessing.Process(target=down_2, args=(url_1_list, 1))
p2 = multiprocessing.Process(target=down_2, args=(url_1_list, 2))
p3 = multiprocessing.Process(target=down_2, args=(url_1_list, 3))
p4 = multiprocessing.Process(target=down_2, args=(url_1_list, 4))
p5 = multiprocessing.Process(target=down_2, args=(url_1_list, 5))
p6 = multiprocessing.Process(target=down_2, args=(url_1_list, 6))
p7 = multiprocessing.Process(target=down_2, args=(url_1_list, 7))
p8 = multiprocessing.Process(target=down_2, args=(url_1_list, 8))
p9 = multiprocessing.Process(target=down_2, args=(url_1_list, 9))
p0.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
p8.start()
p9.start()







