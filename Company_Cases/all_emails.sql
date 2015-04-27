create or replace procedure all_email as
	occurs number := 1;
	start_it number := 1;
	hold number;
	i number := 1;
	pass_thru number;
	
  CURSOR allrecords is
    select employee_id, email_address from stage_employee;
    
    v_mail varchar2(300);
    v_id char(8);

begin
  open allrecords;
  loop
  fetch allrecords into v_id, v_mail;
  exit when allrecords%notfound;
	
	hold :=  instr(v_mail,';',1,occurs);
	pass_thru :=  regexp_count( v_mail, ';' );
	    
	while (i <= pass_thru) loop
	
		insert into employee_email(employee_id,email_address)
		values(v_id, substr(v_mail,start_it,hold - start_it));
	
		start_it := hold + 1;
		hold := instr(v_mail,';',start_it,occurs);	
		i := i + 1;
		end loop;
	
	insert into employee_email(employee_id,email_address)
 	values(v_id,substr(v_mail,instr(v_mail,';',-1,occurs) + 1));
  
  	i := 1;
  	start_it := 1;

	end loop;
	close allrecords;
  commit;
end;