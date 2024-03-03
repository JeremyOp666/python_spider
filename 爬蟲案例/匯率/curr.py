import requests
from parsel import Selector

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
page = requests.get(url)
selector = Selector(text=page.text)

for tr in selector.css('table.table tbody tr'):
    currency = tr.css('div.visible-phone::text').get().strip()
    curr_rate = tr.css('td:nth-child(3)::text').get().strip()
    print(currency, ':', curr_rate)