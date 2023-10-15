'''
This script is a simple web scrapper that asks the user to type in the website along with the HTML keyword they wish to request data about. 
Website Example: 'http://olympus.realpython.org/profiles'
Keyword: 'img'
'''

#Importing urlopen and beautifulsoup libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

#asks the user to type in the url they wish to webscrape
url = input('What URL would you like to search?:  ')
#word = input("What key word do you want to search for?:  ")
print('Example: title, body, img, ect')
term = input('What HTML tag would you like to search for?:  ')
print(f'Searching {url}')

#opens a browser to the url you just provided
page = urlopen(url)

#take the html raw data from the URL and turns it into a string.
html = page.read().decode('utf-8')

#informs the method which parser to use, in this case HTML
soup = bs(html, 'html.parser')

#print(soup.get_text())
result = soup.find_all(term)
#print(result)
print(soup.find_all(term))


#Help from https://realpython.com/python-web-scraping-practical-introduction/