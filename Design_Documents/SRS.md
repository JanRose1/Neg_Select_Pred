Database Selection


To start we'll be taking Fasta files that go over variations of the nucleotide sequence of AIRE, CD8A, and RFXANK, and CD4 genes. 
Each data source has the following number of targets and average number of nucleotides: 
-MHC I/II Binding region: At least 30 nucleotides 
-CD8A binding region: At least 30 nucleotides
-Peptide antigen: At least 20 nucleotides
-CD4 binding region: At least 30 nucleotides

Breakdown

Assumption: Will be assuming all three input amino acid sequences are a total of 20 AA as a baseline.

- Read in Fasta File of Amino Acid Sequences. (1s)
- Simulate protein Folding (400 seconds for amino acid sequence of 20 AA. Time increments by approximately 20s as sequence length n increases)
- Clean Lattice structure (3s for an amino acid sequence of 20AA increase by .25s)
- Calculate Free Energy change (3s) (*2)
  - Calculate change in Entropy (1s)
  - Calculate change in Enthalpy (1s)
  - Calculate change in free energy (1s)
 - Determine Negative selection (1s)
  - Compare free energy change of MHC binding to peptide antigen to that of peptide antigen binding to TCell
  
  408 seconds total or about 6.8 minutes.
