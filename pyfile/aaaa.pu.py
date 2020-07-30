from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import time

def job():
    try:
        html = urlopen('https://news.yahoo.co.jp/topics')
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)

    else:

# Yahooトピックスにアクセスし、ニュース情報を採取
        bs = BeautifulSoup(html.read(), 'lxml')
        newsList = bs.find('div', {'class': 'topicsListAllMain'}).find_all('a')

# 取得したListからニュースのタイトルとURLを取得して表示
        for news in newsList:
            if re.match('^(https://)', news.attrs['href']):
                print(news.get_text())
                print(news.attrs['href'])

job()
