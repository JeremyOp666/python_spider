import requests
import pdfkit
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from requests.exceptions import RequestException
import os



url = input("请输入要转换为 PDF 的网页 URL: ")
parts = url.rsplit('/', 2)

if len(parts) >= 2:
    desired_part = parts[-2]
    if not os.path.exists(desired_part):
        os.makedirs(desired_part)
else:
    print("失敗。url格式https://www.runoob.com/類別/內容.html。")
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser', from_encoding='UTF-8')
anchor_tags = soup.find('div', class_='design', id='leftcolumn').find_all('a')

# Extract href attributes from the anchor tags
href_list = [tag['href'] for tag in anchor_tags]
full_urls = ['https://www.runoob.com'+ href if href.startswith('/') else 'https://www.runoob.com/'+ href for href in href_list]

print(full_urls)
for full in full_urls:
    try:
        print(full)
        response1 = requests.get(full)
        html_content1 = response1.content
        soup1 = BeautifulSoup(html_content1, 'html.parser', from_encoding='UTF-8')  # Use a new BeautifulSoup object

        image_tags = soup1.find_all('img')
        base_url = response1.url

        # 遍历图片标签，将相对路径转换为绝对路径
        for img_tag in image_tags:
            if 'src' in img_tag.attrs:
                src = img_tag['src']
                # 检查是否为相对路径
                if not src.startswith(('http://', 'https://')):
                    # 将相对路径转换为绝对路径
                    img_tag['src'] = urljoin(base_url, src)

        # 重新将修改后的 HTML 内容转换为字符串
        html_content_with_absolute_paths = str(soup1)

        # 提取<div class="article-body">里的内容
        article_body = soup1.find('div', {'class': 'article-body'})
        style_tag = soup1.find_all('style')

        # 将 CSS 导入链接转换为字符串
        css_str = ''.join(str(tag) for tag in style_tag)

        # 将 article_body 转换为字符串
        article_body_str = str(article_body)
        css = """<link rel="stylesheet" href="https://www.runoob.com/wp-content/themes/runoob/style.css?v=1.179" type="text/css" media="all">\n<link rel="stylesheet" href="https://lf3-cdn-tos.bytecdntp.com/cdn/expire-1-M/font-awesome/4.7.0/css/font-awesome.min.css" media="all">\n"""

        # 合并 CSS 导入代码、顶部 JavaScript 代码和 article_body
        html_content_with_css_and_body = css + css_str + article_body_str
        parsed_url = urlparse(full)
        file_name = parsed_url.path.split('/')[-1].split('.')[0]

        # 将 HTML 内容转换为 PDF
        pdf_file = f"{desired_part}\\{file_name}.pdf"
        wkhtmltopdf_path = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        pdfkit.from_string(html_content_with_css_and_body, pdf_file, configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path), options={"enable-local-file-access": "", "encoding": "utf-8"})
        print(f"轉換完成{pdf_file}")
    except RequestException as e:
        print(f"Error accessing URL: {full}")
        print(e)
