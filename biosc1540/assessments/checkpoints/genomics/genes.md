# Genes

<details><summary>Python list of genes</summary>

```python

gene_names = np.array(
    [
        "fadL", "artJ", "araD", "lysS", "cspE", "rfaP", "bfd", "fumB", "bfr", "folK",
        "fsa", "psuG", "feoC", "baeS", "eptA", "loiP", "hemW", "hisA", "ilvA", "rsmJ",
        "thiB", "thiS", "flhe", "astB", "ppiC", "thiQ", "ada", "fadH", "murQ", "nlpE",
        "fpr", "fepG", "queE", "ubiF", "purD", "ecnA", "hisB", "nikR", "kbl", "fadI",
        "thiM", "mtr", "priA", "gutQ", "cysE", "lolB", "glpB", "cysP", "queD", "entF",
        "ratA", "moeB", "hemA", "panC", "cyaY", "nikD", "kdpE", "tauD", "aroC", "uspG",
        "degS", "ilvD", "yehX", "tusA", "ypdE", "yhbQ", "lldD", "entS", "torD", "panM",
        "pspG", "zntA", "rsmC", "bioF", "menC", "ytfQ", "ugpQ", "rfaH", "nikE", "yajO",
        "ung", "hisF", "gss", "recJ", "basR", "glpD", "ubiH", "hycG", "rseC", "cysT",
        "serC", "rhtC", "ilvC", "entH", "proA", "cmoB", "uhpB", "thiP", "leuD", "kdpC",
        "pmbA", "uvrD", "lldP", "tusD", "pspF", "rsmB", "pldA", "polB", "rlmG", "fepD",
        "livM", "ruvX", "yccX", "poxB", "iclR", "cdh", "pgeF", "hyaE", "preT", "hisH",
        "guaB", "tnaB", "nikC", "metF", "zur", "araA", "cedA", "thiE", "ribD", "zupT",
        "mltB", "ugpB", "argE", "mnmE", "prlC", "nrdB", "purK", "ssuC", "metH", "ybgI",
        "ttdA", "livJ", "epmC", "copA", "glyS", "hisC", "pepP", "glpE", "livH", "norR",
        "glnG", "fhuB", "actP", "entE", "yihX", "pepB", "hprS", "ubiX", "tsaD", "tusE",
        "tsaB", "ispH", "ruvC", "metE", "gltB", "nuoF", "cybC", "adeP", "tnaC", "nfuA",
        "potI", "malM", "pxpC", "cysJ", "uxuR", "pbpC", "ubiI", "metR", "livG", "envC",
        "pxpA", "murB", "purH", "yhhW", "entA", "alr", "kdpD", "lpxH", "bioC", "yegD",
        "gshB", "hypD", "mscM", "fes", "ugpE", "eptB", "glmM", "serB", "deoB", "modB",
        "menH", "bioB", "lldR", "metL", "yidZ", "srlR", "fadE", "mobA", "ltaE", "aroE",
        "fepC", "ugpA", "yiiM", "bglA", "cyaA", "fhuD", "agp", "amiA", "gltL", "yjfP",
        "uhpA", "glpA", "hypE", "yfaE", "tus", "csiR", "ygfZ", "pcnB", "hycF", "deoD",
        "lolD", "pepD", "nadB", "garK", "cstA", "glpK", "cysN", "pstS", "yqjG", "kefB",
        "ispD", "parE", "wecH", "gudD", "yeaY", "nrfF", "glnE", "gorA", "thiC", "rlmB",
        "araB", "fliT", "pyrI", "murD", "arfB", "hybE", "ulaB", "rlmJ", "hemY", "yfhb",
        "panF", "yehY", "ccmF", "pepA", "dppB", "artM", "menF", "ileS", "rluF", "rlmKL",
        "thiF", "ftsX", "lolE", "norW", "acnB", "pabB", "hycE", "exuR", "recQ", "livK",
        "bioH", "yehW", "deoA", "tusC", "ttdB", "dmsA", "cysS", "rihA", "ygjG", "bglX",
        "fklB", "cysI", "ynjE", "malZ", "sstT", "menD", "selB", "uvrB", "tdh", "metC",
        "hisP", "truB", "caiC", "hisG", "hycC", "manA", "moeA", "gltS", "argT", "corA",
        "mdtL", "gcvP", "recD", "yeiG", "bcr", "speB", "flgD", "murF", "trmH", "qseC",
        "hldE", "nei", "hycB", "nfeF", "cusR", "baeR", "eutA", "thrA", "ligA", "ettA",
        "carA", "moaD", "menB", "selD", "cecR", "asmA", "ybfF", "cysH", "aroG", "leuA",
        "iscX", "nhaB", "miaB", "dppD", "mepA", "amiD", "pabA", "cpdB", "ebgR", "glnD",
        "pstA", "modC", "zapC", "rffC", "moaA", "aer", "cca", "gntR", "trmA", "speA",
        "rffA", "gntU", "rffT", "motB", "lysO", "allC", "ycdX", "hofM", "lpxB", "hyaB",
        "acs", "bioA", "glpX", "fruA", "asnB", "phoU", "mutL", "gltJ", "queA", "yojI",
        "pyrE", "flgI", "pncC", "gph", "araJ", "hemH", "uxaA", "nirD", "rfaF", "moaE",
        "exuT", "hycD", "aat", "ilvE", "zapE", "ubiD", "ldtE", "ycbX", "glnB", "cobA",
        "tsx", "sdhA", "thiG", "pckA", "nuoE", "ogt", "glmS", "purF", "phoA", "gltK",
        "sltY", "gcvH", "mddA", "gltI", "speE", "pspA", "frdD", "fumC", "tyrB", "fldA",
        "dxs", "arnF", "ruvB", "lpxK", "dnaN", "sufA", "treA", "yebT", "rnr", "msrQ",
        "creB", "fetA", "hybC", "pepE", "rph", "cnoX", "yajL", "feoB", "slmA", "hydN",
        "rlmI", "flgF", "bacA", "ybbO", "dsbC", "tsaA", "ansP", "ccmH", "ypfH", "aceA",
        "kefF", "srlD", "cheB", "era", "slyB", "malY", "nuoG", "comR", "sseA", "ptrA",
        "murE", "mpaA", "nrdG", "osmY", "pat", "thrB", "mukB", "pstC", "dapE", "znuB",
        "amyA", "nudG", "gpmB", "cyoE", "pdxJ", "recN", "ccmB", "rluD", "mutH", "pgl",
        "fadB", "yciH", "cusB", "ribB", "hisQ", "tag", "pyrF", "fadM", "queG", "hdfR",
        "fhuC", "trmL", "hyaA", "napA", "der", "hcr", "gloC", "nagC", "dapF", "prmC",
        "mglA", "gutM", "nagE", "pheA", "nirC", "glnA", "srmB", "nagZ", "pgm", "rapA",
        "entC", "hxpB", "dtpB", "tusB", "hxpA", "degQ", "hemN", "tyrP", "allD", "yedE",
        "aqpZ", "pnp", "nudB", "ffh", "crl", "ghrA", "galK", "ybiV", "yedA", "dapD",
        "hemC", "ydiB", "uxuA", "malE", "ucpA", "aceB", "malF", "cysC", "yjeH", "pepQ",
        "flgN", "argB", "orn", "yfeX", "xerC", "nuoM", "nudK", "secA", "yraP", "ldcA",
        "gltA", "glsA", "potD", "nadK", "pxpB", "mraY", "napH", "ybiI", "pfkB", "hybB",
        "selA", "dgkA", "argG", "menI", "alx", "wzyE", "lolC", "clpX", "dbpA", "queF",
        "msrP", "shoB", "lapB", "amiC", "hscA", "cydC", "modA", "flgJ", "bioP", "iadA",
        "treR", "ybjI", "maeB", "pspD", "opgB", "rraB", "viaA", "katG", "mak", "trxB",
        "lpcA", "truC", "ldcC", "hemL", "proS", "argP", "nrfD", "mutM", "yobA", "glk",
        "argC", "gcvT", "rutR", "mltC", "qseE", "yejF", "nrdD", "appB", "moaB", "oppB",
        "metA", "gpsA", "malP", "allR", "yebS", "proB", "dadA", "exbD", "fdoH", "rnhB",
        "dauA", "rof", "gpmM", "yeiR", "nuoC", "msrB", "aaeR", "folD", "glpG", "frsA",
        "nuoN", "galT", "yidA", "rhtB", "yciA", "thiD", "epmB", "panD", "btuE", "gppA",
        "mlaA", "trpR", "hybO", "gudP", "yaaA", "gntK", "sapC", "acpT", "queC", "fre",
        "metK", "trmG_rlmN", "gsk", "yfcG", "artQ", "rsxD", "ribF", "eco", "sbcD",
        "ppc", "ybaK", "clcA", "psd", "cysD", "tyrA", "cysQ", "aegA", "mdtJ", "gpmA",
        "fadD", "yhjD", "dnaT", "ubiA", "robA", "rarA", "ispF", "dnaQ", "pyrD", "wzxE",
        "purU", "rstB", "nirB", "pncB", "nfi", "pqiC", "mioC", "nemR", "citF", "hflD",
        "metB", "fabB", "astE", "cheR", "mdaB", "lepA", "pdxA", "murJ", "trpS", "hypB",
        "pgi", "nuoL", "dmsD", "yajQ", "soxS", "celF", "dacB", "fxsA", "gltP", "damX",
        "glgP", "rffM", "igaA", "kdpF", "djlA", "hprR", "dcd", "lysA", "rnd", "ndh",
        "rsgA", "phoP", "glnS", "mzrA", "hemB", "ivy", "narQ", "uvrC", "kduD", "wzzE",
        "nadA", "helD", "arnT", "tcyP", "btuD", "recF", "purR", "yigB", "ybgE", "fbaA",
        "glnL", "glyA", "dnaJ", "holB", "rsuA", "polA", "ahpF", "pheS", "folA", "ndk",
        "tolC", "waaA", "rsxG", "pnuC", "psiF", "dsbA", "entB", "folM", "srlB", "rpoH",
        "lamB", "ortT", "ssb1", "rcdA", "tamA", "galM", "aas", "ftsP", "gsiA", "oppD",
        "accA", "rnc", "nrfC", "tldD", "yieF", "menA", "oxc", "crcB", "citT", "ybiB",
        "hiuH", "adk", "gyrB", "ppa", "fdhE", "rutA", "nudJ", "kefG", "fdx", "truD",
        "flk", "holA", "prmA", "dtd", "garL", "hisJ", "smpB", "endA", "pyrB", "sapB",
        "tapT", "yehT", "rstA", "hofP", "tyrR", "inaA", "grxC", "pyk", "mrcA", "rluC",
        "plsB", "lplT", "qseG", "ybdG", "hslO", "murI", "tsaC", "mppA", "sapF", "ampG",
        "ybhA", "sfsB", "ghrB", "mdtG", "lysR", "sugE", "aaeA", "anmK", "plaP", "mgsA",
        "yedF", "clpA", "ispA", "mnmA", "ygfB", "hycH", "prfA", "asnC", "hybG", "copD",
        "manZ", "alaA", "gntT", "csrD", "aspS", "fadR", "rimI", "cysZ", "cbpM", "ygiW",
        "sthA", "xanP", "deoR", "hypC", "hemP", "fixX", "pgpB", "rlpA", "rpoN", "ydiK",
        "nupG", "ampD", "btuC", "ccmA", "clpB", "msrC", "narP", "yqhH", "kdgK", "metN",
        "nuoJ", "bglJ", "tatD", "malG", "ubiJ", "surE", "coaBC", "aaeB", "ldtD", "zntB",
        "ldtB", "yeaG", "znuC", "tar", "tesB", "tpiA", "rlmD", "hybA", "ppx", "kbp",
        "ispG", "narL", "uspC", "mnmG", "nadD", "ddlA", "recR", "trxC", "thiL", "yccA",
        "mdtH", "glnQ", "cpxA", "cheZ", "msbA", "holD", "oxyR", "sppA", "yejK", "pstB",
        "sucA", "aspC", "sodC", "srkA", "guaC", "potA", "bamD", "cls", "ampE", "pspC",
        "xerD", "psiE", "topA", "secM", "nudE", "iscS", "hisS", "greB", "ynaI", "rssA",
        "ycaR", "pdeH", "sapD", "lepB", "hemD", "rsmE", "nadC", "gsiC", "rnt", "mukE",
        "rutC", "pbgA", "fkpB", "wecA", "caiT", "glgB", "pdxH", "accC", "brnQ", "mog",
        "folE", "btsT", "yccS", "yfbR", "hflX", "coaD", "trmB", "rsmG", "npr", "marR",
        "acrD", "gloA", "purE", "ccmC", "purM", "ulaR", "leuS", "qseB", "yhgN", "stpA",
        "argA", "chbA", "uraA", "iraP", "parC", "mlaB", "cfa", "thpR", "truA", "pgsA",
        "satP", "fabD", "cmoA", "kdsA", "murC", "glgX", "ftsN", "malK", "tolQ", "mug",
        "pspB", "cra", "lapA", "pspE", "exbB", "speD", "dsbE", "folC", "rseB", "rsmH",
        "kduI", "pssA", "modE", "pldB", "frdC", "cysK", "cmk", "mrdB", "appC", "plsY",
        "ftsH", "slyD", "kup", "hexR", "yrfG", "ispE", "exoX", "prfB", "secD", "lgt",
        "htpG", "narX", "sspB", "xylA", "cbpA", "hslU", "ydfG", "elbB", "moaC", "dpiA",
        "lptE", "purA", "gloB", "murG", "rssB", "pntA", "matP", "zapD", "ftsE", "glnK",
        "ychE", "rsxA", "cpdA", "nudC", "tatB", "hslJ", "rbsD", "ppiD", "recX", "ruvA",
        "cydB", "nuoH", "ccmD", "elaB", "pqiA", "adhE", "thyA", "alaS", "mrdA", "yqaB",
        "mntR", "aroD", "pntB", "pabC", "dacA", "dsbB", "tatC", "rsxE", "map", "dacC",
        "oppA", "syd", "oppC", "aroF", "galR", "nrfA", "zwf", "mdh", "ppiB", "fabH",
        "dcrB", "ybjG", "purC", "marA", "recO", "mdtD", "arcB", "mtfA", "mlaD", "trkH",
        "fruB", "yrbL", "emtA", "htpX", "citX", "nagB", "minC", "cytR", "asnS", "tgt",
        "secG", "ftsZ", "arfA", "yceG", "pth", "rsmA", "yggS", "yajC", "grcA", "btsS",
        "thiK", "lon", "cyoB", "mreD", "znuA", "sdhE", "hda", "tdk", "narK", "fkpA",
        "nuoK", "pyrG", "blr", "tolB", "ispC", "sodB", "yhdE", "pqiB", "cheY", "efp",
        "uspD", "sfsA", "glnP", "napC", "hscB", "udk", "accD", "lexA", "ubiC", "fldB",
        "ybfE", "rpiA", "fabR", "sanA", "cydA", "kdsC", "fnr", "pdhR", "wrbA", "eno",
        "uspA", "galU", "tsaE", "ispB", "recA", "lspA", "epmA", "clpP", "rsmD", "pitA",
        "yqiA", "dnaC", "hycA", "yfgM", "mlaC", "suhB", "bhsA", "cdd", "epd", "ftsA",
        "folX", "ftsB", "can", "nuoB", "lpxD", "tyrS", "napB", "aroB", "pcm", "bamB",
        "frdA", "upp", "rcsF", "lipB", "hflC", "murA", "yhcN", "yeiP", "yidC", "mglB",
        "napG", "ptsN", "cheW", "fur", "hflK", "mltD", "cdsA", "gpt", "cbdX", "surA",
        "mlaF", "dnaA", "kdsD", "iscA", "diaA", "ppnP", "hinT", "mepM", "ivbL", "sulA",
        "yceF", "rho", "sdhD", "ubiB", "cpoB", "sdhB", "fabI", "yfcD", "rpoB", "purN",
        "dnaG", "rseA", "kdgA", "argR", "mdtI", "lipA", "metJ", "mdoG", "manY", "rplA",
        "rpoC", "manX", "atpA", "lptA", "proQ", "folB", "mgrB", "holE", "sxy", "luxS",
        "rapZ", "ilvL", "asd", "accB", "ilvM", "glyQ", "mtnN", "ecnB", "pal", "holC",
        "trmD", "grxD", "nusB", "minE", "atpH", "acrA", "dinI", "corC", "hspQ", "xseB",
        "ybeY", "fdoI", "lpxC", "rraA", "uspF", "artP", "nsrR", "pgk", "erpA", "rplY",
        "bamC", "pfkA", "ydgT", "btuF", "tesA", "pmrR", "rpoD", "minD", "alaE", "coaE",
        "nusG", "fieF", "pflB", "iscU", "priB", "nudF", "ftnA", "mepS", "yacG", "skp",
        "lolA", "cvpA", "dnaK", "fruK", "lpxA", "mlaE", "yfcE", "hupB", "nrdR", "ribA",
        "yjfN", "ubiE", "miaA", "rpsE", "yebG", "pheL", "rimM", "dam", "ibpA", "uof",
        "atpB", "dcuA", "mreB", "secB", "iscR", "grxB", "hslV", "greA", "gmk", "ptsG",
        "glgA", "frdB", "hpt", "yaiA", "lpxL", "atpD", "mgtS", "ftsQ", "tpx", "maoP",
        "sspA", "crp", "lptB", "rbfA", "osmE", "hfq", "fabZ", "dps", "ynhF", "rhoL",
        "seqA", "dksA", "aspA", "cutA", "ybgC", "uspB", "rplX", "rsfS", "feoA", "nuoI",
        "pyrH", "tsf", "plsX", "gapA", "dut", "mntS", "napD", "nuoA", "rplT", "atpF",
        "rpsL", "sdhC", "ompX", "cpxP", "dsrB", "mgtL", "secY", "cydX", "rplK", "lptC",
        "ptsI", "cspD", "ackA", "rpsF", "secE", "pheM", "bssR", "fusA", "rplO", "rimP",
        "rplI", "zapA", "ispU", "acrZ", "prs", "rpsK", "ypdK", "fis", "trxA", "frr",
        "yceD", "tolR", "yncL", "rnk", "hns", "rpoZ", "cspA", "rpsT", "rpmA", "ahpC",
        "rpsA", "aroK", "rplC", "tatA", "bssS", "yqgB", "rpsB", "apaG", "ydfZ", "rlmE",
        "zapB", "atpI", "rppH", "yodD", "rplF", "rpoE", "hupA", "rpsJ", "ibaG", "rpmB",
        "rplS", "infC", "rnpA", "rplL", "yoeI", "rpsS", "bcp", "rplN", "ihfB", "rplQ",
        "atpG", "tatE", "rplP", "rplD", "rpmG", "nlpI", "hpf", "rpsI", "ygdR", "rmf",
        "rpmI", "atpC", "rplJ", "rplU", "rplR", "rseD", "rpsD", "rpsP", "rpsN", "bolA",
        "rpmC", "pyrL", "rpoA", "rplB", "lpp", "rpsH", "rplE", "ptsH", "rpsG", "rplW",
        "rpmE", "rpsO", "rplV", "chbB", "csrA", "atpE", "yhbY", "rpsC", "rplM", "rpmD",
        "rpsU", "infA", "acpP", "ihfA", "ypfM", "rpmH", "rpmF", "rpsR", "rpsQ", "rpmJ",
        "yrbN"
    ]
)
```
</details>

