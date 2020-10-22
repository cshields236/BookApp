import requests
from bs4 import BeautifulSoup
from Book import Book
from random import randint

response = requests.get("https://www.goodreads.com/review/list?v=2 &id=106016596&shelf=to-read&key =7MFYkvoWpEg6bVvA6GuLyQ")
bookList =[]
titleArr =[]
authorArr = []
ratingArr = []
coversArr = []
isbnArr = []

html_file = response.text
soup = BeautifulSoup(html_file, 'html.parser')
soup.prettify()
# get titles of books from users to read shelf

for book in soup.findAll('td', 'field title', 'title'):
        titleArr.append(book.getText().replace('title','').strip())

#  Get Books author 

for author in  soup.findAll('td', 'field author', 'title'):
    authorArr.append(author.getText().replace('author','').replace('*', '').strip())


for rating in soup.findAll('td', 'field avg_rating', 'title'):
    ratingArr.append(rating.getText().replace('avg rating','').strip())


for isbn in soup.findAll('td', 'field isbn', 'title'):
    isbnArr.append(isbn.getText().replace('isbn', '').strip())


for cover in soup.findAll( 'img'): 
    c = cover.get('src')
    if '.jpg' in str(c):
        coversArr.append(c)


## TODO Pump out a random book 
## TODO Learn about making a front end for this 

for l in range(len(titleArr)):
    b = Book() 
    b.addDetails(titleArr[l], authorArr[l], ratingArr[l], isbnArr[l], coversArr[l])
    bookList.append(b)

