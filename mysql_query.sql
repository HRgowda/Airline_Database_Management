--Firstly use the created database
use airline_data;

CREATE TABLE IF NOT EXISTS Airline (
  Airline_id INT AUTO_INCREMENT PRIMARY KEY,
  Airline_name VARCHAR(50),
  Country VARCHAR(50),
  Aircraft_ID VARCHAR(50),
  Model VARCHAR(50),
  Capacity INT,
  Flight_Status VARCHAR(50)
);
select * from Airline;
INSERT INTO Airline(Airline_name, Country, Aircraft_ID, Model, Capacity, Flight_Status) VALUES ('Air India', 'India','1A-x','Airbus A319-100', 300, 'Active' );
INSERT INTO Airline(Airline_name, Country, Aircraft_ID, Model, Capacity, Flight_Status) VALUES ('Quatar Airways', 'Quatar','2B-x', 'Boeing 78 Dreamliner', 200, 'Active' );
INSERT INTO Airline(Airline_name, Country, Aircraft_ID, Model, Capacity, Flight_Status) VALUES ('Emirates', 'UAE','3C-x', 'Airbus A380', 250, 'Active');
select * from Airline;

