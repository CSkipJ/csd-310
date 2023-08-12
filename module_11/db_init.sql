/*
    Title: jones-whatabook_init.sql
    Author: Charles Jones
    Date: 11 Aug 2023
    Description: whatabook database initialization script for final project.
*/


CREATE DATABASE whatabook1;

USE whatabook1;

DROP USER IF EXISTS 'whatabook_user'@'localhost';
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook1.* TO 'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;


-- drop tables if they exist
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;


CREATE TABLE user (
	user_ID		INT 			NOT NULL	AUTO_INCREMENT,
	last_name	VARCHAR(75) 	NOT NULL,
	first_name	VARCHAR(75)		NOT NULL,
	PRIMARY KEY(user_id)
	);

CREATE TABLE book (
	book_id		INT 			NOT NULL 	AUTO_INCREMENT,
	book_name	VARCHAR(200)	NOT NULL,
	details		VARCHAR(500),
	author		VARCHAR(200)	NOT NULL,
	PRIMARY KEY(book_id)
	);

CREATE TABLE wishlist (
	wishlist_id	INT 			NOT NULL 	AUTO_INCREMENT,
	user_id		INT 			NOT NULL,
	book_id 	INT 			NOT NULL,
	PRIMARY KEY(wishlist_id),
	CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES user(user_id),
	CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES book(book_id)
	);

CREATE TABLE store (
	store_id	INT 			NOT NULL	AUTO_INCREMENT,
	locale		VARCHAR(500)	NOT NULL,
	PRIMARY KEY(store_id)
	);

INSERT INTO user (first_name, last_name)
VALUES 	('Sophia', 'Anderson'),
		('Benjamin', 'Martinez'),
		('Olivia', 'Clark');

INSERT INTO book (book_name, details, author)
VALUES 	('The Enchanted Forest', 'A young adventurer goes on a magical journey through an enchanted forest where they meet all kinds of mystical creatures', 'Emily Turner'),
		('Shadows of the Moon', 'A young hero must embark on an epic quest to restore balance to the land of light and shadow', 'Benjamin Hart'),
		('Whispers of Eternity', 'Step into a world of ancient prophecies and forgotten legends as two unlikely heroes must decipher cryptic clues to unravel a hidden truth', 'Sophia Mitchell'),
		('The Clockwork Magician', 'Follow the adventures of a gifted young inventor as he faces off against a sinister magician in a steampunk dystopia', 'Alexander Harper'),
		('The Celestial Odyseey', 'Venture beyond to stars and across galaxies in a grand space odyssey', 'Isabella Morgan'),
		('Embers of War', 'Amidst a war-torn land, a group of unlikely heroes rise from the ashes to challenge tyranny and fight for a brighter future', 'Liam Roberts'),
		('The Aether Legacy', 'Uncover the secrets of an ancient civilization and harness the power of the mysterious substance known only as aether to protect the world from an impending doom', 'Emma Bennett'),
		('The Song of Stardust', 'Daniel Callisto is a young astrophysicist who uncovers a secret kept by the stars, that they sing. Only he can uncover the mysteries of the universe now that no one will believe him', 'Noah Foster'),
		('Chronicles of the Crimson Kingdom', 'In a realm of swords and sorcery, follow the intertwined destinies of warriors, mages, and monarchs as they navigate through treacherous political intrigues and engage in epic battles for domination over the Crimson Kingdom', 'Olivia Turner');

INSERT INTO store (locale)
VALUES	('123 Book St. Omaha, Nebraska 68108');

INSERT INTO wishlist (user_id, book_id)
VALUES 	(1, 3),
		(1, 5),
		(1, 7),
		(2, 4),
		(2, 6),
		(2, 8),
		(3, 1),
		(3, 9),
		(3, 8);
