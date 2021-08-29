DROP DATABASE IF EXISTS hmkmovies;

CREATE DATABASE IF NOT EXISTS hmkmovies;
GRANT ALL PRIVILEGES ON hmkmovies.* TO 'hmkmovies'@'localhost' IDENTIFIED BY 'hmkmoviespass';

USE hmkmovies;

CREATE TABLE studios (
  id int(10) NOT NULL AUTO_INCREMENT,
  name varchar(250) NOT NULL,
  funding int(10) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE movies (
  id int(10) NOT NULL AUTO_INCREMENT,
  title varchar(250) NOT NULL,
  year int(5) NOT NULL,
  studio_id int(10) NOT NULL, 
  PRIMARY KEY (id),
  FOREIGN KEY (studio_id) REFERENCES studios (id) 
);

CREATE TABLE actors (
  id int(10) NOT NULL AUTO_INCREMENT,
  name varchar(250) NOT NULL,
  birthdate varchar(100) NOT NULL,
  fees int(20) NOT NULL,
  PRIMARY KEY (id)
);


CREATE TABLE actor_movie (
    /*   id int(10) NOT NULL AUTO_INCREMENT, */
    actor_id int(10) NOT NULL,   
    movie_id int(10) NOT NULL,    
    FOREIGN KEY (actor_id) REFERENCES actors (id) ,
    FOREIGN KEY (movie_id) REFERENCES movies (id) 
);

CREATE TABLE studio_contact (
  id int(10) NOT NULL AUTO_INCREMENT,
  name varchar(250) NOT NULL,
  address varchar(250) NOT NULL,
  phone varchar(250) NOT NULL,
  studio_id int(10) NOT NULL, 
  PRIMARY KEY (id),
  FOREIGN KEY (studio_id) REFERENCES studios (id) 
);


CREATE TABLE actor_contact (
  id int(10) NOT NULL AUTO_INCREMENT,
  name varchar(250) NOT NULL,
  address varchar(250) NOT NULL,
  phone varchar(250) NOT NULL,
  actor_id int(10) NOT NULL, 
  PRIMARY KEY (id),
  FOREIGN KEY (actor_id) REFERENCES actors (id) 
);

