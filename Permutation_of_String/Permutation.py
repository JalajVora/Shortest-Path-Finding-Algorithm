#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import permutations
def str_permu_check(a,b):
    result_list_1 = [''.join(p) for p in permutations(a.lower())]
    result_list_2 = [''.join(p) for p in permutations(b.lower())]
    
    if result_list_1[0] in result_list_2:
        return True
    else:
        return False
  
   

tuple_of_inputs = (input(), input())
str_permu_check(tuple_of_inputs[0],tuple_of_inputs[1])

