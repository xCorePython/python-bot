import requests, bs4
result = requests.get('https://status.discord.com')
soup = bs4.BeautifulSoup(result.text, 'html.parser')
list = soup.find('class=\"metric-average color-secondary\"')
print(list)
