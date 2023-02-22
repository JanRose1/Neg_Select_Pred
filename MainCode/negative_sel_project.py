# -*- coding: utf-8 -*-
"""Negative_Sel_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/104bPF4-8FQfMJtnGtGSIz5QoXOzNQKeP
"""

##General Code file to start with.
import numpy as np
import pandas as pd

from bio.Blast import NCBIWWW

#Read in fasta sequence and compare with that of existing Fasta sequence 
#Arguments: string filename, file to compare to 
#Returns: Boolean of matching sequence
def compare_seq(filename,Base_Comparison):
    
    


#Have to start implementing portions of my project

def read_input(file):
  CellDat = pd.read_csv(filename)

def calculate_attachment(Grip,Threshold,cell):
  Calculation = 0
  if (Calculation > 50):
    return True
  return False

def establish_environment(Num_TCells,Concentrations):
    print("\n")

def Michaelis_Menten(Vmax,S,K_M):
    return Vmax*S/(K_M + S)

def error_handle():
    sys.exit("Incongruent Data/check input data")
    return

def check_similarity(sequence1,sequence2):
    threshold = 360  #Could play with having this be user input. Current Score Represents 75% Matching nucleotides
    Best_score = -1
    matrix = substitution_matrices.load("BLOSUM62")
    alignments = pairwise2.align.localds(sequence1,sequence2,-5, -3, match_dict = matrix)
    for i in range(len(alignments)):
        if (alignments[i][2] > threshold and alignments[i][2] > Best_score):
            Best_alignment = i
            Best_score = alignments[i][2]
    if Best_score == -1: 
        error_handle()
    return Best_alignment

def check_deviations(Best_alignment):
    counter = 0
    Differing_indeces = []
    for i in range(len(alignments[Best_alignment][0])):
        if (alignments[Best_alignment][0][i] != alignments[Best_alignment][1][counter] 
            and alignments[Best_alignment][1][counter] == "-"): #This is definitely gonna screw me over
            counter = counter + 1
            i = i - 1
        elif (alignments[Best_alignment][1][i] != alignments[Best_alignment][0][counter]):
            Differing_indeces.append(counter)
            counter = counter + 1
    return Differing_indeces
def Hydrogen_Bond_Strengths(HBond):
    #Units of KJ/mol
    Bond_strengths = {"FHF": 161.5,"OHN": 29, "OHO": 21, "NHN": 13, "NHO": 8, "OH3OH2": 18}
    return Bond_strengths[HBond]

def Enthalpy_calculation(Enthalpies):
    total = 0
    for i in range(len(Enthalpies)):
        total = total + Enthalpies[i]
    return total

def Entropy_Calculation(microstates):
    Kb = 1.380649*10*np.exp(-23)
    return Kb*microstates

def Entropy_change(Entropies):
    total = 0
    for i in range(len(Entropies)):
        total = total + Entropies[i]
    return total

def SFree_E(Enthalpy,Entropy):
    T = 310
    return Enthalpy - T*Entropy

def NSFree_E(Q,G_s):
    T = 310
    R = 8.314
    Q = 1.25
    return G_s + R*T*np.log(Q)

def BindingSites():
    #Need to finish
    return

#Assumptions I'm making
#3d molecule can fold any which way to the point of "Re-arranging itself"

#Can Compare the domains of each one to get my desired results
#For MHC can compare domains for variability. If they submit the entire sequence 
#Gonna use hydrogen bond energies to determine the optimal anchor points and essentially use free energies 
#to distinguish binding strenghts Peptide should bind stronger to mTEC MHC than to 
#peptide otherwise it Undergoes Negatve Selection



## More to come after reading up on things a bit more

#Tests
def read_correctly(Data):
  columns = 0
  while columns != 3:
    print(Data[columns])
    columns += 1

#Main