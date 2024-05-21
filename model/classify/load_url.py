import requests
from bs4 import BeautifulSoup
import re
import csv

# List of sites to load
websites = []
with open('./dataset/verified_online.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        websites.append(row['url'])

# Variables for storing content and URLs
content_list = []
url_array = []

# Define a function to extract website content and URL
def load_website(url, sKey):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # If the request fails, an HTTPError exception will be raised


        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        
            # Store website content
            
            # Find and store all URLs
            for link in soup.find_all('a', href=True):
                sub_url = link['href']
                if re.match(r'http[s]?://', sub_url):
                    url_array.append(sub_url)
            
            file_name = 100000 + sKey
            print(f'success load the {url}')
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
        print(f'Unable to load-HTTPError {url} ')
    except requests.exceptions.RequestException as e:
        print(f'Unable to load-RequestException {url} ')
    except requests.exceptions.Timeout:
        print(f'Unable to load-Timeout {url} ')
    # finally:
    #     # Close the connection
    #     response.close()

# Loop through the list of sites and load each site
key = 0
for website in websites:
    load_website(website, key)
    key = key + 1

# Output results
print('loaded content:', content_list)
print('URL found:', url_array)
