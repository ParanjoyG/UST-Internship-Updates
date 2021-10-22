from bs4 import BeautifulSoup
import requests
import re
from create_speech_lists import links
import os

speech = ""
# os.mkdir('\speeches')

base_url = 'http://obamaspeeches.com/'
limit = len(links)

for i in range(limit) :
    
    link = links[i]

    if link[0] == '/' :
        link = base_url + link[1:]
    else :
        link = base_url + link

    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')

    raw_data = soup.find_all('td')
    raw_speech = raw_data[4].text.split()

    if len(raw_speech) == 0 or len(raw_speech) == 3 :
        raw_speech = raw_data[6].text.split()
    elif len(raw_speech) == 2 :
        raw_speech = raw_data[6].text.split()
    elif len(raw_speech) == 5 :
        raw_speech = raw_data[7].text.split()

    # if i>=20 :
    #     print(f'The speech at {i} is {raw_speech}')

    regex = '^20\d\d'
    pos = -1
    for x in range(len(raw_speech)) :
        if (re.search(regex, raw_speech[x])) :
            pos = x
            break

    # speech = ""
    for x in range (pos+1, len(raw_speech)) :
        speech += raw_speech[x]
        speech += " "
    
    # print(f'The length of speech at {i} is {len(speech)}')

    # file = open(f'speeches/speech {i}.txt', 'w', encoding='utf-8')
    # file.write(speech)
    # file.close()

    print(i)

print(len(speech))  
file = open('everything.txt', 'w', encoding='utf-8')
file.write(speech)
file.close()
