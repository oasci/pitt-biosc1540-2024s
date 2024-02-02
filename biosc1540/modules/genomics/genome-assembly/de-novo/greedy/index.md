# Greedy algorithms

Greedy algorithms are a class of algorithms in computer science that make the most optimal choice at each step as they work towards finding the overall optimal solution to a problem.
The "greediness" of these algorithms comes from their approach to make the locally optimal choice at each step with the hope that these local solutions will lead to a globally optimal solution.
Greedy algorithms are quite powerful in solving a wide range of problems, including those in computational biology, due to their efficiency and simplicity.

## Overview

The de novo assembly process using a greedy algorithm typically consists of several vital steps.
First, pairwise distances between reads are calculated, assessing the degree of overlap between sequences.
This information is then utilized to cluster reads with the greatest overlap, forming groups of potentially contiguous genomic regions.
Subsequently, reads are assembled within each cluster into longer contiguous sequences, or contigs, based on their overlapping regions.
This assembly step is crucial for piecing together the fragmented genomic information in the original short reads.

The process is iterative, as the algorithm refines the assembly by repeatedly calculating distances, clustering, and assembling reads. However, by nature, greedy algorithms may result in locally optimal solutions and struggle to reach a global optimum.
Additionally, repetitive sequences in the genome pose a challenge, as it can lead to ambiguities and errors in the assembly.

## Preliminaries

Let's assume that we have some string, $x$, that has $l$ symbols from the set ${A, C, G, T}$.
For example,

$$
x = [A, A, C, T, G, C, G].
$$

A substring of $x$ is a continuous interval of the symbols in $x$, and it is denoted as

$$
x[i:j] = (x[i], x[i + 1], \ldots x[j]).
$$

This looks very similar to slicing Python lists!


[^huson2001greedy]: Huson, D. H., Reinert, K., & Myers, E. (2001, April). The greedy path-merging algorithm for sequence assembly. In Proceedings of the fifth annual international conference on Computational biology (pp. 157-163). doi: [10.1145/369133.369190](https://doi.org/10.1145/369133.369190)
[^shomorony2016information]: Shomorony, I., Kim, S. H., Courtade, T. A., & Tse, D. N. (2016). Information-optimal genome assembly via sparse read-overlap graphs. *Bioinformatics, 32*(17), i494-i502. doi: [10.1093/bioinformatics/btw450](https://doi.org/10.1093/bioinformatics/btw450)
[^]: Bresler, G., Bresler, M. A., & Tse, D. (2013, April). Optimal assembly for high throughput shotgun sequencing. In BMC bioinformatics (Vol. 14, No. 5, pp. 1-13). BioMed Central. doi: [10.1186/1471-2105-14-S5-S18](https://doi.org/10.1186/1471-2105-14-S5-S18)
