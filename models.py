import sqlite3


class Roll:
    """
    Represents a staff role.

    Attributes:
        id (int): Unique identifier of the role.
        name (str): Name of the role.
    """
    id: int = 0
    name: str = ""

    def __init__(self, id, name):
        """
        Initialize a Roll instance.

        Args:
            id (int): Unique identifier of the role.
            name (str): Name of the role.
        """
        self.id = id
        self.name = name


class Staff:
    """
    Represents a staff member.

    Stores the personal information of a staff member along with
    the role assigned to them.

    Attributes:
        id (int): Unique identifier of the staff member.
        name (str): First name of the staff member.
        family (str): Last name of the staff member.
        national_code (int): National identification code.
        roll (Roll | None): Assigned role of the staff member.
    """
    id: int = 0
    name: str = ""
    family: str = ""
    national_code: int = 0
    roll: Roll = None

    def __init__(self, id, name, family, national_code):
        """
        Initialize a Staff instance.

        Args:
            id (int): Unique identifier of the staff member.
            name (str): First name of the staff member.
            family (str): Last name of the staff member.
            national_code (int): National identification code.
        """
        self.id = id
        self.name = name
        self.family = family
        self.national_code = national_code


class Member:
    """
    Represents a library member.

    Stores the personal information and membership details of a
    registered library member.

    Attributes:
        id (int): Unique identifier of the member.
        name (str): First name of the member.
        family (str): Last name of the member.
        national_code (int): National identification code.
        registration_code (int): Membership registration code.
        expiration_date (int): Membership expiration date.
    """
    id: int = 0
    name: str = ""
    family: str = ""
    national_code: int = 0
    registration_code: int = 0
    expiration_date: int = 0

    def __init__(self, id, name, family, national_code, registration_code, expiration_date):
        """
        Initialize a Member instance.

        Args:
            id (int): Unique identifier of the member.
            name (str): First name of the member.
            family (str): Last name of the member.
            national_code (int): National identification code.
            registration_code (int): Membership registration code.
            expiration_date (int): Membership expiration date.
        """
        self.id = id
        self.name = name
        self.family = family
        self.national_code = national_code
        self.registration_code = registration_code
        self.expiration_date = expiration_date


class Author:
    """
    Represents an author.

    Stores the basic information of a book author.

    Attributes:
        id (int): Unique identifier of the author.
        name (str): First name of the author.
        family (str): Last name of the author.
    """

    id: int = 0
    name: str = ""
    family: str = ""

    def __init__(self, id, name, family):
        """
        Initialize an Author instance.

        Args:
            id (int): Unique identifier of the author.
            name (str): First name of the author.
            family (str): Last name of the author.
        """
        self.id = id
        self.name = name
        self.family = family


class Donor:
    """
    Represents a donor.

    Stores the personal information of a person who donates
    books or other resources to the library.

    Attributes:
        id (int): Unique identifier of the donor.
        name (str): First name of the donor.
        family (str): Last name of the donor.
        national_code (int): National identification code.
    """
    id: int = 0
    name: str = ""
    family: str = ""
    national_code: int = 0

    def __init__(self, id, name, family, national_code):
        """
        Initialize a Donor instance.

        Args:
            id (int): Unique identifier of the donor.
            name (str): First name of the donor.
            family (str): Last name of the donor.
            national_code (int): National identification code.
        """
        self.id = id
        self.name = name
        self.family = family
        self.national_code = national_code


class Publisher:
    """
    Represents a publisher.

    Stores the basic information of a book publisher.

    Attributes:
        id (int): Unique identifier of the publisher.
        name (str): Name of the publisher.
        address (str): Physical address of the publisher.
        phone_number (int): Contact phone number of the publisher.
        email (str): Email address of the publisher.
    """
    id: int = 0
    name: str = ""
    address: str = ""
    phone_number: int = 0
    email: str = ""

    def __init__(self, id, name, address, phone_number, email):
        """
        Initialize a Publisher instance.

        Args:
            id (int): Unique identifier of the publisher.
            name (str): Name of the publisher.
            address (str): Physical address of the publisher.
            phone_number (int): Contact phone number of the publisher.
            email (str): Email address of the publisher.
        """
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email


class Genre:
    """
    Represents a book genre.

    Stores the basic information of a category or genre of books.

    Attributes:
        id (int): Unique identifier of the genre.
        name (str): Name of the genre.
    """
    id: int = 0
    name: str = ""

    def __init__(self, id, name):
        """
        Initialize a Genre instance.

        Args:
            id (int): Unique identifier of the genre.
            name (str): Name of the genre.
        """
        self.id = id
        self.name = name


