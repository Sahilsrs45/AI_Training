CREATE DATABASE IF NOT EXISTS hsbc_bank; 

USE hsbc_bank; 

 

CREATE TABLE Departments ( 

 department_id INT PRIMARY KEY, 

 department_name VARCHAR(80) NOT NULL UNIQUE,
 location VARCHAR(60) NOT NULL, 

 annual_budget DECIMAL(14,2) NOT NULL 

); 

 

CREATE TABLE Employees ( 

 employee_id INT PRIMARY KEY, 

 first_name VARCHAR(50) NOT NULL, 

 last_name VARCHAR(50) NOT NULL, 

 email VARCHAR(120) NOT NULL UNIQUE, 

 gender VARCHAR(20), 

 hire_date DATE NOT NULL, 

 designation VARCHAR(80) NOT NULL, 

 department_id INT NOT NULL, 

 manager_id INT NULL, 

 base_salary DECIMAL(12,2) NOT NULL, 

 employment_status VARCHAR(20) NOT NULL, 

 FOREIGN KEY (department_id) REFERENCES Departments(department_id), 

 FOREIGN KEY (manager_id) REFERENCES Employees(employee_id) 

);

CREATE TABLE Payroll ( 

 payroll_id INT PRIMARY KEY, 

 employee_id INT NOT NULL, 

 pay_month DATE NOT NULL, 

 basic_pay DECIMAL(12,2) NOT NULL, 

 bonus DECIMAL(12,2) NOT NULL DEFAULT 0, 

 allowances DECIMAL(12,2) NOT NULL DEFAULT 0, 

 deductions DECIMAL(12,2) NOT NULL DEFAULT 0, 

 net_pay DECIMAL(12,2) GENERATED ALWAYS AS
 (basic_pay + bonus + allowances - deductions) STORED, 

 payment_status VARCHAR(20) NOT NULL, 

 UNIQUE (employee_id, pay_month), 

 FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) 

); 

 

CREATE TABLE Projects ( 

 project_id INT PRIMARY KEY, 

 project_name VARCHAR(100) NOT NULL, 

 project_type VARCHAR(60) NOT NULL, 

 start_date DATE NOT NULL, 

 end_date DATE NULL, 

 budget DECIMAL(14,2) NOT NULL, 

 project_status VARCHAR(25) NOT NULL 

);

