load data
infile *
append
into table csv_employees
fields terminated by '\t'
(employee_id, first_name, last_name, 
hire_date, job_id, salary,manager_id, department_id)
BEGINDATA
555	Diana	Davids	07-FEB-99	IT_PROG	4200	103	60                          
666	Nancy	Lewis	17-AUG-94 	FI_MGR	12000	101	100                          
777	Daniel	Smith	16-AUG-94 	FI_ACCOUNT	9000	108	100                              
888	John	Kamar	28-SEP-97 	FI_ACCOUNT	8200	108	100                          
999	Ismael	Brown	30-SEP-97 	FI_ACCOUNT	7700	108	100                          
.