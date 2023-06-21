# Да се състави програма на Python, чрез която да се дефинира клас Book, с полета:
# book_name (име на книга),
# book_code (код на книга),
# book_price (цена на книга),
# book_year (година на издаване на книгата),
# book_author (автор на книгата).
# Да се дефинира конструктор, който инициализира полетата на класа.

# Да се създаде списък books, който съдържа четири инстанции на класа Book.

# Да се съставят две функции:
# 1-та функция с име sort_name да извършва сортиране по име на книга (book_name) в низходящ ред и да извежда получения резултат на екрана.
# 2-та функция с име author да извежда на екрана всички книги от един автор.

# Да се състави функция с име search_book, която получава като аргумент код на книга (book_code).
# Ако търсенето на книгата е налично да се изведе нейната година на издаване (book_year). Ако не е налична да се изведе съобщение на 
# екрана "The book is not found!".

class Book:

    def __init__(self, book_name, book_code, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_year = book_year
        self.book_author = book_author

    def __repr__(self):
        return self.book_name + " " + str(self.book_code) + " " + str(self.book_year) + " " + self.book_author

book1 = Book('Sea',2345,2000,'Ivan')
book2 = Book('Moon',2342,2001,'Vanq')
book3 = Book('Star',3454,2005,'Moni')
book4 = Book('Sun',5666,1999,'Moni')

books = [book1,book2,book3,book4]

def sort_name(books):
    return sorted(books, key = lambda y : y.book_name, reverse=True)

print(sort_name(books))

def author(author_search,books):
    for x in books:
        if author_search == x.book_author:
            print(x)

author('Moni',books)

def search_book(book_code,books):
    for x in books:
        if book_code == x.book_code:
            return x.book_year
        return 'The book is not found!'

print(search_book(2345,books))


