CREATE DATABASE FPJ;
USE FPJ;

-- Creation of tables with integrity constraints
CREATE TABLE SUPPLIER (
    codsup VARCHAR(10) PRIMARY KEY,
    namesup VARCHAR(50),
    citysup VARCHAR(50),
    telsup VARCHAR(15)
);

CREATE TABLE DIRECTOR (
    coddirector VARCHAR(10) PRIMARY KEY,
    namdirector VARCHAR(50)
);

CREATE TABLE PROJECT (
    codproj VARCHAR(10) PRIMARY KEY,
    nameproj VARCHAR(100),
    cityproj VARCHAR(50),
    budgetproj DECIMAL(15, 2),
    coddirector VARCHAR(10),
    FOREIGN KEY (coddirector) REFERENCES DIRECTOR(coddirector)
);

CREATE TABLE PART (
    codpart VARCHAR(10) PRIMARY KEY,
    namepart VARCHAR(100),
    colorpart VARCHAR(20),
    weightpart DECIMAL(10, 2),
    citypart VARCHAR(50)
);

CREATE TABLE FPJ (
    codsup VARCHAR(10),
    codpart VARCHAR(10),
    codproj VARCHAR(10),
    qtydelivered INT,
    date_del DATE,
    PRIMARY KEY (codsup, codpart, codproj),
    FOREIGN KEY (codsup) REFERENCES SUPPLIER(codsup),
    FOREIGN KEY (codpart) REFERENCES PART(codpart),
    FOREIGN KEY (codproj) REFERENCES PROJECT(codproj)
);

-- Inserting data
INSERT INTO SUPPLIER VALUES
('S1', 'Alterna', 'Tunis', '71001001'),
('S2', 'Butagaz', 'Tunis', '71123123'),
('S3', 'EDF', 'Nabeul', '72234432');

INSERT INTO DIRECTOR VALUES
('D1', 'Sami Ktata'),
('D2', 'Anis Ksontini'),
('D3', 'Taieb Falfel');

INSERT INTO PROJECT VALUES
('P1', 'Gas Production', 'Gabes', 2590000, 'D2'),
('P2', 'Gas Production', 'Touzeur', 2055000, 'D1'),
('P3', 'Electricity Production', 'Tabarka', 2040000, 'D3');

INSERT INTO PART VALUES
('P1', 'Power Cable', 'Blue', 200, 'Sfax'),
('P2', 'Measuring Device', 'White', 0.44, 'Sfax'),
('P3', 'Feeder', 'Black', 1.5, 'Sfax');

INSERT INTO FPJ VALUES
('S1', 'P1', 'P1', 20, '2019-10-10'),
('S1', 'P2', 'P1', 15, '2019-07-19'),
('S1', 'P3', 'P3', 13, '2019-11-13');

-- Give the part numbers intended for any project happening in the same city as the supplier of those parts.
SELECT DISTINCT FPJ.codpart
FROM FPJ
JOIN SUPPLIER ON FPJ.codsup = SUPPLIER.codsup
JOIN PROJECT ON FPJ.codproj = PROJECT.codproj
WHERE SUPPLIER.citysup = PROJECT.cityproj;

-- Give the project numbers where at least one of the suppliers is not in the same city as where the project is taking place.
SELECT DISTINCT FPJ.codproj
FROM FPJ
JOIN SUPPLIER ON FPJ.codsup = SUPPLIER.codsup
JOIN PROJECT ON FPJ.codproj = PROJECT.codproj
WHERE SUPPLIER.citysup != PROJECT.cityproj;

-- Give the project numbers that use at least one part supplied by 'S3'.
SELECT DISTINCT FPJ.codproj
FROM FPJ
WHERE FPJ.codsup = 'S3';

-- Which projects have the second letter of their name as 'E'?
SELECT codproj
FROM PROJECT
WHERE nameproj LIKE '_E%';

-- Which projects have a director's name ending in 'A'?
SELECT PROJECT.codproj
FROM PROJECT
JOIN DIRECTOR ON PROJECT.coddirector = DIRECTOR.coddirector
WHERE DIRECTOR.namdirector LIKE '%A';

-- How many times has each part been delivered?
SELECT FPJ.codpart, COUNT(*) AS delivery_count
FROM FPJ
GROUP BY FPJ.codpart;

-- How many deliveries were made between 01/01/19 and 01/01/20 by supplier 'S2'?
SELECT COUNT(*) AS delivery_count
FROM FPJ
WHERE FPJ.codsup = 'S2'
  AND FPJ.date_del BETWEEN '2019-01-01' AND '2020-01-01';

-- What is the part with the highest quantity delivered for project 'P1'?
SELECT codpart, MAX(qtydelivered) AS max_quantity
FROM FPJ
WHERE codproj = 'P1'
GROUP BY codpart
ORDER BY max_quantity DESC
LIMIT 1;

-- What is the weight of the part that has been delivered the most?
SELECT PART.weightpart
FROM FPJ
JOIN PART ON FPJ.codpart = PART.codpart
GROUP BY FPJ.codpart, PART.weightpart
ORDER BY COUNT(*) DESC
LIMIT 1;

-- Which parts have never been delivered to projects in 'PARIS'?
SELECT DISTINCT PART.codpart
FROM PART
WHERE PART.codpart NOT IN (
    SELECT FPJ.codpart
    FROM FPJ
    JOIN PROJECT ON FPJ.codproj = PROJECT.codproj
    WHERE PROJECT.cityproj = 'PARIS'
);

-- Which projects have received all the parts?
SELECT PROJECT.codproj
FROM PROJECT
WHERE NOT EXISTS (
    SELECT PART.codpart
    FROM PART
    WHERE PART.codpart NOT IN (
        SELECT FPJ.codpart
        FROM FPJ
        WHERE FPJ.codproj = PROJECT.codproj
    )
);

-- Add 1000 to the budgets of projects in PARIS that have received more than 10 deliveries from suppliers not from PARIS.
UPDATE PROJECT
SET budgetproj = budgetproj + 1000
WHERE cityproj = 'PARIS'
  AND codproj IN (
      SELECT FPJ.codproj
      FROM FPJ
      JOIN SUPPLIER ON FPJ.codsup = SUPPLIER.codsup
      WHERE SUPPLIER.citysup != 'PARIS'
      GROUP BY FPJ.codproj
      HAVING COUNT(*) > 10
  );

-- Change the color of all red parts to orange.
UPDATE PART
SET colorpart = 'Orange'
WHERE colorpart = 'Red';

-- Delete all projects for which there have been no deliveries.
DELETE FROM PROJECT
WHERE codproj NOT IN (
    SELECT DISTINCT codproj
    FROM FPJ
);

-- Increase by 10% all deliveries made by suppliers of red spare parts.
UPDATE FPJ
SET qtydelivered = qtydelivered * 1.1
WHERE codpart IN (
    SELECT codpart
    FROM PART
    WHERE colorpart = 'Red'
);
