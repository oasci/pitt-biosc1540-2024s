# CADD Checkpoint

**Due**: April 18 by 11:59 pm

**Points**: 200

We will be using Dihydrofolate reductase (DHFR) from *E. coli* (UniProt [P0ABQ4](https://www.uniprot.org/uniprotkb/P0ABQ4/entry)) as our biological target.
This enzyme is vital in folate metabolism and is already the target of many inhibitors [^raimondi2019dhfr] [^wrobel2020trimethoprim].

[MolModa](https://durrantlab.pitt.edu/molmoda/) is a new docking tool from the Durrant Lab that runs entirely in your web browser.
If you need help, please consult the [documentation](https://durrantlab.pitt.edu/molmoda/docs/) and [docking tutorial](https://durrantlab.pitt.edu/molmoda/docs/docking/tutorials/td001/).

!!! note

    If you find any bugs in MolModa or have feedback, please email Alex so we can improve!

**Questions:**

1.  Briefly explain the biological role of E. coli DHFR in bacterial folate metabolism. How does DHFR activity contribute to bacterial survival?
2.  Why is E. coli DHFR a valuable target for developing new antibiotics? Relate your answer to the concept of selective inhibition.
3.  Are there any existing classes of antibiotics that target DHFR? Please provide an example and briefly describe its mechanism of action.
4.  Over time, bacteria can develop resistance to antibiotics. How might mutations in the DHFR gene contribute to bacterial resistance against DHFR-targeting antibiotics?

**Bonus:**

Research the concept of broad-spectrum vs. narrow-spectrum antibiotics.
Discuss the advantages and disadvantages of targeting a protein essential for bacterial survival in the context of DHFR inhibitors.

## Target structure selection

Go to the protein's UniProt entry and select one of the [X-ray crystallographic structures](https://www.uniprot.org/uniprotkb/P0ABQ4/entry#structure).
Based on [target structure selection guidelines](https://cadd.crumblearn.org/sbdd/targets/structure/) and your understanding of the DHFR function, choose an appropriate structure from the available options.

**Questions:**

1.  Briefly explain your reasoning behind selecting the chosen structure.
    Consider factors like resolution (impact on docking accuracy), presence/absence of a bound ligand (potential insights into the active site), mutations, or missing residues (potential effects on protein function and docking).
2.  How would you describe or evaluate the quality of this structure?
3.  Why would we choose, or not choose, to use an AlphaFold model?

## Chemical library construction

Search on [PubMed](https://pubchem.ncbi.nlm.nih.gov/) for `Dihydrofolate reductase inhibitor` and download all of those compounds (there should be 30 as of 2024-03-17) as a single 3D SDF file.

Go to the [PubMed Classifications](https://pubchem.ncbi.nlm.nih.gov/classification/#hid=72) and choose a category with more than 1000 compounds under `Drug and Medication Information`.
After selecting a category, tailor the compound filters to your liking until the number of compounds is between 70 and 170.
Download these compounds as a single 3D SDF file.

**Questions:**

1.  Why would we include known DHFR inhibitors in our chemical library?
2.  Using the downloaded SDF file containing known DHFR inhibitors, calculate some basic properties of the library (e.g., average molecular weight, number of rotatable bonds).
    Discuss how these properties might influence their potential as drugs.
3.  Search for a scientific article (not listed in PubMed) describing a recent discovery of a DHFR inhibitor.
    Briefly summarize the key features of the inhibitor and discuss how it compares to the ones found in your library.
4.  Explain the concept of "scaffold diversity" in the context of chemical library construction. Why is it important to consider scaffold diversity?
5.  Analyze the downloaded SDF file containing the additional compounds (not DHFR inhibitors).
    Use software tools (like RDKit) or online resources to identify the main scaffolds present in the library.
    Discuss the level of diversity observed and suggest ways you could improve it if needed.

## Target preparation

Load your PDB structure into [MolModa][molmoda] and prepare it for docking.
This could include removing duplicate chains and water molecules, protonating the protein, and co-crystallized ligands, among other things.

**Questions:**

1.  Why might a PDB file contain duplicate protein chains, and how could their presence affect the docking process?
2.  Discuss the role water molecules play in protein structure and function. Explain the rationale behind removing them for docking simulations, considering potential drawbacks.
3.  Protein function depends on the protonation state of its amino acid residues. Explain why it's important to consider protein protonation during target preparation for docking simulations.
4.  Why might a protein structure contain a bound ligand, and how could its presence affect the docking simulations for new inhibitors?

!!! tip

    Save your progress in a `.molmoda` file frequently!
    There is no cloud or backup of your session; if you close your tab, you will lose all your progress.

## Ligand preparation

Load your compounds from PubMed into [MolModa][molmoda] and prepare them for docking.
This could include conformer generation, protonation, etc.

**Questions:**

1.  Explain why preparing the ligand molecules (downloaded from PubChem) is necessary before performing docking simulations.
    What potential issues could arise if you skip this step?
2.  The prompt mentions conformer generation and protonation as potential ligand preparation steps. Briefly describe each technique and its role in preparing ligands for docking. Are there other common ligand preparation steps you might consider, and why?
3.  How might the specific methods used during ligand preparation (e.g., number of conformers generated, protonation state) influence the outcome of your docking simulations?

## Pocket selection

Using [MolModa][molmoda], detect protein pockets in your protein.
Note all the pockets found, and select one to dock your ligands in.

**Questions:**

1.  Explain how you chose your binding pocket and what considerations you made.
2.  After identifying potential pockets in MolModa,  describe the features you would use to characterize a suitable binding pocket for DHFR inhibitor docking.
    Consider size, shape, hydrophobicity, and proximity to known functional residues.
3.  In a real-world drug discovery project, how might experimental data (e.g., known inhibitor binding site) be used to validate the chosen pocket for in silico docking simulations?

**Bonus:**

Research the concept of allosteric sites versus orthosteric sites for drug targeting.
Explain the difference between these sites and discuss why, for DHFR inhibitors, targeting the orthosteric site would be the preferred approach.

## Docking

Perform docking simulations for each molecule in your library using [MolModa][molmoda].
If needed, review and adjust the software's default settings for docking parameters (search space, flexibility, etc.).
Once the docking setup is complete, initiate the docking simulation. The software will calculate the interaction between each ligand molecule in your library and the protein structure.
After the docking run finishes, the software will provide results for each ligand-protein complex.
These results typically include:

-   Binding pose: The predicted 3D orientation of the ligand molecule within the protein binding pocket.
-   Docking score: A numerical estimate of the binding affinity between the ligand and the protein. Lower scores usually indicate stronger predicted binding.

**Questions:**

1.  Explain the key factors you would consider when evaluating the docking results for your ligand library. Go beyond the docking score and discuss other parameters that indicate a favorable ligand-protein interaction.
2.  How would you analyze the predicted binding poses of your top-scoring ligands?
3.  Docking scores are estimates of binding affinity, not experimental measurements. Discuss the limitations of using docking scores for lead selection and the importance of considering other factors.
4.  In the context of your project,  describe potential reasons why a ligand might have a good docking score but not be a successful inhibitor in real-world applications.
5.  Compare the docking scores of known DHFR inhibitors with those obtained for your other library hits. What insights can you draw from this comparison?

## Analysis

<!-- REFERENCES -->

[^raimondi2019dhfr]: Raimondi, M. V., Randazzo, O., La Franca, M., Barone, G., Vignoni, E., Rossi, D., & Collina, S. (2019). DHFR inhibitors: reading the past for discovering novel anticancer agents. *Molecules, 24*(6), 1140.
[^wrobel2020trimethoprim]: Wróbel, A., Arciszewska, K., Maliszewski, D., & Drozdowska, D. (2020). Trimethoprim and other nonclassical antifolates an excellent template for searching modifications of dihydrofolate reductase enzyme inhibitors. *The Journal of Antibiotics, 73*(1), 5-27.
[molmoda]: https://durrantlab.pitt.edu/molmoda/
