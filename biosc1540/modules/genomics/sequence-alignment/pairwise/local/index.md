# Local

The local alignment method seeks to find the regions of highest similarity within the sequences without necessarily aligning them from end to end.
Local alignment is beneficial in identifying functional domains, motifs, or other conserved sequence elements within larger, more variable sequences.
It allows researchers to pinpoint regions of similarity that may be biologically relevant, even when the overall sequence similarity is low.
The objective is to identify the segments within the sequences that align the best, disregarding other regions that might not align well.

## Smith-Waterman algorithm

Developed by Temple F. Smith and Michael S. Waterman in 1981, the Smith-Waterman algorithm is a cornerstone of bioinformatics.
It is designed specifically for local sequence alignment.
It distinguishes itself from global alignment algorithms by focusing on finding the highest-scoring local alignments between two sequences.
This is especially useful for comparing sequences with varying lengths or when only a portion is similar.
The algorithm uses dynamic programming to calculate the best possible alignment score between subsequences, employing a scoring matrix that rewards matches and penalizes mismatches and gaps.

Notably, the algorithm can be expanded to use two different penalties for gap opening and gap extension, addressing the biological reality that starting a new gap is energetically less favorable than extending an existing one.
This differentiation in gap penalties helps to minimize gaps in the alignment, mirroring biological sequences more accurately.

-   **Match Score:** The score given when two characters at the current position in the compared sequences are the same.
-   **Mismatch Penalty:** The score deducted when the characters do not match.
-   **Gap Penalty:** The penalty applied for introducing a gap in one of the sequences.

### Initialization

When we start with the Smith-Waterman algorithm, we first set up a grid or matrix.
This grid has one sequence listed across the top and the other down the side.
The first step is to fill in the top row and the leftmost column with zeros.
This is because we need a starting point for our calculations, and beginning with zeros allows us to build up scores from nothing, which makes sense for finding local alignments where the alignment could start anywhere within the sequences.

### Matrix Filling

The matrix filling is the core of the Smith-Waterman algorithm, where each cell $(i, j)$ is calculated based on the possibility of a match/mismatch at that position or the introduction of a gap in either sequence.

$$
H(i, j) = \max \left\{ \begin{array}{l} 0, \\ H(i-1, j-1) + s(x_i, y_j), \\ \max_{k\geq1}\{H(i-k, j) - W_k\}, \\ \max_{l\geq1}\{H(i, j-l) - W_l\} \end{array} \right.
$$

Where:

-   $H(i, j)$ is the score at position $(i, j)$ of the matrix.
-   $s(x_i, y_j)$ is the score for aligning characters $x_i$ and $y_j$, which could be a positive value for a match or a negative value for a mismatch.
-   $W_k$ and $W_l$ are the gap penalties for opening a gap of length $k$ or $l$ in one of the sequences.
-   The first term inside the max function ensures that scores do not go negative, allowing the algorithm to reset at points of low similarity, thereby focusing on local alignments.

In other words:

-   If the letters from each sequence at that position are a match, we add to the score. We look back at the cell diagonally up-left from our current position, take its score, and add a certain number (let's say +2 for a simple example) because we found a match.
-   If the letters don't match, we might take a smaller score or subtract because it's not as good as a match.
-   We also consider skipping a letter in one of the sequences. This could happen if there's a gap in one sequence compared to the other. We take a small penalty for this, subtracting a little from our score.
-   The key here is we always pick the option that gives us the highest score, which could even be zero. We never let the score go negative because we're only interested in positive matches.

### Traceback

The traceback step finds the optimal local alignment by starting from the highest-scoring cell in the matrix and tracing back through the cells used to calculate its score until a cell with a score of 0 is reached.

-   Identify the cell $H(i, j)$ with the highest score in the matrix.
-   From $H(i, j)$, move to one of the following cells that was used to calculate $H(i, j)$, according to the rule that maximizes the score:
    -   To $H(i-1, j-1)$ if the move was a diagonal (indicating a match or mismatch).
    -   To $H(i-k, j)$ or $H(i, j-l)$ if the move was vertical or horizontal, indicating a gap of length $k$ or $l$.
-   The traceback continues until a cell with a score of 0 is reached, indicating the start of the optimal local alignment.

In other words:

-   We move from the highest score back towards the beginning, following the path that led to that high score. This could mean moving diagonally (which indicates a match), straight up, or straight left (which indicates a gap).
-   We stop tracing back when we hit a score of zero, which is our cue that this is where the best local alignment starts.

### Example

Consider two sequences to be aligned:

-   Sequence A: `ACTG`
-   Sequence B: `ACG`

We will use the following scoring scheme:

-   Match score: +2
-   Mismatch penalty: -1
-   Linear gap penalty: -2

Create a matrix $H$ with dimensions $5 \times 4$ (since `ACTG` is four characters and `ACG` is three characters, plus one for the initial zeros).

Fill the matrix based on the scoring rules. For simplicity, let's calculate a few cells:

-   For $H(1,1)$ (comparing `A` with `A`): the score is a match, so $H(1,1) = 2$.
-   For $H(2,1)$, considering a mismatch or gap introduces negative scores, we follow the rule that negative scores are reset to 0.

The filled matrix might look like this:

|     | - | A | C | T | G |
|-----|---|---|---|---|---|
| **-** | 0 | 0 | 0 | 0 | 0 |
| **A** | 0 | 2 | 0 | 0 | 0 |
| **C** | 0 | 0 | 4 | 2 | 0 |
| **T** | 0 | 0 | 2 | 3 | 1 |
| **G** | 0 | 0 | 0 | 1 | 5 |

Starting from the highest scoring cell, $H(4,4) = 5$, traceback reveals the alignment:

-   Sequence A: `ACTG`
-   Sequence B: `A-CG`

The score of 5 corresponds to three matches (`A`, `C`, `G`) and one gap (`-`).
