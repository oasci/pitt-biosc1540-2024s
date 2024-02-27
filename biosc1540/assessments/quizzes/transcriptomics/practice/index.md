# Practice problems

## Burrows-Wheeler Transforms

### Problem 1

Given a short RNA sequence, construct the BWT matrix and the final BWT string.
Consider the RNA sequence `AGGCAU$`, where `$` signifies the end of the sequence.

A.  Generate all cyclic rotations of `AGGCAU$`.<br>
B.  Sort the rotations lexicographically.<br>
C.  Write down the last column (the BWT of the sequence).

### Problem 2

Given a BWT string, reconstruct the original RNA sequence. Use the BWT string `G$CUAGA`.

A.  List all suffixes of the BWT string in sorted order.<br>
B.  Reconstruct the original sequence from the BWT string.

### Problem 3

Given the BWT of an RNA sequence `G$CUAGA` and a pattern `AGA`, determine if the pattern exists in the original RNA sequence.

A.  Use the LF-mapping (Last-to-First column mapping) process to find the pattern in the BWT.<br>
B.  Report whether the pattern exists in the sequence and, if so, the position(s) of its occurrence.

### Problem 4

Consider the RNA sequence `UACGUGACG$`.

A. Construct the BWT of the given sequence.<br>
B. Using the BWT, discuss how you would compress the sequence.<br>
C. Explain how you could use the BWT and additional data structures to quickly find occurrences of the substring `GUG` in the sequence.
