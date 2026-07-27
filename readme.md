# Python Library Management
A **Library Management System** developed with **Python**, **SQLite**, and **Object-Oriented Programming (OOP)**.

This project is about creating a simple library management system that can handle a lot of data. It's based on real-life things like books, authors, publishers, members, staff, and rental records. The system lets you add, view, change, and delete information in several database tables using SQLite.

This project is intended as a hands-on exercise in object-oriented programming, database interaction, and software design using Python.

---
# Table of Contents
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
# Overview
As the number of books, members, and transactions increases, manually managing library information becomes increasingly difficult.

This project is a simple way to store and manage library information using SQLite. It uses object-oriented programming, which means it represents real-world things as classes in Python. This makes the code easy to understand, fix, and add to.

The system currently supports complete create, read, update, and delete functions for several entities, which serves as a solid base for developing it into a comprehensive library management tool. This foundation allows for future expansion and enhancement of the application's capabilities.

---
# Features
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
# Technologies
| Technology | Description |
|------------|-------------|
| Python 3 | Main programming language |
| SQLite3 | Embedded relational database |
| Object-Oriented Programming | Software design approach |
| SQL | Database querying language |
---
# Database
The project uses **SQLite** as its database engine.

SQLite is lightweight, portable, and does not require a separate database server, making it a great choice for small-scale educational and desktop applications.

Database file:

```
library new.db
```
This program uses Python's built-in sqlite3 module to connect directly to the database.

---
# Project Structure
```
python-library-management/
│
├── main.py
├── models.py
├── library new.db
├── library new.sql
└── README.md
```
| File | Description |
|------|-------------|
| library.py | Main source code containing all classes and database operations |
| library new.db | SQLite database |
| README.md | Project documentation |
| .gitignore | Files ignored by Git |
---
# System Overview
The system models a real library environment using object-oriented programming principles.

Each class represents a different entity in the library, while the "Library" class acts as a central manager responsible for interacting with the SQLite database.

Current capabilities include:
- Retrieving records from database tables
- Inserting new records
- Updating existing records
- Deleting records
- Managing relationships between library entities

---
# Main Components
The project currently contains the following major components:
| Component | Purpose |
|-----------|---------|
| Data Model | Represents real-world library entities |
| SQLite Database | Stores all library information |
| CRUD Methods | Manage database records |
| Library Class | Central management class |
| Entity Classes | Represent books, members, authors, publishers, etc. |
---
# Design Pattern
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
The separation between entity classes and database methods makes it easier to maintain and expand the project in the future.

---
# Library Entities
The system is made up of a number of classes, each of which represents a real-life object you'd find in a library.

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
| Source | This is where you can find the books or information you need, like a reference or a citation. |
| Translator | Represents translators. |
| Book | This is what we call the items in our library collection. |
| Rent | Represents borrowing transactions. |
| Library | Handles all database operations. |
---
# Entity Fields
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
| national_code | int | This is a unique number that identifies a person in a country |
| roll | Roll | Staff role |
---
## Member
| Field | Type | Description |
|------|------|-------------|
| id | int | Member identifier |
| name | str | First name |
| family | str | Last name |
| national_code | int | This is a unique number that identifies a person in a country |
| registration_code | int | Membership code |
| expiration date | number | membership ends on this date |
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
# CRUD Operations
This project can currently perform basic operations like creating, reading, updating, and deleting data for several types of information stored in a SQLite database.
| Entity | Read | Insert | Update | Delete |
|---------|:---:|:------:|:------:|:------:|
| Author | Approved | Approved | Approved | Approved |
| Publisher | Yes | Yes | Yes | Yes |
It seems like the input is solely gibberish and doesn't contain any meaningful text. Therefore, the output will be an empty string.
| Designer | Yes | Yes | Yes | Yes |
No text is provided to rewrite.
| Translator | Approved | Approved | Approved | Approved |
| Roll | Time | Time | Time | Time |
| Employees | Time | Time | Time | Time |
| Member | Time | Time | Time | Time |
| Donor | Time | Time | Time | Time |
| Book | Time | Time | Time | Time |
| Rental Options | Time | Time | Time | Time | It looks like you're trying to create a table for rental options with time slots.
> ✅ Implemented
> ⏳ Planned for future implementation
---
# Database Tables
The SQLite database is organized into several tables that represent different entities.
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
# Methods Overview
The Library class is a way to work with the database. It has methods that let you do things with the data.
| Entity | Available Methods |
|---------|-------------------|
| Author | get_all(), insert(), update(), delete() |
| Publisher | get_all(), insert(), update(), delete() |
| Genre | get_all(), insert(), update(), delete() |
| Designer | get_all(), insert(), update(), delete() |
| Source | get_all(), insert(), update(), delete() |
| Translator | get_all(), insert(), update(), delete() |

Each of the CRUD methods talks directly to the SQLite database and then gives back Python objects that show the matching records.

---
# Requirements
Before you start this project, it's really important to have the right software installed on your computer.
| Software | Version |
|----------|---------|
| Python | 3.10 or later |
| SQLite | Built into Python (`sqlite3`) |

No external libraries are required.

---
# Installation
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
# How to use
When you start the project, it links up with a SQLite database and shows you different ways to add, remove, and change data.

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

When the results come back, they are changed into a format that Python can understand before being shown.

---
# Example Output
Example of retrieving authors from the database:
```
Authors

ID    Name       Family

1     Abbas      Maroufi
2     Simin      Daneshvar
3     Sadegh     Hedayat
```
Example of retrieving publishers:
```
Publishers

ID    Name

1     jangal
2     Ghoghnous
3     Negah
```
---
# Learning Objectives
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
# Future Improvements
This project can be expanded with additional features such as:
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
# Project Statistics
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
# Contributing
Contributions are welcome.

If you have a suggestion to improve the project, you can use the following:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

Bug reports and feature requests are also welcome.

---
# License
This project is released under the MIT License.

You're allowed to use, change, and share this project for learning or personal use.

---
# Author
Developed by **Mahan Khoshdel**

GitHub: https://github.com/mahan-khoshdel

If this project was helpful to you, consider giving it a star rating ⭐ on GitHub.