## fadL

## artJ

## araD

## lysS

## cspE

## rfaP

## bfd

## fumB

## bfr

## folK

## fsa

## psuG

## feoC

## baeS

## eptA

## loiP

## hemW

## hisA

## ilvA

## rsmJ

## thiB

## thiS

## flhe

## astB

## ppiC

## thiQ

## ada

## fadH

## murQ

## nlpE

## fpr

## fepG

## queE

## ubiF

## purD

## ecnA

## hisB

## nikR

## kbl

## fadI

## thiM

## mtr

## priA

## gutQ

## cysE

## lolB

## glpB

## cysP

## queD

## entF

## ratA

## moeB

## hemA

## panC

## cyaY

## nikD

## kdpE

## tauD

## aroC

## uspG

## degS

## ilvD

## yehX

## tusA

## ypdE

## yhbQ

## lldD

## entS

## torD

## panM

## pspG

## zntA

## rsmC

## bioF

## menC

## ytfQ

## ugpQ

## rfaH

## nikE

## yajO

## ung

## hisF

## gss

## recJ

## basR

## glpD

## ubiH

## hycG

## rseC

## cysT

## serC

## rhtC

## ilvC

## entH

## proA

## cmoB

## uhpB

## thiP

## leuD

## kdpC

## pmbA

