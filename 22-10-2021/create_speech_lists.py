from bs4 import BeautifulSoup
import requests

raw_text = requests.get('http://obamaspeeches.com/').text
soup = BeautifulSoup(raw_text, 'lxml')

raw_links = soup.find_all('a')
links = []
for link in raw_links :
    x = link['href']
    if x not in links :
        links.append(x)
links = links[:-2]

# for link in links :
#     if '\n' in link :
#         print(link)