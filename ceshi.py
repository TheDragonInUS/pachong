from lxml import etree

html = '''
<h1 class="header">登录</h1>
<form action="/login" method="post">
    <label for="username">用户: </label><input type="text" name="username" />
    <label for="password">密码：</label><input type="password" name="password" />
    <input type="submit" value="Submit" />
</form>'''

# 生成DOM
dom = etree.HTML(html)

# 取内容 /text()
contents = dom.xpath('//h1[@class="header"]/text()')
print(contents)

# 取属性 /@attrib
attribs = dom.xpath('//form/label[@for="username"]/@for')
print(attribs)