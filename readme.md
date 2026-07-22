# 📚 Python Library Management

A **Library Management System** developed with **Python**, **SQLite**, and **Object-Oriented Programming (OOP)**.

This project demonstrates how to build a simple yet extensible library management system by modeling real-world entities such as books, authors, publishers, members, staff, and rental records. It also provides CRUD (Create, Read, Update, Delete) operations for several database tables using SQLite.

The project is intended as a practical exercise in object-oriented programming, database interaction, and software design using Python.

---

# 📑 Table of Contents

- Overview
- Features
- Technologies
- Project Structure
- Database
- System Overview
- Library Entities
- CRUD Operations
- Class Fields
- Database Tables
- Methods Overview
- Installation
- Requirements
- Usage
- Example Output
- Learning Objectives
- Future Improvements
- Project Statistics
- Contributing
- License

---

# 📖 Overview

Managing library information manually becomes increasingly difficult as the number of books, members, and transactions grows.

This project provides a simple object-oriented solution that stores and manages library information using SQLite. Every real-world object inside the system is represented as a Python class, making the code easier to understand, maintain, and extend.

The current implementation includes complete CRUD operations for several entities and lays the foundation for expanding the system into a fully functional library management application.

---

# ✨ Features

- Object-Oriented Programming (OOP)
- SQLite Database Integration
- Multiple Related Entities
- CRUD Operations
- Clean Class Design
- Easy-to-read Source Code
- Extensible Architecture
- Database-backed Data Storage
- Simple Python Implementation
- Beginner-Friendly Project

---

# 🛠 Technologies

| Technology | Description |
|------------|-------------|
| Python 3 | Main programming language |
| SQLite3 | Embedded relational database |
| Object-Oriented Programming | Software design approach |
| SQL | Database querying language |

---

# 🗄 Database

The project uses **SQLite** as its database engine.

SQLite is lightweight, portable, and does not require a separate database server, making it an excellent choice for educational and small-scale desktop applications.

Database file:

```
library new.db
```

The application connects directly to the database using Python's built-in **sqlite3** module.

---

# 📂 Project Structure

```
python-library-management/
│
├── library.py
├── library new.db
├── README.md
├── LICENSE
└── .gitignore
```

| File | Description |
|------|-------------|
| library.py | Main source code containing all classes and database operations |
| library new.db | SQLite database |
| README.md | Project documentation |
| LICENSE | Project license |
| .gitignore | Files ignored by Git |

---

# 🏛 System Overview

The system models a real-world library environment using object-oriented programming principles.

Each class represents a different entity within the library, while the `Library` class acts as the central manager responsible for interacting with the SQLite database.

Current capabilities include:

- Retrieving records from database tables
- Inserting new records
- Updating existing records
- Deleting records
- Managing relationships between library entities

---

# 📦 Main Components

The project currently contains the following major components:

| Component | Purpose |
|-----------|---------|
| Data Model | Represents real-world library entities |
| SQLite Database | Stores all library information |
| CRUD Methods | Manage database records |
| Library Class | Central management class |
| Entity Classes | Represent books, members, authors, publishers, etc. |

---

# 🏗 Design Pattern

The project follows a simple object-oriented architecture.

```
SQLite Database
        │
        ▼
    Library Class
        │
 ┌──────┼───────────────┐
 │      │               │
 ▼      ▼               ▼
Authors Publishers   Translators
 │
 ▼
Books
 │
 ▼
Members
 │
 ▼
Rent Records
```

The separation between entity classes and database methods makes the project easier to maintain and expand in the future.

---

# 🏷 Library Entities

The system is composed of multiple classes that model real-world objects inside a library.

| Entity | Description |
|---------|-------------|
| Roll | Represents staff roles. |
| Staff | Represents library employees. |
| Member | Represents registered library members. |
| Author | Represents book authors. |
| Donor | Represents book donors. |
| Publisher | Represents publishing companies. |
| Genre | Represents book categories. |
| Designer | Represents book designers. |
| Source | Represents book sources or references. |
| Translator | Represents translators. |
| Book | Represents books in the library. |
| Rent | Represents borrowing transactions. |
| Library | Handles all database operations. |

---

# 📖 Entity Fields

## Roll

| Field | Type | Description |
|------|------|-------------|
| id | int | Unique role identifier |
| name | str | Role name |

---

## Staff

| Field | Type | Description |
|------|------|-------------|
| id | int | Staff identifier |
| name | str | First name |
| family | str | Last name |
| national_code | int | National identification number |
| roll | Roll | Staff role |

---

## Member

| Field | Type | Description |
|------|------|-------------|
| id | int | Member identifier |
| name | str | First name |
| family | str | Last name |
| national_code | int | National identification number |
| registration_code | int | Membership code |
| expiration_date | int | Membership expiration date |

---

## Author

| Field | Type | Description |
|------|------|-------------|
| id | int | Author identifier |
| name | str | First name |
| family | str | Last name |

---

## Donor

| Field | Type | Description |
|------|------|-------------|
| id | int | Donor identifier |
| name | str | First name |
| family | str | Last name |

---

## Publisher

| Field | Type | Description |
|------|------|-------------|
| id | int | Publisher identifier |
| name | str | Publisher name |
| address | str | Company address |
| phone_number | str | Contact number |
| email | str | Email address |

---

## Genre

| Field | Type | Description |
|------|------|-------------|
| id | int | Genre identifier |
| name | str | Genre name |

---

## Designer

| Field | Type | Description |
|------|------|-------------|
| id | int | Designer identifier |
| name | str | First name |
| family | str | Last name |

---

## Source

| Field | Type | Description |
|------|------|-------------|
| id | int | Source identifier |
| name | str | Source name |
| author_name | str | Source author |

