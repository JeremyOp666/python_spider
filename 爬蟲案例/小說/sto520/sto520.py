
import cloudscraper
from lxml.html import fromstring
import os, sys, re
import requests
import parsel
from time import sleep




headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"
}

scraper=cloudscraper.create_scraper(browser={
        'browser': 'firefox',
        'platform': 'windows',
        'mobile': False
    })


def fetch_content_with_retry(url, headers, max_retries=5):
    for _ in range(max_retries):
        resp = scraper.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.text
        sleep(1)
    return None

novel_url = 'https://sto520.com/book/xxxx/'

resp = fetch_content_with_retry(novel_url, headers)
if resp is None:
    print("Failed to fetch the page.")
    sys.exit(1)

selector = parsel.Selector(resp)

novel_title = selector.css('.bookinfo .booktitle::text').get()
novel_intro = selector.css('p.bookintro::text').getall()
novel_picture = selector.css('.bookcover img.thumbnail::attr(src)').get()
novel_author = selector.css('p a.red::text').get()
novel_latest = selector.css('p a.bookchapter::text').get()
novel_time = selector.css('p.booktime::text').get()
novel_intro1 = "".join(novel_intro)
BookInfo = f"""
小說標題: {novel_title}

小說簡介:
{novel_intro1}
作者: {novel_author}

最新章節: {novel_latest}

最後{novel_time}
"""
print(BookInfo)

if not os.path.exists(novel_title):
    os.makedirs(novel_title)

with open(f"{novel_title}/BookInfo.txt", "w", encoding="utf-8") as file:
    file.write(BookInfo)

charlist = selector.css('#list-chapterAll dd a::attr(href)').getall()
for link in charlist:
    resp2 = fetch_content_with_retry(link, headers)
    if resp2 is not None:
        selector1 = parsel.Selector(resp2)
        novel_charname = selector1.css('.book.read h1::text').get()
        novel_content = selector1.css('p.readcotent.bbb.font-normal::text').getall()
        novel_content1 = "".join(novel_content)
        novel_content2 = novel_content1.replace("寫到這裡我希望讀者記一下我們域名ＳＴＯ５２０．ＣＯＭ", "")
        novel_content2 = novel_content2.replace("  【請記住我們的域名sto520.com 思兔閱讀，如果喜歡本站請分享到Facebook臉書】", "")
        novel_content2 = novel_content2.replace("【Google搜索sto520.com思兔閱讀】", "")
        novel_content2 = novel_content2.replace("記住本站域名ＳＴＯ５２０．ＣＯＭ", "")
        novel_content2 = novel_content2.replace("Google搜索sto520.com思兔閱讀", "")
        novel_content2 = novel_content2.replace("【思兔閱讀ＳＴＯ５２０．ＣＯＭ,無錯章節閱讀】", "")
        novel_content2 = novel_content2.replace("【無錯章節小說閱讀，google搜尋sto520.com思兔閱讀】", "")


        novel_content2 = '\n'.join([line.lstrip() for line in novel_content2.split('\n')])
        if not os.path.exists(f"{novel_title}/章節內容"):
            os.makedirs(f"{novel_title}/章節內容")

        with open(f"{novel_title}/章節內容/{novel_charname}.txt", "w", encoding="utf-8") as f:
            f.write(novel_charname)
            f.write('\n')
            f.write(novel_content2)
            f.write('\n')
    else:
        print(f"Failed to fetch content for chapter {link}. Skipping...")





print("保存完成")










