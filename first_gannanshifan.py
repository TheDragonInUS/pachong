import requests
from lxml import etree


def xinxi_list():

    url_list = []
    url_get = "http://www.gnnu.cn/html/63/"
    url_list.append(url_get)
    for i in range(2, 126):
        start_url = url_get + str(i) + ".htm"
        url_list.append(start_url)
    return url_list


def get_content(url_get):

    response = requests.get(url=url_get)
    content = response.content.decode("gb18030")
    content = etree.HTML(content)
    content_title = content.xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[@id="li1"]/a[1]/@title')
    # content = etree.tostring(content).decode("gb2312")
    return content_title


def url_get(url_list):
    for i in url_list:
        print("working in %s" % i)
        f_title = get_content(i)
        for q in f_title:
            with open("母校新闻.txt", "a") as f:
                f.write(q+"\r\n")


xinxi_list = xinxi_list()
url_get(xinxi_list)