class Designer:
    """
    Represents a designer.

    Stores the basic information of a book designer.

    Attributes:
        id (int): Unique identifier of the designer.
        name (str): First name of the designer.
        family (str): Last name of the designer.
    """
    id: int = 0
    name: str = ""
    family: str = ""

    def __init__(self, id, name, family):
        """
        Initialize a Designer instance.

        Args:
            id (int): Unique identifier of the designer.
            name (str): First name of the designer.
            family (str): Last name of the designer.
        """
        self.id = id
        self.name = name
        self.family = family


class Source:
    """
    Represents a book source.

    Stores the basic information of a source or reference material
    associated with a book.

    Attributes:
        id (int): Unique identifier of the source.
        name (str): Name of the source.
        author_name (str): Name of the source author.
    """
    id: int = 0
    name: str = ""
    author_name: str = ""

    def __init__(self, id, name, author_name):
        """
        Initialize a Source instance.

        Args:
            id (int): Unique identifier of the source.
            name (str): Name of the source.
            author_name (str): Name of the source author.
        """
        self.id = id
        self.name = name
        self.author_name = author_name


class Translator:
    """
    Represents a translator.

    Stores the basic information of a book translator.

    Attributes:
        id (int): Unique identifier of the translator.
        name (str): First name of the translator.
        family (str): Last name of the translator.
    """
    id: int = 0
    name: str = ""
    family: str = ""

    def __init__(self, id, name, family):
        """
        Initialize a Translator instance.

        Args:
            id (int): Unique identifier of the translator.
            name (str): First name of the translator.
            family (str): Last name of the translator.
        """
        self.id = id
        self.name = name
        self.family = family


class Book:
    """
    Represents a book.

    Stores the complete information of a book including publication
    details, publisher, contributors, and classifications.

    Attributes:
        id (int): Unique identifier of the book.
        title (str): Title of the book.
        year_of_publication (int): Year when the book was published.
        price (int): Price of the book.
        print_turn (int): Printing edition number of the book.
        circulation (int): Number of printed copies.
        isbn (int): International Standard Book Number.
        publisher (Publisher | None): Publisher of the book.
        designer (Designer | None): Designer of the book.
        sources (list[Source]): List of sources related to the book.
        translators (list[Translator]): List of translators of the book.
        authors (list[Author]): List of authors of the book.
        genres (list[Genre]): List of genres assigned to the book.
        donors (list[Donor]): List of donors associated with the book.
    """

    id: int = 0
    title: str = ""
    year_of_publication: int = 0
    price: int = 0
    print_turn: int = 0
    circulation: int = 0
    isbn: int = 0
    publisher: Publisher = None
    designer: Designer = None
    sources: list[Source] = []
    translators: list[Translator] = []
    authors: list[Author] = []
    genres: list[Genre] = []
    donors: list[Donor] = []

    def __init__(self, id, title, year_of_publication, price, print_turn, circulation, isbn):
        """
        Initialize a Book instance.

        Args:
            id (int): Unique identifier of the book.
            title (str): Title of the book.
            year_of_publication (int): Year when the book was published.
            price (int): Price of the book.
            print_turn (int): Printing edition number of the book.
            circulation (int): Number of printed copies.
            isbn (int): International Standard Book Number.
        """
        self.id = id
        self.title = title
        self.year_of_publication = year_of_publication
        self.price = price
        self.print_turn = print_turn
        self.circulation = circulation
        self.isbn = isbn


class Rent:
    """
    Represents a book rental transaction.

    Stores information about a rented book, including rental dates,
    the member who rented the book, and the staff member who processed
    the transaction.

    Attributes:
        id (int): Unique identifier of the rental.
        received_date (int): Date when the book was rented.
        return_date (int): Date when the book should be returned.
        book (Book | None): Rented book.
        member (Member | None): Member who rented the book.
        staff (Staff | None): Staff member responsible for the rental.
    """
    id: int = 0
    received_date: int = 0
    return_date: int = 0
    book: Book = None
    member: Member = None
    staff: Staff = None

    def __init__(self, id, received_date, return_date):
        """
        Initialize a Rent instance.

        Args:
            id (int): Unique identifier of the rental.
            received_date (int): Date when the book was rented.
            return_date (int): Date when the book should be returned.
        """
        self.id = id
        self.received_date = received_date
        self.return_date = return_date


