# -*- coding: utf-8 -*-
"""Negative_Sel_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/104bPF4-8FQfMJtnGtGSIz5QoXOzNQKeP
"""

#Assumptions I'm making
#3d molecule can fold any which way to the point of "Re-arranging itself"
#Can Compare the domains of each one to get my desired results
#For MHC can compare domains for variability. If they submit the entire sequence 
#Gonna use hydrogen bond energies to determine the optimal anchor points and essentially use free energies 
#to distinguish binding strenghts Peptide should bind stronger to mTEC MHC than to 
#peptide otherwise it Undergoes Negatve Selection
#Change in microstates is defined as maximum number of possible configurations that can be taken as binding pockets 


##General Code file to start with.
import numpy as np
import pandas as pd
import math
import sys
import copy
import pprint

def SFree_E(Enthalpy,Entropy):
    T = 310
    return Enthalpy - T*Entropy

def calculate_directions(n,last_cord,Past_cords):
    directions = []
    k = [1,-1]
    for i in range(0,len(k)):
        result = last_cord[2] + k[i]
        if result < 0 or result > n:
            continue
        newCord = [last_cord[0],last_cord[1],result]
        exists = False
        for i in range(0,len(Past_cords)):
            if newCord == Past_cords[i]:
                exists = True
        if exists != True:
            directions.append(newCord)
            
    for i in range(0,len(k)):
        result = last_cord[1] + k[i]
        if result < 0 or result > n:
            continue
        newCord = [last_cord[0],result,last_cord[2]]
        exists = False
        for i in range(0,len(Past_cords)):
            if newCord == Past_cords[i]:
                exists = True
        if exists != True:
            directions.append(newCord)
            
    for i in range(0,len(k)):
        result = last_cord[0] + k[i]
        if result < 0 or result > n:
            continue
        newCord = [result,last_cord[1],last_cord[2]]
        exists = False
        for i in range(0,len(Past_cords)):
            if newCord == Past_cords[i]:
                exists = True
        if exists != True:
            directions.append(newCord)
    return directions  

def possible_connections(n,last_cord):
    directions = []
    k = [1,-1]
    for i in range(0,len(k)):
        result = last_cord[2] + k[i]
        if result < 0 or result > n:
            continue
        newCord = [last_cord[0],last_cord[1],result]
        directions.append(newCord)
    
    for i in range(0,len(k)):
        result = last_cord[1] + k[i]
        if result < 0 or result > n:
            continue
        newCord = [last_cord[0],result,last_cord[2]]
        directions.append(newCord)
    
    for i in range(0,len(k)):
        result = last_cord[0] + k[i]
        if result < 0 or result > n:
            continue
        newCord = [result,last_cord[1],last_cord[2]]
        directions.append(newCord)
    
    return directions

def backtracking(AA,Past_cords):
    totalHH = 0
    for i in range(0,len(Past_cords)):
        if AA[i] == 'H':
            locations = possible_connections(len(AA),Past_cords[i])
            for x in range(0,len(locations)):
                index = 0
                if locations[x] in Past_cords:
                    index = Past_cords.index(locations[x])
                    if (index != i + 1 or index != i - 1) and AA[index] == 'H':
                        totalHH += 1
                else:
                    continue
    return totalHH

def findfactors(num):
    num = num - 2
    factors = []
    for i in range(1,num+1):
        if num % i==0:
            factors.append(i)
    divisor = 0
    if len(factors) > 2:
        for i in factors:
            if i != num and i > divisor:
                divisor = i
    else:
        divisor = factors[len(factors) - 1]
    return divisor

def divideString(string, n):
    str_size = len(string) - 2
   
 
    # Check if string can be divided in n equal parts
    if n < 3:
        print ("Chunks too small to perform proper folding")
        return
    elif str_size % n != 0:
        print ("Invalid Input: String size is not divisible by n")
        return
    
 
    # Calculate the size of parts to find the division points
    part_size = n
    chunks = []
    allchunks = []
    k = 1
    for i in range(2,len(string)):
        if k != part_size:
            chunks.append(string[i])
            k += 1
        else: 
            chunks.append(string[i])
            
            allchunks.append(chunks)
            chunks = []
            k = 1
    
    return allchunks

