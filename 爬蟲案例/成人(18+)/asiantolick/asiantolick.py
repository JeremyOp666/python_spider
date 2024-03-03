import requests
from parsel import Selector
import os
url = "https://asiantolick.com/post-15859/-cosdeluxe-%E3%82%B3%E3%82%B9%E3%83%97%E3%83%AC%E3%83%92%E3%83%A1%E3%82%AB%E3%83%AF%E3%83%A6%E3%82%A6%E3%83%8A-31p-"

headers = {
    'authority': 'asiantolick.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'referer': 'https://asiantolick.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Avast Secure Browser";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Avast/121.0.0.0',
}

response = requests.get(
    url,
    headers=headers
)

selector = Selector(text=response.text)

images = selector.css('div.spotlight-group img::attr(src)').getall()
name = selector.css('div.spotlight-group img::attr(alt)').extract_first()



for image in images:
    filename = image.split('/')[-1]
    filename = filename.split("&")[0]
    print(filename)
    if not os.path.exists(name):
        os.makedirs(name)
    img_content = requests.get(url=image).content
    print("下載完成" + filename)
    with open(f"{name}/" + filename, mode='wb') as f:
        f.write(img_content)
print("下載全部完成")

