-- Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
-- Each row of Employees table contains the id and the name of an employee in a company.
-- Each row of EmployeeUNI table contains the id and the corresponding unique id of an employee in the company.
SELECT unique_id, name
FROM Employees e
LEFT JOIN EmployeeUNI u
ON e.id = u.id