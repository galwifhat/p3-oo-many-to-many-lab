class Author:
    all = []

    def __init__(self, name):
        self.name = name

    # return a list of related contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # return a list of related books using the Contract class as an intermediary.
    def books(self):
        return [contract.book for contract in self.contracts()]

    # create and return a new Contract object between the author and
    # the specified book with the specified date and royalties
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # return the total amount of royalties that the author has earned
    # from all of their contracts.
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)  # books() that returns a list of its books>

    # returns a list of its contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # returns a list of its authors
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)  # contracts() that returns a list of its contracts

    # return all contracts that have the same date as the date passed into the method
    # sorts all contracts by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    # validates author of type Author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception

    # validates book of type Book
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception

    # validates date of type str
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception

    # validates royalties of type int
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception
