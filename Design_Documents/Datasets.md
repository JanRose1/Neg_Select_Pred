**Preface**

I will be pulling various fasta file sequences from uniprot.org related to functional variations of amino acid (AA) sequences of MHC I alpha 1 and alpha 2 subunits, MHC II alpha1 and Alpha2, and the variable regions of mTEC molecules. We will use this to determine if the specific combination of MHC alpha regions and mTEC variable regions results in negative selection.

We expect to get a result determining that the cell underwent negative selection or not. For the purposes of visualizing the Lattice structure utilized the code will also be printing the folded proteins such that it's more clear to visualize how binding was determined. 

The Fasta files will only contain information about the sequence and what molecule they correspond to. 

**Proteins utilized:**

- MHC I and II: Major histocompatability Complex molecules are found on antigen presenting cells. These regulate immune responses of the body and make sure that immune cells don't initiate auto-immune responses against the body's own immune system. 

- Variable Regions of T-Cell Receptor molecules: Bind to antigens and plays a role in the adaptive immune response.

- CD4: Coreceptor with T-cell receptor on T lymphocyte to recognize antigens displayed by antigens presenting class II MHC molecules. Is used to bind to 
AIRE to determine cell fate.

- CD8: Coreceptor with T-cell receptor on T lymphocyte to recognize antigens displayed by antigens presenting class I MHC molecules. Is used to bind to 
AIRE to determine cell fate.

**Data Format:**

- FASTA Files

- ~30 Bytes (each)





**Citation/Database**

MHC II https://www.uniprot.org/uniprotkb/Q95379/entry

MHC I https://www.uniprot.org/uniprotkb/Q95460/entry

T-Cell Receptor https://www.uniprot.org/uniprotkb/P20963/entry

CD8A - https://www.ncbi.nlm.nih.gov/gene/925#general-protein-info

CD4 - https://www.ncbi.nlm.nih.gov/gene/920

**Justification** 

These are good datasets to utilize because they contain the exact sequence that corresponds to the segment of the AA sequence we care about most. That database also provides sequences that are significantly similar to the one being currently observed which makes testing on real data much easier.


