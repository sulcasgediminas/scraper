import requests
from bs4 import BeautifulSoup

url = 'https://finviz.com/news.ashx'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    link_element = soup.find('td', class_='news_link-cell')

    if link_element:
        extracted_text = link_element.get_text(separator=" ", strip=True)
        print(extracted_text)
    else:
        print("No matching element found.")
