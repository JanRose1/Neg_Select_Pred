#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import SFree_E



def SFree_E():
    
    #Test 1
    Enthalpy = 10
    Entropy = 1
    V = SFree_E(Enthalpy,Entropy)
    assert V == -300, "The expected Value should be 0"	
    
    #Test 2
    Enthalpy = -10
    V = SFree_E(Enthalpy,Entropy)
    assert V == -320, "The expected Value should be 0"	
    
    #Test 3
    Enthalpy = 600
    Entropy = 100
    V = SFree_E(Enthalpy,Entropy)
    assert V == -30400, "The expected Value should be 0"	
    


