from parsel import Selector
import requests
import os
import re

url = 'https://meitulu.me/item/3103.html'

resp = requests.get(url)

selector = Selector(text=resp.text)


items = selector.css('section.mb-3 > div.mb-1')

image_count = None
resolution = None
model_name = None
release_time = None

for item in items:
    text = item.css('::text').get()
    if text.startswith('圖片數量：'):
        image_count = text.replace('圖片數量：', '')
    elif text.startswith('分 辨 率：'):
        resolution = text.replace('分 辨 率：', '')
    elif text.startswith('模特姓名：'):
        model_name = item.css('a::text').get()
    elif text.startswith('發行時間：'):
        release_time = text.replace('發行時間：', '')
print('圖片數量：', image_count)
print('分 辨 率：', resolution)
print('模特姓名：', model_name)
print('發行時間：', release_time)
print('開始爬取圖片')
result = []

image_urls = selector.css('div.mb-4.container-inner-fix-m img::attr(src)').getall()
name = selector.css('div.mb-4.container-inner-fix-m img::attr(alt)').extract_first()
pattern = r'[/《》！]'
name = re.sub(pattern, '_', name)
pagination_links = selector.css('ul.pagination.my-pagination li.page-item a.page-link')

max_page = 0

for link in pagination_links:
    page_text = link.xpath('text()').get()
    if page_text.isdigit():
        page_number = int(page_text)
        if page_number > max_page:
            max_page = page_number

for image_url in image_urls:
    result.append(image_url)

for i in range(2, max_page+1):
    url2 = url.replace('.html', f'_{i}.html')
    resp = requests.get(url2)
    selector = Selector(text=resp.text)
    image_urls = selector.css('div.mb-4.container-inner-fix-m img::attr(src)').getall()
    for image_url in image_urls:
        result.append(image_url)
for image in result:
    filename = image.split('/')[-1]
    image = "https://meitulu.me" + image
    if not os.path.exists(name):
        os.makedirs(name)
    img_content = requests.get(url=image).content
    print("下載完成" + filename)
    with open(f"{name}/" + filename, mode='wb') as f:
        f.write(img_content)
print("下載全部完成")




