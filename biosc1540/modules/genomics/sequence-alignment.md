# Sequence alignment

!!! danger "DRAFT"

    This page is a work-in-progress and is subject to change at any moment.

### Attribution

Adapted from the Wikipedia article on [sequence alignment](https://en.wikipedia.org/wiki/Sequence_alignment), [multiple sequence alignment], [homology](https://en.wikipedia.org/wiki/Homology_(biology), and [consensus sequence](https://en.wikipedia.org/wiki/Consensus_sequence).

## Introduction

In bioinformatics, a **sequence alignment** is a way of arranging the 2 or more sequences of DNA, RNA, or protein to identify regions of similarity that may be a consequence of functional, structural, or evolutionary relationships between the sequences.  In many cases, the input set of query sequences are assumed to have an evolutionary relationship by which they share a linkage and are descended from a common ancestor. Aligned sequences of nucleotide or amino acid residues are typically represented as rows within a matrix. **Gaps** are inserted between the residues so that identical or similar characters are aligned in columns.  A **pairwise alignment** aligns two sequences, while a **multiple sequence alignment (MSA)** aligns three or more.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/Histone_Alignment.png" width="50%" />
    <figcaption> A multiple sequence alignment of mammalian histone proteins. Sequences are the amino acids for residues 120-180 of the proteins. Residues that are **conserved** across all sequences are highlighted in grey. Below the protein sequences is a key denoting conserved sequence (*), conservative mutations (:), semi-conservative mutations (.), and non-conservative mutations ( ). Conservative mutations result in amino acids that are chemically similar to each other, while non-conservative mutations result in chemically distance residues </figcaption>
</figure>

## Homology

In biology, homology is similarity due to **shared ancestry** between a pair of structures or genes in different taxa. A common anatomical example of homologous structures is the forelimbs of vertebrates, where the wings of bats and birds, the arms of primates, the front flippers of whales and the forelegs of four-legged vertebrates like dogs and crocodiles are all derived from the same ancestral tetrapod structure. Evolutionary biology explains homologous structures adapted to different purposes as the result of descent with modification from a common ancestor.

**Sequence homology** between protein or DNA sequences is similarly defined in terms of shared ancestry. Two segments of DNA can have shared ancestry because of either a speciation event or a gene duplication event. Homology among proteins or DNA is inferred from their sequence similarity. Significant similarity is strong evidence that two sequences are related by divergent evolution from a common ancestor. Alignments of multiple sequences are used to discover homologous regions.

### Interpretation

If two sequences in an alignment share a **common ancestor**, mismatches can be interpreted as point mutations and gaps as indels (that is, insertion or deletion mutations) introduced in one or both lineages in the time since they diverged from one another. In sequence alignments of proteins, the degree of similarity between amino acids occupying a particular position in the sequence can be interpreted as a rough measure of how **conserved** a particular region is among lineages. The absence of substitutions, or the presence of only very **conservative mutations** (that is, the substitution of amino acids whose side chains have similar biochemical properties) in a particular region of the sequence, suggest that this region has structural or functional importance.

### Conserved sequences

In evolutionary biology, conserved sequences are identical or similar sequences in nucleic acids (DNA and RNA) or proteins across species, or within a genome, or between donor and receptor taxa. Conservation indicates that a sequence has been maintained by natural selection, likely because mutations in the sequence dramatically harm the health and fitness of the organism.

A **highly conserved sequence** is one that has remained relatively unchanged far back up the phylogenetic tree, and hence far back in geological time. Examples of highly conserved sequences include the RNA components of ribosomes present in all domains of life, the homeobox sequences widespread amongst eukaryotes, and the tmRNA in bacteria. The study of sequence conservation overlaps with the fields of genomics, proteomics, evolutionary biology, phylogenetics, bioinformatics and mathematics.

Just because two sequences are similar does not mean that the sequence has been conserved and the sequences are homologs.  **Convergent evolution** can result in two un-related sequence becoming similar.  In some cases, two sequences can code for proteins or parts of proteins with similar function but with no shared evolutionary history.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/9/94/Caspase-motif-alignment.png" width="80%" />
    <figcaption> MSA of the seven Drosophila caspases colored by motifs.  Note the long stretches of gaps (-) required to align the sequences </figcaption>
</figure>

### Global and local alignments

**Global alignments**, which attempt to align every residue in every sequence, are most useful when the sequences in a set are similar and of roughly equal size. (This does not mean global alignments cannot start and/or end in gaps.) **Local alignments** are more useful for dissimilar sequences that are suspected to contain relatively small regions of similarity or similar sequence motifs within their larger sequence context.

## Multiple sequence alignment


### Introduction

Multiple sequence alignment is an extension of pairwise alignment to incorporate more than two sequences at a time. Multiple alignment methods try to align all of the sequences in a given query set. Multiple alignments are often used in identifying conserved sequence regions across a group of sequences hypothesized to be evolutionarily related. Such conserved sequence motifs can be used in conjunction with structural and mechanistic information to locate the catalytic active sites of enzymes. Alignments are also used to aid in establishing evolutionary relationships by constructing **phylogenetic trees**. Multiple sequence alignment is often used to assess sequence conservation of protein domains, tertiary and secondary structures, and even functionally significant individual amino acids or nucleotides.

Multiple sequence alignment also refers to the process of aligning a set of sequences. MSAs require more sophisticated methodologies than pairwise alignment because they are more computationally complex. Multiple sequence alignments is computationally difficult one of the original challenges tackled by computational biologists. The utility of these alignments in bioinformatics has led to the development of a variety of methods suitable for aligning three or more sequences.

### Consensus sequences

MSAs allow determination of a **consensus sequence**.  In molecular biology and bioinformatics, the consensus sequence (or canonical sequence) is the calculated sequence of most frequent residues, either nucleotide or amino acid, found at each position in a sequence alignment. Consensus sequences are often printed at the bottom of MSAs, and can be elaborated on using sequence logos (see below).  Developing software for pattern recognition is a major topic in genetics, molecular biology, and bioinformatics. Specific sequence motifs can function as regulatory sequences controlling biosynthesis, or as signal sequences that direct a molecule to a specific site within the cell or regulate its maturation. Since the regulatory function of these sequences is important, they are thought to be conserved across long periods of evolution. In some cases, evolutionary relatedness can be estimated by the amount of conservation of these sites.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Hemagglutinin-alignments.png" width="30%" />
    <figcaption> MSA of 27 avian influenza hemagglutinin protein sequences colored by residue conservation (top) and residue properties (bottom) </figcaption>
</figure>


### Phylogenetic use

Multiple sequence alignments can be used to create a phylogenetic treeLinks to an external site. This is made possible by two reasons. The first is because functional domains that are known in annotated sequences can be used for alignment in non-annotated sequences. The other is that conserved regions known to be functionally important can be found. This makes it possible for multiple sequence alignments to be used to analyze and find evolutionary relationships through homology between sequences. Point mutations and insertion or deletion events (called indels) can be detected.

Multiple sequence alignments can also be used to identify functionally important sites, such as binding sites, active sites, or sites corresponding to other key functions, by locating conserved domains. When looking at multiple sequence alignments, it is useful to consider different aspects of the sequences when comparing sequences. These aspects include identity, similarity, and homology. Identity means that the sequences have identical residues at their respective positions. On the other hand, similarity has to do with the sequences being compared having similar residues quantitatively. For example, in terms of nucleotide sequences, pyrimidines are considered similar to each other, as are purines. Similarity ultimately leads to homology, in that the more similar sequences are, the closer they are to being homologous. This similarity in sequences can then go on to help find common ancestry.

### Gallary

Below are examples of MSAs.  Try to determine what the color-coding indicates, how highly conserved regions are with the alignments, and if a consensus sequence is shown.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/79/RPLP0_90_ClustalW_aln.gif" width="50%" />
    <figcaption> First 90 positions of a protein multiple sequence alignment of instances of the acidic ribosomal protein P0 (L10E) from several organisms. Generated with ClustalX. </figcaption>
</figure>

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/WPP_domain_alignment.PNG" width="70%" />
    <figcaption> . </figcaption>
</figure>

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Muscle_alignment_view.png/1600px-Muscle_alignment_view.png" width="70%" />
    <figcaption> These are sequences being compared in a MUSCLE multiple sequence alignment (MSA). Each sequence name (leftmost column) is from various louse species, while the sequences themselves are in the second column. Note the large insertion present in a single sequence </figcaption>
</figure>

## Sequence logos

### Attribution

Adapted from the Wikipedia entry on [Sequence Logos](https://en.wikipedia.org/wiki/Sequence_logo)


### Introduction

In bioinformatics, a **sequence logo** is a graphical representation of the sequence similarity of nucleotides (in a strand of DNA/RNA) or amino acids (in protein sequences). A sequence logo is created from a collection of aligned sequences and depicts the **consensus sequence** and diversity of the sequences. Sequence logos are frequently used to depict sequence characteristics such as protein-binding sites in DNA or functional units in proteins.

A sequence logo consists of a stack of letters at each position, though sometimes one letter is much larger than the others. The relative sizes of the letters indicate their frequency in the sequences. The total height of the letters depicts the information content of the position, with more informative positions giving researchers more confidence in conclusions about a position in the logo.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/bf/KozakConsensus.jpg" width="50%" />
    <figcaption> A sequence logo showing the most conserved bases around the initiation codon from all human mRNAs (Kozak consensus sequence). Note that the initiation codon is not drawn to scale. </figcaption>
</figure>

### Sequence motif

Similarity in a sequence alignment or sequence logo may be due to relatively recent common ancestory, or simply similar molecular function.  Sequence that are functionally similar are termed **sequence motifs**.   A sequence motif is a nucleotide or amino-acid sequence pattern that is widespread and usually assumed to be related to biological function of the macromolecule.

### Consensus logo

A consensus logo is a simplified variation of a sequence logo. Like a sequence logo, a consensus logo is created from a collection of aligned protein or DNA/RNA sequences and conveys information about the conservation of each position of a sequence motif or sequence alignment. However, a consensus logo displays only conservation information, and not explicitly the frequency information of each nucleotide or amino acid at each position. Instead of a stack made of several characters, denoting the relative frequency of each character, the consensus logo depicts the degree of conservation of each position using the height of the consensus character at that position.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/85/LexA_gram_positive_bacteria_sequence_logo.png" width="50%" />
    <figcaption> A consensus logo for the LexA-binding motif of several Gram-positive species.</figcaption>
</figure>


## Vocab


* **Alignment**: A comparison of two or more gene or protein sequences in order to determine their degree of similarity in amino acid or bases, respectively.
* **Amino acid motifs**: Three-dimensional protein structural elements that are composed of a combination of secondary structures. They include HELIX-LOOP-HELIX MOTIFS and ZINC FINGERS. Motifs are typically the most conserved regions of PROTEIN DOMAINS and are critical for domain function. However, the same motif may occur in proteins or enzymes with different functions.
* **Consensus Sequence**: A theoretical representative nucleotide or amino acid sequence in which each nucleotide or amino acid is the one which occurs most frequently at that site in the different sequences which occur in nature. The phrase also refers to an actual sequence which approximates the theoretical consensus. A known CONSERVED SEQUENCE set is represented by a consensus sequence. Commonly observed supersecondary protein structures (AMINO ACID MOTIFS) are often formed by conserved sequences.
* **Conserved sequence**: A sequence of amino acids in a polypeptide or of nucleotides in DNA or RNA that is similar across multiple species. A known set of conserved sequences is represented by a consensus sequence. Motifs are often composed of conserved sequences, but not always.
* **Sequence alignment**: A method for aligning sequences of a protein or nucleic acid to identify regions of similarity that may indicate structural, functional, and/or evolutionary relationships.
