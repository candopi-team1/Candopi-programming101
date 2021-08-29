USE hmkmovies;

INSERT INTO studios (name, funding) VALUES('Warner Bros',  200);
INSERT INTO studios (name, funding) VALUES('Fox',  300);
INSERT INTO studios (name, funding) VALUES('MGM',  280);
INSERT INTO studios (name, funding) VALUES('Disney',  500);
INSERT INTO studios (name, funding) VALUES('Raintree',  600);
INSERT INTO studios (name, funding) VALUES('Shaw Bros', 720);


INSERT INTO Movies ( title, year ,studio_id) VALUES('The Good,the Bad,and the Ugly', '1923', 1);
INSERT INTO Movies ( title, year ,studio_id) VALUES('A few Good Men', '1923', 2);

INSERT INTO Movies ( title, year ,studio_id) VALUES('Harry Potter and the Deathly Hallows', '2001', 6);
INSERT INTO Movies ( title, year, studio_id) VALUES('James Bond : Skyfall', '2013', 6);
INSERT INTO Movies ( title, year, studio_id) VALUES('Sky Craters', '2013', 6);
INSERT INTO Movies ( title, year, studio_id) VALUES('Sky Gladiators', '2013', 4);

INSERT INTO Movies ( title, year,studio_id) VALUES('Top Gun', '1998', 3);
INSERT INTO Movies ( title, year,studio_id) VALUES('Young Guns', '1998', 3);
INSERT INTO Movies ( title, year ,studio_id) VALUES('Johnny English', '2008', 4);
INSERT INTO Movies ( title, year ,studio_id) VALUES('Johnny English Reborn', '2012', 4);


INSERT INTO Actors ( name, birthdate, fees)
VALUES('John Wayne', ' 12 Feb 1872', '20000');
INSERT INTO Actors ( name, birthdate, fees)
VALUES('Tom Cruise', '25 Nov 1976', '50000');
INSERT INTO Actors ( name, birthdate, fees)
VALUES('Daniel Craig', '3 Jul 1983', '27000');
INSERT INTO Actors ( name, birthdate, fees)
VALUES('Daniel Radcliffe', '30 Apr 1990', '15000');
INSERT INTO Actors ( name, birthdate, fees)
VALUES('Rowan Aktinson', '18 Jun 1989', '34000');

INSERT INTO actor_movie ( actor_id, movie_id) Values(1 , 1 );
INSERT INTO actor_movie ( actor_id, movie_id) Values( 1, 2);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 2, 2);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 2, 7);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 2, 5);

INSERT INTO actor_movie ( actor_id, movie_id) Values(  3 ,4 );
INSERT INTO actor_movie ( actor_id, movie_id) Values(  3 , 5);
INSERT INTO actor_movie ( actor_id, movie_id) Values(  3 , 6);


INSERT INTO actor_movie ( actor_id, movie_id) Values(  4, 3); 
INSERT INTO actor_movie ( actor_id, movie_id) Values(  4, 6); 


INSERT INTO actor_movie ( actor_id, movie_id) Values( 5, 9);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 5, 10);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 5, 1);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 5, 2);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 5, 3);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 5, 4);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 5, 5);
INSERT INTO actor_movie ( actor_id, movie_id) Values( 5, 6);

INSERT INTO studio_contact ( name,   address,   phone,  studio_id) VALUES('' , 'California', '555-7813-15', 1);
INSERT INTO studio_contact ( name,   address,   phone,  studio_id) VALUES('' , 'New York', '555-8245-32', 2);
INSERT INTO studio_contact ( name,   address,   phone,  studio_id) VALUES('' , '123 Hollywod', '555-314-55', 3);

INSERT INTO studio_contact ( name,   address,   phone,  studio_id) VALUES('' , '23 Disneyland', '555-1234-55', 4);
INSERT INTO studio_contact ( name,   address,   phone,  studio_id) VALUES('' , 'Caldecott Hill', '94681590', 5);
INSERT INTO studio_contact ( name,   address,   phone,  studio_id) VALUES('' , '123 Hongkong', '555-2534-55', 6);

INSERT INTO actor_contact ( name,   address,   phone,  actor_id) VALUES('' , 'Wild West', '555-1424-24',  1);
INSERT INTO actor_contact ( name,   address,   phone,  actor_id) VALUES('' , 'Air Force', '555-4208-58',  2);
INSERT INTO actor_contact ( name,   address,   phone,  actor_id) VALUES('' , 'M17 HQ', '555-8274-02',  3);

INSERT INTO actor_contact ( name,   address,   phone,  actor_id) VALUES('' , 'Hogwarts', '555-9144-39',  4);
INSERT INTO actor_contact ( name,   address,   phone,  actor_id) VALUES('' , 'Joke Academy', '555-0259-42',  5);



