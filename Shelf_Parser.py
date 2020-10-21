import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.goodreads.com/review/list?v=2 &id=106016596&shelf=to-read&key =7MFYkvoWpEg6bVvA6GuLyQ")

html_file = response.text
soup = BeautifulSoup(html_file, 'html.parser')
soup.prettify()
toRead_title = soup.findAll('td', 'field title', 'title')
for book in toRead_title:
    if  book.getText() is not 'title':
        print(book.getText().replace('title','').strip())


# toRead_author =  soup.findAll('td', 'field author', 'title')
# for author in toRead_author:
#     print(author.getText())

# for tag in soup.findAll('td', 'field title'):
#     print(tag)

