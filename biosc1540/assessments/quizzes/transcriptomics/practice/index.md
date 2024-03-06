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

Given a short RNA, construct the BWT matrix and the final BWT string.
Consider the sequence `GACTTC$`, where `$` signifies the end of the sequence.

A.  Generate all cyclic rotations of `GACTTC$`.<br>
B.  Sort the rotations lexicographically.<br>
C.  Write down the last column (the BWT of the sequence).

### Problem 13

Given a BWT string, reconstruct the original RNA sequence.
Use the BWT string `G\$CCGGTC`.

A.  List all suffixes of the BWT string in sorted order.<br>
B.  Reconstruct the original sequence from the BWT string.

### Problem 14

Explain how the Burrows-Wheeler Transform rearranges the characters of a string into runs of similar characters and how this property is exploited for read mapping and data compression.

### Problem 15

What does the Burrows-Wheeler Transform (BWT) primarily facilitate in bioinformatics applications?

**A.** Gene prediction.<br>
**B.** Protein structure prediction.<br>
**C.** Data compression and efficient string searching.<br>
**D.** Phylogenetic analysis.

### Problem 16

The FM-index, used in conjunction with the BWT for read mapping, relies on which of the following for efficient searching?

**A.** Linear search algorithms.<br>
**B.** Backward search algorithms.<br>
**C.** Depth-first search algorithms.<br>
**D.** Greedy algorithms.

### Problem 17

Which of the following is a key advantage of using BWT-based algorithms for read mapping?

**A.** They require no preprocessing of the reference genome.<br>
**B.** They guarantee 100% accuracy in mapping reads.<br>
**C.** They are less memory-intensive than other approaches.<br>
**D.** They can directly map reads to a protein database without translating DNA sequences.

### Problem 18

How do BWT-based read mapping algorithms typically handle reads that map to repetitive regions in the genome?

**A.** By automatically discarding such reads.<br>
**B.** By mapping the read to the first occurring location of the repeat.<br>
**C.** By reporting all possible mapping locations for the read.<br>
**D.** By converting repetitive sequences into unique sequences before mapping.

### Problem 19

Beyond read mapping, which of the following applications can also utilize the Burrows-Wheeler Transform?

**A.** Predicting RNA secondary structures.<br>
**B.** Identifying protein-protein interactions.<br>
**C.** Compressing genomic data for storage.<br>
**D.** Simulating cellular metabolic pathways.

### Problem 20

What is an essential component of constructing an FM-index for a genome?

**A.** Calculating the eigenvalues of DNA sequence matrices.<br>
**B.** Performing a Fourier transform on the genomic sequence.<br>
**C.** Creating a suffix array from the BWT of the genome.<br>
**D.** Mapping all known SNPs to the reference genome.

### Problem 21

Which of the following is a challenge when using BWT-based algorithms for mapping reads to large and complex genomes?

**A.** Increased risk of introducing mutations into the genome.<br>
**B.** Reduced ability to detect single nucleotide polymorphisms (SNPs).<br>
**C.** Higher computational memory requirements.<br>
**D.** Complete inability to map reads to non-coding regions.

### Problem 22

Given a short DNA sequence, "AGTCAGTC", implement a basic version of the Burrows-Wheeler Transform (BWT) to produce its transformed sequence.
Show each step of the transformation process, including the creation of the matrix of cyclically shifted sequences, sorting of this matrix, and extraction of the last column to form the BWT output.

### Problem 23

Describe a strategy to improve the accuracy of read mapping in regions with high genomic repetition using BWT.
Your answer should include a brief explanation of why repetitive sequences pose a challenge for read mapping and propose a computational or algorithmic solution to mitigate these issues.

## RNA quantification

### Problem 24

Describe a scenario in which RNA-seq data might be significantly contaminated by noise. How would you differentiate between noise and true biological signal in this dataset?
Propose a computational approach for filtering out noise, and discuss the potential impacts of this process on the interpretation of gene expression levels.

### Problem 25

