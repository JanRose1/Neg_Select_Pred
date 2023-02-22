#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Neg_Sel_Pred.negative_sel_project import check_similarity



def test_similarity():
    
    sequence_data2 = open("sample_fasta.fasta").read() 
    sequence_data = open("sample_fasta-ref.fasta").read() 
    V = check_similarity(sequence_data,sequence_data2)
    assert V == 0, "The expected Value should be 0"	
    


