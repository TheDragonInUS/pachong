"""

保定新闻 -- 爬虫

"""
import requests
from lxml import etree


def write_file(fun):

    def write_file(i):
        a = fun(i)
        with open("xinxi.txt", 'a') as f:
            massage = a[0] + "\t" + a[1] + "\t" + "http://www.bd.gov.cn/"+a[2] + "\r\n"
            f.write(massage)

    return write_file


url = "http://www.bd.gov.cn/index.do?view=jrbdlist&ccid=173&cpid=172&page="


def my_request(url1, page):
    response = requests.get(url1 + str(page))
    content = response.content.decode()
    content = etree.HTML(content)

    page_end = content.xpath(
        '''//table[@class="list_page"]//tr[1]/td[2]/span[2]/text()''')[0]

    @write_file
    def page_message(i):
        tr = str(i)
        time_xpath = '''//table[@class="list"]//tr[%s]/td[2]/text()''' % tr
        time_push_xpath = '''//table[@class="list"]//tr[%s]/td[1]/a[1]/text()''' % tr
        href_xpath = '''//table[@class="list"]//tr[%s]/td[1]/a/@href''' % tr
        time_push = content.xpath(time_xpath)[0]
        title = content.xpath(time_push_xpath)[0]
        href = content.xpath(href_xpath)[0]
        print(title, time_push, href)  # 结束的页数
        return title, time_push, href

    for i in range(1, 15):
        page_message(i)

    return page_end


a = my_request(url, 1)
print(a)

for i in range(1, int(a)):
    import time
    time.sleep(0.05)
    my_request(url, i)


