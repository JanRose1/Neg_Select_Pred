#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import calculate_directions



def calculate_directions():
    
    #Test 1
    last_coordinate = [0,0,1]
    Past_coordinates = [[0,0,0]]
    V = calculate_directions(2,last_cordinate,Entropy)
    assert V == [[0,0,2],[0,1,1],[1,0,1]], "Arrays don't match"	
    
    #Test 2
    last_coordinate = [3,5,6]
    Past_coordinates = [[3,5,7],[3,5,5],[3,6,6],[3,4,6],[4,5,6],[2,5,6]]
    V = calculate_directions(7,last_cordinate,Entropy)
    assert V == [], "Arrays don't match"	
    
    #Test 3
    last_coordinate = [0,0,1]
    Past_coordinates = [[0,0,0]]
    V = calculate_directions(0,last_cordinate,Entropy)
    assert V == [], "Arrays don't match"	
    


