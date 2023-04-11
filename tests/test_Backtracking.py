#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from MainCode.negative_sel_project import backtracking


def test_backtracking():
    
    #Test 1
    AA = 'HPHP'
    Past_coordinates = [[0,0,0],[0,0,1],[0,0,2],[0,1,2]]
    V = backtracking(AA,Past_coordinates)
    assert 0 == 0, "Backtracking not working"	
    
    
    


