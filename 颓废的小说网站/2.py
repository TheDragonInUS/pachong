import requests
response = requests.get('http://www.555x.org/home/down/txt/id/45279')
print(response.content)