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
x[i:j] = (x[i], x[i + 1], \ldots, x[j]).
$$

This looks very similar to slicing Python lists!
For example,

```python
dna_seq = ["A", "A", "C", "T", "G", "C", "G"]
```

if we wanted the `CTG` substring we would use

```python
dna_seq[2:5]
```

!!! info

    We are going to assume that that $i$ starts at zero to be consistent with Python indexing.
    Most mathematical formulations start at 1.

### Prefix

When the first index of the substring is `0`, we give this a special name called the prefix.
For example, `dna_seq[0:3]` and `dna_seq[0:2]` would be valid prefixes; the only thing that is changing is the length of the substring.
We will refer to this as $x_l$.

### Suffix

A suffix is when we slice a portion from the end; for example, `dna_seq[2:l]` would give us `["C", "T", "G", "C", "G"]` if we assume that `l` is the total length of `dna_seq`.
We will refer to this as $x^l$.

One way to keep track if $x_l$ or $x^l$ is the prefix or suffix substring is to imaging we have our DNA sequence vertically from beginning (bottom) to end (top).
Thus, $x_l$ would be near the bottom of $x$ so that is the prefix substring.
$x^l$ would be near the top of $x$ so that is the suffix substring.

## Overlap

In the context of DNA sequences, an overlap occurs when the suffix of one sequence ($x^l$) is identical to the prefix of another sequence ($y_l$).
This means that the end portion of the first sequence ($x$) matches the starting portion of the second sequence ($y$).
We can arbitrarily select each sequence to be $x$ or $y$, so an overlap could also be $x_l$ and $y^l$.

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

[^huson2001greedy]: Huson, D. H., Reinert, K., & Myers, E. (2001, April). The greedy path-merging algorithm for sequence assembly. In Proceedings of the fifth annual international conference on Computational biology (pp. 157-163). doi: [10.1145/369133.369190](https://doi.org/10.1145/369133.369190)
[^shomorony2016information]: Shomorony, I., Kim, S. H., Courtade, T. A., & Tse, D. N. (2016). Information-optimal genome assembly via sparse read-overlap graphs. *Bioinformatics, 32*(17), i494-i502. doi: [10.1093/bioinformatics/btw450](https://doi.org/10.1093/bioinformatics/btw450)
[^]: Bresler, G., Bresler, M. A., & Tse, D. (2013, April). Optimal assembly for high throughput shotgun sequencing. In BMC bioinformatics (Vol. 14, No. 5, pp. 1-13). BioMed Central. doi: [10.1186/1471-2105-14-S5-S18](https://doi.org/10.1186/1471-2105-14-S5-S18)
