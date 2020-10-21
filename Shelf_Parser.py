import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.goodreads.com/review/list?v=2 &id=106016596&shelf=to-read&key=7MFYkvoWpEg6bVvA6GuLyQ")

html_file = response.text
soup = BeautifulSoup(html_file, 'html.parser')
soup.prettify()
toRead = soup.findAll('td', 'field title', 'value')
for book in toRead:
    print(book.getText())


