# Global

Global pairwise sequence alignment is a computational technique used in bioinformatics to align two DNA sequences and identify regions of similarity that may indicate functional, structural, or evolutionary relationships between them.
This method is essential for various applications, including gene identification, phylogenetic analysis, and the study of evolutionary biology.

## Needleman-Wunsch algorithm

The Needleman-Wunsch algorithm,[^needleman1970general] developed by Saul B. Needleman and Christian D. Wunsch in 1970, is a pioneering method in bioinformatics for aligning protein or nucleotide sequences.
This algorithm was among the first applications of dynamic programming to compare biological sequences.
It introduced a systematic way to tackle the complex problem of sequence alignment by breaking it down into smaller, manageable parts.

The algorithm operates on optimizing the global alignment between two sequences.
It generates all possible alignments, scoring each based on a predefined scoring system and identifying the alignment(s) with the highest score as the optimal solution.
This approach ensures that the alignment spans the entire length of both sequences, accommodating matches, mismatches, and gaps (insertions or deletions) to maximize the overall alignment score.
The process of the Needleman-Wunsch algorithm can be divided into three main steps: initialization, matrix filling, and traceback.

### Initialization

The initialization phase involves creating a scoring matrix, $T$, with one sequence (Seq1: "ATTAC") on the x-axis and the other (Seq2: "AATTC") on the y-axis.

The scoring matrix is initialized as follows:

-   Start with a cell $(0,0)$ having a score of $0$.
-   Each subsequent cell in the first row and column is assigned a gap penalty, which accumulates linearly.
    For a gap penalty of $-1$, the initialization looks like this:

| **D** |   | **A** | **A** | **T** | **T** | **C** |
|---|---|---|---|---|---|---|
|   | 0 | -1| -2| -3| -4| -5|
| **A** | -1|   |   |   |   |   |
| **T** | -2|   |   |   |   |   |
| **T** | -3|   |   |   |   |   |
| **A** | -4|   |   |   |   |   |
| **C** | -5|   |   |   |   |   |

### Filling the Matrix

To fill the matrix, we calculate the score for each cell using the following equation:

$$
\text{D}(i,j) = \max\begin{cases}
T[i-1,j-1] + s(a,b) & \text{(diagonal, match/mismatch)} \\
T[i-1,j] - \text{gap penalty} & \text{(up, gap)} \\
T[i,j-1] - \text{gap penalty} & \text{(left, gap)}
\end{cases}
$$

where $s(a,b)$ is the score of aligning character $a$ from Seq1 with character $b$ from Seq2.
For example, $s(A,A) = +1$ for a match and $s(A,T) = -1$ for a mismatch.
The gap penalty is typically $-1$.

Let's calculate the score for cell $(1,1)$, assuming $s(A,A) = +1$ and the gap penalty as $-1$:

-   From diagonal ($T[0,0]$): $0 + 1 = 1$
-   From up ($T[0,1]$): $-1 - 1 = -2$
-   From left ($T[1,0]$): $-1 - 1 = -2$

The maximum of these scores is $1$, so $T[1,1] = 1$.

| **D** |   | **A**  | **A**  | **T**  | **T**  | **C**  |
|---|---|----|----|----|----|----|
|   | 0 | -1 | -2 | -3 | -4 | -5 |
| **A** | -1| 1  | 0  | -1 | -2 | -3 |
| **T** | -2| 0  | 0  | 1  | 0  | -1 |
| **T** | -3| -1 | -1 | 1  | 2  | 1  |
| **A** | -4| -2 | 0  | 0  | 1  | 1  |
| **C** | -5| -3 | -1 | -1 | 0  | 2  |

### Traceback

Once the matrix is filled, we find the optimal path by starting from the bottom-right corner and moving to the cell that contributed to its score until we reach $(0,0)$.
The path to each cell indicates whether the characters are aligned (diagonal move), or a gap is introduced (up or left move).
For instance, if the final cell's score was obtained from a diagonal move, it suggests a match or mismatch based on the alignment score.
If the score came from moving up or left, it indicates introducing a gap in Seq1 or Seq2, respectively.

Given the sequences Seq1: "ATTAC" and Seq2: "AATTC", let's illustrate a simplified example of filling one more cell and performing a traceback:

-   For cell $(2,1)$, we consider:
-   Diagonal ($T[1,0] - 1 = -2$) for a mismatch,
-   Up ($T[1,1] - 1 = 0$) for a gap,
-   Left ($T[2,0] - 1 = -3$) for a gap.

Choosing the highest score, we fill $T[2,1]$ with $0$ to introduce a gap.

The traceback process would then start from $T[5,5]$, considering the entire matrix filled, and proceed to $T[0,0]$, highlighting the optimal alignment.

**Example 1:**

```text
-  A  T  T  A  C
#  *  *  *  #  *
A  A  T  T  -  C```
```

Score = 2

| **D** |   | **A** | **A** | **T** | **T** | **C** |
|---|---|----|-----|----|----|----|
|   | **0** | **-1** | -2  | -3 | -4 | -5 |
| **A** | -1 | 1  | **0** | -1 | -2 | -3 |
| **T** | -2 | 0  | 0   | **1** | 0  | -1 |
| **T** | -3 | -1 | -1  | 1  | **2** | 1  |
| **A** | -4 | -2 | 0   | 0  | **1** | 1  |
| **C** | -5 | -3 | -1  | -1 | 0  | **2** |

**Example 2:**

```text
A  -  T  T  A  C
*  #  *  *  #  *
A  A  T  T  -  C
```

Score = 2

| **D** |   | **A**   | **A**  | **T**  | **T**  | **C**  |
|---|---|-----|----|----|----|----|
|   | **0** | -1  | -2 | -3 | -4 | -5 |
| **A** | -1 | **1** | **0** | -1 | -2 | -3 |
| **T** | -2 | 0   | 0  | **1** | 0  | -1 |
| **T** | -3 | -1  | -1 | 1   | **2** | 1  |
| **A** | -4 | -2  | 0  | 0   | **1** | 1  |
| **C** | -5 | -3  | -1 | -1  | 0   | **2** |

<!-- REFERENCES -->

[^needleman1970general]: Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. *Journal of molecular biology, 48*(3), 443-453. doi: [10.1016/0022-2836(70)90057-4](https://doi.org/10.1016/0022-2836(70)90057-4)
