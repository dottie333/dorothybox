-- From Dorothy H. Sanchez
-- This is for processing multiple email addresses

create or replace procedure separate_email as
	occurs number := 1;
	start_it number := 1;
	hold number;
	i number := 1;
	pass_thru number;	

begin
	
	select instr(email_address,';',1,occurs) into hold from stage_employee where employee_id = 12345;
	select regexp_count( email_address, ';' ) into pass_thru from stage_employee where employee_id = 12345;
	    

	for c_emails in (select employee_id, email_address 
	from stage_employee where employee_id = 12345) loop 

	while (i <= pass_thru) loop
	
		insert into employee_email(employee_id,email_address)
		values(c_emails.employee_id, substr(c_emails.email_address,start_it,hold - start_it));
	
		start_it := hold + 1;
		hold := instr(c_emails.email_address,';',start_it,occurs);	
		i := i + 1;
		end loop;
	
	insert into employee_email(employee_id,email_address)
 	values(c_emails.employee_id,substr(c_emails.email_address,instr(c_emails.email_address,';',-1,occurs) + 1));

	end loop;


	commit;
	
end;
/
	