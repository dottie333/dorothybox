USE [AdventureWorks2012]
GO

/****** Object:  StoredProcedure [dbo].[separate_email]    Script Date: 10/10/2014 10:41:06 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		<Author,Dorothy H. Sanchez>
-- Create date: <Create Date,10/10/2014,>
-- Description:	<Description,separate email addresses based on Employee_id,>
-- =============================================
CREATE procedure [dbo].[separate_email]( 
	@occurs int = 1,
	@start_it int= 1,
	@hold int,
	@i int = 1,
	@v_id int,
	@v_email nvarchar(500),
	@pass_thru int)
as	
begin
	
	select @hold  = dbo.instr(email_address,';',1,@occurs) from stage_employee where employee_id = 12345;
	select @pass_thru  = dbo.count( email_address, ';' ) from stage_employee where employee_id = 12345;
	    

	declare c_emails cursor for select employee_id, email_address from stage_employee where employee_id = 12345;

	open c_emails
	fetch next from c_emails into @v_id,@v_email 

	while (@i <= @pass_thru) begin
	
		insert into employee_email(employee_id,email_address)
		values(@v_id, substring(@v_email,@start_it,@hold - @start_it));
	
		select @start_it = @hold + 1
		select @hold = dbo.instr(@v_email,';',@start_it,@occurs)	
		select @i = @i + 1
		
		end
	
	insert into employee_email(employee_id,email_address)
 	values(@v_id,substring(@v_email,dbo.instr(@v_email,';',-1,@pass_thru) + 1,len(@v_email)));

end

GO

