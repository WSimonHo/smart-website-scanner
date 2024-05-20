import requests
from bs4 import BeautifulSoup
import re
import csv

# 要載入的網站列表
websites = []
with open('./dataset/archive/verified_online.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        websites.append(row['url'])


# print(websites)

# 用於儲存內容和URL的變量
content_list = []
url_array = []

# 定義一個函數來提取網站內容和URL
def load_website(url, sKey):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 如果請求失敗，將引發HTTPError異常


        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        
            # 儲存網站內容
            # content_list.append(soup.get_text())
            
            # 尋找並儲存所有URL
            for link in soup.find_all('a', href=True):
                sub_url = link['href']
                if re.match(r'http[s]?://', sub_url):  # 確保URL是完整的
                    url_array.append(sub_url)
            
            file_name = 100000 + sKey
            print(f'success載入 {url}')
            # print(f'success載入 {response.text}')
            with open('website_content_3.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([file_name,url])
            
            output_file = './web_content/' + str(file_name) + '.html'
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(response.text)
        else:
            print(f"statu not 200 {url}")
        response.close()
                
    except requests.exceptions.HTTPError as e:
        # print(f'無法載入 {url} - HTTP錯誤: {e}')
        print(f'無法載入-HTTPError {url} ')
    except requests.exceptions.RequestException as e:
        # print(f'無法載入 {url} - 請求錯誤: {e}')
        print(f'無法載入-RequestException {url} ')
    except requests.exceptions.Timeout:
        # Handle Timeout error (TCP connection fail)
        print(f'無法載入-Timeout {url} ')
    # finally:
    #     # Close the connection
    #     response.close()

# 遍歷網站列表並載入每個網站
key = 0
for website in websites:
    # if key == 100:
    #     break
    # print(f'!!!loading {website} ')
    load_website(website, key)
    key = key + 1

# 輸出結果
print('載入的內容:', content_list)
print('找到的URL:', url_array)
