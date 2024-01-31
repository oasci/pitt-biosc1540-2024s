# Lecture 07

**Date:** Jan 30, 2024

## Learning objectives

What you should be able to do after today's lecture.

1.  🧫 Define antibiotic resistance and assess its global impact on public health.
2.  🧫 Analyze challenges arising from antibiotic resistance and evaluate genomics' role in mitigating them.
3.  🧫 🧮 Explain the principles underlying Sanger sequencing.
4.  🧫 🧮 Outline the methodology of Illumina sequencing, specifically the sequencing by synthesis approach.
5.  🧫 🧮 Identify and contrast Sanger sequencing with Illumina sequencing, covering principles, methods, applications, and technological advancements.

## Readings

Relevant content for today's lecture.

-   [Genomics learning scenario](/modules/genomics/learning-scenario)
-   [Sequencing](/modules/genomics/sequencing/)

## Activities

-   [Outbreak Investigation Simulation: Mysterious Respiratory Illness](./amr-activity.md)

## Presentation

[Live link](https://slides.com/d/YJdzcYY/live) for during class.
Full presentation (below) will be released afterwards.

<iframe src="https://slides.com/aalexmmaldonado/biosc1540-2024s-l07/embed?byline=hidden&share=hidden" width="100%" height="600" title="biosc1540-2024s-L07" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

### Practice questions

What is the primary purpose of using dideoxynucleotides in Sanger sequencing reactions?<br>

A. To increase the speed of DNA synthesis.<br>
B. To label DNA fragments.<br>
C. To terminate DNA synthesis at specific bases.<br>
D. To enhance the fidelity of DNA replication.

??? note "Answer"

    **C**

A 500-base pair fragment is sequenced with Sanger using four chain termination reactions.
Three reactions (with ddATP, ddCTP, and ddTTP) produce reads up to 400 nucleotides long.
However, the maximum read length observed in the ddGTP reaction only reads 100 nucleotides.
What is the best explanation?<br>

A. ddGTP molecules were degraded.<br>
B. There is a single-point mutation in the original sequence at position 101.<br>
C. Non-specific primer binding occurs.<br>
D. There are six consecutive cytosine bases in the original DNA sequence starting at base 95.

??? note "Answer"

    **D**

    The answer cannot be A, because if the the ddGTP molecules were degraded then the DNA polymerase would not be able to incorporate ddGTP.
    If only dGTP (with the 3' OH group) can be used, then we would never have premature termination.
    Therefore, we would have sequences much longer than 100 base pairs.

    The presence of a single-point mutation would have no affect in whether the replication was terminated always at 100.
    Thus, the answer cannot be B.
    One could argue that, theoretically, we could have induced a single-point mutation to a ddNTP nucleotide in the original strand.
    This would me our original strand would be unintentionally shortened to to 100 base pairs; something extremely unlikely to happen only in the ddGTP-involved reaction.

    Non-specific primer binding could potentially lead to issues in PCR amplification, but Sanger sequencing primers are designed to be specific for the target sequence.
    If there was non-specific primer binding, we would still have the possibility of having sequences longer than 100 base pairs.

    This leaves **D** as our answer; however, we can sill rationalize it.
    Suppose I am sequencing 5' CCCCCCGTTAATC 3' in the dGTP+ddGTP solution.

    Starting at the 3' end, DNA polymerase will incorporate either dGTP or ddGTP into the growing strand.
    If a ddGTP is incorporated, then replication terminates at that nucleotide.
    If dGTP is incorporated, then DNA polymerase would continue until we reached CCCCCC.
    At each C in the reference strand, DNA polymerase will incorporate either a dGTP or ddGTP.
    At position 95, we could incorporate ddGTP and terminate replication or dGTP and continue.
    Suppose we incorporate dGTP and move to position 96; this is C again so we have a chance of incorporating dGTP (continue) or ddGTP (terminate).
    Because each consecutive C in the reference strand is a chance to prematurely terminate replication, it is thus likely we terminate before getting past 100 nucleotides.
