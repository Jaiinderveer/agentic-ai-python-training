import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text,'html.parser')
# p_tags = soup.find_all('p',class_ = 'star-rating Three')
a_tags = soup.find_all('a')

for a_tag in a_tags:
    print(a_tag.text)