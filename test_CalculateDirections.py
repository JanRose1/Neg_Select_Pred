#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from MainCode.negative_sel_project import calculate_directions



def calculate_directions():
    
    #Test 1
    last_coordinate = [0,0,1]
    Past_coordinates = [[0,0,0]]
    V = calculate_directions(2,last_cordinate,Entropy)
    assert V == [[0,0,2],[0,1,1],[1,0,1]], "Arrays don't match"	
    


