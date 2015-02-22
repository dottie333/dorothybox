load data
infile 'D:\interview_project\csv_data.csv'
into table hr.csv_employees
fields terminated by ','
TRAILING NULLCOLS
(employee_id, first_name, last_name, 
hire_date, job_id, salary,
manager_id nullif manager_id = BLANKS, department_id nullif department_id= BLANKS)
.