#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from MainCode.negative_sel_project import findfactors



def test_FindFactors():
    
    #Test 1
    V = findfactors(10)
    assert V == 4, "Wrong Value"	
    
  
    


