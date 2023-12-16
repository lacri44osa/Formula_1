CREATE TABLE Personal_data(
    id integer PRIMARY KEY UNIQUE,
    passport_number int NOT NULL,
    passport_organ VARCHAR(100) NOT NULL,
    passport_date date NOT NULL,
    snils int NOT NULL,
    phone_number int NOT NULL
)

CREATE TABLE Visitor(
    id integer PRIMARY KEY UNIQUE,
    name varchar(100) NOT NULL,
    surname varchar(100)NOT NULL,
    middle_name varchar(100),
    ticket_number int,
    ticket_price int,
    seat_number int 
)

CREATE TABLE Violator(
    id integer PRIMARY KEY UNIQUE,
    FOREIGN KEY (seat_number_id) REFERENCES Visitor(seat_number) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (ticket_number_id) REFERENCES Visitor(ticket_number) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (name_id) REFERENCES Visitor(name) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (surname_id) REFERENCES Visitor(surname) ON DELETE NO ACTION ON UPDATE NO ACTION
)

CREATE TABLE Racer(
    id integer PRIMARY KEY UNIQUE,
    name varchar(100) NOT NULL,
    surname varchar(100) NOT NULL,
    middle_name varchar(100),
    team_name_id int NOT NULL,
    FOREIGN KEY (personal_data_id) REFERENCES Personal_data(id) ON DELETE NO ACTION ON UPDATE NO ACTION
)

CREATE TABLE Mechanics(
    id integer PRIMARY KEY UNIQUE,
    name varchar(100) NOT NULL,
    surname varchar(100) NOT NULL,
    middle_name varchar(100),
     team_name_id int NOT NULL,
     FOREIGN KEY (personal_data_id) REFERENCES Personal_data(id) ON DELETE NO ACTION ON UPDATE NO ACTION
)

CREATETABLE Spotter(
    id integer PRIMARY KEY UNIQUE,
    NAME varchar(100) NOT NULL,
    surname varchar(100) NOT NULL,
    middle_name varchar(100),
    team_name_id int NOT NULL,
    FOREIGN KEY (personal_data_id) REFERENCES Personal_data(id) ON DELETE NO ACTION ON UPDATE NO ACTION
)

CREATE TABLE Race_team(
    id integer PRIMARY KEY UNIQUE,
    team_name varchar(100) NOT NULL,
    FOREIGN KEY (mechanics_id) REFERENCES Mechanics(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (racer_id) REFERENCES Racer(id) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (spotter_id) REFERENCES Spotter(id) ON DELETE NO ACTION ON UPDATE NO ACTION
)

CREATE TABLE Car(
    id integer PRIMARY KEY UNIQUE,
    FOREIGN KEY (team_name_id) REFERENCES Race_team(team_name) ON DELETE SET NULL ON UPDATE NO ACTION,
    car_brand varchar(100) NOT NULL
)

CREATE TABLE Team Sponsor(
    id integer PRIMARY KEY UNIQUE,
    FOREIGN KEY (team_name_id) REFERENCES Race_team(team_name) ON DELETE CASCADE ON UPDATE NO ACTION,
    sponsor_name varchar(50)
)

CREATE TABLE Results(
    id integer PRIMARY KEY UNIQUE,
    FOREIGN KEY (team_name_id) REFERENCES Race_team(team_name) ON DELETE CASCADE ON UPDATE NO ACTION,
    place varchar(100) NOT NULL,
    time datetime
)