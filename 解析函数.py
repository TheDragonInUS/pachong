from lxml import etree

html = etree.parse("./母校.html")
print(html)
result = html.xpath("""/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[@id="li1"]/a[1]""")
print(len(result))
print(result)



# from lxml import etree
# html = etree.parse('hello.html')
# print(html)
# result = etree.tostring(html, pretty_print=True)
# print(result)