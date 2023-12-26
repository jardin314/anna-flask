DROP TABLE IF EXISTS contactInfo;
DROP TABLE IF EXISTS user;

CREATE TABLE contactInfo (
  id integer PRIMARY KEY AUTOINCREMENT,
  name varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  phone varchar(50) NOT NULL,
  messageBody text NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT unique NOT NULL,
  password TEXT NOT NULL
);
