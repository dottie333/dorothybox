#Company Case


The company has 2 tables:

Stage_employee table as follows:

|Employee_id 	|	char(8)|
|First_name	|	nvarchar2(100)|
|Last_name	|	nvarchar2(100)|
|Email_address	|	nvarhar2(1000)|

Employee_email table as follows:

		|Employee_id		|char(8)|
		|Email_address		|nvarchar2(300)|

The email_address field contains multiple email addresses, separated by semicolons. 

We need to separate the email address from the stage_employee tables, for each employee, 
and insert them into the employee_email table. 
 
The sample stage_employee table

|Employee_id	|	12345|
|First_name	|	John|
|Last_name	|	Doe|
|Email_address	| johndoe@riverside.com;jdoe@riverside.com;doe.john@riverside.com|

The results in the employee_email table should look like the following:

Record 1	|employee_id	|	12345|
		|Email_address	|	johndoe@riverside.com|

Record 2	|employee_id	|	12345|
		|Email_address	|	jdoe@riverside.com|

Record3		|employee_id	|	12345|
		|Email_address	|	doe.john@riverside.com|


# Company Solution

I completed the project on 2 platforms.  
I used PL/SQL on an Oracle 11.2.0 platform and I also implemented it on SQL Server 2012 platform.
  
For Oracle 11.2.0 using PL/SQL, follow procedure **updated_email.sql**

For SQL Server 2012, I created 2 user defined functions:   
One to allow SQL Server to accept the INSTR function behavior 
that is available in the Oracle database, and another defined 
function that will allow for counting the occurrence of the semicolon in a string.
  
For SQL Server 2012, follow procedure **email_procedure.sql**, 
add user defined functions: **instr_function** and **count_function**.

	
Reference material used: 	www.sqlines.com/oracle/functions/instr
				www.sqlines.com/oracle/function/substr
				www.sql-server-helper.com/functions/count-character.aspx



