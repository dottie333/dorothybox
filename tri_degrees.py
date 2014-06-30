# Author:  Dorothy H. Sanchez
# This code will return the degrees of a triangle

import math
def tri_degrees(a,b,c):

    try:
        cosA = (math.pow(b,2) + math.pow(c,2) - math.pow(a,2)) / (2*b*c)
        cos_a =  math.acos(cosA)
        deg_a = int(round(math.degrees(cos_a)))

        cosB = (math.pow(c,2) + math.pow(a,2) - math.pow(b,2)) / (2*c*a)
        cos_b =  math.acos(cosB)
        deg_b = int(round(math.degrees(cos_b)))

        deg_c = 180 - deg_a - deg_b

        degree_set = [deg_a, deg_b, deg_c]
        degree_set.sort()
        
        if deg_a == 0 or deg_b == 0 or deg_c == 0:
            return [0,0,0]
        if deg_a + deg_b + deg_c == 180:
            return degree_set
        
    except ValueError:
        return [0,0,0]
    
    
    

   
    
    
print tri_degrees(8,6,7)
print tri_degrees(4,4,4)
print tri_degrees(3,4,5)
print tri_degrees(2,2,5)
print tri_degrees(10,20,30)


    
