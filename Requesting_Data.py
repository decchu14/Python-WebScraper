# This script contains the basics of beautifulsoup library
import requests
from bs4 import BeautifulSoup

# requesting hackernews website by passing the link
res = requests.get("https://news.ycombinator.com/")

# parsing the website throught html parser and assigning it to a variable named soup
soup = BeautifulSoup(res.text, 'html.parser')

# soup variable is an object which contains the html code of the page of which link was passed
print(soup)

# printing the body of the soup
print(soup.body)

# printing the body content of the soup
print(soup.body.content)

# printing all div tags
print(soup.find_all('div'))

# printing all a tags
print(soup.find_all('a'))

# printing title tag
print(soup.title)

# print the first a tag
print(soup.a)

# print the first a tag same as above line number 30
print(soup.find('a'))
