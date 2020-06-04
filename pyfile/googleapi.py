import requests
from bs4 import BeautifulSoup

arg = 'Python'
result = requests.get('https://www.google.com/search?q={}/'.format(arg))
soup = BeautifulSoup(result.text, 'html.parser')
list = soup.findAll(True, {'class' : 'BNeawe vvjwJb AP7Wnd'})
a = str(list).strip('<div class="BNeawe vvjwJb AP7Wnd">')
b = a.split('</div>, <div class="BNeawe vvjwJb AP7Wnd">')
c = b[1].split('[<div class="BNeawe vvjwJb AP7Wnd">')
d = b[9].split('</div>]')
e = c + b[2:8] + d
print(e)