Given raw RNA-seq data from multiple samples, including control and treated groups under different conditions, explain how you would normalize this data to account for variations in sequencing depth and RNA composition.

### Problem 26

Explain how RNA-seq data can be used to identify alternative splicing events. Discuss the challenges associated with quantifying splice variants from short-read sequencing data and propose computational strategies to overcome these challenges. How do changes in splicing patterns contribute to the complexity of gene expression and cellular function?

### Problem 27

Long non-coding RNAs play crucial roles in gene regulation, yet their quantification poses significant challenges.
Discuss these challenges, including issues related to lncRNA annotation, low abundance, and sequence similarity with other transcripts.
Propose a computational approach for accurately quantifying lncRNAs from RNA-seq data and discuss the potential biological insights that could be gained from such analysis.

### Problem 28

What is the primary goal of RNA-seq normalization?

**A.** To adjust for gene length variations in different samples.<br>
**B.** To ensure comparability between samples by correcting for sequencing depth and RNA composition effects.<br>
**C.** To amplify the signal of lowly expressed genes.<br>
**D.** To eliminate all sources of biological variation between samples.

### Problem 29

Which of the following methods is commonly used for differential gene expression analysis in RNA-seq data?

**A.** Principal Component Analysis (PCA).<br>
**B.** Hierarchical Clustering.<br>
**C.** DESeq2.<br>
**D.** K-means clustering.

### Problem 30

Which of the following best describes the role of transcriptome assembly in RNA-seq analysis?

**A.** It is used to identify single nucleotide polymorphisms (SNPs) within coding regions.<br>
**B.** It involves the alignment of RNA-seq reads to a reference genome to identify expressed genes.<br>
**C.** It is the process of piecing together RNA-seq reads to reconstruct the full-length transcripts that were present in the sample.<br>
**D.** It refers to the quantification of each gene's expression level based on the number of reads aligned to its exons.

### Problem 31

What is a major challenge when quantifying gene expression using RNA-seq data from highly heterogeneous samples, such as those obtained from tumor tissues?

**A.** Determining the exact time of day the sample was collected.<br>
**B.** Accounting for the high degree of genetic similarity between different species.<br>
**C.** Deconvolving the mixed expression profiles to identify the contributions from different cell types.<br>
**D.** Ensuring that all RNA molecules are sequenced at exactly the same rate.

## Salmon

### Problem 32

What is the primary method used by Salmon for mapping reads to transcripts?

**A.** Exact alignment using dynamic programming.<br>
**B.** Quasi-mapping to a reference transcriptome.<br>
**C.** Greedy alignment to a reference genome.<br>
**D.** K-mer based mapping to a reference proteome.

### Problem 33

Which of the following best describes the purpose of "quasi-mapping" in Salmon?

**A.** To identify the exact location of reads on the genome.<br>
**B.** To rapidly approximate the positions where reads may originate from the transcriptome.<br>
**C.** To generate a complete, gapless alignment of reads to transcripts.<br>
**D.** To correct sequencing errors in reads before mapping.

### Problem 34

Salmon utilizes a specific model to correct for biases in RNA-seq data. What does this model account for?

**A.** Only sequence composition bias at the beginning of reads.<br>
**B.** Only PCR amplification bias.<br>
**C.** Sequence-specific and positional-specific biases.<br>
**D.** The length of the poly-A tail in eukaryotic mRNAs.

### Problem 35

In Salmon, what is the significance of using "effective length" for transcripts during quantification?

**A.** It adjusts for the physical length of the transcript to aid in visualization.<br>
**B.** It represents the actual length of the transcript after splicing.<br>
**C.** It corrects for biases introduced by variable transcript lengths and sequencing depth.<br>
**D.** It is used to calculate the cost of sequencing per base pair.

### Problem 36

How does Salmon deal with transcripts that have multiple potential origins for a given read?

