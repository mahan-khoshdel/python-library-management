DROP TABLE IF EXISTS books ;
CREATE TABLE IF NOT EXISTS books (
id integer PRIMARY KEY AUTOINCREMENT ,
title varchar (20) , 
year_of_publication integer ,
price integer ,
print_turn integer ,
circulation integer ,
ISBN integer ,
publisher_id integer ,
designer_id integer
);

DROP TABLE IF EXISTS staff ;
CREATE TABLE IF NOT EXISTS staff (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20) ,
family varchar (20) ,
national_code integer ,
roll_id integer
);

DROP TABLE IF EXISTS members ;
CREATE TABLE IF NOT EXISTS members (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20) ,
family varchar (20) ,
national_code integer ,
registration_date integer ,
expiration_date integer
);

DROP TABLE IF EXISTS authors ;
CREATE TABLE IF NOT EXISTS authors (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20) ,
family varchar (20)
);

DROP TABLE IF EXISTS donors ;
CREATE TABLE IF NOT EXISTS donors (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20) ,
family varchar (20) ,
national_code integer
);

DROP TABLE IF EXISTS publishers ;
CREATE TABLE IF NOT EXISTS publishers (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20) ,
address varchar (30) ,
phone_number integer ,
email varchar (30)
);

DROP TABLE IF EXISTS genres ;
CREATE TABLE IF NOT EXISTS genres (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20)
);

DROP TABLE IF EXISTS designers ;
CREATE TABLE IF NOT EXISTS designers (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20) ,
family varchar (30)
);

DROP TABLE IF EXISTS sources ;
CREATE TABLE IF NOT EXISTS sources (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (30) ,
author_name varchar (30)
);

DROP TABLE IF EXISTS translators ;
CREATE TABLE IF NOT EXISTS translators (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20) ,
family varchar (20)
);

DROP TABLE IF EXISTS rents ;
CREATE TABLE IF NOT EXISTS rents (
id integer PRIMARY KEY AUTOINCREMENT ,
received_date integer ,
return_date integer ,
book_id integer ,
member_id integer ,
staff_id integer
);

DROP TABLE IF EXISTS rolls ;
CREATE TABLE IF NOT EXISTS rolls (
id integer PRIMARY KEY AUTOINCREMENT ,
name varchar (20)
);

DROP TABLE IF EXISTS book_source ;
CREATE TABLE IF NOT EXISTS book_source (
id integer PRIMARY KEY AUTOINCREMENT ,
book_id integer ,
source_id integer
);

DROP TABLE IF EXISTS book_translator ;
CREATE TABLE IF NOT EXISTS book_translator (
id integer PRIMARY KEY AUTOINCREMENT ,
book_id integer ,
translator_id integer
);

DROP TABLE IF EXISTS book_author ;
CREATE TABLE IF NOT EXISTS book_author (
id integer PRIMARY KEY AUTOINCREMENT ,
book_id integer ,
author_id integer
);

DROP TABLE IF EXISTS book_genre ;
CREATE TABLE IF NOT EXISTS book_genre (
id integer PRIMARY KEY AUTOINCREMENT ,
book_id integer ,
genre_id integer
);

DROP TABLE IF EXISTS book_donor ;
CREATE TABLE IF NOT EXISTS book_donor (
id integer PRIMARY KEY AUTOINCREMENT ,
book_id integer ,
donor_id integer
);