
-- Reference file for creating a MySQL Database from CSD310


-- Instruction 1 (Take Screenshot of CDL)
CREATE DATABASE whatabook;
SHOW DATABASES; --- just to check


-- Instruction 2 (Take Screenshot of the create user and maybe the priviledge execution)
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';


-- Instruction 3 (create the ORD from 10.2 take screenshot of everything)


-- create table user
CREATE TABLE user (
    user_id     INT             NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);

-- create table book
CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500)    NOT NULL,
    PRIMARY KEY(book_id)
);

-- create table wishlist
CREATE TABLE wishlist (
    wishlist_id INT             NOT NULL    AUTO_INCREMENT,
    user_id     INT             NOT NULL,
    book_id     INT             NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book      FOREIGN KEY (book_id)
    REFERENCES book(book_id),
    CONSTRAINT fk_user      FOREIGN KEY (user_id)
    REFERENCES user(user_id)
);

-- create table store
CREATE TABLE store(
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

-- Instruction 4 (insert records into table)
/*
1 store
9 books
3 users
1 wishlist for each user
*/

-- insert store record
INSERT INTO store(locale) VALUES ('100 Renaissance Center, Detroit, MI 48243');

-- insert book records x9
INSERT INTO book(book_name, author, details) VALUES('The Lightning Thief','Rick Riordan', 'The first book in the Percy Jackson and the Olympians Saga');
INSERT INTO book(book_name, author, details) VALUES('The Sea of Monsters', 'Rick Riordan', 'The second book in the Percy Jackson and the Olympians Saga');
INSERT INTO book(book_name, author, details) VALUES('Star Wars: Shadow of the Sith','Adam Christopher', 'The Empire is dead. Nearly two decades after the Battle of Endor...');
INSERT INTO book(book_name, author, details) VALUES('Star Wars: A New Dawn', 'John Jackson Miller', 'The war is over, The separatists have been defeated, and the Jedi rebellion...');
INSERT INTO book(book_name, author, details) VALUES('CISSP All-in-One Exam Guide, Ninth Edition', 'Fernando Maymi', 'Certified Information Systems Security Professional Exam guide.');
INSERT INTO book(book_name, author, details) VALUES('The Story of Doctor Dolittle', 'Melissa Dalton Martinez', 'A Doctor who can speak to and understand animals.');
INSERT INTO book(book_name, author, details) VALUES('Fairy Tale', 'Stephen King', 'The story follows Charlie Reade a highschooler, that may be a lot more special than you think');
INSERT INTO book(book_name, author, details) VALUES('Heir to the Darkmage', 'Lisa Cassidy', 'Ambition drives her. Danger thrills her. But magic always has a price.');
INSERT INTO book(book_name, author, details) VALUES('Mark of the Huntress', 'Lisa Cassidy', '2nd book: Loyalty. Magic. Ambition. Which will triumph');

-- insert users x3
INSERT INTO user(first_name, last_name) VALUES('James', 'Blazinhoff');
INSERT INTO user(first_name, last_name) VALUES('Luke', 'Skywalker');
INSERT INTO user(first_name, last_name) VALUES('Obi-wan', 'Kenobi');

-- insert wishlist stuff x3 for each user
-- User 1
INSERT INTO wishlist(user_id, book_id) VALUES(
    (SELECT user_id FROM user WHERE last_name = 'Blazinhoff'), 
    (SELECT book_id FROM book WHERE book_name = 'The Lightning Thief')

);
-- User 2
INSERT INTO wishlist(user_id, book_id) VALUES(
    (SELECT user_id FROM user WHERE last_name = 'Skywalker'), 
    (SELECT book_id FROM book WHERE book_name = 'Heir to the Darkmage')

);
-- User 3
INSERT INTO wishlist(user_id, book_id) VALUES(
    (SELECT user_id FROM user WHERE last_name = 'Kenobi'), 
    (SELECT book_id FROM book WHERE book_name = 'The Story of Doctor Dolittle')

);
