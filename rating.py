class Book:
    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

    def describe(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Rating:", self.rating)

    def is_good_book(self):
        if self.rating >= 4:
            print("Recommended")
        else:
            print("Average")

# წიგნების ობიექტები
book1 = Book("Harry Potter", "J.K. Rowling", 5)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 4)
book3 = Book("Some Story", "Unknown Author", 3)
book4 = Book("Learning Python", "Mark Lutz", 5)

# წიგნების სია
books = [book1, book2, book3, book4]

print("Recommended books:\n")

# რეკომენდებული წიგნების დაბეჭდვა
for book in books:
    if book.rating >= 4:
        book.describe()
        print("Recommended\n")