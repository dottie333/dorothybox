#P Versus NP Problem

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
  
This function can be performed on any size data set. I have demonstrated that for a given   
value P, the correct answer NP will be returned. For example, a given value of 21 will  
return the data sets in the amount of 21.   
  
I repeat, in answering Wikipedia question,” If the solution to a problem can be quickly  
verified by a computer, can the computer also solve that problem quickly?”   
The above demonstration has proven that the answer is yes.  
