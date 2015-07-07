-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Droping the database if it already exists, creating it and then selelcting it
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;


-- Cretes a table of players which will hold all of the players of the tournament
-- Each player has an id and a name
CREATE TABLE players(
	id SERIAL PRIMARY KEY, 
	name TEXT
);

-- Creates a table that holds all the matches that are held. For each match you have
-- a winner and a user which will contain id corresponding to that person
-- relating back to the players table
CREATE TABLE matches (
	id SERIAL PRIMARY KEY, 
	winner INTEGER REFERENCES players(id), 
	loser INTEGER REFERENCES players(id)
);