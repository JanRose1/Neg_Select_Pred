NEGATIVE_SELECTION_PREDICTION



Overall Timeline
- Activity 1: Set up Github Repository
  - [X] Task 1.1: Set up Github Repository
  - [X] Task 1.2: Set up Design Docs
  - [X] Task 1.3: Set up Project Timeline
  - [X] Task 1.4: Set up Project Task List
  - [X] Task 1.5: Set up Code Structure
- Activity 1.5: Clean up Design Documentation
  - [X] Task 1.5.1: Make projects inputs more clear
  - [X] Task 1.5.2: Make project outputs more clear
  - [X] Task 1.5.3: Provide clearer names to project files
  - [X] Task 1.5.4: Reorganize Github accordingly
- Activity 2: Research Immune system cell Differentiation
  - [X] Task 2.1: Research potential Cell Differentiation
  - [X] Task 2.2: Find simplest form of Immune cell differentiation and selection process
  - [X] Task 2.3: Choose essential functions for code
- Activity 3: Build Initial Code
  - [X] Task 3.1: Design Basic Structure of code
  - [X] Task 3.2: Define Intermediate Steps
  - [X] Task 3.3: Define Output function
- Activity 4: Iteration and improvement
  - [] Task 4.1: Test code
  - [] Task 4.2: Repeat step 3 but adding onto basic structure

---------------
First Major output
- Activity 1: Download Dataset
  -  [X] Task 1.1: Download FASTA files 
  -  [] Task 1.2: Prep Datasets and separate protein sequences if necesarry 
   -  How is Data prepared?
   - Fasta file contains Amino Acid Sequence of MHC I or II binding region, Peptide sequence, and TCell Binding site
  - [] Task 1.3: Input data and read into my code
- Activity 2: Translate Amino Acid sequences into Hydrophobic or Polar designation
- Activity 3: Simulate protein folding of the Amino Acid Sequence.
- Activity 4: Simulate binding of Peptide antigen to MHC binding region
- Activity 5: Simulate binding of Peptide antigen to alpha protein
- Activity 6: 
- Output: 


-------------------
More in Depth Activity 2
  -  [] Task 2.1: Download FASTA files 
  -  [] Task 2.2: Input data and read into my code
  -  [] Task 2.3: Blast comparison of Amino Acids
    - [] The first implementation of this function will be using two of the same fasta sequences which should be guaranteed to be similar  
  -  [] Task 2.4: Compare FASTA file sequences and compare with known sequence that acts as a baseline.
  -  [] Task 2.5: If not comparable to known variation, confirm that Amino Acid sequence is that of desired protein or something different altogether. 
    - [] Same as task 2.3 The first implementation of this function will be using two of the same fasta file sequences to confirm that they're the same. 
  - Output will be stored as an array within the code.
Completion crtieria means being able to adequately differentiate variations in the target protein sequence and the location of the sequence. This information is to be saved in order to be used for future calculations.
--------------------------
More in Depth Activity 3
- [] Task 3.1: Using Fasta files for CD4 and CD8. Input Data and read into code
- [] Task 3.2: Blast Comparison for Abnormalities on CD8 and CD4 
- [] Task 3.3: If CD8 or/and CD 4 can't be expressed give cell - designation on both/either
- Completion crtieria means being able to adequately differentiate variations in the target protein sequence and the location of the sequence. Completion crtieria means knowing if CD8 and CD4 will be expressed by the lymphocytes or if they will lack expression. Furthermore information about the Amino Acid variation will be saved for future calculations.
-------------------------
More in Depth Activity 4: 
- [] Task 4.1: Find algorithmic calculation of PPI of CD4 and CD8 and corresponding MHC II and MHC I binding with residues
- [] Task 4.2: Make sure calculation can take into account differences in bonding based on changes in number of H bonds that can be formed, Van-der Waals and salt bridges.
Completion crtieria means getting a reasonable calculation for the strength of the PPI between CD4, CD8 and MHC Class II and Class I surface molecules on mTec AIRE proteins. This will effectively determine the fate of the lymphocyte being evaluated.