---

## Translator

| Field | Type | Description |
|------|------|-------------|
| id | int | Translator identifier |
| name | str | First name |
| family | str | Last name |

---

## Book

| Field | Type | Description |
|------|------|-------------|
| id | int | Book identifier |
| title | str | Book title |
| year_of_publication | int | Publication year |
| price | float | Book price |
| print_turn | int | Edition number |
| circulation | int | Number of printed copies |
| isbn | str | ISBN code |
| publisher | Publisher | Related publisher |
| designer | Designer | Book designer |
| authors | list | Book authors |
| translators | list | Book translators |
| genres | list | Book genres |
| donors | list | Book donors |
| sources | list | Book sources |

---

## Rent

| Field | Type | Description |
|------|------|-------------|
| id | int | Rental identifier |
| received_date | str | Borrow date |
| return_date | str | Return date |
| member | Member | Borrowing member |
| staff | Staff | Responsible staff |
| book | Book | Borrowed book |

---

# ⚙ CRUD Operations

The project currently implements CRUD functionality for several entities stored in the SQLite database.

| Entity | Read | Insert | Update | Delete |
|---------|:---:|:------:|:------:|:------:|
| Author | ✅ | ✅ | ✅ | ✅ |
| Publisher | ✅ | ✅ | ✅ | ✅ |
| Genre | ✅ | ✅ | ✅ | ✅ |
| Designer | ✅ | ✅ | ✅ | ✅ |
| Source | ✅ | ✅ | ✅ | ✅ |
| Translator | ✅ | ✅ | ✅ | ✅ |
| Roll | ⏳ | ⏳ | ⏳ | ⏳ |
| Staff | ⏳ | ⏳ | ⏳ | ⏳ |
| Member | ⏳ | ⏳ | ⏳ | ⏳ |
| Donor | ⏳ | ⏳ | ⏳ | ⏳ |
| Book | ⏳ | ⏳ | ⏳ | ⏳ |
| Rent | ⏳ | ⏳ | ⏳ | ⏳ |

> ✅ Implemented  
> ⏳ Planned for future implementation

---

# 🗃 Database Tables

The SQLite database is organized into multiple tables representing different entities.

| Table | Description |
|--------|-------------|
| rolls | Staff roles |
| staffs | Library staff |
| members | Registered members |
| authors | Author information |
| donors | Donor information |
| publishers | Publisher information |
| genres | Book genres |
| designers | Book designers |
| sources | Book sources |
| translators | Translator information |
| books | Book information |
| rents | Rental records |

---

# 🔧 Methods Overview

The `Library` class provides methods for interacting with the database.

| Entity | Available Methods |
|---------|-------------------|
| Author | get_all(), insert(), update(), delete() |
| Publisher | get_all(), insert(), update(), delete() |
| Genre | get_all(), insert(), update(), delete() |
| Designer | get_all(), insert(), update(), delete() |
| Source | get_all(), insert(), update(), delete() |
| Translator | get_all(), insert(), update(), delete() |

Each CRUD method communicates directly with the SQLite database and returns Python objects representing the corresponding records.

---

# ⚙ Requirements

Before running this project, make sure the following software is installed on your system.

| Software | Version |
|----------|---------|
| Python | 3.10 or later |
| SQLite | Built into Python (`sqlite3`) |

No external libraries are required.

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/mahan-khoshdel/python-library-management.git
```

Navigate to the project directory:

```bash
cd python-library-management
```

Make sure the database file exists:

```
library new.db
```

Run the application:

```bash
python library.py
```

---

# ▶ Usage

After running the project, the application connects to the SQLite database and demonstrates different CRUD operations.

Examples include:

- Reading all authors
- Reading all publishers
- Reading all genres
- Reading all designers
- Reading all translators
- Reading all sources
- Inserting new records
- Updating existing records
- Deleting records

The returned records are converted into Python objects before being displayed.

---

# 💻 Example Output

Example of retrieving authors from the database:

```
Authors

ID    Name       Family

1     George     Orwell
2     Jane       Austen
3     Leo        Tolstoy
```

Example of retrieving publishers:

```
Publishers

ID    Name

1     O'Reilly
2     Penguin
3     Pearson
```

---

# 🧠 Learning Objectives

This project was developed to improve practical knowledge in:

- Object-Oriented Programming (OOP)
- Python Class Design
- SQLite Database Programming
- CRUD Operations
- SQL Statements
- Database Modeling
- Code Organization
- Data Relationships
- Python Data Structures
- Software Design Principles

---

# 🚧 Future Improvements

The project can be extended with additional features such as:

- Complete CRUD operations for all entities
- Book management
- Member management
- Staff management
- Rental management
- Book reservation system
- Search by title, author, ISBN, and publisher
- Login and authentication
- Fine calculation for overdue books
- Dashboard and reports
- Command Line Interface (CLI)
- Graphical User Interface (GUI)
- Logging
- Exception handling
- Parameterized SQL queries
- Unit testing
- Documentation generation

---

# 📊 Project Statistics

| Item | Value |
|------|------:|
| Programming Language | Python |
| Database | SQLite |
| Programming Style | Object-Oriented Programming |
| Database Tables | 12 |
| Entity Classes | 12 |
| CRUD Modules | 6 |
| External Dependencies | None |

---

# 🤝 Contributing

Contributions are welcome.

If you have suggestions for improving the project, feel free to:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

Bug reports and feature requests are also appreciated.

---

# 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.

---

# 👨‍💻 Author

Developed by **Mahan Khoshdel**

GitHub: https://github.com/mahan-khoshdel

If you found this project helpful, consider giving it a ⭐ on GitHub.