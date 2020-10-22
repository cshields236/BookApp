class Book:
    # TODO Add isbn, number of pages, cover image
    def __init__(self):
        type = 'book'
        
    def addDetails(self, title, author, avg_rating):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating

    def showBook(self):
        print('Title ' + self.title + '\n'
              + 'Author ' + self.author + '\n'
              + 'Average Rating ' + self.avg_rating)