def chunkFold(AA,index,chunks,last_cord,Past_cords,Maxcon,optimal_route):
    
    #We calculated the possible directions now we start placing AA 
    #then backtrack to make sure we have the best route
    if index == len(chunks):
        Connections = backtracking(AA,Past_cords)
        if Maxcon < Connections:
            Maxcon = Connections
            optimal_route = copy.deepcopy(Past_cords)
        Past_cords.pop()
        return Past_cords,Maxcon,optimal_route
        
        
    
    directions = calculate_directions(len(AA),last_cord,Past_cords) #I'm essentially hoping for each recursive call to store different directions
    
    
    #Here we're going backwards on the list. Last direction added is our final coordinate for the time being
    for i in range(len(directions) - 1 ,- 1,-1):
        Past_cords.append(directions[i])
        index += 1
        Past_cords, Maxcon,optimal_route = chunkFold(AA,index,chunks,directions[i],Past_cords,Maxcon,optimal_route)
        index = index - 1
        directions.pop()
    
    if bool(directions) == False:
        Past_cords.pop() #Need it or index messes up
        return Past_cords,Maxcon,optimal_route


def proteinfolding(AA,n):
    optimal_route = []
    Maxcon = -1 
    Lattice = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
    #Make all this global
    
    
    #Divide the AA string into chunks as shown in this paper https://www.wseas.org/multimedia/journals/circuits/2018/a225901-397.pdf
    chunks = divideString(AA,findfactors(n))
    
    ##Have to find a consistent way to start in the center
    center = math.ceil((n-1)/2)
    #print(math.ceil((n-2)/2))
    
    #Set the first two Letters at the center
    Lattice [center][center][center] = AA[0]
    Lattice [center][center][math.ceil((n-2)/2)] = AA[1]
    
    #Keep running list of points that have been used
    Past_cords = [[center,center,center],[center,center,math.ceil((n-2)/2)]]
    
    #Repeat this step for the number of chunks there are
    for i in range(0,len(chunks)):
        #print(chunks[i])
        #Past_cords[len(Past_cords) - 1]
        Past_cords,Maxcon,optimal_route = chunkFold(AA,0,chunks[i],Past_cords[len(Past_cords) - 1],Past_cords,Maxcon,optimal_route)
        Past_cords = copy.deepcopy(optimal_route)
        
    return optimal_route

def clean_lattice(size,lattice):
    #For now only focusing on cleaning rows
    count = 0
    for i in range(0,size):
        if sum(map(sum, lattice[count])) == 0:
            del lattice[count]
        else:
            count += 1
    #pprint.pprint(lattice)
    return lattice

def MostP(size,lattice):
    
    countP = 0
    maxP = 0
    face = 0
    #First we'll be checking for the face on top
    for x in range(0,size): #Checks row
        for y in range(0,size): #Checks element
            if lattice[0][x][y] == 1:
                 countP += 1
    if maxP < countP:
        maxP = countP
        face = 0
    
    countP = 0
    #We check the bottom face
    for x in range(0,size): #Checks row
        for y in range(0,size): #Checks element
             if lattice[len(lattice) - 1][x][y] == 1:
                countP += 1
    if maxP < countP:
        maxP = countP
        face = size - 1
        
    return maxP,face

def AA_import_todict(file):
    """
    Function to import file containing table of amino acid information and convert it into a dictionary
    Parameters:
    file (path): Path to file containing table of AA info
    Returns:
    AA_info (dict): Dictionary of AA info
    """
    AA_info = {}
    with open(file) as f:
        next(f) # skip header line
        for line in f:
            parsed_line = line.split()
            aa_code = parsed_line[1]
            aa_type = parsed_line[2]
            pka1 = parsed_line[3]
            pka2 = parsed_line[4]
            pka3 = parsed_line[5]
            charged_atom = parsed_line[6]

            AA_info[aa_code] = {
                'type': aa_type,
                'pka1': pka1,
                'pka2': pka2,
                'pka3': pka3,
                'charged_atom': charged_atom
            }

    return AA_info

