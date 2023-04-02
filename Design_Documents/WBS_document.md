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
  - [] Task 4.2: Repeat step 4.1 but adding onto basic structure

---------------
Steps to Major Output (Activity 3)
- Activity 1: Download Dataset
  -  [X] Task 1.1: Download FASTA files 
  -  [X] Task 1.2: Prep Datasets and separate protein sequences if necesarry 
   -  How is Data prepared?
   - Fasta file contains Amino Acid Sequence of MHC I or II binding region, Peptide sequence, and TCell Binding site
  - [X] Task 1.3: Input data and read into my code
- Activity 2: Translate Amino Acid sequences into Hydrophobic or Polar designation
  - [] Optional: Task 2.5 implement comparison of Amino Acid sequence to confirm use of correct MHC and mTEC sequences
- Activity 3: Simulate protein folding of the Amino Acid Sequences.
- Activity 4: Clean HP lattice structures of faces that contain only zeros. 
- Activity 5: Simulate binding of Peptide antigen to MHC binding region
- Activity 6: Simulate binding of Peptide antigen to TCell
- Activity 7: Compare Free energy change of peptide antigen bound to MHC and peptide antigen bound to TCell
- Output: Result that says whether the TCell underwent negative selection or not

-------------------
More in Depth Activity 2
Input: Fasta Files of Amino Acids (Ex.: "ATGCDSR")
  -  [X] Task 2.1: Download FASTA files 
  -  [X] Task 2.2: Input data and read into my code
  -  [X] Task 2.3: Read in amino acid sequence and designate Hydrophobic (2) or Polar (1)
    - [X] This will be done to facilitate the protein folding simulation later. 
    - [X] Output will be stored as a string sequence within the code.
More in Depth Activity 2.5 (Optional)
  -  [] Task 2.5.1: Compare FASTA file sequences and compare with known sequence that acts as a baseline.
  -  [] Task 2.5.2: If not comparable to known variation, confirm that Amino Acid sequence is that of desired protein or something different altogether. 
  -  [] Task 2.5.3: Raise error if sequences do not match. 
Output: String sequences of Amino Acids converted to 1 and 2 (Ex.: "1212212")
Completion crtieria means convert the amino acid sequence into a series of P/1 and H/2 to adequately differentiate Polar and non-polar AA in the target protein sequence and their location in the sequence. This information is to be saved in order to be used for future calculations.
--------------------------
More in Depth Activity 3
Input: String Sequence of Amino Acids
  - [X] Task 3.1: Create Lattice n^3 structure based on the size n of the sequence.
  - [X] Task 3.2: Divide sequence chunks of n size 
  - [X] Task 3.3: Find the optimal fold that maximizes having non consecutive H bonds adjacent to each other on the 3D lattice structure.
Output: 3D list/Matrix of 1s, 2s, and 0s.
**Completion crtieria means successfully finding a protein folding conformation that maximizes non-consecutive adjacent H bonds as described above.
-------------------------**
More in Depth Activity 4
Input: 3D lattice structure of simulated protein folding
  - [X] Task 4.1: Iterate through faces of lattice structure. (Top to Bottom and left to right) 
   - [X] Task 4.1.1: Check if face has only zeros comprising it
   - [X] Task 4.1.2: Delete Face if it only has zeros in it.
Output: 3D lattice with excess faces eliminated.
**Completion crtieria means successfully eliminating the excess zeros.
-------------------------**
More in Depth Activity 5 
Input: 3D lattice of peptide and MHC protein
- [X] Task 5.1: Check outermost faces of the lattice structures to find the one with the most polar residues
- [X] Task 5.2: Use potential number of hydrogen bonds formed as a means of determining change in enthalpy and entropy. 
  - [X] Task 5.2.1: Change in entropy is calculated by multiplying Boltzmann constant with the difference between total contact points and those remaining 
       after H bonds are "bound"
  - [X] Task 5.2.2: Change in enthalpy is calculated based on number of hydrogen bonds that can form. 
- [X] Task 5.3: Determine free energy change based on calculated enthalpy and entropy
Output: Free energy change of bound peptide and MHC protein binding region
**Completion crtieria means getting a reasonable calculation for free energy change between peptide antigen and the MHC Class II and Class I surface molecules. This will effectively help determine the fate of the lymphocyte being evaluated.
--------------------------**
More in Depth Activity 6
Input: 3D lattice of peptide antigen and TCell binding region
- [X] Task 6.1: Repeat steps of task 5
Output: Free energy change of bound peptide and TCell
**Completion crtieria means getting a reasonable calculation for free energy change between peptide antigen and TCell. This will effectively help determine the fate of the lymphocyte being evaluated.
--------------------------**

