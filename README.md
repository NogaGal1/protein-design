# Protein Design - Random Protein Sequence Generator

## Description
This program generates random protein sequences for a protein design research project.

Each protein sequence:
- Contains exactly 150 amino acids.
- Always starts with Methionine (M).
- Contains 50% nonpolar amino acids.
- Contains 30% polar amino acids.
- Contains 10% positively charged amino acids.
- Contains 10% negatively charged amino acids.

All generated sequences are unique.

## Input
The program asks the user to enter the number of protein sequences to generate.

The accepted input is an integer between 1 and 1000.

Invalid inputs are rejected, and the user is asked to try again.

## Output
The generated sequences are saved in:

results/Out_RandProtSeq.txt

The output follows FASTA format:

>Rand_Prot1
M...
>Rand_Prot2
M...

## How to Run
Run the following command from the repository directory:

python scripts/protein_design.py
