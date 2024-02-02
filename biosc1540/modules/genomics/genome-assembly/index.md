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

<!-- REFERENCES -->

[^jung2020twelve]: Jung, H., Ventura, T., Chung, J. S., Kim, W. J., Nam, B. H., Kong, H. J., ... & Eyun, S. I. (2020). Twelve quick steps for genome assembly and annotation in the classroom. *PLoS computational biology, 16*(11), e1008325. doi: [10.1371/journal.pcbi.1008325](https://doi.org/10.1371/journal.pcbi.1008325)
[^ee372]: [EE 372: Data Science for High-Throughput Sequencing](https://data-science-sequencing.github.io/)
