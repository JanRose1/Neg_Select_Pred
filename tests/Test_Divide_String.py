#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import divideString


def Divide_String():
    
    #Test 1
    AA = 'HPHPHPHP'
    n = 2
    V = divideString(AA,n)
    assert V == [['H', 'P', 'H'], ['P', 'H', 'P']], "Wrong chunks"	
    
    
    


