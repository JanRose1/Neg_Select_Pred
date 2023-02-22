#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import Entropy_Calculation



def test_similarity():
    
    microstates = 0
    V = Entropy_Calculation(0)
    assert V == 0, "The expected Value should be 0"	
    


