import requests  # like a web browser without the GUI
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.body)  # Read the docs for all the different things you can do
print(soup.body.contents)
print(soup.find_all('a'))
print(soup.find('a'))
