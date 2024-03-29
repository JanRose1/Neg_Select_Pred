#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from MainCode.negative_sel_project import clean_lattice


def test_CleanLattice():
    
    #Test 1
    n = 3
    distance = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    distance[1][1][1] = 1
    distance = clean_lattice(n,distance)
    assert distance == [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], "Clean Lattice not working"	
    
    
    


