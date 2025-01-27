CREATE DATABASE Estate;
USE Estate;

-- Creation of tables
CREATE TABLE Building (
    id INT PRIMARY KEY,
    addressNumber VARCHAR(10),
    addressStreet VARCHAR(100),
    addressPostalCode VARCHAR(10),
    addressCity VARCHAR(50),
    fiberOptic BOOLEAN,
    privateParking BOOLEAN
);

CREATE TABLE Apartment (
    building INT,
    number INT,
    description VARCHAR(255),
    rent DECIMAL(10, 2),
    area DECIMAL(10, 2),
    terrace BOOLEAN,
    energyClass VARCHAR(10),
    heating VARCHAR(50),
    parkingSpace BOOLEAN,
    parkingPrice DECIMAL(10, 2),
    PRIMARY KEY (building, number),
    FOREIGN KEY (building) REFERENCES Building(id)
);

CREATE TABLE Room (
    building INT,
    apartment INT,
    number INT,
    area DECIMAL(10, 2),
    function VARCHAR(50),
    PRIMARY KEY (building, apartment, number),
    FOREIGN KEY (building, apartment) REFERENCES Apartment(building, number)
);

CREATE TABLE Photo (
    number INT PRIMARY KEY,
    title VARCHAR(100),
    description VARCHAR(255),
    uri VARCHAR(255),
    building INT,
    apartment INT,
    FOREIGN KEY (building, apartment) REFERENCES Apartment(building, number)
);

-- Trigger to check that the parking space price is NULL if the apartment does not have a parking space
DELIMITER //

CREATE TRIGGER trg_check_parking_price
BEFORE INSERT ON Apartment
FOR EACH ROW
BEGIN
    IF NEW.parkingSpace = FALSE AND NEW.parkingPrice IS NOT NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The parking price must be NULL if parkingSpace is FALSE';
    END IF;
END; //

DELIMITER ;

-- Test for trg_check_parking_price
INSERT INTO Building (id, addressNumber, addressStreet, addressPostalCode, addressCity, fiberOptic, privateParking)
VALUES (1, '10', 'Avenue de la République', '75011', 'Paris', TRUE, TRUE);

INSERT INTO Apartment (building, number, description, rent, area, terrace, energyClass, heating, parkingSpace, parkingPrice)
VALUES (1, 101, 'Apartment with parking', 1200.00, 80, TRUE, 'A', 'Central', TRUE, 150.00);

INSERT INTO Apartment (building, number, description, rent, area, terrace, energyClass, heating, parkingSpace, parkingPrice)
VALUES (1, 102, 'Apartment without parking', 1000.00, 70, FALSE, 'B', 'Central', FALSE, 100.00);


-- Trigger to update the total area of an apartment when a room is inserted
DELIMITER //

CREATE TRIGGER trg_update_area_insert
AFTER INSERT ON Room
FOR EACH ROW
BEGIN
    UPDATE Apartment
    SET area = area + NEW.area
    WHERE building = NEW.building AND number = NEW.apartment;
END; //

DELIMITER ;

-- Test for trg_update_area_insert
INSERT INTO Apartment (building, number, description, rent, area, terrace, energyClass, heating, parkingSpace, parkingPrice)
VALUES (1, 201, 'Apartment with rooms', 1500.00, 0, FALSE, 'A', 'Central', TRUE, NULL);

INSERT INTO Room (building, apartment, number, area, function)
VALUES (1, 201, 1, 15.5, 'Bedroom');

INSERT INTO Room (building, apartment, number, area, function)
VALUES (1, 201, 2, 20.0, 'Living Room');

SELECT area FROM Apartment WHERE building = 1 AND number = 201;

-- Trigger to update the total area when a room is updated
DELIMITER //

CREATE TRIGGER trg_update_area_update
AFTER UPDATE ON Room
FOR EACH ROW
BEGIN
    UPDATE Apartment
    SET area = area - OLD.area + NEW.area
    WHERE building = NEW.building AND number = NEW.apartment;
END; //

DELIMITER ;

-- Test for trg_update_area_update
UPDATE Room
SET area = 18.0
WHERE building = 1 AND apartment = 201 AND number = 1;

SELECT area FROM Apartment WHERE building = 1 AND number = 201;

-- Trigger to update the total area when a room is deleted
DELIMITER //

CREATE TRIGGER trg_update_area_delete
AFTER DELETE ON Room
FOR EACH ROW
BEGIN
    UPDATE Apartment
    SET area = area - OLD.area
    WHERE building = OLD.building AND number = OLD.apartment;
END; //

DELIMITER ;

-- Test for trg_update_area_delete
DELETE FROM Room
WHERE building = 1 AND apartment = 201 AND number = 2;

SELECT area FROM Apartment WHERE building = 1 AND number = 201;

-- Extension of the trigger to check for private parking and initialize area to 0
DELIMITER //

CREATE TRIGGER trg_enforce_parking_and_initialize
BEFORE INSERT ON Apartment
FOR EACH ROW
BEGIN
    -- Check that the building has private parking if the apartment has a parking space
    IF NEW.parkingSpace = TRUE THEN
        DECLARE hasPrivateParking BOOLEAN;
        SELECT privateParking INTO hasPrivateParking FROM Building WHERE id = NEW.building;
        IF hasPrivateParking IS NULL OR hasPrivateParking = FALSE THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'An apartment cannot have a parking space if the building does not have private parking';
        END IF;
    END IF;

    -- Initialize the area to 0 if it is not specified
    IF NEW.area IS NULL THEN
        SET NEW.area = 0;
    END IF;
END; //

DELIMITER ;

-- Test for trg_enforce_parking_and_initialize
INSERT INTO Building (id, addressNumber, addressStreet, addressPostalCode, addressCity, fiberOptic, privateParking)
VALUES (2, '5', 'Rue du Soleil', '75001', 'Paris', TRUE, FALSE);

INSERT INTO Apartment (building, number, description, rent, area, terrace, energyClass, heating, parkingSpace, parkingPrice)
VALUES (2, 301, 'Apartment with parking', 2000.00, NULL, TRUE, 'A', 'Central', TRUE, 200.00);

INSERT INTO Apartment (building, number, description, rent, area, terrace, energyClass, heating, parkingSpace, parkingPrice)
VALUES (2, 302, 'Apartment without parking', 1500.00, NULL, FALSE, 'B', 'Electric', FALSE, NULL);

SELECT area FROM Apartment WHERE building = 2 AND number = 302;