## uvrD

## lldP

## tusD

## pspF

## rsmB

## pldA

## polB

## rlmG

## fepD

## livM

## ruvX

## yccX

## poxB

## iclR

## cdh

## pgeF

## hyaE

## preT

## hisH

## guaB

## tnaB

## nikC

## metF

## zur

## araA

## cedA

## thiE

## ribD

## zupT

## mltB

## ugpB

## argE

## mnmE

## prlC

## nrdB

## purK

## ssuC

## metH

## ybgI

## ttdA

## livJ

## epmC

## copA

## glyS

## hisC

## pepP

## glpE

## livH

## norR

## glnG

## fhuB

## actP

## entE

## yihX

## pepB

## hprS

## ubiX

## tsaD

## tusE

## tsaB

## ispH

## ruvC

## metE

## gltB

## nuoF

## cybC

## adeP

## tnaC

## nfuA

## potI

## malM

## pxpC

## cysJ

## uxuR

## pbpC

## ubiI

## metR

## livG

## envC

## pxpA

## murB

## purH

## yhhW

## entA

## alr

## kdpD

## lpxH

## bioC

## yegD

## gshB

## hypD

## mscM

## fes

## ugpE

## eptB

## glmM

## serB

## deoB

## modB

## menH

## bioB

## lldR

