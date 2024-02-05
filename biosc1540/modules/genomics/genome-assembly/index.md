# Genome assembly

In bioinformatics, genome assembly represents the process of combining many short DNA sequences to recreate the original chromosomes from which the DNA originated.
Sequence assembly is one of the basic steps after performing next-generation sequencing, PacBio SMRT sequencing, or Nanopore sequencing.
The established genome assembly can be submitted to databases such as the European Nucleotide Archive, NCBI Assembly, and Ensembl Genomes.
You can also browse these databases for genomic sequences done by other researchers.

!!! quote "**Figure 1**"

    <figure markdown>
    ![](https://sandbox.dodona.be/en/activities/1535795563/description/6Vg7bgJkMY2_iKxn/media/fragment-assembly.png){ alight=left width=500 }
    </figure>

    Credit: [Dodona](https://dodona.be/en/exercises/1535795563/#)

There are two different types of genome assembly: [de novo](./de-novo/) assembly and mapping to a [reference](./reference/) genome (also known as reference-based alignment).
[De novo](./de-novo/) assembly refers to the genome assembly of a novel genome from scratch without reference to genomic data.
A reference genome or a [reference assembly](./reference/) is a digital nucleic acid sequence database that represents a species’ set of genes.
Once the reference genome is available, with its aid, the genome assembly becomes much easier, quicker, and even more accurate.
Therefore, unless necessary, researchers choose the method of [reference-based alignment](./reference/).
Reference-based alignment has become the current standard in diagnostics.

A high-quality and well-annotated genome assembly is increasingly becoming an essential tool for applied and basic research across many biological disciplines in the 21st century that can turn any organism into a model organism.
Thus, securing complete and accurate reference genomes and annotations before analyzing post-genome studies such as genome-wide association studies, structural variations, and posttranslational studies (methylation or histone modification) has become a cornerstone of modern genomics.
However, early works have warned against its applications in genome assembly because the resultant assemblies may contain biases toward errors and chromosomal rearrangements in the existing reference genome.

## Contigs

In the context of genome assembly, a contig (derived from the word “contiguous”) is a set of DNA segments or sequences that overlap in a way that provides a contiguous representation of a genomic region.

!!! quote "**Figure 2**"

    <figure markdown>
    ![](/img/genomics/contigs.png){ alight=left width=800 }
    </figure>

    Credit: [National Human Genome Research Institute](https://www.genome.gov/genetics-glossary/Contig)

The process of generating an assembly involves the isolation of genomic DNA from a biological sample and fragmentation of DNA into small pieces that are then sequenced individually.
Once the sequences of these small pieces, called reads, are obtained, researchers assemble these like tiny pieces of a giant puzzle into progressively larger contiguous sequence pieces, which are called contigs.
This approach is termed Whole Genome Shotgun (WGS) sequencing.

Contigs are the first level in the hierarchy of a genomic assembly.
The next step is to build scaffolds (supercontigs).
To build a scaffold, researchers place several contigs in the correct order and orientation.

Therefore, contigs can refer both to overlapping DNA sequences and to overlapping physical segments.
They play a crucial role in reconstructing the original DNA sequence of a chromosome or a region of a chromosome.

## Coverage

Starting with some notation, let

-   $G$ = Length of the genome,
-   $L$ = Read length,
-   $N$ = Number of reads.

We assume that $L$ is fixed.
We first derive a relationship between the above three values that would result in successful assembly.
Since $L$ and $G$ are fixed with our choice of experiment and technology, we need to choose $N$ (i.e., "How much sequencing do I need to do?").
Intuitively, the reads must cover the entire genome, and each base has to be covered by at least 1 read.
Therefore $LN>G$ or $N>G/L$.
In order to achieve this lower bound, we need to have all $LN$ reads aligning perfectly without overlap, which is highly unlikely.

It turns out that if we let ϵ represent the probability of not achieving full genome coverage, then

$$
N \leq \frac{G}{L} \ln \left( \frac{G}{\varepsilon} \right)
\tag{1}
$$

If this condition is met, then we have achieved coverage with probability $\leq 1 - \varepsilon$.
This result is more stringent than our previous bound due to the ln(G/ϵ) term, which is greater than 1.

In isolation, $N$ is not too informative.
For a particular sequencing experiment, $N$=100 million reads could be large or small depending on the size of the genome and the length of each read.
Because the reads are random, some bases will be covered more often than other bases.
Therefore rather than using $N$, we are instead interested in the coverage depth, or the average coverage per base, which is described by

$$
c = \frac{NL}{G} \leq \ln \left( \frac{G}{\varepsilon} \right).
$$

As an example, if the genome of interest is about one billion base pairs long, then we need at least 25x coverage depth since $G = 10^{9}$; $\varepsilon = 0.01$, $\Rightarrow c = 25.328$.
Note that $LG$ is quite small, and therefore the number of reads can be approximated with a Poisson distribution with mean

$$
c= \frac{NL}{G}.
$$

## Unresolvable repeats

Unresolvable repeats pose a significant hurdle in genome assembly, as they create ambiguity in determining the correct order and arrangement of DNA sequences.
The key strategy employed to handle unresolvable repeats involves essentially leaving them out of the assembly.
This approach is crucial for ensuring the accuracy and reliability of the assembled genome.

Unresolvable repeats have a profound effect on the assembly process, leading to the fragmentation of the genome.
When faced with unresolvable repeats, the assembly algorithm breaks down the genetic sequence into smaller, manageable fragments.
This fragmentation is a necessary step to navigate the complexities introduced by repeats and ensures a more accurate reconstruction of the genome.

## Shortest common superstring

The shortest common superstring (SCS) problem is a concept in computer science that holds significant importance in bioinformatics, especially in genome assembly.
The Shortest Common Superstring problem involves finding the shortest string that contains all given strings as subsequences.
In simpler terms, if you have a set of strings, the challenge is to construct the smallest possible string that includes each of these strings as a part of it without necessarily keeping them contiguous but preserving their order.

In bioinformatics, the SCS problem is particularly relevant in assembling genomes from sequencing reads.
Genome assembly entails piecing together DNA sequences to reconstruct the original genome from which the DNA was sampled.
Due to the limitations in sequencing technology, genomes are often sequenced in small fragments.
These fragments must then be assembled like a puzzle to deduce the original genome sequence.

DNA is broken into numerous small pieces in genome sequencing, sequenced to produce reads.
These reads are short sequences of nucleotides (A, C, G, T).
The main challenge is assembling these reads in the correct order to reconstruct the genome's original sequence.
This process is akin to solving the SCS problem, where each read is a string.
The goal is to merge them into a single, continuous sequence that is as short as possible while still containing all the original sequences.

The key to solving this problem lies in finding overlaps between the reads.
By identifying how the end of one read overlaps with the beginning of another, it's possible to stitch these reads together to minimize redundancy, thus approaching the shortest common superstring.

It's important to note that the SCS problem is NP-hard, meaning that no known algorithm can solve it efficiently for all possible input sets.
In the context of genome assembly, this complexity is managed through various heuristic and approximation algorithms that seek to find a solution that is good enough, if not mathematically perfect.

Imagine the original DNA sequence we aim to reconstruct is: `ACGTACGTGACG`.
If we are provided three sequencing reads:

1.  `ACGTAC`
2.  `TACGTG`
3.  `GTGACG`

Identify Overlaps:

-   The suffix of Read 1 (`ACGTAC`) overlaps with the prefix of Read 2 (`TACGTG`) by five nucleotides (`ACGT`).
-   The suffix of Read 2 (`TACGTG`) overlaps with the prefix of Read 3 (`GTGACG`) by two nucleotides (`GT`).

Merge Based on Overlaps:

-   Merging Read 1 and Read 2 through their overlap gives us `ACGTACGTG`.
-   Then, merging this combined sequence with Read 3 by aligning the overlap of GT gives us the complete sequence `ACGTACGTGACG`.

!!! warning

    When we discuss an overlap between two sequences in the context of DNA sequencing or bioinformatics, we refer to the condition where the suffix of one sequence matches the prefix of another sequence.
    This scenario facilitates the sequential alignment and assembly of fragments into a longer, continuous sequence.

    If the suffix of one sequence matches the suffix of another, we do not typically describe this as an overlap in the context of sequencing assembly or similar applications.
    This is because such a match does not provide a way to extend the sequence by combining the two sequences end-to-end.
    Instead, it indicates that both sequences end in the same way but does not necessarily provide a direct means of linking one sequence to the beginning of another to form a longer chain.

    **Overlap Case** (Suffix of $x$ matches Prefix of $y$).

    $$
    x = 5' [A, C, G, T, A, C] 3'
    $$

    $$
    y = 5' [A, C, T, G, G, C] 3'
    $$

    Here, if the suffix of $x$ (e.g., $[T, A, C]$) matches the prefix of $y$ (e.g., $[T, A, C]$), we can align and connect these sequences to form a longer sequence because there is a continuity that allows for extension.

    **Non-Overlap Case** (Suffix of $x$ matches Suffix of $y$).

    $$
    x = 5' [A, G, T, C, G, A] 3'
    $$

    $$
    y = 5' [T, T, C, G, A] 3'
    $$

    If the suffix of $x$ (e.g., $[C, G, A]$) matches the suffix of $y$ (e.g., $[C, G, A]$), there is no direct way to extend the sequence by concatenating $x$ and $y$ because both sequences end in the same manner.
    This scenario doesn't contribute to the assembly of a longer sequence from fragments.

<!-- REFERENCES -->

[^jung2020twelve]: Jung, H., Ventura, T., Chung, J. S., Kim, W. J., Nam, B. H., Kong, H. J., ... & Eyun, S. I. (2020). Twelve quick steps for genome assembly and annotation in the classroom. *PLoS computational biology, 16*(11), e1008325. doi: [10.1371/journal.pcbi.1008325](https://doi.org/10.1371/journal.pcbi.1008325)
[^ee372]: [EE 372: Data Science for High-Throughput Sequencing](https://data-science-sequencing.github.io/)
