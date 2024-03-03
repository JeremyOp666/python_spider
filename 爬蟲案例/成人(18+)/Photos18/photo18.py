import requests
from bs4 import BeautifulSoup
import re, os

url = 'https://www.photos18.com/v/XXXX'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

img_divs = soup.find_all('div', class_='my-2 imgHolder')

image_links = []
for div in img_divs:
    link = div.find('a')['href']
    image_links.append(link)

for link in image_links:
    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Referer': url,
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }
    img_content = requests.get(url=link, headers=headers).content
    if not os.path.exists('img'):
        os.makedirs('img')
    title = re.search(r'/(\d+)\.webp', link).group(1) + '.jpg'
    file_name = title + '.jpg'
    pattern = r'[/《》！]'
    file_name1 = re.sub(pattern, '_', file_name)
    print("下載完成" + file_name1)
    with open("img/" + file_name1, mode='wb') as f:
        f.write(img_content)