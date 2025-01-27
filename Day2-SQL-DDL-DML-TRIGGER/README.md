# Day2-SQL-DDL-DML-TRIGGER
## FPJ Database Project

### Overview
The FPJ database is designed to manage information about suppliers, directors, projects, parts, and the relationships between them. It implements complex queries, constraints, and data manipulation operations to manage and analyze deliveries of parts to various projects.

This project is built with a relational structure and includes comprehensive SQL queries to extract insights and enforce business rules.

### Tables

#### 1. `SUPPLIER`
Stores information about suppliers.
- `codsup` (VARCHAR) - Primary key, unique identifier for the supplier.
- `namesup` (VARCHAR) - Name of the supplier.
- `citysup` (VARCHAR) - City where the supplier is located.
- `telsup` (VARCHAR) - Telephone number of the supplier.

#### 2. `DIRECTOR`
Stores information about directors overseeing projects.
- `coddirector` (VARCHAR) - Primary key, unique identifier for the director.
- `namdirector` (VARCHAR) - Name of the director.

#### 3. `PROJECT`
Stores details about projects.
- `codproj` (VARCHAR) - Primary key, unique identifier for the project.
- `nameproj` (VARCHAR) - Name of the project.
- `cityproj` (VARCHAR) - City where the project is located.
- `budgetproj` (DECIMAL) - Budget allocated for the project.
- `coddirector` (VARCHAR) - Foreign key referring to `DIRECTOR(coddirector)`.

#### 4. `PART`
Stores information about parts used in projects.
- `codpart` (VARCHAR) - Primary key, unique identifier for the part.
- `namepart` (VARCHAR) - Name of the part.
- `colorpart` (VARCHAR) - Color of the part.
- `weightpart` (DECIMAL) - Weight of the part.
- `citypart` (VARCHAR) - City where the part is stored.

#### 5. `FPJ`
Tracks the delivery of parts to projects by suppliers.
- `codsup` (VARCHAR) - Foreign key referring to `SUPPLIER(codsup)`.
- `codpart` (VARCHAR) - Foreign key referring to `PART(codpart)`.
- `codproj` (VARCHAR) - Foreign key referring to `PROJECT(codproj)`.
- `qtydelivered` (INT) - Quantity of parts delivered.
- `date_del` (DATE) - Date of the delivery.
- Primary key is a composite of `codsup`, `codpart`, and `codproj`.

### Key Features

#### Data Integrity Constraints
- Foreign keys ensure relationships between suppliers, parts, and projects are maintained.
- Composite primary keys in the `FPJ` table prevent duplicate entries for the same supplier, part, and project combination.

#### Queries and Business Insights
1. **Identify parts delivered to projects in the same city as the supplier.**
2. **Find projects where suppliers are located in different cities than the project.**
3. **List projects that use parts supplied by S3.**
4. **Retrieve projects with specific name or director patterns.**
5. **Aggregate data on deliveries.**
6. **Advanced conditions and updates**


## Estate Database Project
### Overview
The Estate Database is designed to manage information related to buildings, apartments, rooms, photos, and parking availability. The database includes a set of tables, triggers, and constraints to ensure data integrity and implement certain business rules.

This project allows the management of apartments, buildings, and rooms along with their characteristics like rent, area, energy consumption, parking availability, and more. Triggers are implemented to handle automatic updates and validations when inserting, updating, or deleting data.

### Tables

#### 1. `Building`
Stores information about buildings, including the address, fiber optic availability, and parking status.
- `id` (INT) - Primary key, unique identifier for the building.
- `addressNumber` (VARCHAR) - The building's address number.
- `addressStreet` (VARCHAR) - The street name.
- `addressPostalCode` (VARCHAR) - The postal code.
- `addressCity` (VARCHAR) - The city where the building is located.
- `fiberOptic` (BOOLEAN) - Indicates if the building has fiber optic internet.
- `privateParking` (BOOLEAN) - Indicates if the building has private parking.

#### 2. `Apartment`
Stores information about individual apartments within buildings, including rent, area, and parking availability.
- `building` (INT) - Foreign key referring to `Building(id)`.
- `number` (INT) - Primary key, the unique number for each apartment.
- `description` (VARCHAR) - Description of the apartment.
- `rent` (DECIMAL) - The rent for the apartment.
- `area` (DECIMAL) - The area of the apartment in square meters.
- `terrace` (BOOLEAN) - Indicates if the apartment has a terrace.
- `energyClass` (VARCHAR) - The energy consumption class of the apartment.
- `heating` (VARCHAR) - The heating type used in the apartment.
- `parkingSpace` (BOOLEAN) - Indicates if the apartment has a parking space.
- `parkingPrice` (DECIMAL) - The price for the parking space.

#### 3. `Room`
Stores information about individual rooms within apartments.
- `building` (INT) - Foreign key referring to `Apartment(building)`.
- `apartment` (INT) - Foreign key referring to `Apartment(number)`.
- `number` (INT) - The unique number for the room within the apartment.
- `area` (DECIMAL) - The area of the room in square meters.
- `function` (VARCHAR) - The function of the room (e.g., bedroom, kitchen, etc.).

#### 4. `Photo`
Stores information about photos related to apartments.
- `number` (INT) - Primary key, identifier for each photo.
- `title` (VARCHAR) - The title of the photo.
- `description` (VARCHAR) - A description of the photo.
- `uri` (VARCHAR) - The URI (or path) to the photo.
- `building` (INT) - Foreign key referring to `Apartment(building)`.
- `apartment` (INT) - Foreign key referring to `Apartment(number)`.

### Triggers

#### 1. `trg_check_parking_price`
This trigger is executed before inserting a new apartment. It checks that the `parkingPrice` is set to `NULL` if the apartment does not have a parking space (`placeParking = FALSE`). If this condition is violated, the insertion will be blocked.

#### 2. `trg_update_area_insert`
This trigger is executed after a new room is inserted into the database. It updates the `area` of the apartment by adding the area of the newly inserted room.

#### 3. `trg_update_area_update`
This trigger is executed after updating a room's area. It updates the `area` of the apartment by subtracting the old room's area and adding the new room's area.

#### 4. `trg_update_area_delete`
This trigger is executed after a room is deleted. It updates the `area` of the apartment by subtracting the deleted room's area.

#### 5. `trg_enforce_parking_and_initialize`
This trigger is executed before inserting a new apartment. It checks the following:
- Ensures that the building has private parking (`privateParking = TRUE`) if the apartment has a parking space (`placeParking = TRUE`).
- Initializes the `area` to `0` if the area is not provided when inserting the apartment.

### Example Queries

#### 1. Insert a New Building:
```sql
INSERT INTO Building (id, addressNumber, addressStreet, addressPostalCode, addressCity, fiberOptic, privateParking)
VALUES (1, '10', 'Avenue de la République', '75011', 'Paris', TRUE, TRUE);

INSERT INTO Apartment (building, number, description, rent, area, terrace, energyClass, heating, parkingSpace, parkingPrice)
VALUES (1, 101, 'Apartment with parking', 1200.00, 80, TRUE, 'A', 'Central', TRUE, 150.00);

INSERT INTO Room (building, apartment, number, area, function)
VALUES (1, 101, 1, 15.5, 'Bedroom');

UPDATE Room
SET area = 18.0
WHERE building = 1 AND apartment = 101 AND number = 1;

DELETE FROM Room
WHERE building = 1 AND apartment = 101 AND number = 1;

