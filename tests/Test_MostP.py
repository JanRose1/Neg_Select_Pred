#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import MostP


def MostP():
    
    #Test 1
    n = 3
    distance = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    distance[2][2][2] = 1
    distance = clean_lattice(n,distance)
    V = MostP(3,distance)
    assert V == [1,0], "MostP not working"	
    
    
    