## metL

## yidZ

## srlR

## fadE

## mobA

## ltaE

## aroE

## fepC

## ugpA

## yiiM

## bglA

## cyaA

## fhuD

## agp

## amiA

## gltL

## yjfP

## uhpA

## glpA

## hypE

## yfaE

## tus

## csiR

## ygfZ

## pcnB

## hycF

## deoD

## lolD

## pepD

## nadB

## garK

## cstA

## glpK

## cysN

## pstS

## yqjG

## kefB

## ispD

## parE

## wecH

## gudD

## yeaY

## nrfF

## glnE

## gorA

## thiC

## rlmB

## araB

## fliT

## pyrI

## murD

## arfB

## hybE

## ulaB

## rlmJ

## hemY

## yfhb

## panF

## yehY

## ccmF

## pepA

## dppB

## artM

## menF

## ileS

## rluF

## rlmKL

## thiF

## ftsX

## lolE

## norW

## acnB

## pabB

## hycE

## exuR

## recQ

## livK

## bioH

## yehW

## deoA

## tusC

## ttdB

## dmsA

## cysS

## rihA

## ygjG

## bglX

## fklB

## cysI

## ynjE

## malZ

## sstT

## menD

## selB

## uvrB

## tdh

## metC

## hisP

## truB

## caiC

