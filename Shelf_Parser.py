import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.goodreads.com/review/list?v=2 &id=106016596&shelf=to-read&key =7MFYkvoWpEg6bVvA6GuLyQ")
bookArr =[]

html_file = response.text
soup = BeautifulSoup(html_file, 'html.parser')
soup.prettify()
# get titles of books from users to read shelf
toRead_title = soup.findAll('td', 'field title', 'title')
for book in toRead_title:
    if  book.getText() is not 'title':
        bookArr.append(book.getText().replace('title','').strip())
#  Get Books authors 
toRead_author =  soup.findAll('td', 'field author', 'title')
for author in toRead_author:
    print(author.getText().replace('author','').strip())

toRead_rating =  soup.findAll('td', 'field avg_rating', 'title')
for author in toRead_rating:
    print(author.getText().replace('avg rating','').strip())

## TODO Make nested lists with title, author, rating and ISBN https://docs.python.org/3/tutorial/datastructures.html
## TODO Display all data together 
## TODO Pump out a random book 
## TODO Learn about making a front end for this 


print(bookArr)