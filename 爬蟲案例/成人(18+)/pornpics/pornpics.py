import requests
from parsel import Selector
import os
import re

def check_url(url):
    pattern = r'^https://www.pornpics.com/.+/galleries/.+$'
    if re.match(pattern, url):
        print("URL符合模式:https://www.pornpics.com/XXX/galleries/XXXXXXX")
    else:
        print("URL不符合模式必須是https://www.pornpics.com/XXX/galleries/XXXXXXX")
        exit()

url = 'https://www.pornpics.com/XXX/galleries/XXXXXXX'
check_url(url)

resp = requests.get(url)
selector = Selector(text=resp.text)
title = selector.xpath('//ul[@id="tiles"]/li/a/img/@alt').extract_first()
urls = selector.css('li.thumbwook a.rel-link::attr(href)').getall()
filename = url.split("/")[-1]


for url in urls:
    filename = url.split("/")[-1]
    if not os.path.exists(title):
        os.makedirs(title)
    img_content = requests.get(url=url).content
    print("下載完成" + filename)
    with open(f"{title}/" + filename, mode='wb') as f:
        f.write(img_content)
print("下載全部完成")