## hisG

## hycC

## manA

## moeA

## gltS

## argT

## corA

## mdtL

## gcvP

## recD

## yeiG

## bcr

## speB

## flgD

## murF

## trmH

## qseC

## hldE

## nei

## hycB

## nfeF

## cusR

## baeR

## eutA

## thrA

## ligA

## ettA

## carA

## moaD

## menB

## selD

## cecR

## asmA

## ybfF

## cysH

## aroG

## leuA

## iscX

## nhaB

## miaB

## dppD

## mepA

## amiD

## pabA

## cpdB

## ebgR

## glnD

## pstA

## modC

## zapC

## rffC

## moaA

## aer

## cca

## gntR

## trmA

## speA

## rffA

## gntU

## rffT

## motB

## lysO

## allC

## ycdX

## hofM

## lpxB

## hyaB

## acs

## bioA

## glpX

## fruA

## asnB

## phoU

## mutL

## gltJ

## queA

## yojI

## pyrE

## flgI

## pncC

## gph

## araJ

## hemH

## uxaA

## nirD

## rfaF

## moaE

## exuT

## hycD

## aat

## ilvE

## zapE

## ubiD

## ldtE

## ycbX

## glnB

## cobA

## tsx

## sdhA

## thiG

## pckA

## nuoE

## ogt

