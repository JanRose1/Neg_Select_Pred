#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import Hydrogen_Bond_Strengths



def test_Hydrogen_Bonds():
    
    
    V = Hydrogen_Bond_Strengths("FHF")
    assert V == 161.5, "The expected Value should be 161.5"	
    


