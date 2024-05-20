from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import csv
import os

hostname = ''
content = ''
soup = BeautifulSoup(content, 'html.parser')
results = {}


csv_file2 = './csv/ph_db_url.csv'
with open(csv_file2, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Loop through each row in the CSV file
    for row in reader:
        url = row[2]
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        print( f"hostname {url}" )


        with open('website_url_5_p.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                url,
                1
            ])