def convertAA(MHC,Peptide,Binding,Table):
    MHCconvert = []
    MHCstring = ''
    Peptideconvert = []
    Peptidestring = ''
    Bindingconvert = []
    Bindingstring = ''
    for i in MHC:
        if Table[i]['type'] == 'non-polar':
            MHCconvert.append(2)
            MHCstring += 'H'
        elif Table[i]['type'] == 'polar_uncharged':
            MHCconvert.append(1)
            MHCstring += 'P'
        elif Table[i]['type'] == 'polar_charged':
            MHCconvert.append(1)
            MHCstring += 'P'
    
    for i in Peptide:
        if Table[i]['type'] == 'non-polar':
            Peptideconvert.append(2)
            Peptidestring += 'H'
        elif Table[i]['type'] == 'polar_uncharged':
            Peptideconvert.append(1)
            Peptidestring += 'P'
        elif Table[i]['type'] == 'polar_charged':
            Peptideconvert.append(1)
            Peptidestring += 'P'
    
    for i in Binding:
        if Table[i]['type'] == 'non-polar':
            Bindingconvert.append(2)
            Bindingstring += 'H'
        elif Table[i]['type'] == 'polar_uncharged':
            Bindingconvert.append(1)
            Bindingstring += 'P'
        elif Table[i]['type'] == 'polar_charged':
            Bindingconvert.append(1)
            Bindingstring += 'P'
    
    return MHCconvert,MHCstring,Peptideconvert,Peptidestring,Bindingconvert,Bindingstring

def createLattice(AA1,Conversion1):
    n1 = len(AA1)
    LatticeSize = n1**3
    Lattice = [[[0 for k in range(n1)] for j in range(n1)] for i in range(n1)]
    #pprint.pprint(Lattice)
    optimal_route1 = proteinfolding(AA1,n1)
    for i in range(0,len(optimal_route1)):
        Lattice[optimal_route1[i][0]][optimal_route1[i][1]][optimal_route1[i][2]] = Conversion1[i]
    Lattice = clean_lattice(n1,Lattice)
    print("This is the protein")
    pprint.pprint(Lattice)
    MaxPLattice,Ideal_face = MostP(n1,Lattice)
    return MaxPLattice,Ideal_face

#Main 
#Testing Protein Folding
print("Input the location of the MHC file you want to read in")
string1 = input()
print("Input the location of the Peptide file you want to read in")
string2 = input()
print("Input the location of the Binding Site file you want to read in")
string3 = input()
print("Input the location of the AA Table file you want to read in")
string4 = input()

#Read in Amino Acid Strings
MHC = open(string1).read() 
Peptide = open(string2).read()
Binding = open(string3).read()

AA_Table = AA_import_todict(string4)


MHCCon = []
PeptideCon = []
BindingCon = []
MHCCon,MHC,PeptideCon,Peptide,BindingCon,Binding = convertAA(MHC,Peptide,Binding,AA_Table)
#Folding for the first peptide sequence    
#Code 
print("This is the Protein")
MaxPMHC, MHCFace = createLattice(MHC,MHCCon)
print("This is the Peptide")
MaxPPeptide,PeptideFace = createLattice(Peptide,PeptideCon)
print("This is the Variable Region")
MaxPBinding,BindingFace = createLattice(Binding,BindingCon)

#sys.exit(1)
#Just doing basic entropy change and enthalpy = number of bonds formed. 

FMHCEntropy = len(MHC)*len(MHC)
#print(FMHCEntropy)
FBindingEntropy = len(Binding)*len(Binding)
#print(FBindingEntropy)
BMHCEntropy = abs(len(MHC)*len(MHC) - abs(MaxPPeptide - MaxPMHC))
#print(BMHCEntropy)
BBindingEntropy = abs(len(Binding)*len(Binding) - abs(MaxPPeptide - MaxPBinding))
#print(BBindingEntropy)
DMHCEntropy = FMHCEntropy - BMHCEntropy 
#print(DMHCEntropy)
DBindingEntropy = FBindingEntropy - BBindingEntropy
#print(DBindingEntropy)


#For now ignoring Enthalpy changes. 


StandardGBinding = 0
StandardGMHC = 0
if MaxPPeptide <= MaxPBinding:
    StandardGBinding = SFree_E(-MaxPPeptide*50,DBindingEntropy)
else:
    StandardGBinding = SFree_E(-MaxPBinding*50,DBindingEntropy)
    
if MaxPPeptide <= MaxPMHC:
    StandardGMHC = SFree_E(-MaxPPeptide*50,DBindingEntropy)
else:
    StandardGMHC = SFree_E(-MaxPMHC*50,DBindingEntropy)

print(StandardGBinding)
print(StandardGMHC)
#Comparing both
if StandardGBinding <= StandardGMHC:
    print("Safe from negative Selection")
else:
    print("Underwent Negative Selection")
    
