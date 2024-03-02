# Practice problems

## RNA sequencing

### Problem 1

What is the purpose of bioinformatics analysis in RNA-seq?

**A.** to assemble the genome<br>
**B.** to identify single nucleotide polymorphisms (SNPs)<br>
**C.** to align reads to a reference genome and quantify gene expression<br>
**D.** to visualize protein structures

### Problem 2

Which of the following is a measure of gene expression calculated from RNA-seq data?

**A.** RPKM (Reads Per Kilobase Million)<br>
**B.** BLAST score<br>
**C.** GC content<br>
**D.** Amino acid sequence

### Problem 3

What is differential gene expression analysis in RNA-seq?

**A.** Comparing gene expression between different cell types or conditions<br>
**B.** Measuring the number of exons in a gene<br>
**C.** Identifying the location of enhancer regions in the genome<br>
**D.** Analyzing the methylation status of DNA

### Problem 4

What is the term used to describe the process of aligning short sequence reads to a reference genome in RNA-seq analysis?

**A.** Transcriptome assembly<br>
**B.** Read mapping<br>
**C.** Base calling<br>
**D.** Sequence alignment

### Problem 5

Describe how RNA-seq can be used in the diagnosis and treatment of diseases.
Include a discussion on the identification of disease biomarkers, understanding disease mechanisms, and implications for personalized medicine.

### Problem 6

Describe the general workflow of RNA sequencing, including the steps involved from sample preparation to data analysis.

### Problem 7

Discuss the significance of differential gene expression analysis in RNA-seq experiments. How is it performed, and what biological insights can it provide?

### Problem 8

Describe the challenges associated with RNA-seq data analysis, including quality control, read alignment, and normalization techniques.

### Problem 9

Discuss the importance of RNA-seq in understanding alternative splicing events and isoform diversity within genes.

### Problem 10

Describe the role of bioinformatics tools and algorithms in the analysis of RNA-seq data, including methods for transcriptome assembly, quantification, and visualization.

### Problem 11

Explain the importance of experimental design in RNA-seq studies. What factors should researchers consider when designing RNA-seq experiments to ensure robust and reliable results?

## Burrows-Wheeler Transforms

### Problem 12

Given a short RNA sequence, construct the BWT matrix and the final BWT string.
Consider the RNA sequence `AGGCAU$`, where `$` signifies the end of the sequence.

A.  Generate all cyclic rotations of `AGGCAU$`.<br>
B.  Sort the rotations lexicographically.<br>
C.  Write down the last column (the BWT of the sequence).

### Problem 13

Given a BWT string, reconstruct the original RNA sequence.
Use the BWT string `G$CUAGA`.

A.  List all suffixes of the BWT string in sorted order.<br>
B.  Reconstruct the original sequence from the BWT string.

### Problem 14

Consider the RNA sequence `UACGUGACG$`.

A. Construct the BWT of the given sequence.<br>
B. Using the BWT, discuss how you would compress the sequence.<br>
C. Explain how you could use the BWT and additional data structures to quickly find occurrences of the substring `GUG` in the sequence.

### Problem 15

Explain how the Burrows-Wheeler Transform rearranges the characters of a string into runs of similar characters and how this property is exploited for read mapping and data compression.

Certainly! Here are the multiple-choice questions formatted as requested:

### Problem 16

What does the Burrows-Wheeler Transform (BWT) primarily facilitate in bioinformatics applications?

**A.** Gene prediction.<br>
**B.** Protein structure prediction.<br>
**C.** Data compression and efficient string searching.<br>
**D.** Phylogenetic analysis.

### Problem 17

The FM-index, used in conjunction with the BWT for read mapping, relies on which of the following for efficient searching?

**A.** Linear search algorithms.<br>
**B.** Backward search algorithms.<br>
**C.** Depth-first search algorithms.<br>
**D.** Greedy algorithms.

### Problem 18

Which of the following is a key advantage of using BWT-based algorithms for read mapping?

**A.** They require no preprocessing of the reference genome.<br>
**B.** They guarantee 100% accuracy in mapping reads.<br>
**C.** They are less memory-intensive than other approaches.<br>
**D.** They can directly map reads to a protein database without translating DNA sequences.

### Problem 19

How do BWT-based read mapping algorithms typically handle reads that map to repetitive regions in the genome?

**A.** By automatically discarding such reads.<br>
**B.** By mapping the read to the first occurring location of the repeat.<br>
**C.** By reporting all possible mapping locations for the read.<br>
**D.** By converting repetitive sequences into unique sequences before mapping.

### Problem 20

Beyond read mapping, which of the following applications can also utilize the Burrows-Wheeler Transform?

**A.** Predicting RNA secondary structures.<br>
**B.** Identifying protein-protein interactions.<br>
**C.** Compressing genomic data for storage.<br>
**D.** Simulating cellular metabolic pathways.

### Problem 21

What is an essential component of constructing an FM-index for a genome?

**A.** Calculating the eigenvalues of DNA sequence matrices.<br>
**B.** Performing a Fourier transform on the genomic sequence.<br>
**C.** Creating a suffix array from the BWT of the genome.<br>
**D.** Mapping all known SNPs to the reference genome.

### Problem 22

Which of the following is a challenge when using BWT-based algorithms for mapping reads to large and complex genomes?

**A.** Increased risk of introducing mutations into the genome.<br>
**B.** Reduced ability to detect single nucleotide polymorphisms (SNPs).<br>
**C.** Higher computational memory requirements.<br>
**D.** Complete inability to map reads to non-coding regions.

### Problem 23

Given a short DNA sequence, "AGTCAGTC", implement a basic version of the Burrows-Wheeler Transform (BWT) to produce its transformed sequence.
Show each step of the transformation process, including the creation of the matrix of cyclically shifted sequences, sorting of this matrix, and extraction of the last column to form the BWT output.

### Problem 24

You are provided with a BWT output "TTGGCAC\$A" and its original length. Reconstruct the original sequence by applying the reverse BWT process.
Document each step, including the initial reconstruction of the table and the final sequence recovery.
Explain the significance of the "$" symbol in BWT outputs.

### Problem 25

Describe a strategy to improve the accuracy of read mapping in regions with high genomic repetition using BWT.
Your answer should include a brief explanation of why repetitive sequences pose a challenge for read mapping and propose a computational or algorithmic solution to mitigate these issues.
