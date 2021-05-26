CREATE TABLE IF NOT EXISTS employee (

employeeID bigint NOT NULL PRIMARY KEY,
email VARCHAR(100) NOT NULL,
firstName VARCHAR(100) NOT NULL,
lastName VARCHAR(100) NOT NULL

);

CREATE TABLE IF NOT EXISTS project (

projectID bigint NOT NULL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
stage VARCHAR(100) NOT NULL,
description VARCHAR(500) NOT NULL

);


CREATE TABLE IF NOT EXISTS project_employee (

employeeID bigint REFERENCES employee,
projectID bigint REFERENCES project


);