## glmS

## purF

## phoA

## gltK

## sltY

## gcvH

## mddA

## gltI

## speE

## pspA

## frdD

## fumC

## tyrB

## fldA

## dxs

## arnF

## ruvB

## lpxK

## dnaN

## sufA

## treA

## yebT

## rnr

## msrQ

## creB

## fetA

## hybC

## pepE

## rph

## cnoX

## yajL

## feoB

## slmA

## hydN

## rlmI

## flgF

## bacA

## ybbO

## dsbC

## tsaA

## ansP

## ccmH

## ypfH

## aceA

## kefF

## srlD

## cheB

## era

## slyB

## malY

## nuoG

## comR

## sseA

## ptrA

## murE

## mpaA

## nrdG

## osmY

## pat

## thrB

## mukB

## pstC

## dapE

## znuB

## amyA

## nudG

## gpmB

## cyoE

## pdxJ

## recN

## ccmB

## rluD

## mutH

## pgl

## fadB

## yciH

## cusB

## ribB

## hisQ

## tag

## pyrF

## fadM

## queG

## hdfR

## fhuC

## trmL

## hyaA

## napA

## der

## hcr

## gloC

## nagC

## dapF

## prmC

## mglA

## gutM

## nagE

## pheA

## nirC

## glnA

## srmB

## nagZ

## pgm

## rapA

## entC

## hxpB

## dtpB

## tusB

## hxpA

## degQ

## hemN

## tyrP

## allD

## yedE

## aqpZ

## pnp

## nudB

## ffh

## crl

## ghrA

## galK

## ybiV

## yedA

## dapD

## hemC

## ydiB

## uxuA

## malE

## ucpA

## aceB

## malF

## cysC

## yjeH

## pepQ

## flgN

## argB

## orn

## yfeX

## xerC

## nuoM

## nudK

## secA

## yraP

## ldcA

## gltA

## glsA

## potD

## nadK

## pxpB

## mraY

## napH

## ybiI

## pfkB

## hybB

## selA

## dgkA

## argG

## menI

## alx

## wzyE

## lolC

## clpX

## dbpA

## queF

## msrP

## shoB

## lapB

## amiC

## hscA

## cydC

## modA

## flgJ

## bioP

## iadA

## treR

## ybjI

## maeB

## pspD

## opgB

## rraB

## viaA

## katG

## mak

## trxB

## lpcA

## truC

## ldcC

## hemL

## proS

## argP

## nrfD

## mutM

## yobA

## glk

## argC

## gcvT

## rutR

## mltC

## qseE

## yejF

## nrdD

## appB

## moaB

## oppB

## metA

## gpsA

## malP

## allR

## yebS

## proB

## dadA

## exbD

## fdoH

## rnhB

## dauA

## rof

## gpmM

## yeiR

## nuoC

## msrB

## aaeR

## folD

## glpG

## frsA

## nuoN

## galT

## yidA

## rhtB

## yciA

## thiD

## epmB

## panD

## btuE

## gppA

## mlaA

## trpR

## hybO

## gudP

## yaaA

## gntK

## sapC

## acpT

## queC

## fre

## metK

## trmG_rlmN

## gsk

## yfcG

## artQ

## rsxD

## ribF

## eco

## sbcD

## ppc

## ybaK

## clcA

## psd

## cysD

## tyrA

## cysQ

## aegA

## mdtJ

## gpmA

## fadD

## yhjD

## dnaT

## ubiA

## robA

## rarA

## ispF

## dnaQ

## pyrD

## wzxE

## purU

## rstB

## nirB

## pncB

## nfi

## pqiC

## mioC

## nemR

## citF

## hflD

## metB

## fabB

## astE

## cheR

## mdaB

## lepA

## pdxA

## murJ

## trpS

## hypB

## pgi

## nuoL

## dmsD

## yajQ

## soxS

## celF

## dacB

## fxsA

## gltP

## damX

## glgP

## rffM

## igaA

## kdpF

## djlA

## hprR

## dcd

## lysA

## rnd

## ndh

## rsgA

## phoP

## glnS

## mzrA

## hemB

## ivy

## narQ

## uvrC

## kduD

## wzzE

