import requests

cookies = {
    'ipcountry': 'TW',
    'AVS': '55r8bakosiersjatgvmmiqtqc1',
    '__cflb': '02DiuDFSTg91mAHCXomJsywZC5pSxs3zvyLoiHAqEgqme',
    '__PPU_tuid': '7341982048326009531',
    '_gid': 'GA1.2.1554532719.1709438408',
    'noShowToday': 'true',
    'cf_clearance': '38rFxGtIjx1pkm0y8zBHHaOKZ1447X2.DTJv3xNAGOM-1709438407-1.0.1.1-m9t_ChbVmSfJwFwoZ9J6ZeDDykCoFvfrsyyQfgvT_duF9yY.dFvUQUAcMf5dfI_vZaypg3UItfeFyiIYTmF5BQ',
    '_clck': 'o4qfo1%7C2%7Cfjr%7C0%7C1523',
    'cover': '1',
    'guide': '1',
    'ipm5': 'c8873b29ef2d66db26058760d12903c1',
    'login_reminder': '1',
    'bnState_1997123': '{"impressions":6,"delayStarted":0}',
    '_ga': 'GA1.1.283634273.1709438408',
    '_ga_VW05C6PGN3': 'GS1.1.1709438407.1.1.1709439039.58.0.0',
    '_ga_C1BGNGMN6J': 'GS1.2.1709438408.1.1.1709439039.0.0.0',
    '__cf_bm': 'kd7oF6ebOuJC_1APcwvkyc474Ad0moq1I0LjH_MQQws-1709439040-1.0.1.1-IPlLvFNsqxY.S.TCeBq6s0JWq_.TfsI16QuDAprFkakqIlodTRSgpUgbPWEuTa_MT9Ou8nWZrdseyWYQ8kqnEA',
    '_clsk': '1apwq4g%7C1709439495784%7C13%7C0%7Cp.clarity.ms%2Fcollect',
}

headers = {
    'authority': '18comic.vip',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'ipcountry=TW; AVS=55r8bakosiersjatgvmmiqtqc1; __cflb=02DiuDFSTg91mAHCXomJsywZC5pSxs3zvyLoiHAqEgqme; __PPU_tuid=7341982048326009531; _gid=GA1.2.1554532719.1709438408; noShowToday=true; cf_clearance=38rFxGtIjx1pkm0y8zBHHaOKZ1447X2.DTJv3xNAGOM-1709438407-1.0.1.1-m9t_ChbVmSfJwFwoZ9J6ZeDDykCoFvfrsyyQfgvT_duF9yY.dFvUQUAcMf5dfI_vZaypg3UItfeFyiIYTmF5BQ; _clck=o4qfo1%7C2%7Cfjr%7C0%7C1523; cover=1; guide=1; ipm5=c8873b29ef2d66db26058760d12903c1; login_reminder=1; bnState_1997123={"impressions":6,"delayStarted":0}; _ga=GA1.1.283634273.1709438408; _ga_VW05C6PGN3=GS1.1.1709438407.1.1.1709439039.58.0.0; _ga_C1BGNGMN6J=GS1.2.1709438408.1.1.1709439039.0.0.0; __cf_bm=kd7oF6ebOuJC_1APcwvkyc474Ad0moq1I0LjH_MQQws-1709439040-1.0.1.1-IPlLvFNsqxY.S.TCeBq6s0JWq_.TfsI16QuDAprFkakqIlodTRSgpUgbPWEuTa_MT9Ou8nWZrdseyWYQ8kqnEA; _clsk=1apwq4g%7C1709439495784%7C13%7C0%7Cp.clarity.ms%2Fcollect',
    'dnt': '1',
    'referer': 'https://18comic.vip/',
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
    'https://18comic.vip/album/420375/%E7%82%B9%E5%88%B0%E5%8D%B3%E6%AD%A2milky-way-%E3%81%B5%E3%81%AA%E3%81%A4%E3%81%8B%E3%81%9A%E3%81%8D-%E3%81%99%E3%82%93%E3%81%A9%E3%82%81-%E3%83%9F%E3%83%AB%E3%82%AD%E3%83%BC%E3%82%A6%E3%82%A7%E3%82%A4',
    cookies=cookies,
    headers=headers,
)
print(response.text)