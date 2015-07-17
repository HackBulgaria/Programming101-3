DROP TABLE IF EXISTS Domains;

CREATE TABLE Domains(
  domain_id INTEGER PRIMARY KEY,
  domain TEXT UNIQUE,
  visited INTEGER
);

DROP TABLE IF EXISTS Links;

CREATE TABLE Links(
  link_id INTEGER PRIMARY KEY,
  url TEXT UNIQUE,
  domain_id INTEGER,
  FOREIGN KEY(domain_id) REFERENCES Domains(domain_id)
);

DROP TABLE IF EXISTS Servers;

CREATE TABLE Servers(
  server_id INTEGER PRIMARY KEY,
  link_id INTEGER,
  url TEXT,
  server_string TEXT,
  FOREIGN KEY(link_id) REFERENCES Links(link_id)
);


INSERT INTO Domains(domain, visited)
VALUES ("http://start.bg", 0);