CREATE TABLE EmployeeProjects ( 

 assignment_id INT PRIMARY KEY, 

 employee_id INT NOT NULL, 

 project_id INT NOT NULL, 

 assigned_date DATE NOT NULL, 

 role_on_project VARCHAR(60) NOT NULL, 

 allocation_pct INT NOT NULL, 

 UNIQUE (employee_id, project_id), 

 CHECK (allocation_pct BETWEEN 1 AND 100), 

 FOREIGN KEY (employee_id) REFERENCES Employees(employee_id), 

 FOREIGN KEY (project_id) REFERENCES Projects(project_id) 

); 
INSERT INTO Departments (department_id, department_name, location, annual_budget) VALUES 

  (1, 'Retail Banking', 'Pune', 18000000), 

  (2, 'Risk & Compliance', 'Mumbai', 22000000), 

  (3, 'Technology', 'Pune', 35000000), 

  (4, 'Human Resources', 'Hyderabad', 10000000), 

  (5, 'Finance', 'Bengaluru', 16000000), 

  (6, 'Customer Operations', 'Chennai', 14000000); 
  
  INSERT INTO Employees (employee_id, first_name, last_name, email, gender, hire_date, designation, department_id, manager_id, base_salary, employment_status) VALUES 

  (1001, 'Aarav', 'Sharma', 'aarav.sharma1001@example.com', 'Male', '2020-01-01', 'Manager', 1, NULL, 135000, 'Active'), 

  (1002, 'Diya', 'Kapoor', 'diya.kapoor1002@example.com', 'Female', '2021-02-02', 'Manager', 2, NULL, 135000, 'Active'), 

  (1003, 'Kabir', 'Mehta', 'kabir.mehta1003@example.com', 'Male', '2022-03-03', 'Manager', 3, NULL, 135000, 'Active'), 

  (1004, 'Ananya', 'Rao', 'ananya.rao1004@example.com', 'Female', '2023-04-04', 'Manager', 4, NULL, 135000, 'Active'), 

  (1005, 'Vihaan', 'Singh', 'vihaan.singh1005@example.com', 'Male', '2024-05-05', 'Manager', 5, NULL, 135000, 'Active'), 

  (1006, 'Meera', 'Nair', 'meera.nair1006@example.com', 'Female', '2025-06-06', 'Manager', 6, NULL, 135000, 'Active'),
  (1007, 'Arjun', 'Gupta', 'arjun.gupta1007@example.com', 'Male', '2020-07-07', 'Associate', 1, 1001, 97000, 'Active'), 

  (1008, 'Isha', 'Patel', 'isha.patel1008@example.com', 'Female', '2021-08-08', 'Specialist', 2, 1002, 105500, 'Active'), 

  (1009, 'Reyansh', 'Iyer', 'reyansh.iyer1009@example.com', 'Male', '2022-09-09', 'Senior Analyst', 3, 1003, 114000, 'Active'), 

  (1010, 'Sara', 'Das', 'sara.das1010@example.com', 'Female', '2023-10-10', 'Analyst', 4, 1004, 46000, 'Active'), 

  (1011, 'Aditya', 'Sharma', 'aditya.sharma1011@example.com', 'Male', '2024-11-11', 'Associate', 5, 1005, 54500, 'Active'), 

  (1012, 'Riya', 'Kapoor', 'riya.kapoor1012@example.com', 'Female', '2025-12-12', 'Specialist', 6, 1006, 63000, 'Active'), 

  (1013, 'Dev', 'Mehta', 'dev.mehta1013@example.com', 'Male', '2020-01-13', 'Senior Analyst', 1, 1001, 71500, 'Active'), 

  (1014, 'Nisha', 'Rao', 'nisha.rao1014@example.com', 'Female', '2021-02-14', 'Analyst', 2, 1002, 80000, 'Active'), 
  (1015, 'Karan', 'Singh', 'karan.singh1015@example.com', 'Male', '2022-03-15', 'Associate', 3, 1003, 88500, 'Active'), 

  (1016, 'Tara', 'Nair', 'tara.nair1016@example.com', 'Female', '2023-04-16', 'Specialist', 4, 1004, 97000, 'Active'), 

  (1017, 'Rohan', 'Gupta', 'rohan.gupta1017@example.com', 'Male', '2024-05-17', 'Senior Analyst', 5, 1005, 105500, 'Active'),
  (1018, 'Pooja', 'Patel', 'pooja.patel1018@example.com', 'Female', '2025-06-18', 'Analyst', 6, 1006, 114000, 'Active'), 

  (1019, 'Ishaan', 'Iyer', 'ishaan.iyer1019@example.com', 'Male', '2020-07-19', 'Associate', 1, 1001, 46000, 'Active'), 

  (1020, 'Neha', 'Das', 'neha.das1020@example.com', 'Female', '2021-08-20', 'Specialist', 2, 1002, 54500, 'Inactive'), 

  (1021, 'Siddharth', 'Sharma', 'siddharth.sharma1021@example.com', 'Male', '2022-09-21', 'Senior Analyst', 3, 1003, 63000, 'Active'), 

  (1022, 'Aditi', 'Kapoor', 'aditi.kapoor1022@example.com', 'Female', '2023-10-22', 'Analyst', 4, 1004, 71500, 'Active'), 

  (1023, 'Varun', 'Mehta', 'varun.mehta1023@example.com', 'Male', '2024-11-23', 'Associate', 5, 1005, 80000, 'Active'), 

  (1024, 'Kavya', 'Rao', 'kavya.rao1024@example.com', 'Female', '2025-12-24', 'Specialist', 6, 1006, 88500, 'Active'), 

  (1025, 'Rahul', 'Singh', 'rahul.singh1025@example.com', 'Male', '2020-01-25', 'Senior Analyst', 1, 1001, 97000, 'Active'), 

  (1026, 'Simran', 'Nair', 'simran.nair1026@example.com', 'Female', '2021-02-26', 'Analyst', 2, 1002, 105500, 'Active'), 

  (1027, 'Yash', 'Gupta', 'yash.gupta1027@example.com', 'Male', '2022-03-01', 'Associate', 3, 1003, 114000, 'Active'), 

  (1028, 'Priya', 'Patel', 'priya.patel1028@example.com', 'Female', '2023-04-02', 'Specialist', 4, 1004, 46000, 'Inactive'), 
  (1029, 'Aman', 'Iyer', 'aman.iyer1029@example.com', 'Male', '2024-05-03', 'Senior Analyst', 5, 1005, 54500, 'Active'), 

  (1030, 'Tanvi', 'Das', 'tanvi.das1030@example.com', 'Female', '2025-06-04', 'Analyst', 6, 1006, 63000, 'Active'); 

