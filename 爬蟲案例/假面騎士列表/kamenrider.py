import requests
from bs4 import BeautifulSoup
'''
此腳本爬取https://kamenrider.fandom.com/wiki/List_of_Kamen_Riders的所有假面騎士列表
並儲存到kamenrider_scraper.txt裡面
'''
print("開始執行")
headers = {
    'authority': 'kamenrider.fandom.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

response = requests.get('https://kamenrider.fandom.com/wiki/List_of_Kamen_Riders', headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'sortable'})

    tbody = table.find('tbody')

    rows = tbody.find_all('tr')
    with open('kamenrider_scraper.txt', 'w', encoding='utf-8') as f:  # 使用with open语句打开文件
        for row in rows:
            td = row.find_all('td')
            if len(td) >= 2:
                result = td[1].get_text(strip=True)
                f.write(result + '\n')

else:
    print(f"連接失敗. Status code: {response.status_code}")
    exit()
print("-------------------------------------------")

print(f"爬取成功以保存列表到kamenrider_scraper.txt")