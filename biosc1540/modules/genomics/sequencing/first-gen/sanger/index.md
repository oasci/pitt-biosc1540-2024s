# Sanger

Sanger sequencing, also known as the "chain termination method," is a DNA sequencing technique that was developed by the English biochemist Frederick Sanger and his colleagues in 1977.[^sanger1977dna]
This method is designed for determining the sequence of nucleotide bases in a piece of DNA (commonly less than 1,000 bp in length) with 99.99% base accuracy.[^shendure2008next]
These fragments were used to assemble larger DNA fragments and, eventually, entire chromosomes.

<iframe width="100%" height="473" src="https://www.youtube.com/embed/dVRB4CaLizc?si=pQdxZk8AKEtR9Jk0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## DNA replication

DNA replication is the process by which a cell makes identical copies of its DNA.
The process involves unwinding the double helix structure of DNA and separating the two strands by breaking the hydrogen bonds between the base pairs.
Each strand is a template for synthesizing a new complementary strand by the enzyme DNA polymerase.

A DNA primer is attached to the template strand by hybridization, and deoxynucleosides triphosphates (dNTPPs) are sequentially added to the primer strand by DNA polymerase.

!!! quote "**Figure 1**"

    <figure markdown>
    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Nucleotides_1.svg/1920px-Nucleotides_1.svg.png){ alight=left width=800 }
    </figure>

!!! quote "**Figure 2**"

    <figure markdown>
    ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/DNA_synthesis_EN.png/1920px-DNA_synthesis_EN.png){ alight=left width=800 }
    </figure>

## Primer

A primer is a short, single-stranded DNA molecule that is a starting point for DNA synthesis.
The primer is complementary to the template DNA (the DNA to be sequenced) and initiates the polymerase chain reaction (PCR).
The PCR reaction amplifies the DNA region of interest before Sanger sequencing.
The amplified DNA is then subjected to Sanger sequencing, which uses the M13 sequence as a universal primer.

The M13-tailed primers are used to simplify the workflow when sequencing PCR products and they reduce the loss of the 5' unresolvable bases.
When the PCR primers contain M13 tails on their 5' ends, the M13 sequence is incorporated into the amplicons.
This enables sequencing master mixes containing the universal M13 forward, or M13 reverse primers.
The sequence for the M13 forward and reverse primers is as follows:

-   M13 forward primer sequence: `5′ TGTAAAACGACGGCCAGT 3′`
-   M13 reverse primer sequence: `5′ CAGGAAACAGCTATGACC 3′`

The primer is designed for the known sequences at the 3' end of the template strand.
M13 sequences are generally attached to the 3' end, and the primer of this M13 is made.

## Terminating replication

The reaction mixture also contains **di**deoxynucleoside triphosphate (ddNTPs) and usual dNTPs.
Suppose ddNTPs are incorporated during replication instead of usual dNTPs in the growing DNA strand.
In that case, the replication stops at that nucleotide.
The ddNTPs are analogs of dNTPs but lack a hydroxyl group (-OH) at c3 of the ribose sugar.