class Library:
    """
    Represents a library management system.

    Stores collections of library entities including books, members,
    staff, authors, publishers, and rental records.

    Attributes:
        rolls (list[Roll]): List of available staff roles.
        staffs (list[Staff]): List of library staff members.
        members (list[Member]): List of library members.
        authors (list[Author]): List of book authors.
        donors (list[Donor]): List of book donors.
        publishers (list[Publisher]): List of book publishers.
        genres (list[Genre]): List of book genres.
        designer (list[Designer]): List of book designers.
        sources (list[Source]): List of book sources.
        translators (list[Translator]): List of book translators.
        books (list[Book]): List of books in the library.
        rents (list[Rent]): List of rental transactions.
    """
    rolls: list[Roll] = []
    staffs: list[Staff] = []
    members: list[Member] = []
    authors: list[Author] = []
    donors: list[Donor] = []
    publishers: list[Publisher] = []
    genres: list[Genre] = []
    designer: list[Designer] = []
    sources: list[Source] = []
    translators: list[Translator] = []
    books: list[Book] = []
    rents: list[Rent] = []

    # def get_all_rolls(self):
    # cn = sqlite3.connect("library new.db")
    # cr = cn.cursor()
    # s = "select * from rolls"
    # result = list(cr.execute(s))
    # rolls = []
    # for roll in result:
    # rolls.append(Roll(roll[0], roll[1]))
    # return rolls

    # def get_all_staffs(self):
    # cn = sqlite3.connect("library new.db")
    # cr = cn.cursor()
    # s = "select * from staffs"
    # result = list(cr.execute(s))
    # staffs = []
    # for staff in result:
    # staffs.append(Staff(staff[0], staff[1],
    # staff[2], staff[3], staff[4]))
    # return staffs

    # def get_all_members(self):
    # cn = sqlite3.connect("library new.db")
    # cr = cn.cursor()
    # s = "select * from members"
    # result = list(cr.execute(s))
    # members = []
    # for member in result:
    # members.append(
    # Member(member[0], member[1], member[2], member[3], member[4], member[5]))
    # return members

    def get_all_authors(self):
        """
        Retrieve all authors from the database.

        Returns:
            list[Author]: A list containing all authors stored in the database.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = "select * from authors"
        result = list(cr.execute(s))
        authors = []
        for author in result:
            authors.append(Author(author[0], author[1], author[2]))
        return authors

    def insert_author(self, author: Author):
        """
        Insert a new author into the database.

        Args:
            author (Author): Author object containing the information
                to be stored.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"Insert Into authors(name,family) Values ('{author.name}','{author.family}')"
        cr.execute(s)
        cn.commit()

    def delete_author(self, id):
        """
        Delete an author from the database.

        Args:
            id (int): Unique identifier of the author to delete.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"delete from authors where id={id}"
        cr.execute(s)
        cn.commit()

    def update_author(self, author: Author):
        """
        Update an existing author in the database.

        Args:
            author (Author): Author object containing the updated information.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"update authors set name='{author.name}' , family='{author.family}' where id={author.id}"
        cr.execute(s)
        cn.commit()

    # def get_all_donors(self):
        #"""
        #Retrieve all donors from the database.
