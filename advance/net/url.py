import requests

response = requests.get('https://www.imooc.com')
content = str(response.content, encoding='utf-8') # ==> 打印具体内容
print(content)