## nadA

## helD

## arnT

## tcyP

## btuD

## recF

## purR

## yigB

## ybgE

## fbaA

## glnL

## glyA

## dnaJ

## holB

## rsuA

## polA

## ahpF

## pheS

## folA

## ndk

## tolC

## waaA

## rsxG

## pnuC

## psiF

## dsbA

## entB

## folM

## srlB

## rpoH

## lamB

## ortT

## ssb1

## rcdA

## tamA

## galM

## aas

## ftsP

## gsiA

## oppD

## accA

## rnc

## nrfC

## tldD

## yieF

## menA

## oxc

## crcB

## citT

## ybiB

## hiuH

## adk

## gyrB

## ppa

## fdhE

## rutA

## nudJ

## kefG

## fdx

## truD

## flk

## holA

## prmA

## dtd

## garL

## hisJ

## smpB

## endA

## pyrB

## sapB

## tapT

## yehT

## rstA

## hofP

## tyrR

## inaA

## grxC

## pyk

## mrcA

## rluC

## plsB

## lplT

## qseG

## ybdG

## hslO

## murI

## tsaC

## mppA

## sapF

## ampG

## ybhA

## sfsB

## ghrB

## mdtG

## lysR

## sugE

## aaeA

## anmK

## plaP

## mgsA

## yedF

## clpA

## ispA

## mnmA

## ygfB

## hycH

## prfA

## asnC

## hybG

## copD

## manZ

## alaA

## gntT

## csrD

## aspS

## fadR

## rimI

## cysZ

## cbpM

## ygiW

## sthA

## xanP

## deoR

## hypC

## hemP

## fixX

## pgpB

## rlpA

## rpoN

## ydiK

## nupG

## ampD

## btuC

## ccmA

## clpB

## msrC

## narP

## yqhH

## kdgK

## metN

## nuoJ

## bglJ

## tatD

## malG

## ubiJ

## surE

## coaBC

## aaeB

## ldtD

## zntB

## ldtB

## yeaG

## znuC

## tar

## tesB

## tpiA

## rlmD

## hybA

## ppx

## kbp

## ispG

## narL

## uspC

## mnmG

## nadD

## ddlA

## recR

## trxC

## thiL

## yccA

## mdtH

## glnQ

## cpxA

## cheZ

## msbA

## holD

## oxyR

## sppA

## yejK

## pstB

## sucA

## aspC

## sodC

## srkA

## guaC

## potA

## bamD

## cls

## ampE

## pspC

## xerD

## psiE

## topA

## secM

## nudE

## iscS

## hisS

## greB

## ynaI

## rssA

## ycaR

## pdeH

## sapD

## lepB

## hemD

## rsmE

## nadC

## gsiC

## rnt

## mukE

## rutC

## pbgA

## fkpB

## wecA

## caiT

## glgB

## pdxH

## accC

## brnQ

## mog

## folE

## btsT

## yccS

## yfbR

## hflX

## coaD

## trmB

## rsmG

## npr

## marR

## acrD

## gloA

## purE

## ccmC

## purM

## ulaR

## leuS

## qseB

## yhgN

## stpA

## argA

## chbA

## uraA

## iraP

## parC

## mlaB

## cfa

## thpR

## truA

## pgsA

## satP

## fabD

## cmoA

## kdsA

## murC

## glgX

## ftsN

## malK

## tolQ

## mug

## pspB

## cra

## lapA

## pspE

## exbB

## speD

## dsbE

## folC

## rseB

## rsmH

## kduI

## pssA

## modE

## pldB

## frdC

## cysK

## cmk

## mrdB

## appC

## plsY

## ftsH

## slyD

## kup

## hexR

## yrfG

## ispE

## exoX

## prfB

## secD

## lgt

## htpG

## narX

## sspB

## xylA

## cbpA

## hslU

## ydfG

## elbB

## moaC

## dpiA

## lptE

## purA

## gloB

## murG

## rssB

## pntA

## matP

## zapD

## ftsE

## glnK

## ychE

## rsxA

## cpdA

## nudC

## tatB

## hslJ

## rbsD

## ppiD

## recX

## ruvA

## cydB

## nuoH

## ccmD

## elaB

## pqiA

## adhE

## thyA

## alaS

## mrdA

## yqaB

## mntR

## aroD

## pntB

## pabC

## dacA

## dsbB

## tatC

## rsxE

## map

## dacC

## oppA

## syd

## oppC

## aroF

## galR

## nrfA

## zwf

## mdh

## ppiB

## fabH

## dcrB

## ybjG

## purC

## marA

## recO

## mdtD

## arcB

## mtfA

## mlaD

## trkH

## fruB

## yrbL

## emtA

## htpX

## citX

## nagB

## minC

## cytR

## asnS

## tgt

## secG

## ftsZ

## arfA

## yceG

## pth

## rsmA

## yggS

## yajC

## grcA

## btsS

## thiK

