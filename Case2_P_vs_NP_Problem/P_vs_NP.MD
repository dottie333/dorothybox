#My First Attempt at the P versus NP Problem

The example from Wikipedia was used in solving the problem of P versus NP,   
[https://en.wikipedia.org/wiki/P_versus_NP_problem] .  Wikipedia asked the question,  
” If the solution to a problem can be quickly verified by a computer, can the computer  
also solve that problem quickly?” The answer is yes.   
  
The problem is one of 7 unsolved problems listed by the Clay Mathematics Institute.  
It carries a US$1,000,000 prize for the first correct solution.  

I am concentrating on the third paragraph and using the example given in the third paragraph.   
A subset sum can always be accomplished if you have all the possible combinations of the   
subsets from a set.  Using python 2.7 I was able to produce all the combinations.  
The set n = [-2,-3, 15, 14, 7,-10] as shown in the example.  
  
Run the script **all_combinations.py**   
  
This code output shows all possible combinations of subsets with the total calculations  
for each subset.  It provides the number count, elements in the subset count, the subset,   
and the total for each subset.Now, using the same n set, if I wanted to find a subset  
totaling zero or any other value.  I would run the following script, **find_subset.py**.  
  
##Conclusion  
  
My code is not feasible for a large dataset because the more data elements in the set,  
the more combinations are added, which will increase processing  time.    
This will never work in large sets. This can be used on a small set. A set of 12 are less.  
As it has been pointed out, it does not address the problem.  This is done in    
EXPTIME not in polynomial time.   Nevertheless, it was fun creating.  
In answering Wikipedia question,” If the solution to a problem can be quickly   
verified by a computer, can the computer also solve that problem quickly?”     
I still think the answer should be yes.  Now, I need to prove it somehow.   