!!! quote "**Figure 3**"

    <figure markdown>
    ![](https://www.onlinebiologynotes.com/wp-content/uploads/2017/07/ddNTPs-1.jpg){ alight=left width=800 }
    </figure>

This lack of hydroxyl group prevents ddNTPs from making a phosphodiester bond with the next nucleotide, thus terminating the nucleotide chain.
Respective ddNTPs of dNTPs terminate the chain at their respective site.
For example, ddATP terminates at the A site, ddCTP at the C site, ddGTP at the G site, and ddTTP at the T site.

The DNA sample is divided into four separate sequencing reactions containing all four standard deoxynucleotides (dATP, dGTP, dCTP, and dTTP) and the DNA polymerase.
Only one of the four dideoxynucleotides (ddATP, ddGTP, ddCTP, or ddTTP) is added to each reaction.
In contrast, the other added nucleotides are ordinary ones.

## PCR

The sequencing begins by dividing the DNA sample into four separate reactions, each containing all four standard deoxynucleotides (dATP, dGTP, dCTP, and dTTP) and the DNA polymerase enzyme.
In these reactions, only one type of dideoxynucleotide (ddATP, ddGTP, ddCTP, or ddTTP) is added to each reaction alongside the regular deoxynucleotides.

As the DNA polymerase extends the DNA chain during each sequencing reaction, termination occurs at different positions depending on which dideoxynucleotide is present.
This results in the production of a series of DNA fragments of varying lengths in each reaction.

The termination at specific bases generates a unique pattern of fragments in each reaction.
These fragments represent the particular nucleotide positions in the original DNA sequence.
Using different dideoxynucleotides in separate reactions allows the researcher to obtain information about the sequence at each position along the DNA template.

!!! quote "**Figure 4**"

    <figure markdown>
    ![](/img/seq/sanger-sequencing_steps_process_diagram.png){ alight=left width=600 }
    </figure>

    Credit: [Millipore Sigma](https://www.sigmaaldrich.com/US/en/technical-documents/protocol/genomics/sequencing/sanger-sequencing)

## Fluorescence

The addition of fluorescent tags to dideoxynucleotides (ddNTPs) facilitates the detection and determination of DNA sequences.
Each ddNTP (ddATP, ddGTP, ddCTP, or ddTTP) is labeled with a distinct fluorescent tag.

!!! quote "**Figure 5**"

    <figure markdown>
    ![](https://upload.wikimedia.org/wikipedia/commons/0/09/%D0%A4%D0%BB%D1%83%D0%BE%D1%80%D0%B5%D1%81%D1%86%D0%B5%D0%BD%D1%82%D0%BD%D1%8B%D0%B5_%D0%B4%D0%B8%D0%B4%D0%B5%D0%B7%D0%BE%D0%BA%D1%81%D0%B8%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80%D1%8B_%D0%A1%D0%B0%D0%BD%D0%B3%D0%B5%D1%80.svg){ alight=left width=600 }
    </figure>

This labeling allows the simultaneous sequencing of DNA fragments from four separate reactions.
After the DNA fragments are generated and separated by size through gel electrophoresis, adding fluorescent tags enables researchers to visualize and distinguish the terminated fragments based on their specific ddNTP.
Automated sequencing machines can detect the color-coded fragments, providing a faster and more accurate means of determining the DNA sequence.
This fluorescence-based approach enhances sensitivity and precision and reduces ambiguity in reading sequences.
The use of fluorescently labeled ddNTPs has become a standard practice in Sanger sequencing, particularly in high-throughput sequencing projects, contributing to the efficiency and automation of the sequencing process.

## Gel electrophoresis detection

TODO:

## Chromatogram

A chromatogram represents the migration of labeled sequencing products via capillary electrophoresis.
Fluorescence is detected at the end of the capillary, and signal intensity from four color channels, each representing a DNA base, is plotted on the y-axis relative to time on the x-axis.

!!! quote "**Figure 6**"

    <figure markdown>
    ![](https://media.labxchange.org/xblocks/lb-LabXchange-22c08d85-html-1/Sanger%20Sequencing%20Figures_Nicole-14.1624866693317-6ba38bd8669aa942be7db5f53a49c621.png){ alight=left width=800 }
    </figure>

    An example of a sequencing chromatogram. Each DNA nucleotide, adenine, cytosine, guanine, and thymine, has its color on the chromatogram for visualization.

Most trace viewers show a processed version of the chromatogram; analysis software manipulates raw data from the sequencer to facilitate base calling.
The start of the processed trace, assigned position 1, is the software's best guess of the first peak.

### Trace start

The first 20 to 40 bases are typically not well resolved. Very short sequencing products do not migrate predictably during capillary electrophoresis, and the analysis software has difficulty assigning bases within this region, causing Ns to appear in the sequence. To avoid critical data falling in this region, we recommend designing primers that bind at least 60 bp, preferably 100 bp, away from critical bases. Note that the sequence of the primer will not be seen in the results, as bases within the primer are not labeled during the extension reaction.

!!! quote "**Figure 7**"

    <figure markdown>
    ![](https://www.azenta.com/sites/default/files/web-media-library/blog/analyzing-sanger-sequencing-data/fig_02_start-trace.png){ alight=left width=800 }
    </figure>

### Trace middle

Most sequencing protocols are optimized to provide the best peak resolution between roughly 100 and 500 bases. Peaks should be sharp and well-spaced in this range, and the base calling is most reliable.

!!! quote "**Figure 8**"

    <figure markdown>
    ![](https://www.azenta.com/sites/default/files/web-media-library/blog/analyzing-sanger-sequencing-data/fig_03_middle-trace.png){ alight=left width=800 }
    </figure>

### Trace end

Toward the end of the trace, expect peaks to be less defined and lower in intensity. The base calling will also be less reliable. Due to the nature of in vitro polymerization, larger sequencing products are generated less efficiently than their shorter counterparts. Thus, the larger products are fewer in number and produce a weaker signal. Also, with any electrophoresis method, it becomes increasingly difficult to resolve a single-base difference as DNA fragments become larger. For example, the difference in molecular weight between 100 bp and 101 bp is 1%, whereas it's just 0.1% between 1,000 bp and 1,001 bp.

!!! quote "**Figure 9**"

    <figure markdown>
    ![](https://www.azenta.com/sites/default/files/web-media-library/blog/analyzing-sanger-sequencing-data/fig_04_end-trace.png){ alight=left width=800 }
    </figure>

### Dye blobs

Broad C and T peaks may be observed around position 80. Known as "dye blobs," these peaks represent aggregates of unincorporated dye terminators. Although most cleanup protocols are effective at removing leftover nucleotides after completion of the sequencing reaction, no method is 100% effective. Dye blobs are more frequently observed in inefficient sequencing reactions, with a higher fraction of unincorporated nucleotides and a low signal-to-noise ratio. Please note that the sequence within this region can often be determined by manual inspection of the chromatogram, even if the analysis software is unable to assign bases (i.e., Ns appear in the sequence). Suppose you need to sequence a key base, such as an SNP.
In that case, we recommend using primers that bind at least 100 bp away from the key base to avoid it falling within the dye blob region.

!!! quote "**Figure 10**"

    <figure markdown>
    ![](https://www.azenta.com/sites/default/files/web-media-library/blog/analyzing-sanger-sequencing-data/fig_07_dye-blobs.png){ alight=left width=800 }
    </figure>

### Assigning bases

Once the sequencer collects the raw data, it's processed and analyzed by base-calling software. The four dyes used in Sanger sequencing have slightly different mobility properties due, in part, to their unequal molecular weights. Therefore, the relative position of the peaks must be slightly adjusted to compensate for these differences (see figure below). After this correction, the algorithm identifies peaks and assigns bases.

!!! quote "**Figure 11**"

    <figure markdown>
    ![](https://www.azenta.com/sites/default/files/web-media-library/blog/analyzing-sanger-sequencing-data/fig_09_raw.png){ alight=left width=800 }
    </figure>

<!-- REFERENCES -->

[^sanger1977dna]: Sanger, F., Nicklen, S., & Coulson, A. R. (1977). DNA sequencing with chain-terminating inhibitors. *Proceedings of the national academy of sciences, 74*(12), 5463-5467. doi: [10.1073/pnas.74.12.5463](https://doi.org/10.1073/pnas.74.12.5463)
[^shendure2008next]: Shendure, J., & Ji, H. (2008). Next-generation DNA sequencing. *Nature biotechnology, 26*(10), 1135-1145. doi: [10.1038/nbt1486](https://doi.org/10.1038/nbt1486)

[^shuhaib2023mastering]: Al-Shuhaib, M. B. S., & Hashim, H. O. (2023). Mastering DNA chromatogram analysis in Sanger sequencing for reliable clinical analysis. *J. Genet. Eng. Biotechnol., 21*(1), 115. doi: [10.1186/s43141-023-00587-6](https://doi.org/10.1186/s43141-023-00587-6)
[^lopez2021sanger]: Arteche-López, A., Ávila-Fernández, A., Romero, R., Riveiro-Álvarez, R., López-Martínez, M. A., Giménez-Pardo, A., ... & Ayuso, C. (2021). Sanger sequencing is no longer always necessary based on a single-center validation of 1109 NGS variants in 825 clinical exomes. *Scientific reports, 11*(1), 5697. doi: [10.1038/s41598-021-85182-w](https://doi.org/10.1038/s41598-021-85182-w)
[^cario2020sanger]: De Cario, R., Kura, A., Suraci, S., Magi, A., Volta, A., Marcucci, R., ... & Sticchi, E. (2020). Sanger validation of high-throughput sequencing in genetic diagnosis: Still the best practice?. *Frontiers in genetics, 11*, 592588. doi: [10.3389/fgene.2020.592588](https://doi.org/10.3389/fgene.2020.592588)
[^giani2020long]: Giani, A. M., Gallo, G. R., Gianfranceschi, L., & Formenti, G. (2020). Long walk to genomics: History and current approaches to genome sequencing and assembly. *Computational and Structural Biotechnology Journal*, 18, 9-19. doi: [10.1016/j.csbj.2019.11.002](https://doi.org/10.1016/j.csbj.2019.11.002)
[^crossley2020guidelines]: Crossley, B. M., Bai, J., Glaser, A., Maes, R., Porter, E., Killian, M. L., ... & Toohey-Kurth, K. (2020). Guidelines for Sanger sequencing and molecular assay monitoring. *Journal of Veterinary Diagnostic Investigation, 32*(6), 767-775. doi: [10.1177/1040638720905833](https://doi.org/110.1177/1040638720905833)