## lon

## cyoB

## mreD

## znuA

## sdhE

## hda

## tdk

## narK

## fkpA

## nuoK

## pyrG

## blr

## tolB

## ispC

## sodB

## yhdE

## pqiB

## cheY

## efp

## uspD

## sfsA

## glnP

## napC

## hscB

## udk

## accD

## lexA

## ubiC

## fldB

## ybfE

## rpiA

## fabR

## sanA

## cydA

## kdsC

## fnr

## pdhR

## wrbA

## eno

## uspA

## galU

## tsaE

## ispB

## recA

## lspA

## epmA

## clpP

## rsmD

## pitA

## yqiA

## dnaC

## hycA

## yfgM

## mlaC

## suhB

## bhsA

## cdd

## epd

## ftsA

## folX

## ftsB

## can

## nuoB

## lpxD

## tyrS

## napB

## aroB

## pcm

## bamB

## frdA

## upp

## rcsF

## lipB

## hflC

## murA

## yhcN

## yeiP

## yidC

## mglB

## napG

## ptsN

## cheW

## fur

## hflK

## mltD

## cdsA

## gpt

## cbdX

## surA

## mlaF

## dnaA

## kdsD

## iscA

## diaA

## ppnP

## hinT

## mepM

## ivbL

## sulA

## yceF

## rho

## sdhD

## ubiB

## cpoB

## sdhB

## fabI

## yfcD

## rpoB

## purN

## dnaG

## rseA

## kdgA

## argR

## mdtI

## lipA

## metJ

## mdoG

## manY

## rplA

## rpoC

## manX

## atpA

## lptA

## proQ

## folB

## mgrB

## holE

## sxy

## luxS

## rapZ

## ilvL

## asd

## accB

## ilvM

## glyQ

## mtnN

## ecnB

## pal

## holC

## trmD

## grxD

## nusB

## minE

## atpH

## acrA

## dinI

## corC

## hspQ

## xseB

## ybeY

## fdoI

## lpxC

## rraA

## uspF

## artP

## nsrR

## pgk

## erpA

## rplY

## bamC

## pfkA

## ydgT

## btuF

## tesA

## pmrR

## rpoD

## minD

## alaE

## coaE

## nusG

## fieF

## pflB

## iscU

## priB

## nudF

## ftnA

## mepS

## yacG

## skp

## lolA

## cvpA

## dnaK

## fruK

## lpxA

## mlaE

## yfcE

## hupB

## nrdR

## ribA

## yjfN

## ubiE

## miaA

## rpsE

## yebG

## pheL

## rimM

## dam

## ibpA

## uof

## atpB

## dcuA

## mreB

## secB

## iscR

## grxB

## hslV

## greA

## gmk

## ptsG

## glgA

## frdB

## hpt

## yaiA

## lpxL

## atpD

## mgtS

## ftsQ

## tpx

## maoP

## sspA

## crp

## lptB

## rbfA

## osmE

## hfq

## fabZ

## dps

## ynhF

## rhoL

## seqA

## dksA

## aspA

## cutA

## ybgC

## uspB

## rplX

## rsfS

## feoA

## nuoI

## pyrH

## tsf

## plsX

## gapA

## dut

## mntS

## napD

## nuoA

## rplT

## atpF

## rpsL

## sdhC

## ompX

## cpxP

## dsrB

## mgtL

## secY

## cydX

## rplK

## lptC

## ptsI

## cspD

## ackA

## rpsF

## secE

## pheM

## bssR

## fusA

## rplO

## rimP

## rplI

## zapA

## ispU

## acrZ

## prs

## rpsK

## ypdK

## fis

## trxA

## frr

## yceD

## tolR

## yncL

## rnk

## hns

## rpoZ

## cspA

## rpsT

## rpmA

## ahpC

## rpsA

## aroK

## rplC

## tatA

## bssS

## yqgB

## rpsB

## apaG

## ydfZ

## rlmE

## zapB

## atpI

## rppH

## yodD

## rplF

## rpoE

## hupA

## rpsJ

## ibaG

## rpmB

## rplS

## infC

## rnpA

## rplL

## yoeI

## rpsS

## bcp

## rplN

## ihfB

## rplQ

## atpG

## tatE

## rplP

## rplD

## rpmG

## nlpI

## hpf

## rpsI

## ygdR

## rmf

## rpmI

## atpC

## rplJ

## rplU

## rplR

## rseD

## rpsD

## rpsP

## rpsN

## bolA

## rpmC

## pyrL

## rpoA

## rplB

## lpp

## rpsH

## rplE

## ptsH

## rpsG

## rplW

## rpmE

## rpsO

## rplV

## chbB

## csrA

## atpE

## yhbY

## rpsC

## rplM

## rpmD

## rpsU

## infA

## acpP

## ihfA

## ypfM

## rpmH

## rpmF

## rpsR

## rpsQ

## rpmJ

## yrbN
