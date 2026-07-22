# Python Library Management

A simple Library Management System built with Python and SQLite using Object-Oriented Programming (OOP).

This project demonstrates how to model a library database with Python classes and perform CRUD (Create, Read, Update, Delete) operations on multiple entities stored in an SQLite database.

---

## Features

- Object-Oriented Design (OOP)
- SQLite Database Integration
- CRUD Operations
- Modular Entity Classes
- Easy to Extend
- Well Documented Code

---

## Entities

The system includes the following entities:

- Roll
- Staff
- Member
- Author
- Donor
- Publisher
- Genre
- Designer
- Source
- Translator
- Book
- Rent

---

## CRUD Operations

The project currently supports CRUD operations for several entities, including:

- Author
- Publisher
- Genre
- Designer
- Source
- Translator

Each entity contains methods to:

- Retrieve all records
- Insert new records
- Update existing records
- Delete records

---

## Technologies

- Python 3
- SQLite3
- Object-Oriented Programming (OOP)

---

## Project Structure

```
project/
│
├── library.py
├── library new.db
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mahan-khoshdel/python-library-management.git
```

Move into the project directory:

```bash
cd python-library-management
```

---

## Usage

Run the Python file:

```bash
python library.py
```

The program connects to the SQLite database and demonstrates reading records from several tables such as:

- Authors
- Publishers
- Genres
- Designers
- Sources
- Translators

Sample insert, update, and delete operations are also included in the source code as examples.

---

## Database

The project uses SQLite as its database engine.

Before running the project, make sure the database file exists:

```
library new.db
```

The database should contain the required tables such as:

- authors
- publishers
- genres
- designers
- sources
- translators

---

## Learning Objectives

This project was created to practice:

- Python OOP
- Database Design
- SQLite Programming
- CRUD Operations
- Class Relationships
- Clean Code Structure

---

## Future Improvements

- Complete Book CRUD
- Complete Member CRUD
- Complete Staff CRUD
- Rental Management
- Search Functionality
- Command Line Interface (CLI)
- Exception Handling
- Parameterized SQL Queries
- Unit Tests

---

## License

This project is licensed under the MIT License.