#
        #Returns:
            #list[Donor]: A list containing all donors stored in the database.
        #"""      
        # cn = sqlite3.connect("library new.db")
        # cr = cn.cursor()
        # s = "select * from donors"
        # result = list(cr.execute(s))
        # donors = []
        # for donor in result:
        # donors.append(Donor(donor[0], donor[1], donor[2], donor[3]))
        # return donors

    def get_all_publishers(self):
        """
        Retrieve all publishers from the database.

        Returns:
            list[Publisher]: A list containing all publishers stored in the database.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = "select * from publishers"
        result = list(cr.execute(s))
        publishers = []
        for publisher in result:
            publishers.append(Publisher(
                publisher[0], publisher[1], publisher[2], publisher[3], publisher[4]))
        return publishers

    def insert_publisher(self, publisher: Publisher):
        """
        Insert a new publisher into the database.

        Args:
            publisher (Publisher): Publisher object containing the information
                to be stored.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"Insert Into publishers(name,address,phone_number,email) Values ('{publisher.name}','{publisher.address}','{publisher.phone_number}','{publisher.email}')"
        cr.execute(s)
        cn.commit()

    def delete_publisher(self, id):
        """
        Delete a publisher from the database.

        Args:
            id (int): Unique identifier of the publisher to delete.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"delete from publishers where id={id}"
        cr.execute(s)
        cn.commit()

    def update_publisher(self, publisher: Publisher):
        """
        Update an existing publisher in the database.

        Args:
            publisher (Publisher): Publisher object containing the updated information.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"update publishers set name='{publisher.name}' , address='{publisher.address}' , phone_number='{publisher.phone_number}' , email='{publisher.email}' where id={publisher.id}"
        cr.execute(s)
        cn.commit()

    def get_all_genres(self):
        """
        Retrieve all genres from the database.

        Returns:
            list[Genre]: A list containing all genres stored in the database.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = "select * from genres"
        result = list(cr.execute(s))
        genres = []
        for genre in result:
            genres.append(Genre(genre[0], genre[1]))
        return genres

    def insert_genre(self, genre: Genre):
        """
        Insert a new genre into the database.

        Args:
            genre (Genre): Genre object containing the information
                to be stored.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"Insert Into genres(name) Values ('{genre.name}')"
        cr.execute(s)
        cn.commit()

    def delete_genre(self, id):
        """
        Delete a genre from the database.

        Args:
            id (int): Unique identifier of the genre to delete.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"delete from genres where id={id}"
        cr.execute(s)
        cn.commit()

    def update_genre(self, genre: Genre):
        """
        Update an existing genre in the database.

        Args:
            genre (Genre): Genre object containing the updated information.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"update genres set name='{genre.name}' where id={genre.id}"
        cr.execute(s)
        cn.commit()

    def get_all_designers(self):
        """
        Retrieve all designers from the database.

        Returns:
            list[Designer]: A list containing all designers stored in the database.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = "select * from designers"
        result = list(cr.execute(s))
        designers = []
        for designer in result:
            designers.append(Designer(designer[0], designer[1], designer[2]))
        return designers

    def insert_designer(self, designer: Designer):
        """
        Insert a new designer into the database.

        Args:
            designer (Designer): Designer object containing the information
                to be stored.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"Insert Into designers(name,family) Values ('{designer.name}','{designer.family}')"
        cr.execute(s)
        cn.commit()

    def delete_designer(self, id):
        """
        Delete a designer from the database.

        Args:
            id (int): Unique identifier of the designer to delete.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"delete from designers where id={id}"
        cr.execute(s)
        cn.commit()

    def update_designer(self, designer: Designer):
        """
        Update an existing designer in the database.

        Args:
            designer (Designer): Designer object containing the updated information.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"update designers set name='{designer.name}' , family='{designer.family}' where id={designer.id}"
        cr.execute(s)
        cn.commit()

    def get_all_sources(self):
        """
        Retrieve all sources from the database.

        Returns:
            list[Source]: A list containing all sources stored in the database.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = "select * from sources"
        result = list(cr.execute(s))
        sources = []
        for source in result:
            sources.append(Source(source[0], source[1], source[2]))
        return sources

    def insert_source(self, source: Source):
        """
        Insert a new source into the database.

        Args:
            source (Source): Source object containing the information
                to be stored.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"Insert Into sources(name,author_name) Values ('{source.name}','{source.author_name}')"
        cr.execute(s)
        cn.commit()

    def delete_source(self, id):
        """
        Delete a source from the database.

        Args:
            id (int): Unique identifier of the source to delete.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"delete from sources where id={id}"
        cr.execute(s)
        cn.commit()

    def update_source(self, source: Source):
        """
        Update an existing source in the database.

        Args:
            source (Source): Source object containing the updated information.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"update sources set name='{source.name}' , author_name='{source.author_name}' where id={source.id}"
        cr.execute(s)
        cn.commit()

    def get_all_translators(self):
        """
        Retrieve all translators from the database.

        Returns:
            list[Translator]: A list containing all translators stored in the database.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = "select * from translators"
        result = list(cr.execute(s))
        translators = []
        for translator in result:
            translators.append(Translator(
                translator[0], translator[1], translator[2]))
        return translators

    def insert_translator(self, translator: Translator):
        """
        Insert a new translator into the database.

        Args:
            translator (Translator): Translator object containing the information
                to be stored.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"Insert Into translators(name,family) Values ('{translator.name}','{translator.family}')"
        cr.execute(s)
        cn.commit()

    def delete_translator(self, id):
        """
        Delete a translator from the database.

        Args:
            id (int): Unique identifier of the translator to delete.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"delete from translators where id={id}"
        cr.execute(s)
        cn.commit()

    def update_translator(self, translator: Translator):
        """
        Update an existing translator in the database.

        Args:
            translator (Translator): Translator object containing the updated information.
        """
        cn = sqlite3.connect("library new.db")
        cr = cn.cursor()
        s = f"update translators set name='{translator.name}' , family='{translator.family}' where id={translator.id}"
        cr.execute(s)
        cn.commit()

    # def get_all_books(self):
        #"""
        #Retrieve all books from the database.

        #Returns:
            #list[Book]: A list containing all books stored in the database.
        #"""
        # cn = sqlite3.connect("library new.db")
        # cr = cn.cursor()
        # s = "select * from books"
        # result = list(cr.execute(s))
        # books = []
        # for book in result:
        # books.append(Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6],
        # book[7], book[8], book[9], book[10], book[11], book[12], book[13]))
        # return books

    # def get_all_rents(self):
        #"""
        #Retrieve all rents from the database.

        #Returns:
            #list[Rent]: A list containing all rental records stored in the database.
        #"""
        # cn = sqlite3.connect("library new.db")
        # cr = cn.cursor()
        # s = "select * from rents"
        # result = list(cr.execute(s))
        # rents = []
        # for rent in result:
        # rents.append(Rent(rent[0], rent[1], rent[2],
        # rent[3], rent[4], rent[5]))
        # return rents