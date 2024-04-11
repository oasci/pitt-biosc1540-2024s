# CADD Checkpoint

**Due**: April 18 by 11:59 pm

**Points**: 200

We will be using Dihydrofolate reductase (DHFR) from *E. coli* (UniProt [P0ABQ4](https://www.uniprot.org/uniprotkb/P0ABQ4/entry)) as our biological target.
This enzyme is vital in folate metabolism and is already the target of many inhibitors [^raimondi2019dhfr] [^wrobel2020trimethoprim].

[MolModa](https://durrantlab.pitt.edu/molmoda/) is a new docking tool from the Durrant Lab that runs entirely in your web browser.
If you need help, please consult the [documentation](https://durrantlab.pitt.edu/molmoda/docs/) and [docking tutorial](https://durrantlab.pitt.edu/molmoda/docs/docking/tutorials/td001/).

!!! note

    If you find any bugs in MolModa or have feedback, please email Alex so we can improve it!

## Deliverables

Please submit the following materials:

-   (125 points) A PDF of your responses to the questions along with any other images or information you'd like to submit.
-   (75 points) A finalized `.molmoda` file containing your prepped protein, ligands, pockets, and docking results.

## Background

**Questions**

1.  Briefly explain the biological role of *E. coli* DHFR in bacterial folate metabolism.
    How does DHFR activity contribute to bacterial survival?
    (5 points)
2.  Why is *E. coli* DHFR a valuable target for developing new antibiotics?
    (5 points)
3.  Are there any existing classes of antibiotics that target DHFR?
    Please provide an example and briefly describe its mechanism of action.
    (5 points)
4.  Over time, bacteria can develop resistance to antibiotics.
    How might mutations in the folA gene contribute to bacterial resistance against DHFR-targeting antibiotics?
    (5 points)

**Bonus** (5 points)

Research the concept of broad- vs. narrow-spectrum antibiotics.
Discuss the advantages and disadvantages of targeting a protein essential for bacterial survival in the context of DHFR inhibitors.

## Target structure selection

Go to the protein's UniProt entry and select one of the [X-ray crystallographic structures](https://www.uniprot.org/uniprotkb/P0ABQ4/entry#structure).
Based on target structure selection guidelines and your understanding of the DHFR function, choose an appropriate structure from the available options.

**Questions**

1.  Briefly explain your reasoning behind selecting your structure.
    (5 points)
2.  Why would we not choose to use an AlphaFold model?
    (5 points)

## Chemical library construction

Search on [PubChem](https://pubchem.ncbi.nlm.nih.gov/) for `Dihydrofolate reductase inhibitor` and download all of those compounds as a single 3D SDF file.
Click [here](./PubChem_max_dose_records.sdf){:download="PubChem_max_dose_records.sdf"} to download 35 additional compounds from the `PubChem Compound TOC: Maximum Drug Dose` list.
These two SDF files are your chemical library for docking.

**Questions**

1.  Why would we include known DHFR inhibitors in our chemical library?
    (5 points)
2.  Search for a scientific article describing a recent discovery of a DHFR inhibitor.
    Briefly summarize the key features of the inhibitor and discuss how it compares to the ones found in your library.
    (5 points)
3.  Explain the concept and importance of scaffold diversity in the context of chemical library construction.
    (5 points)

**Bonus** (20 points)

Analyze your SDF files using [RDKit](https://www.rdkit.org/docs/index.html) to identify the main scaffolds present in the library.
Include example figures in your submission.
Discuss the level of diversity observed and suggest ways you could improve it if needed.

## Target preparation

Load your PDB structure into [MolModa][molmoda] and prepare it for docking.
This could include removing duplicate chains and water molecules, protonating the protein, and co-crystallized ligands, among other things.

**Questions**

1.  Why might a crystallographic structure contain duplicate protein chains and how could their presence affect the docking process?
    (5 points)
2.  Explain the rationale behind removing water molecules for docking simulations, considering potential drawbacks or advantages.
    (5 points)
3.  Explain why it is important to consider protein protonation during target preparation for docking simulations.
    (5 points)
4.  Why might a protein structure contain a bound ligand, and how could its presence affect the docking simulations for new inhibitors?
    (5 points)

!!! tip

    Save your progress in a `.molmoda` file frequently!
    There is no cloud or backup of your session; if you close your tab, you will lose all your progress.

## Ligand preparation

Load your compounds from PubMed into [MolModa][molmoda] and prepare them for docking.
This could include conformer generation, protonation, etc.

**Questions**

1.  Briefly describe conformer generation and protonation techniques and its role in preparing ligands for docking.
    Are there other common ligand preparation steps you might consider, and why?
    (5 points)

## Pocket selection

Using [MolModa][molmoda], detect protein pockets in your protein.
Note all the pockets found, and select one to dock your ligands in.

**Questions**

1.  After identifying potential pockets in MolModa, describe the features you would use to characterize a suitable binding pocket for DHFR inhibitor docking.
    (5 points)
2.  In a real-world drug discovery project, how might experimental data (e.g., known inhibitor binding site) be used to validate the chosen pocket for in silico docking simulations?
    (5 points)

**Bonus** (10 points)

Research the concept of allosteric sites versus orthosteric sites for drug targeting.
Explain the difference between these sites and discuss why, for DHFR inhibitors, targeting the orthosteric site would be the preferred approach.

## Docking

Perform docking simulations for each molecule in your library using [MolModa][molmoda].

!!! warning

    Change the exhaustiveness parameter to `4` and only dock around 10 compounds at a time.
    You can change which molecules to dock by hiding the ones you are not docking on the navigation menu on the left.

Once the docking setup is complete, initiate the docking simulation.
The software will calculate the interaction between each ligand molecule in your library and the protein structure.
After the docking run finishes, the software will provide results for each ligand-protein complex.

**Questions**

1.  Explain the key factors you would consider when evaluating the docking results for your ligand library.
    Go beyond the docking score and discuss other parameters that indicate a favorable ligand-protein interaction.
    (10 points)
2.  How would you analyze the predicted binding poses of your top-scoring ligands?
    (5 points)
3.  Discuss the limitations of using docking scores for lead selection and the importance of considering other factors.
    (10 points)
4.  In the context of your project, describe potential reasons why a ligand might have a good docking score but not be a successful inhibitor in real-world applications.
    (10 points)
5.  Compare the docking scores of known DHFR inhibitors with those obtained for your other library hits.
    What insights can you draw from this comparison?
    (10 points)

## Lead optimization

Following the docking simulations, you'll have a list of potential DHFR inhibitors with predicted binding affinities.
However, docking scores are just estimates, and further validation is crucial to identify promising drug candidates.

**Bonus** (15 points)

Considering the limitations of docking scores, discuss several in silico (computational) approaches you could utilize to further analyze your top docking hits.
What information might these approaches provide to refine your selection?
Beyond in silico methods, outline the essential in vitro (experimental) assays you would perform to validate the top docking hits.
Briefly explain how these assays would assess the potential of a ligand as a DHFR inhibitor.

<!-- REFERENCES -->

[^raimondi2019dhfr]: Raimondi, M. V., Randazzo, O., La Franca, M., Barone, G., Vignoni, E., Rossi, D., & Collina, S. (2019). DHFR inhibitors: reading the past for discovering novel anticancer agents. *Molecules, 24*(6), 1140.
[^wrobel2020trimethoprim]: Wróbel, A., Arciszewska, K., Maliszewski, D., & Drozdowska, D. (2020). Trimethoprim and other nonclassical antifolates an excellent template for searching modifications of dihydrofolate reductase enzyme inhibitors. *The Journal of Antibiotics, 73*(1), 5-27.
[molmoda]: https://durrantlab.pitt.edu/molmoda/
