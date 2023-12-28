# Protein targets

We will select a single bacterial protein drug target for students to prepare their [checkpoints](/syllabus/assessments#checkpoints) and [portfolio](/syllabus/assessments#portfolio) on.
Targets were manually curated to minimize technical challenges as the portfolio was built with the following procedure.

1.  Go to the [Therapeutic Target Database][ttd] and perform a `Drug Binding Sites of Target` search with the `1A00-1C4Z: Bacterial infection` disease class.
    This ensures that we will have experimental protein-ligand structures to compare our docking results.
    At the time of search (database lasted updated July 31st, 2023) this was around 35 targets.
2.  Remove non-bacterial proteins resulting in 15 targets.
3.  Remove targets with fewer than three drug binding sites leaving 8 options.
4.  Keep only targets of type `Clinical trial Target` or `Successful Target` leaving 7 options: [T02228][T02228], [T02702][T02702], [T24634][T24634], [T38179][T38179], [T58093][T58093], [T79068][T79068], [T88240][T88240].
5.  Inspect their [UniProt][uniprot] IDs and keep only those with a 5/5 annotation score which eliminates [T38179][T38179] and [T58093][T58093].
6.  Eliminate targets that do not have crystallographic structures of the full amino acid sequence and a resolution less than 2.0 Å.
    This eliminates [T02228][T02228].
7.  Exclude proteins where the `Subcellular Location` is not `cytosol` which disqualifies [T79068][T79068].
    We have [T02702][T02702], [T24634][T24634], and [T88240][T88240] remaining.

Now that we have sufficiently narrowed down our options with reasonable criteria we need to inspect each one.

| Target ID | Species | UniProt ID | Pfram ID | Gene ID | BindingDB Hits | AA length |
| --------- | ------- | ---------- | -------- | ------- | -------------- | --------- |
| [**T02702**][T02702] | [*Escherichia coli*][T02702-taxon] | [P0ABQ4][T02702-uniprot] | [PF00186][T02702-pfam] | [944790][T02702-gene] | [203][T02702-binding] | 159 |
| [**T24634**][T24634] | [*Escherichia coli*][T24634-taxon] | [P0A749][T24634-uniprot] | [PF00275][T24634-pfam] | [947703][T02702-gene] | [123][T02702-binding] | 419 |
| [**T88240**][T88240] | [*Escherichia coli*][T88240-taxon] | [P0AC13][T88240-uniprot] | [PF00809][T88240-pfam] | [947691][T02702-gene] | [12][T02702-binding] | 282 |

Given the information in the table above, I am selecting [T02702][T02702] as our class target because it is small and has rich data sets available.
We will be using PDB:[4NX7][T02702-pdb] for all structure-based projects which is shown below.

<div id="T02702-view" class="mol-container"></div>
<script>
var uri = 'https://files.rcsb.org/view/4NX7.pdb';
jQuery.ajax( uri, {
    success: function(data) {
        // https://3dmol.org/doc/GLViewer.html
        let viewer = $3Dmol.createViewer(
            document.querySelector('#T02702-view'),
            { backgroundAlpha: '0.0' }
        );
        viewer.addModel(data, "pdb");
        viewer.setStyle({}, {cartoon: {color: 'spectrum'}});
        viewer.setStyle({chain: 'A', resn: 'NAP'}, {stick: {}, cartoon: {color: "spectrum"}});
        viewer.setStyle({chain: 'A', resn: 'FOL'}, {stick: {}, cartoon: {color: "spectrum"}});
        //viewer.zoomTo({chain: 'A'})
        viewer.setView([ -27.445891782407415, -43.435508680555664, -13.037306134259268, 5.65664475061444, -0.22058041847687523, -0.7738522089149095, -0.2985868860486118, 0.5131694741719096 ]);
        viewer.setClickable({}, true, function(atom,viewer,event,container) {
            console.log(viewer.getView());
        });
        viewer.render();
    },
    error: function(hdr, status, err) {
        console.error( "Failed to load " + uri + ": " + err );
    },
});
</script>

This structure contains the folic acid (shown below)

<div id="T02702-view-fol" class="mol-container"></div>
<script>
var uri = 'https://files.rcsb.org/view/4NX7.pdb';
jQuery.ajax( uri, {
    success: function(data) {
        // https://3dmol.org/doc/GLViewer.html
        let viewer = $3Dmol.createViewer(
            document.querySelector('#T02702-view-fol'),
            { backgroundAlpha: '0.0' }
        );
        viewer.addModel(data, "pdb");
        viewer.setStyle({}, {cartoon: {color: 'spectrum', opacity: 0.7}});
        viewer.setStyle({chain: 'A', resn: 'FOL'}, {stick: {}, cartoon: {color: "spectrum"}});
        //viewer.zoomTo({chain: 'A', resn: 'FOL'})
        viewer.setView([ -32.547607993175994, -41.25645756970604, -9.412751450973127, 89.11940629090779, -0.037906881925660725, 0.6863373194627387, 0.007354544019402897, -0.7262575733840186 ]);
        viewer.setClickable({}, true, function(atom,viewer,event,container) {
            console.log(viewer.getView());
        });
        viewer.render();
    },
    error: function(hdr, status, err) {
        console.error( "Failed to load " + uri + ": " + err );
    },
});
</script>

and NADP<sup>+</sup> (shown below).

<div id="T02702-view-nadp" class="mol-container"></div>
<script>
var uri = 'https://files.rcsb.org/view/4NX7.pdb';
jQuery.ajax( uri, {
    success: function(data) {
        // https://3dmol.org/doc/GLViewer.html
        let viewer = $3Dmol.createViewer(
            document.querySelector('#T02702-view-nadp'),
            { backgroundAlpha: '0.0' }
        );
        viewer.addModel(data, "pdb");
        viewer.setStyle({}, {cartoon: {color: 'spectrum', opacity: 0.7}});
        viewer.setStyle({chain: 'A', resn: 'NAP'}, {stick: {}, cartoon: {color: "spectrum"}});
        // viewer.zoomTo({chain: 'A', resn: 'NAP'})
        viewer.setView([ -30.45120773583884, -50.287406944067804, -14.264100091682097, 55.483758672781306, 0.5686868275193964, -0.7931960296207532, 0.17607850085579368, 0.12818624082238306 ]);
        viewer.setClickable({}, true, function(atom,viewer,event,container) {
            console.log(viewer.getView());
        });
        viewer.render();
    },
    error: function(hdr, status, err) {
        console.error( "Failed to load " + uri + ": " + err );
    },
});
</script>

<!-- LINKS -->

[ttd]: https://db.idrblab.net/ttd/
[ttd-search]: https://db.idrblab.net/ttd/search/ttd/target-binding-site-by-d-list?name=1A00-1C4Z%3A%20Bacterial%20infection
[uniprot]: https://www.uniprot.org/

[T02228]: https://db.idrblab.net/ttd/data/target-binding-site/details/t02228
[T38179]: https://db.idrblab.net/ttd/data/target-binding-site/details/t38179
[T58093]: https://db.idrblab.net/ttd/data/target-binding-site/details/t58093
[T79068]: https://db.idrblab.net/ttd/data/target-binding-site/details/t79068

[T02702]: https://db.idrblab.net/ttd/data/target-binding-site/details/t02702
[T02702-uniprot]: https://www.uniprot.org/uniprotkb/P0ABQ4
[T02702-taxon]: https://www.uniprot.org/taxonomy/83333
[T02702-pfam]: https://www.ebi.ac.uk/interpro/entry/pfam/PF00186/
[T02702-gene]: https://www.ncbi.nlm.nih.gov/gene/944790
[T02702-binding]: https://www.bindingdb.org/rwd/jsp/dbsearch/PrimarySearch_ki.jsp?polymerid=1876&complexid=50000388&tag=blast&blastSeq=UNIPROT:P0ABQ4&accession_number=P0ABQ4&submit=Search
[T02702-pdb]: https://www.rcsb.org/structure/4NX7

[T24634]: https://db.idrblab.net/ttd/data/target-binding-site/details/t24634
[T24634-uniprot]: https://www.uniprot.org/uniprotkb/P0A749
[T24634-taxon]: https://www.uniprot.org/taxonomy/83333
[T24634-pfam]: https://www.ebi.ac.uk/interpro/entry/pfam/PF00275/
[T24634-gene]: https://www.ncbi.nlm.nih.gov/gene/947703
[T24634-binding]: https://www.bindingdb.org/rwd/jsp/dbsearch/PrimarySearch_ki.jsp?polymerid=6059&tag=pol&target=UNIPROT:P0A749&accession_number=P0A749&submit=Search

[T88240]: https://db.idrblab.net/ttd/data/target-binding-site/details/t88240
[T88240-uniprot]: https://www.uniprot.org/uniprotkb/P0AC13
[T88240-taxon]: https://www.uniprot.org/taxonomy/83333
[T88240-pfam]: https://www.ebi.ac.uk/interpro/entry/pfam/PF00809/
[T88240-gene]: https://www.ncbi.nlm.nih.gov/gene/947691
[T88240-binding]: https://www.bindingdb.org/rwd/jsp/dbsearch/PrimarySearch_ki.jsp?polymerid=50001939&tag=pol&target=UNIPROT:P0AC13&accession_number=P0AC13&submit=Search
