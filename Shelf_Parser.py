import requests
from bs4 import BeautifulSoup
from Book import Book

response = requests.get("https://www.goodreads.com/review/list?v=2 &id=106016596&shelf=to-read&key =7MFYkvoWpEg6bVvA6GuLyQ")
bookList =[]
titleArr =[]
authorArr = []
ratingArr = []

html_file = response.text
soup = BeautifulSoup(html_file, 'html.parser')
soup.prettify()
# get titles of books from users to read shelf
toRead_title = soup.findAll('td', 'field title', 'title')
for book in toRead_title:
        titleArr.append(book.getText().replace('title','').strip())

#  Get Books author 
toRead_author =  soup.findAll('td', 'field author', 'title')
for author in toRead_author:
    authorArr.append(author.getText().replace('author','').replace('*', '').strip())

toRead_rating =  soup.findAll('td', 'field avg_rating', 'title')
for author in toRead_rating:
    ratingArr.append(author.getText().replace('avg rating','').strip())

## TODO Use classes instead
## TODO Display all data together 
## TODO Pump out a random book 
## TODO Learn about making a front end for this 

for l in range(len(titleArr)):
    b = Book()
    b.addDetails(titleArr[l], authorArr[l], ratingArr[l])
    bookList.append(b)


print(bookList[1].title + bookList[1].author)
