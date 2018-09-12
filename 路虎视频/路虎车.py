import requests
from lxml import etree

url = "https://sou.autohome.com.cn/shipin?error=0&entry=45&q=%c2%b7%bb%a2&page=1"


def xinxi_list():
    """
    分析网页：进行新闻网页分析，获取爬虫信息
    :return: 路由列表
    """
    url_list = []
    url_get = "https://sou.autohome.com.cn/shipin?error=0&entry=45&q=%c2%b7%bb%a2&page="
    url_list.append(url_get)

    for i in range(1, 10):
        print(i)
        start_url = url_get + str(i)
        url_list.append(start_url)
    return url_list


def get_content(url_get):
    """
    获取的函数文件
    :param url_get: 参数
    :return: 返回新闻列表
    """
    response = requests.get(url=url_get)
    content = response.content.decode("gb18030")
    content = etree.HTML(content)
    content_title = content.xpath('/html[1]/body[1]/div[3]/div[1]/div[2]/div[1]/div[1]/ul[1]/li/a/@href')
    # content = etree.tostring(content).decode("gb2312")
    return content_title


def url_get(url_list):
    """

    :param url_list: 文件写入
    :return: none
    """
    for i in url_list:
        print("working in %s" % i)
        f_url = get_content(i)
        print(f_url)
        for q in f_url:
            with open("./视频链接.txt", "a") as f:
                f.write(q+"\r\n")


xinxi_list = xinxi_list()
print(url_get(xinxi_list))

# response = requests.get(url+"1")
# print(response.status_code)
# print(response.content.decode("gb18030"))
