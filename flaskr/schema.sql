DROP TABLE IF EXISTS contactInfo;

CREATE TABLE contactInfo (
  id int PRIMARY KEY autoincrement,
  name varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  phone varchar(50) NOT NULL,
  messageBody text NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
