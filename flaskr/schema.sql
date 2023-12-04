-- Clear old contents. 
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS administrators;
DROP TABLE IF EXISTS maps;
DROP TABLE IF EXISTS sprites;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS existing_entities;

-- Create the user table. 
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    authority INTEGER NOT NULL
);

-- Create the admin table. 
CREATE TABLE administrators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL, 
    authority INTEGER NOT NULL
);

-- Create the map table.
CREATE TABLE maps (
    id INTEGER PRIMARY KEY, 
    row_id INTEGER NOT NULL,
    row_content TEXT NOT NULL
); 

-- Create the sprites table. 
CREATE TABLE sprites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT UNIQUE NOT NULL,
    health INTEGER NOT NULL, 
    hunger INTEGER NOT NULL, 
    thirst INTEGER NOT NULL, 
    excitement INTEGER NOT NULL,
    strength INTEGER NOT NULL,

    symbol TEXT UNIQUE NOT NULL
);

-- Create the items table. 
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT UNIQUE NOT NULL,
    health INTEGER NOT NULL, 
    hunger INTEGER NOT NULL, 
    thirst INTEGER NOT NULL, 
    excitement INTEGER NOT NULL,
    strength INTEGER NOT NULL,

    symbol TEXT UNIQUE NOT NULL
);

-- Create the existing_entities table.
CREATE TABLE existing_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT UNIQUE NOT NULL,
    health INTEGER NOT NULL, 
    hunger INTEGER NOT NULL, 
    thirst INTEGER NOT NULL, 
    excitement INTEGER NOT NULL,
    strength INTEGER NOT NULL,

    map_id INTEGER NOT NULL,
    position_x INTEGER NOT NULL,
    position_y INTEGER NOT NULL, 
    entity_owner TEXT UNIQUE NOT NULL

); 