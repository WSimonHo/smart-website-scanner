from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import csv
import os
import re

hostname = ''
filename = ''
content = ''
# soup = BeautifulSoup(content, 'html.parser')
results = {}

def check_website_links(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Finding all the <Meta>, <Script>, and <Link> tags
    meta_tags = soup.find_all('meta')
    script_tags = soup.find_all('script')
    link_tags = soup.find_all('link')

    total_links = len(meta_tags) + len(script_tags) + len(link_tags)
    return total_links

def check_anchor_url(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Finding all the <a> tags
    anchor_tags = soup.find_all('a')
    
    # Counting the number of anchor tags with different domain names
    different_domain_count = 0
    for anchor in anchor_tags:
        href = anchor.get('href')
        if href is not None and not re.match(r'^#|javascript:', href):
            if not href.startswith('/') and not href.startswith('http'):
               different_domain_count += 1

    return different_domain_count 

def check_request_url(content):
    return 0

def check_email_submission(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Checking for the use of "mail()" function in PHP
    email_submission = soup.find_all(lambda tag: tag.name == 'form' and 'mail(' in tag.get('action', ''))
    
    # Checking for the use of "mailto:" function
    mailto_links = soup.find_all('a', href=lambda href: href and href.lower().startswith('mailto:'))
    
    return len(mailto_links) + len(email_submission)

def check_different_href_urls(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Finding elements with "onMouseOver" attributes
    elements = soup.find_all(attrs={"onMouseOver": True})

    count_different_href_urls = 0
    for element in elements:
        # Finding elements with "onMouseOver" and "onClick" attributes
        href_url = element.get("href")
        onclick_href_url = element.get("onClick", "").split("=")[-1].strip("'\";")
        onmouseover_href_url = element.get("onMouseOver", "").split("=")[-1].strip("'\";")

        count_different_href_urls

        if href_url:
            if onmouseover_href_url != href_url:
                count_different_href_urls = count_different_href_urls + 1
        elif onclick_href_url:
            if onmouseover_href_url != onclick_href_url:
                count_different_href_urls = count_different_href_urls + 1

    return count_different_href_urls

def check_right_click_disabled(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Searching for the event "event.button==2" in the HTML content
    if ".button==2" in content:
        return 1

    return 0

def check_popup_window_text_fields(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Finding the URL of the pop-up window
    popup_url = None
    count_popup_window_text_fields = 0
    for script in soup.find_all('script'):
        if 'window.open' in script.text:
            # popup_url = script.text.split('window.open(')[1].split(',')[0].strip("'")
            pattern = r"window\.open\((.*?)\)"
            popup_match = re.findall(pattern, content)

            count_popup_window_text_fields = len(popup_match)

            # if popup_url:
            #     Sending a GET request to the pop-up window URL and retrieving the HTML content
            #     popup_response = requests.get(popup_url)
            #     popup_html_content = popup_response.text

            #     # Parsing the pop-up window HTML content
            #     popup_soup = BeautifulSoup(popup_html_content, 'html.parser')

            #     # Finding input elements in the pop-up window HTML content
            #     input_elements = popup_soup.find_all('input')

            #     for input_element in input_elements:
            #         input_type = input_element.get('type')
            #         if input_type == 'text':
            #             count_popup_window_text_fields = count_popup_window_text_fields + 1

    return count_popup_window_text_fields

def check_iframe_redirection(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Finding iframe elements in the HTML content
    iframe_elements = soup.find_all('iframe')
    return len(iframe_elements)    

def check_favicon_external_domain(content):
    soup = BeautifulSoup(content, 'html.parser')
    # Finding the favicon link element in the HTML content
    favicon_links = soup.find_all('link', rel=['icon', 'shortcut icon'])
    count_favicon_link = 0
    for favicon_link in favicon_links:
        if favicon_link:
            favicon_url = favicon_link.get('href')
            parsed_url = urlparse(favicon_url)
            domain = parsed_url.netloc

            # Checking if the favicon URL domain is different from the URL domain
            if domain != parsed_url.netloc:
                count_favicon_link = count_favicon_link + 1

    return count_favicon_link
    

def save_data_to_csv( item ):
    with open('./csv/train/website_content_without_url_3.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # print( f"item {item}" )
        writer.writerow([
            # hostname, 
            filename,
            item['website_links'],
            item['anchor_url'],
            item['request_url'],
            item['email_submission'],
            item['different_href_urls'],
            item['right_click_disabled'],
            item['popup_window_text_fields'],
            item['iframe_redirection'],
            item['favicon_external_domain'],
            1
        ])

def start_classify(file_path):
    with open(file_path, 'r') as html_file:
        content = html_file.read()
        results = {}
        results['website_links'] = check_website_links(content)
        results['anchor_url'] = check_anchor_url(content)
        results['request_url'] = check_request_url(content)
        results['email_submission'] = check_email_submission(content)
        results['different_href_urls'] = check_different_href_urls(content)
        results['right_click_disabled'] = check_right_click_disabled(content)
        results['popup_window_text_fields'] = check_popup_window_text_fields(content)
        results['iframe_redirection'] = check_iframe_redirection(content)
        results['favicon_external_domain'] = check_favicon_external_domain(content)
        save_data_to_csv( results )
                

folder_path = './dataset/phishing_without_url'
# folder_path = './demo'
files = os.listdir(folder_path)


key = 0
# Loop through each file
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    parts = file_name.split(".", 1)  # Split the string at the first dot
    filename = parts[0] 
    print( f"filename {filename}" )
    start_classify(file_path)