
import cloudscraper
from lxml.html import fromstring
import os, sys, re
import requests
import parsel
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"
}

novel_url = 'https://www.69shu.pro/book/xxxx.htm'


resp = requests.get(url=novel_url, headers=headers)
resp.encoding = "gbk"

if resp is None:
    print("連接失敗.")
    sys.exit(1)

selector = parsel.Selector(resp.text)
book_title = selector.css('div.bread a:nth-last-child(1)::text').get()
url = novel_url.replace(".htm", "/")
resp = requests.get(url=url, headers=headers)
resp.encoding = "gbk"
selector0 = parsel.Selector(resp.text)
charlist = selector0.css('div#catalog ul li a::attr(href)').getall()

for link in charlist:
    resp2 = requests.get(url=link, headers=headers)
    resp2.encoding = "gbk"
    if resp2 is not None:
        selector1 = parsel.Selector(resp2.text)
        novel_charname = selector1.css('div.txtnav h1::text').get()
        novel_content = selector1.css('div.txtnav::text').getall()
        novel_content1 = "".join(novel_content)
        novel_content2 = '\n'.join([line.lstrip() for line in novel_content1.split('\n')])

        if not os.path.exists(f"{book_title}"):
            os.makedirs(f"{book_title}")

        with open(f"{book_title}/{novel_charname}.txt", "w", encoding="utf-8") as f:
            f.write(novel_charname)
            f.write('\n')
            f.write(novel_content2)
            f.write('\n')
        print(f"保存章節完成{novel_charname}")

    else:
        print(f"無法獲取章節內容 {link}. 跳過...")
print("保存完成")










