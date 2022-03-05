# File    : bookClub.py
# Author  : Joseph Kroeker
# Purpose : Automate book club functionality
# Changes : 03/05/2022 - Created class w/ help_msg

from genericClient import GenericClient


class Book():
    def __init__(self, title='The Old Man and the Sea', author='Ernest Hemingway', page_count='127', rating='3.8',
                 link='https://www.goodreads.com/book/show/2165.The_Old_Man_and_the_Sea'):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.rating = rating
        self.link = link


class BookList():
    def __init__(self):
        self.book_shelf = []
        self.add_book_help = '!addBook title, author, link, page count - Add a new book to the current bookshelf\n\n' \
                             'title - The title of the book you would like to add to bookshelf\n' \
                             'author (optional) - The author of the book that you would like to add\n' \
                             'link (optional) - A link to the Goodreads about page for the book (fuck goodreads)\n' \
                             'page count (optional) - the number of pages in the desired book'

    def add_book(self, msgSplit):
        # Function : add_book
        # Purpose  : Adds a book to the current bookshelf
        if not any(msgSplit):                # If there are no input arguments
            return self.add_book_help
        self.book_shelf.append(Book(msgSplit[0]))
        response = f'"{self.book_shelf[-1].title}"'
        return response

    def list_books(self):
        # Function : list_books
        # Purpose  : list all books in the current bookshelf
        response = ''
        for book in self.book_shelf:
            response += f'"{book.title}" by {book.author}\n'
        return response


class BCClient(GenericClient):
    def __init__(self):
        super(BCClient, self).__init__()
        self.bookList = BookList()

    def parse_msg(self, msg):
        # Function : parse_msg
        # Purpose  : Respond to non-generic messages that are directed towards the bot
        # Inputs   : msg - message that was received
        if '!addBook' in msg.content:  # Add a book to the list
            msgSplit = msg.content.replace('!addBook', '', 1).split(',')    # Remove command word and split list
            msgSplit = [s.strip() for s in msgSplit]    # Strip all leading whitespace
            self.response = self.bookList.add_book(msgSplit)
        elif '!listBooks' in msg.content:               # List all books currently in the list
            self.response = self.bookList.list_books()
        else:  # Not a currently accepted command
            self.response = ''

    def help_msg(self):
        # Function : help_msg
        # Purpose  : Book Club help message that will be output when needed
        self.response = 'Hello, I am the book club bot! I will keep track of the different choices for the book club\n\n' \
                        'Command List:\n' \
                        '!addBook title, author, link, page count - Add a new book to the current bookshelf\n' \
                        '!listBooks - List all books in the current bookshelf\n' \
                        '\nFor further help on a specific command use !command --help or !command -h'
