#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import Enthalpy_calculation



def test_Enthalpy_Calculation():
    Enthalpies = [2,1]
    V = Enthalpy_Calculation(Enthalpies)
    assert V == 3, "The expected Value should be 3"	
    


