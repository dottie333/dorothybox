
# Author:  Dorothy H. Sanchez
# ******************************
# This code block will calculate the number of Saturdays and Sundays   
# between two dates.

from datetime import date
from datetime import timedelta

def checkweekends(a,b):
    count = 0
    
    while a <= b:
        if a.weekday() == 5 or a.weekday() == 6:
            count += 1
        # If you want to see the dates and date number include the following line.
        # print a ,'  ', a.weekday() 
    
        a += timedelta(days = 1)   
        
    return count
    


print checkweekends(date(2013, 9, 10), date(2013, 9,28))
print checkweekends(date(2013,1,1),date(2013,2,1))
print checkweekends(date(2013,3,1),date(2013,3,30))

    
