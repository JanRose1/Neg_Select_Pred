# BIOINF576
This project will essentially cover the following 

# **Goal**

Establishing an analysis of the thymus's self regulatory system that kills off self-recognizing T-Cells by a means known as negative selection. Typically most of the self-recognizing T-cells are killed off by the thymus for obvious reasons of wanting to avoid having these T-cells attack the host's immune system and thus cause a form of autoimmune disease. That said, it seems that some self-identifying T-cells are left alive and play some sort of role in immune system homeostasis by becoming further specialized after having survived this "cleansing" process. A lot of literature still doesn't quite understand why this happens and what specific factors come into play to determine which self-recognizing T-Cells are left alive and what they should specialize as.  
The goal of this project is to create a software that models the process of negative selection via the comparison of binding strength between MHC molecules and the antigen they present and the binding strength between the mTEC molecule and the antigen being presented. Should time permit the project scope may expand beyond just this single set of interactions. 

**Assumptions/Limitations**
- Molecule can fold any which way to the point of "Re-arranging itself" within 3D space to achieve optimal tertiary structure
- Optimal tertiary structure is achieved via lowest internal free energy state. Molecule will always achieve this lowest form of free energy.
- Optimal binding is achieved via the lowest change in free energy. All binding will always take form in the most optimal configuration.
- Steric hindrance will typically not be considered.
- Threshold will strictly indicate undergoing negative selection or not. (For the moment)
- Negative Selection is purely determined from mTEC having stronger binding than MHC molecule and effects of CD8 and CD4 binding. Environmental factors     will not come into play when determining binding strength. 


**Input:**

Fasta files with Amino Acid Sequence of:
Peptide Antigen
MHC I alpha1 and Alpha2 antigen binding regions
MHC II alpha1 and Beta1 antigen binding regions
Variable region of the T Cell receptor (Antigen Binding site)

**Output:** 

Output on whether TCell underwent negative selection based on antigen binding to variable region.

![BIOINF 576 Pipeline](https://user-images.githubusercontent.com/69280191/211373953-a5e3a8bf-5ec0-422e-8e61-527db37a4651.png)

