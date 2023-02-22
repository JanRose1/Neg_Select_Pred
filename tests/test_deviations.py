#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import check_deviations



def test_deviations():
    sequence_data = ["ALCD","ALDD"]
    V = check_deviations(0,sequence_data)
    assert V == [2], "The expected differeing Indice should be 2"	
    


