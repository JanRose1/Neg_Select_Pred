#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from MainCode.negative_sel_project import divideString


def test_DivideString():
    
    #Test 1
    AA = "HPHPHPHP"
    n = 2
    V = divideString(AA,3)
    assert V == [['H', 'P', 'H'], ['P', 'H', 'P']], "Wrong chunks"	
    
    
    