**A.** It assigns the read to the longest transcript.<br>
**B.** It discards reads that cannot be uniquely mapped.<br>
**C.** It uses an expectation-maximization (EM) algorithm to probabilistically assign reads to transcripts.<br>
**D.** It randomly assigns the read to one of the possible transcripts.

### Problem 37

What feature allows Salmon to perform transcript quantification at a faster rate compared to traditional alignment methods?

**A.** Utilizing GPU acceleration for all computations.<br>
**B.** The avoidance of full read alignment in favor of quasi-mapping.<br>
**C.** Performing all calculations in a cloud-based environment.<br>
**D.** Requiring less computational memory due to simplified data structures.

### Problem 38

Explain how Salmon adjusts for transcript abundance estimation using the concept of "effective length".
Why is this adjustment necessary, and what factors does it take into account?

### Problem 39

Discuss the role of the expectation-maximization (EM) algorithm in the context of Salmon's quantification process.
How does the EM algorithm contribute to the accuracy of transcript abundance estimates?

### Problem 40

Salmon incorporates bias correction mechanisms to improve the accuracy of transcript quantification.
Describe the types of biases that are accounted for by Salmon and the importance of correcting these biases in RNA-seq data analysis.

### Problem 41

Salmon can output quantification results in the form of Transcripts Per Million (TPM) among other metrics.
Explain the significance of TPM as a measure of transcript abundance and how it facilitates comparison across samples.

### Problem 42

Describe the fundamental approach Salmon takes to estimate transcript abundance from RNA-seq data.
How does it differ from traditional read alignment, and what advantages does this approach offer in terms of computational efficiency and accuracy?

## Differential gene expression analysis

### Problem 43

What is differential gene expression analysis and why is it important in understanding biological processes?

### Problem 44

Describe the basic workflow of a differential gene expression analysis starting from RNA sequencing data to the identification of differentially expressed genes.

### Problem 45

Discuss the importance of biological replicates in differential gene analysis. How do they impact the statistical power of the analysis?

### Problem 46

What is the role of normalization in RNA-seq data analysis? Describe at least two methods used for normalization and their purposes.

### Problem 47

Identify and explain two common statistical tests used in differential gene expression analysis. Discuss their assumptions and applicability.

### Problem 48

What is the primary goal of differential gene expression analysis?

**A.** To identify genes that show significant differences in expression across various conditions or treatments.<br>
**B.** To categorize genes into different clusters based on their sequence similarity.<br>
**C.** To predict the 3D structure of proteins encoded by genes.<br>
**D.** To determine the entire DNA sequence of an organism's genome.

### Problem 49

Which statistical method is commonly used for identifying differentially expressed genes in RNA-seq data?

**A.** Principal component analysis (PCA).<br>
**B.** T-test.<br>
**C.** EdgeR.<br>
**D.** K-means clustering.

### Problem 50

In the context of differential gene expression analysis, what does the term "fold change" refer to?

**A.** The change in gene expression level from the control group to the treatment group.<br>
**B.** The number of times a gene's expression doubles in response to a condition.<br>
**C.** The difference in gene expression levels between two groups, adjusted for variance.<br>
**D.** The ratio of the average expression levels of a gene in one condition to its average expression levels in another condition.

### Problem 50

Why is multiple testing correction important in differential gene expression analysis?

**A.** To increase the statistical power of the tests.<br>
**B.** To reduce the chance of false positives due to the large number of genes tested.<br>
**C.** To ensure that all genes are expressed equally across samples.<br>
**D.** To validate the experimental conditions.

### Problem 51

Which of the following is NOT a commonly used software or package for differential gene expression analysis?

**A.** DESeq2.<br>
**B.** EdgeR.<br>
**C.** BLAST.<br>
**D.** limma.

### Problem 52

What is the purpose of normalization in differential gene expression analysis?

**A.** To align DNA sequences from different samples.<br>
**B.** To adjust for differences in sequencing depth and gene length across samples.<br>
**C.** To enhance the visual representation of gene expression data.<br>
**D.** To identify single-nucleotide polymorphisms (SNPs).
