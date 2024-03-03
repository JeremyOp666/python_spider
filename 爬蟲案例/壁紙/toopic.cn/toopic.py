import requests
from bs4 import BeautifulSoup
import os

def homepage_crawler():
    url = 'https://www.toopic.cn/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div_tags = soup.find_all('div', class_='auto mt30 layout')

    for i in range(len(div_tags) - 1):
        start_div = div_tags[i]
        end_div = div_tags[i + 1]

        content_between_divs = start_div.find_next_sibling('ul')

        category = start_div.find('h2').text.strip()
        if not os.path.exists(category):
            os.makedirs(category)

        image_tags = content_between_divs.find_all('img', class_='lazy')
        for image_tag in image_tags:
            image_link = image_tag['data-original']
            image_description = image_tag['alt'] + ".png"
            image_link = "https://www.toopic.cn" + image_link
            headers = {
                'sec-ch-ua': '"Not A(Brand";v="99", "Avast Secure Browser";v="121", "Chromium";v="121"',
                'Sec-GPC': '1',
                'DNT': '1',
                'Referer': 'https://www.toopic.cn/',
                'sec-ch-ua-mobile': '?0',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Avast/121.0.0.0',
                'sec-ch-ua-platform': '"Windows"',
            }
            img_content = requests.get(url=image_link, headers=headers).content
            print("下載完成" + image_description)
            with open(f"{category}/" + image_description, mode='wb') as f:
                f.write(img_content)
        print("下載完類別" + category + "\n")



def target_crawler():
    url = input("請輸入目標網站URL：")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if not os.path.exists("壁紙下載"):
            os.makedirs("壁紙下載")

        image_tag = soup.find('img')

        if image_tag:
            image_link = image_tag['src']
            image_link = "https://www.toopic.cn" + image_link
            image_description = image_tag['alt'] + ".png"
            headers = {
                'sec-ch-ua': '"Not A(Brand";v="99", "Avast Secure Browser";v="121", "Chromium";v="121"',
                'Sec-GPC': '1',
                'DNT': '1',
                'Referer': 'https://www.toopic.cn/',
                'sec-ch-ua-mobile': '?0',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Avast/121.0.0.0',
                'sec-ch-ua-platform': '"Windows"',
            }
            img_content = requests.get(url=image_link, headers=headers).content
            with open(f"壁紙下載/" + image_description, mode='wb') as f:
                f.write(img_content)
            print("下載完成" + image_description)
        else:
            print("未找到圖片連結")
    else:
        print("無法連接到目標網站！")

def main():
    while True:
        print("\n歡迎使用toopic壁紙爬蟲：")
        print("1. 首頁爬蟲")
        print("2. 目標網頁爬蟲")
        print("0. 退出")
        choice = input("請輸入您的選擇：")

        if choice == '1':
            homepage_crawler()
        elif choice == '2':
            target_crawler()
        elif choice == '0':
            print("謝謝使用，再見！")
            break
        else:
            print("無效的選擇，請重新輸入！")


if __name__ == "__main__":
    main()