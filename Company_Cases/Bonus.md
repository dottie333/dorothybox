#Bonus

Now that we know that the email separations can be made.  
We need to look at the whole picture.  

The specifications only stated to show that separating the 
email addresses were possible.  However, if we wanted this method 
to automatically be done over all records in the stage table, 
we would need to create an explicit cursor to hold all the records, 
and then using the previous method to process over all records.
    
For Oracle in PL/SQL view the procedure all_emails.sql.

Notice that after the last email address is processed for each employee_id.  
The counters must be reset for the position to start the next record for the 
email addresses and the position of the semicolon in the next record email addresses.  
