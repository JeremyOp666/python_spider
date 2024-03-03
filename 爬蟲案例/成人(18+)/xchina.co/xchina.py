import cloudscraper
from lxml.html import fromstring
import os, sys, re
import requests
from parsel import Selector
if not os.path.exists('img'):
    os.makedirs('img')
url = 'https://xchina.co/photo/id-xxxxxxxxxx.html'
scraper = cloudscraper.create_scraper(browser={
    'browser': 'firefox',
    'platform': 'windows',
    'mobile': False
})
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"
}
resp = scraper.get(url, headers=headers).text
selector = Selector(text=resp)
anchor_elements = selector.css('div.pager a')
href_attributes = anchor_elements.xpath('@href').extract()
for href in href_attributes:
    scraper=cloudscraper.create_scraper(browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        })
    resp = scraper.get(f'https://xchina.co{href}', headers=headers).text
    img_info = re.findall(r'<a href="(.*?)"><figure class="item" style="padding-bottom: .*?; background-image: url\(\'.*?\'\);"><img class="cr_only" src=".*?" alt="(.*?)" />', resp)
    for link, title in img_info:
        link_url = 'https://xchina.co' + link
        resp1 = scraper.get(url = link_url, headers=headers).text
        img_url = re.findall(r'<img src="(.*?)" alt=".*?" onload="imgLoad\(this\);"', resp1)[0]
        img_content = scraper.get(url = img_url, headers=headers).content
        if not os.path.exists('img'):
            os.makedirs('img')
        file_name = title + '.jpg'
        pattern = r'[/《》！]'
        file_name1 = re.sub(pattern, '_', file_name)
        print("下載完成"+ file_name1)
        with open("img/"+ file_name1, mode='wb') as f:
            f.write(img_content)
print("保存完成")





