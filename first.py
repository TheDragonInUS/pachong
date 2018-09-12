import requests

response = requests.get("http://www.baidu.com")

print(response.status_code)
with open("baidu.html", "w") as f:
    f.write(response.content.decode())