INSERT INTO Projects (project_id, project_name, project_type, start_date, end_date, budget, project_status) VALUES 

  (201, 'Digital Onboarding', 'Digital Banking', '2026-01-15', '2026-12-31', 7500000, 'Active'), 

  (202, 'Fraud Detection', 'Risk Analytics', '2026-02-01', '2027-01-31', 9200000, 'Active'), 

  (203, 'Core Banking Upgrade', 'Technology', '2025-11-01', '2026-10-31', 14000000, 'Completed'),
  (204, 'Customer 360', 'Analytics', '2026-03-10', '2027-03-09', 6100000, 'Active'), 

  (205, 'Regulatory Reporting', 'Compliance', '2026-04-01', '2026-12-31', 4800000, 'Active'), 

  (206, 'Payroll Automation', 'HR Technology', '2026-05-01', '2027-02-28', 3100000, 'Active'), 

  (207, 'Branch Modernization', 'Operations', '2026-06-15', NULL, 8200000, 'On Hold'), 

  (208, 'Cloud Migration', 'Technology', '2026-07-01', NULL, 12000000, 'Active'); 

INSERT INTO EmployeeProjects (assignment_id, employee_id, project_id, assigned_date, role_on_project, allocation_pct) VALUES 

  (1, 1001, 201, '2026-01-15', 'Lead', 50), 

  (2, 1001, 204, '2026-01-15', 'Lead', 50), 

  (3, 1002, 202, '2026-02-15', 'Lead', 50), 

  (4, 1002, 205, '2026-02-15', 'Lead', 50), 

  (5, 1003, 203, '2026-03-15', 'Lead', 50), 

  (6, 1003, 206, '2026-03-15', 'Lead', 50), 

  (7, 1004, 204, '2026-04-15', 'Lead', 50), 

  (8, 1004, 207, '2026-04-15', 'Lead', 50), 

  (9, 1005, 205, '2026-05-15', 'Lead', 50), 

  (10, 1005, 208, '2026-05-15', 'Lead', 50), 

  (11, 1006, 206, '2026-06-15', 'Lead', 50), 

  (12, 1006, 201, '2026-06-15', 'Lead', 50), 

  (13, 1007, 207, '2026-07-15', 'Contributor', 50), 

  (14, 1007, 202, '2026-07-15', 'Contributor', 50), 

  (15, 1008, 208, '2026-08-15', 'Contributor', 50), 

  (16, 1008, 203, '2026-08-15', 'Contributor', 50), 

  (17, 1009, 201, '2026-01-15', 'Contributor', 50), 

  (18, 1009, 204, '2026-01-15', 'Contributor', 50), 

  (19, 1010, 202, '2026-02-15', 'Contributor', 50), 

  (20, 1010, 205, '2026-02-15', 'Contributor', 50), 

  (21, 1011, 203, '2026-03-15', 'Contributor', 50), 

  (22, 1011, 206, '2026-03-15', 'Contributor', 50), 

  (23, 1012, 204, '2026-04-15', 'Contributor', 50), 

  (24, 1012, 207, '2026-04-15', 'Contributor', 50), 

  (25, 1013, 205, '2026-05-15', 'Contributor', 50), 

  (26, 1013, 208, '2026-05-15', 'Contributor', 50), 

  (27, 1014, 206, '2026-06-15', 'Contributor', 50), 

  (28, 1014, 201, '2026-06-15', 'Contributor', 50), 

  (29, 1015, 207, '2026-07-15', 'Contributor', 50), 

  (30, 1015, 202, '2026-07-15', 'Contributor', 50), 

  (31, 1016, 208, '2026-08-15', 'Contributor', 75), 

  (32, 1017, 201, '2026-01-15', 'Contributor', 75), 

  (33, 1018, 202, '2026-02-15', 'Contributor', 75), 

  (34, 1019, 203, '2026-03-15', 'Contributor', 75), 

  (35, 1020, 204, '2026-04-15', 'Contributor', 75), 

  (36, 1021, 205, '2026-05-15', 'Contributor', 75), 

  (37, 1022, 206, '2026-06-15', 'Contributor', 75), 

  (38, 1023, 207, '2026-07-15', 'Contributor', 75), 

  (39, 1024, 208, '2026-08-15', 'Contributor', 75), 

  (40, 1025, 201, '2026-01-15', 'Contributor', 75), 

  (41, 1026, 202, '2026-02-15', 'Contributor', 75), 

  (42, 1027, 203, '2026-03-15', 'Contributor', 75), 

  (43, 1028, 204, '2026-04-15', 'Contributor', 75), 

  (44, 1029, 205, '2026-05-15', 'Contributor', 75), 

  (45, 1030, 206, '2026-06-15', 'Contributor', 75); 

