.load data
infile 'D:\interview_project\txt_data.txt'
into table hr.txt_employees
fields terminated by '\t'
TRAILING NULLCOLS
(employee_id, first_name, last_name, 
hire_date, job_id, salary,manager_id nullif manager_id=BLANKS, department_id nullif department_id=BLANKS)