INSERT INTO Payroll (payroll_id, employee_id, pay_month, basic_pay, bonus, allowances, deductions, payment_status) VALUES 

  (1, 1001, '2026-08-01', 135000, 5000, 16200.0, 10800.0, 'Paid'), 

  (2, 1002, '2026-08-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (3, 1003, '2026-08-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (4, 1004, '2026-08-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (5, 1005, '2026-08-01', 135000, 5000, 16200.0, 10800.0, 'Paid'), 

  (6, 1006, '2026-08-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (7, 1007, '2026-08-01', 97000, 0, 11640.0, 7760.0, 'Paid'), 

  (8, 1008, '2026-08-01', 105500, 0, 12660.0, 8440.0, 'Paid'), 

  (9, 1009, '2026-08-01', 114000, 5000, 13680.0, 9120.0, 'Paid'), 

  (10, 1010, '2026-08-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 

  (11, 1011, '2026-08-01', 54500, 0, 6540.0, 4360.0, 'Paid'), 

  (12, 1012, '2026-08-01', 63000, 0, 7560.0, 5040.0, 'Paid'), 

  (13, 1013, '2026-08-01', 71500, 5000, 8580.0, 5720.0, 'Paid'), 

  (14, 1014, '2026-08-01', 80000, 0, 9600.0, 6400.0, 'Paid'), 

  (15, 1015, '2026-08-01', 88500, 0, 10620.0, 7080.0, 'Paid'), 
  (16, 1016, '2026-08-01', 97000, 0, 11640.0, 7760.0, 'Paid'), 

  (17, 1017, '2026-08-01', 105500, 5000, 12660.0, 8440.0, 'Paid'), 

  (18, 1018, '2026-08-01', 114000, 0, 13680.0, 9120.0, 'Paid'), 

  (19, 1019, '2026-08-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 

  (20, 1020, '2026-08-01', 54500, 0, 6540.0, 4360.0, 'Paid'), 

  (21, 1021, '2026-08-01', 63000, 5000, 7560.0, 5040.0, 'Paid'), 

  (22, 1022, '2026-08-01', 71500, 0, 8580.0, 5720.0, 'Paid'), 

  (23, 1023, '2026-08-01', 80000, 0, 9600.0, 6400.0, 'Paid'), 

  (24, 1024, '2026-08-01', 88500, 0, 10620.0, 7080.0, 'Paid'), 

  (25, 1025, '2026-08-01', 97000, 5000, 11640.0, 7760.0, 'Paid'), 

  (26, 1026, '2026-08-01', 105500, 0, 12660.0, 8440.0, 'Paid'), 

  (27, 1027, '2026-08-01', 114000, 0, 13680.0, 9120.0, 'Paid'), 

  (28, 1028, '2026-08-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 

  (29, 1029, '2026-08-01', 54500, 5000, 6540.0, 4360.0, 'Paid'), 

  (30, 1030, '2026-08-01', 63000, 0, 7560.0, 5040.0, 'Paid'), 

  (31, 1001, '2026-09-01', 135000, 5000, 16200.0, 10800.0, 'Paid'), 

  (32, 1002, '2026-09-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (33, 1003, '2026-09-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (34, 1004, '2026-09-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (35, 1005, '2026-09-01', 135000, 5000, 16200.0, 10800.0, 'Paid'), 

  (36, 1006, '2026-09-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (37, 1007, '2026-09-01', 97000, 0, 11640.0, 7760.0, 'Paid'), 

  (38, 1008, '2026-09-01', 105500, 0, 12660.0, 8440.0, 'Paid'), 

  (39, 1009, '2026-09-01', 114000, 5000, 13680.0, 9120.0, 'Paid'), 

  (40, 1010, '2026-09-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 

  (41, 1011, '2026-09-01', 54500, 0, 6540.0, 4360.0, 'Paid'), 

  (42, 1012, '2026-09-01', 63000, 0, 7560.0, 5040.0, 'Paid'), 

  (43, 1013, '2026-09-01', 71500, 5000, 8580.0, 5720.0, 'Paid'), 

  (44, 1014, '2026-09-01', 80000, 0, 9600.0, 6400.0, 'Paid'), 

  (45, 1015, '2026-09-01', 88500, 0, 10620.0, 7080.0, 'Paid'), 

  (46, 1016, '2026-09-01', 97000, 0, 11640.0, 7760.0, 'Paid'), 

  (47, 1017, '2026-09-01', 105500, 5000, 12660.0, 8440.0, 'Paid'), 

  (48, 1018, '2026-09-01', 114000, 0, 13680.0, 9120.0, 'Paid'), 

  (49, 1019, '2026-09-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 

  (50, 1020, '2026-09-01', 54500, 0, 6540.0, 4360.0, 'Paid'), 

  (51, 1021, '2026-09-01', 63000, 5000, 7560.0, 5040.0, 'Paid'), 

  (52, 1022, '2026-09-01', 71500, 0, 8580.0, 5720.0, 'Paid'), 

  (53, 1023, '2026-09-01', 80000, 0, 9600.0, 6400.0, 'Paid'), 

  (54, 1024, '2026-09-01', 88500, 0, 10620.0, 7080.0, 'Paid'), 

  (55, 1025, '2026-09-01', 97000, 5000, 11640.0, 7760.0, 'Paid'), 

  (56, 1026, '2026-09-01', 105500, 0, 12660.0, 8440.0, 'Paid'),
  (57, 1027, '2026-09-01', 114000, 0, 13680.0, 9120.0, 'Paid'), 

  (58, 1028, '2026-09-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 

  (59, 1029, '2026-09-01', 54500, 5000, 6540.0, 4360.0, 'Paid'), 

  (60, 1030, '2026-09-01', 63000, 0, 7560.0, 5040.0, 'Paid'), 

  (61, 1001, '2026-10-01', 135000, 5000, 16200.0, 10800.0, 'Pending'), 

  (62, 1002, '2026-10-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (63, 1003, '2026-10-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (64, 1004, '2026-10-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (65, 1005, '2026-10-01', 135000, 5000, 16200.0, 10800.0, 'Paid'), 

  (66, 1006, '2026-10-01', 135000, 0, 16200.0, 10800.0, 'Paid'), 

  (67, 1007, '2026-10-01', 97000, 0, 11640.0, 7760.0, 'Paid'), 

  (68, 1008, '2026-10-01', 105500, 0, 12660.0, 8440.0, 'Pending'), 

  (69, 1009, '2026-10-01', 114000, 5000, 13680.0, 9120.0, 'Paid'), 

  (70, 1010, '2026-10-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 

  (71, 1011, '2026-10-01', 54500, 0, 6540.0, 4360.0, 'Paid'), 

  (72, 1012, '2026-10-01', 63000, 0, 7560.0, 5040.0, 'Paid'), 

  (73, 1013, '2026-10-01', 71500, 5000, 8580.0, 5720.0, 'Paid'), 
  (74, 1014, '2026-10-01', 80000, 0, 9600.0, 6400.0, 'Paid'), 

  (75, 1015, '2026-10-01', 88500, 0, 10620.0, 7080.0, 'Pending'), 

  (76, 1016, '2026-10-01', 97000, 0, 11640.0, 7760.0, 'Paid'), 

  (77, 1017, '2026-10-01', 105500, 5000, 12660.0, 8440.0, 'Paid'), 

  (78, 1018, '2026-10-01', 114000, 0, 13680.0, 9120.0, 'Paid'), 

  (79, 1019, '2026-10-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 
  (80, 1020, '2026-10-01', 54500, 0, 6540.0, 4360.0, 'Paid'), 

  (81, 1021, '2026-10-01', 63000, 5000, 7560.0, 5040.0, 'Paid'), 

  (82, 1022, '2026-10-01', 71500, 0, 8580.0, 5720.0, 'Pending'), 

  (83, 1023, '2026-10-01', 80000, 0, 9600.0, 6400.0, 'Paid'), 

  (84, 1024, '2026-10-01', 88500, 0, 10620.0, 7080.0, 'Paid'), 

  (85, 1025, '2026-10-01', 97000, 5000, 11640.0, 7760.0, 'Paid'), 

  (86, 1026, '2026-10-01', 105500, 0, 12660.0, 8440.0, 'Paid'), 

  (87, 1027, '2026-10-01', 114000, 0, 13680.0, 9120.0, 'Paid'),
  (88, 1028, '2026-10-01', 46000, 0, 5520.0, 3680.0, 'Paid'), 

  (89, 1029, '2026-10-01', 54500, 5000, 6540.0, 4360.0, 'Pending'),
  (90, 1030, '2026-10-01', 63000, 0, 7560.0, 5040.0, 'Paid');
  
  SELECT COUNT(*) AS departments FROM Departments; 

SELECT COUNT(*) AS employees FROM Employees; 

SELECT COUNT(*) AS payroll_rows FROM Payroll; 

SELECT COUNT(*) AS projects FROM Projects; 

SELECT COUNT(*) AS assignments FROM EmployeeProjects; 

SELECT e.employee_id, e.first_name, d.department_name 

FROM Employees e JOIN Departments d ON e.department_id = d.department_id 

ORDER BY e.employee_id LIMIT 10; 

-- Expected row counts: Departments = 6; Employees = 30; Payroll = 90; Projects = 8; EmployeeProjects = 45.

-- Level 1 — Database fundamentals and SELECT
-- Q1. List all databases on the server. 
SHOW DATABASES;


-- Q2. Select the hsbc_bank database. 
USE hsbc_bank;
-- Q3. List all tables in hsbc_bank. 
SHOW TABLES;
-- Q4. Describe the structure of Employees. 
DESCRIBE Employees;
-- Q5. Describe the structure of Payroll. 
DESCRIBE Payroll;
-- Q6. Display every column of Employees. 
SELECT * FROM Employees;
-- Q7. Display employee_id, first_name and last_name only. 
SELECT employee_id, first_name, last_name
FROM Employees;
-- Q8. Display distinct designations. 
SELECT DISTINCT designation
FROM Employees;
-- Q9. Display distinct department locations.
SELECT DISTINCT location
FROM Departments;
-- Q10. Retrieve all department names and annual budgets. 
SELECT department_name, annual_budget
FROM Departments;
-- Q11. Retrieve the first 10 employees ordered by employee_id.  
SELECT *
FROM Employees
ORDER BY employee_id
LIMIT 10;

-- Q12. Create a full_name alias by concatenating first_name and last_name. 
SELECT employee_id, CONCAT(first_name,' ',last_name) AS full_name
FROM Employees;
-- Q13. Show employee name and annualized base salary (base_salary * 12). 
SELECT CONCAT(first_name,' ',last_name) AS employee_name,
       base_salary * 12 AS annual_salary
FROM Employees;
-- Q14. Display all project names, statuses and budgets. 
SELECT project_name, project_status, budget
FROM Projects;
-- Q15. List payroll records with calculated net_pay. 
SELECT payroll_id,
       employee_id,
       pay_month,
       net_pay
FROM Payroll;

-- Level 2
-- Q16. Find employees with base_salary greater than 90000.
SELECT *
FROM Employees
WHERE base_salary > 90000;

-- Q17. Find employees earning between 60000 and 110000.
SELECT *
FROM Employees
WHERE base_salary BETWEEN 60000 AND 110000;

-- Q18. Find employees hired on or after 2024-01-01.
SELECT *
FROM Employees
WHERE hire_date >= '2024-01-01';

-- Q19. List active employees only.
SELECT *
FROM Employees
WHERE employment_status = 'Active';

-- Q20. Find employees whose first name begins with A.
SELECT *
FROM Employees
WHERE first_name LIKE 'A%';

-- Q21. Find employees whose last name contains a.
SELECT *
FROM Employees
WHERE last_name LIKE '%a%';

-- Q22. Find employees in department IDs 1, 3 or 5.
SELECT *
FROM Employees
WHERE department_id IN (1,3,5);

-- Q23. Find employees with no manager assigned.
SELECT *
FROM Employees
WHERE manager_id IS NULL;

-- Q24. List employees sorted by salary highest first.
SELECT *
FROM Employees
ORDER BY base_salary DESC;

-- Q25. Show the five highest-paid employees.
SELECT *
FROM Employees
ORDER BY base_salary DESC
LIMIT 5;

-- Q26. List projects with a NULL end_date.
SELECT *
FROM Projects
WHERE end_date IS NULL;

-- Q27. Find projects with budgets above 7000000.
SELECT *
FROM Projects
WHERE budget > 7000000;

-- Q28. Find payroll records whose payment_status is Pending.
SELECT *
FROM Payroll
WHERE payment_status = 'Pending';

-- Q29. List employees hired during calendar year 2025 using a date range.
SELECT *
FROM Employees
WHERE hire_date BETWEEN '2025-01-01' AND '2025-12-31';

-- Q30. Display employee names in uppercase.
SELECT UPPER(CONCAT(first_name,' ',last_name)) AS employee_name
FROM Employees;

-- Q31. Show the length of each employee first name.
SELECT first_name,
       LENGTH(first_name) AS name_length
FROM Employees;

-- Q32. Show each employee hire year using YEAR().
SELECT first_name,
       YEAR(hire_date) AS hire_year
FROM Employees;

-- Q33. Display salaries rounded to the nearest thousand.
SELECT first_name,
       ROUND(base_salary,-3) AS rounded_salary
FROM Employees;

-- Q34. Show employees whose designation is Analyst or Associate.
SELECT *
FROM Employees
WHERE designation IN ('Analyst','Associate');

-- Q35. Show active employees ordered by department and salary descending.
SELECT *
FROM Employees
WHERE employment_status='Active'
ORDER BY department_id, base_salary DESC;

-- Level 3
-- Q36. Count all employees.
SELECT COUNT(*) AS total_employees
FROM Employees;

-- Q37. Count active and inactive employees separately.
SELECT employment_status,
       COUNT(*) AS employee_count
FROM Employees
GROUP BY employment_status;

-- Q38. Find minimum, maximum and average base salary.
SELECT MIN(base_salary) AS min_salary,
       MAX(base_salary) AS max_salary,
       AVG(base_salary) AS avg_salary
FROM Employees;

-- Q39. Calculate the total monthly base salary of all employees.
SELECT SUM(base_salary) AS total_base_salary
FROM Employees;

-- Q40. Count employees in each department_id.
SELECT department_id,
       COUNT(*) AS employee_count
FROM Employees
GROUP BY department_id;

-- Q41. Find average base salary by department_id.
SELECT department_id,
       AVG(base_salary) AS avg_salary
FROM Employees
GROUP BY department_id;

-- Q42. Find highest base salary in each department_id.
SELECT department_id,
       MAX(base_salary) AS highest_salary
FROM Employees
GROUP BY department_id;

-- Q43. Find departments with more than four employees using HAVING.
SELECT department_id,
       COUNT(*) AS employee_count
FROM Employees
GROUP BY department_id
HAVING COUNT(*) > 4;

-- Q44. Find departments whose average salary exceeds 80000.
SELECT department_id,
       AVG(base_salary) AS avg_salary
FROM Employees
GROUP BY department_id
HAVING AVG(base_salary) > 80000;

-- Q45. Count employees by designation.
SELECT designation,
       COUNT(*) AS employee_count
FROM Employees
GROUP BY designation;

-- Q46. Find designations with at least three employees.
SELECT designation,
       COUNT(*) AS employee_count
FROM Employees
GROUP BY designation
HAVING COUNT(*) >= 3;

-- Q47. Calculate total net payroll for each pay_month.
SELECT pay_month,
       SUM(net_pay) AS total_net_pay
FROM Payroll
GROUP BY pay_month;

-- Q48. Calculate total bonus paid for each pay_month.
SELECT pay_month,
       SUM(bonus) AS total_bonus
FROM Payroll
GROUP BY pay_month;

-- Q49. Find payroll months with total deductions above 200000.
SELECT pay_month,
       SUM(deductions) AS total_deductions
FROM Payroll
GROUP BY pay_month
HAVING SUM(deductions) > 200000;

-- Q50. Count Paid versus Pending payroll rows by month.
SELECT pay_month,
       payment_status,
       COUNT(*) AS payroll_count
FROM Payroll
GROUP BY pay_month, payment_status;

-- Q51. Find the average budget of Active projects.
SELECT AVG(budget) AS avg_active_budget
FROM Projects
WHERE project_status = 'Active';

-- Q52. Count projects by project_status.
SELECT project_status,
       COUNT(*) AS project_count
FROM Projects
GROUP BY project_status;

-- Q53. Find project statuses with more than one project.
SELECT project_status,
       COUNT(*) AS project_count
FROM Projects
GROUP BY project_status
HAVING COUNT(*) > 1;

-- Q54. Calculate total project budget by project_type.
SELECT project_type,
       SUM(budget) AS total_budget
FROM Projects
GROUP BY project_type;

-- Q55. Find departments where the maximum employee salary exceeds 120000.
SELECT department_id,
       MAX(base_salary) AS max_salary
FROM Employees
GROUP BY department_id
HAVING MAX(base_salary) > 120000;

-- level 4
-- Q56. Display employee names with their department names.
SELECT e.employee_id,
       CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       d.department_name
FROM Employees e
INNER JOIN Departments d
ON e.department_id = d.department_id;

-- Q57. Display employee names with their manager names.
SELECT e.employee_id,
       CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       CONCAT(m.first_name,' ',m.last_name) AS manager_name
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id;

-- Q58. Show department names and number of employees.
SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count
FROM Departments d
LEFT JOIN Employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;

-- Q59. Display payroll details with employee names.
SELECT p.payroll_id,
       CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       p.pay_month,
       p.net_pay
FROM Payroll p
INNER JOIN Employees e
ON p.employee_id = e.employee_id;

-- Q60. Show employees and projects assigned to them.
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       pr.project_name
FROM EmployeeProjects ep
INNER JOIN Employees e
ON ep.employee_id = e.employee_id
INNER JOIN Projects pr
ON ep.project_id = pr.project_id;

-- Q61. Display projects with department names.
SELECT p.project_name,
       d.department_name
FROM Projects p
INNER JOIN Departments d
ON p.department_id = d.department_id;

-- Q62. Show all employees even if they have no project assigned.
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       p.project_name
FROM Employees e
LEFT JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id
LEFT JOIN Projects p
ON ep.project_id = p.project_id;

-- Q63. Find employees working on more than one project.
SELECT e.employee_id,
       CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       COUNT(ep.project_id) AS project_count
FROM Employees e
INNER JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id
GROUP BY e.employee_id, employee_name
HAVING COUNT(ep.project_id) > 1;

-- Q64. Display the highest-paid employee.
SELECT *
FROM Employees
WHERE base_salary = (
    SELECT MAX(base_salary)
    FROM Employees
);

-- Q65. Find employees earning above company average salary.
SELECT *
FROM Employees
WHERE base_salary >
(
    SELECT AVG(base_salary)
    FROM Employees
);

-- Q66. Find departments whose average salary exceeds company average salary.
SELECT department_id,
       AVG(base_salary) AS avg_salary
FROM Employees
GROUP BY department_id
HAVING AVG(base_salary) >
(
    SELECT AVG(base_salary)
    FROM Employees
);

-- Q67. Find employees in the same department as employee_id = 1.
SELECT *
FROM Employees
WHERE department_id =
(
    SELECT department_id
    FROM Employees
    WHERE employee_id = 1
);

-- Q68. Find employees who have payroll records.
SELECT *
FROM Employees
WHERE employee_id IN
(
    SELECT employee_id
    FROM Payroll
);

-- Q69. Find employees who do not have payroll records.
SELECT *
FROM Employees
WHERE employee_id NOT IN
(
    SELECT employee_id
    FROM Payroll
);

-- Q70. Count employees assigned to each project. 
SELECT pr.project_name,COUNT(ep.employee_id) AS employee_count
FROM Projects pr
INNER JOIN EmployeeProjects ep
ON pr.project_id = ep.project_id
GROUP BY pr.project_name;
-- Q71. Display all projects and assigned employees (including projects with no employees).
SELECT pr.project_name, ep.employee_id
FROM Projects pr
LEFT JOIN EmployeeProjects ep
ON pr.project_id = ep.project_id;

-- Q72. Display employees who are not assigned to any project. 
SELECT e.* 
FROM Employees e
LEFT JOIN EmployeeProjects ep
ON e.employee_id = ep.employee_id
WHERE ep.employee_id IS NULL;

-- Q73. Display employee names and their manager names. 
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       CONCAT(m.first_name,' ',m.last_name) AS manager_name
FROM Employees e
INNER JOIN Employees m
ON e.manager_id = m.employee_id;

-- Q74. Display all employees and their managers including employees without managers. 
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       CONCAT(m.first_name,' ',m.last_name) AS manager_name
FROM Employees e
LEFT JOIN Employees m
ON e.manager_id = m.employee_id;

-- Q75. Display employees earning more than their managers. 
SELECT CONCAT(e.first_name,' ',e.last_name) AS employee_name,
       e.base_salary AS employee_salary,
       CONCAT(m.first_name,' ',m.last_name) AS manager_name,
       m.base_salary AS manager_salary
FROM Employees e
INNER JOIN Employees m
ON e.manager_id = m.employee_id
WHERE e.base_salary > m.base_salary;

-- Q76. Join Employees, Departments and Payroll to show employee, department, month and net pay.
SELECT
    CONCAT(e.first_name,' ',e.last_name) AS employee_name,
    d.department_name,
    p.pay_month,
    p.net_pay
FROM Employees e
JOIN Departments d
    ON e.department_id = d.department_id
JOIN Payroll p
    ON e.employee_id = p.employee_id;

-- Q77. Find total net payroll by department for October 2026 using three tables.
SELECT
    d.department_name,
    SUM(p.net_pay) AS total_net_payroll
FROM Departments d
JOIN Employees e
    ON d.department_id = e.department_id
JOIN Payroll p
    ON e.employee_id = p.employee_id
WHERE p.pay_month = '2026-10-01'
GROUP BY d.department_name;

-- Q78. Find departments with October 2026 total net payroll greater than 500000.
SELECT
    d.department_name,
    SUM(p.net_pay) AS total_net_payroll
FROM Departments d
JOIN Employees e
    ON d.department_id = e.department_id
JOIN Payroll p
    ON e.employee_id = p.employee_id
WHERE p.pay_month = '2026-10-01'
GROUP BY d.department_name
HAVING SUM(p.net_pay) > 500000;

-- Q79. Join Employees, EmployeeProjects and Projects to list each employee with project name and role.
SELECT
    CONCAT(e.first_name,' ',e.last_name) AS employee_name,
    p.project_name,
    ep.role_on_project
FROM Employees e
JOIN EmployeeProjects ep
    ON e.employee_id = ep.employee_id
JOIN Projects p
    ON ep.project_id = p.project_id;

-- Q80. Find all Active projects and the names of employees assigned to them.
SELECT
    p.project_name,
    CONCAT(e.first_name,' ',e.last_name) AS employee_name
FROM Projects p
JOIN EmployeeProjects ep
    ON p.project_id = ep.project_id
JOIN Employees e
    ON ep.employee_id = e.employee_id
WHERE p.project_status = 'Active';

-- Q81. Show the number of distinct projects per employee using a three-table join.
SELECT
    e.employee_id,
    CONCAT(e.first_name,' ',e.last_name) AS employee_name,
    COUNT(DISTINCT p.project_id) AS project_count
FROM Employees e
JOIN EmployeeProjects ep
    ON e.employee_id = ep.employee_id
JOIN Projects p
    ON ep.project_id = p.project_id
GROUP BY e.employee_id, employee_name;

