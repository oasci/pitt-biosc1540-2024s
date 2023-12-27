# Scripts

## `prefetch`

### Usage

`prefetch [options] <SRA accession> [...]`

:   Download SRA files and their dependencies

`prefetch [options] --cart <kart file>`

:   Download cart file

`prefetch [options] <URL> --output-file <FILE>`

:   Download `URL` to `FILE`

`prefetch [options] <URL> [...] --output-directory <DIRECTORY>`

:   Download `URL` or `URL`s to `DIRECTORY`

`prefetch [options] <SRA file> [...]`

:   Check `SRA file` for missed dependencies and download them

### Options

`-T|--type <value>`: Specify file type to download. Default: sra

`-t|--transport <http|fasp|both>`: Transport.

-   `fasp`: fasp only;
-   `http`: http only;
-   `both` **[default]**: first try fasp (ascp), use http if cannot download using fasp

`--location <value>`: Location of data.

`-N|--min-size <size>`: Minimum file size to download in KB (inclusive).

`-X|--max-size <size>`: Maximum file size to download in KB (exclusive).
Default: 20G

`-f|--force <yes|no|all|ALL>`: Force object download.

-   `no` **[default]**: skip download if the object if found and complete;
-   `yes`: download it even if it is found and is complete;
-   `all`: ignore lock files (stale locks or it is being downloaded by another process use at your own risk!);
-   `ALL`: ignore lock files, restart download from beginning.

`-r|--resume <yes|no> `: Resume partial downloads.
**Default:** `yes`.

`-C|--verify <yes|no> `: Verify after download.
**Default:** `yes`.

`-p|--progress`: Show progress.

`-H|--heartbeat <value>`: Time period in minutes to display download progress where `0` is no progress.
**Default:** `1`

`--eliminate-quals`: Don't download QUALITY column.

`-c|--check-all`: Double-check all refseqs.

`-S|--check-rs <yes|no|smart>`: Check for refseqs in downloaded files.
Smart **[default]**: skip check for large encrypted non-sra files.

`-o|--order <kart|size>`: Kart prefetch order when downloading kart: one of: kart, size.

-   `kart`: in kart order;
-   `size` **[default]**: smallest first.

`-R|--rows <rows>`: Kart rows to download.
Row list should be ordered.
**Default:** `all`.

`--perm <PATH>`: `PATH` to jwt cart file.

`--ngc <PATH>`: `PATH` to ngc file.

`--cart <PATH>`: To read kart file.

`-a|--ascp-path <ascp-binary|private-key-file>`: Path to ascp program and private key file (asperaweb_id_dsa.putty)

`--ascp-options <value>`: Arbitrary options to pass to ascp command line.

`-o|--output-file <FILE>`: Write file to `FILE` when downloading single file.

`-O|--output-directory <DIRECTORY>`: Save files to `DIRECTORY/`

`-h|--help`: Output brief explanation for the program.

`-V|--version`: Display the version of the program then quit.

`-L|--log-level <level>`: Logging level as number or enum string.
One of (`fatal`|`sys`|`int`|`err`|`warn`|`info`|`debug`) or (`0`-`6`).
**Default:** is `warn`.

`-v|--verbose`: Increase the verbosity of the program status messages.
Use multiple times for more verbosity.
Negates quiet.

`-q|--quiet`: Turn off all status messages for the program.
Negated by verbose.

`--option-file <file>`: Read more options and parameters from the file.

## `fasterq-dump`

The fasterq-dump tool extracts data in FASTQ- or FASTA-format from SRA-accessions.
It is a commandline-tool that is available for Linux, macOS, and Windows.

[Documentation](https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump)

### Usage

`fasterq-dump <path> [options]`

`fasterq-dump <accession> [options]`

### Options

`-F|--format`: format (`special`, `fastq`, default=fastq)

`-o|--outfile`: output-file

`-O|--outdir`: output-dir

`-b|--bufsize`: size of file-buffer dflt=`1MB`

`-c|--curcache`: size of cursor-cache dflt=`10MB`

`-m|--mem`: memory limit for sorting dflt=`100MB`

`-t|--temp`: where to put temp. files dflt=`curr dir`

`-e|--threads`: how many thread dflt=`6`

`-p|--progress`: show progress

`-x|--details`: print details

`-s|--split-spot`: split spots into reads

`-S|--split-files`: write reads into different files

`-3|--split-3`: writes single reads in special file

`--concatenate-reads`: writes whole spots into one file

`-Z|--stdout`: print output to stdout

`-f|--force`: force to overwrite existing file(s)

`--skip-technical`: skip technical reads

`--include-technical`: include technical reads

`-M|--min-read-len`: filter by sequence-len

`--table`: which seq-table to use in case of pacbio

`-B|--bases`: filter by bases

`-A|--append`: append to output-file

`--fasta`: produce FASTA output

`--fasta-unsorted`: produce FASTA output, unsorted

`--fasta-ref-tbl`: produce FASTA output from REFERENCE tbl

`--fasta-concat-all`: concatenate all rows and produce FASTA

`--internal-ref`: extract only internal REFERENCEs

`--external-ref`: extract only external REFERENCEs

`--ref-name`: extract only these REFERENCEs

`--ref-report`: enumerate references

`--use-name`: print name instead of seq-id

`--seq-defline`: custom defline for sequence: `$ac=accession`, `$sn=spot-name`, `$sg=spot-group`, `$si=spot-id`, `$ri=read-id`, `$rl=read-length`.

`--qual-defline`: custom defline for qualities: same as `seq-defline`

`-U|--only-unaligned`: process only unaligned reads

`-a|--only-aligned`: process only aligned reads

`--disk-limit`: explicitly set disk-limit

`--disk-limit-tmp`: explicitly set disk-limit for temp files

`--size-check`: switch to control:

-   `on` **[default]**: perform size-check;
-   `off`: do not perform size-check;
-   `only`: perform size-check only.

`--ngc <PATH>`: `PATH` to ngc file

`-h|--help`: Output brief explanation for the program.

`-V|--version`: Display the version of the program then quit.

`-L|--log-level <level>`: Logging level as number or enum string.
One of (`fatal`|`sys`|`int`|`err`|`warn`|`info`|`debug`) or (`0`-`6`).
**Default:** is `warn`.

`-v|--verbose`: Increase the verbosity of the program status messages.
Use multiple times for more verbosity.
Negates quiet.

`-q|--quiet`: Turn off all status messages for the program.
Negated by verbose.

`--option-file <file>`: Read more options and parameters from the file.

## `vdb-dump`

### Usage

`vdb-dump <path> [<path> ...] [options]`

### Options

`-I|--row_id_on`: print row id

`-l|--line_feed <line_feed>`: line-feed's inbetween rows

`-N|--colname_off`: do not print column-names

`-X|--in_hex`: print numbers in hex

`-T|--table <table>`: table-name

`-R|--rows <rows>`: rows
**Default:** `all`.

`-C|--columns <columns>`: columns.
**Default:** `all`.

`-S|--schema <schema>`: schema-name

`-A|--schema_dump`: dumps the schema

`-E|--table_enum`: enumerates tables

`-O|--column_enum`: enumerates columns in extended form

`-o|--column_enum_short`: enumerates columns in short form

`-D|--dna_bases`: force dna-bases if column fits pattern

`-M|--max_length <max_length>`: limits line length

`-i|--indent_width <indent_width>`: indents the line

`-f|--format <format>`: output format:

-   `csv`: comma separated values on one line
-   `xml`: xml-style without complete xml-frame
-   `json`: json-style
-   `piped`: 1 line per cell: row-id, column-name: value
-   `tab`: 1 line per row: tab-separated values only
-   `fastq`: FASTQ ( 4 lines ) for each row
-   `fastq1`: FASTQ ( 4 lines ) for each fragment
-   `fasta`: FASTA ( 2 lines ) for each fragment if possible
-   `fasta1`: one FASTA-record for the whole accession (REFSEQ)
-   `fasta2`: one FASTA-record for each REFERENCE in cSRA
-   `qual`: QUAL ( 2 lines ) for each row
-   `qual1`: QUAL ( 2 lines ) for each fragment if possible

`-r|--id_range`: prints id-range

`-n|--without_sra`: without sra-type-translation

`-x|--exclude <columns>`: exclude these columns

`-b|--boolean <1 or T>`: defines how boolean's are printed (1,T)

`-j|--obj_version`: request vdb-version

`--obj_timestamp`: request object modification date

`-y|--obj_type`: report type of object

`-u|--numelem`: print only element-count

`-U|--numelemsum`: sum element-count

`--phys-blobs`: show physical blobs

`--vdb-blobs`: show VDB-blobs

`--phys`: enumerate physical columns

`--readable`: enumerate readable columns

`--idx-report`: enumerate all available index

`--idx-range <idx-name>`: enumerate values and row-ranges of one index

`--cur-cache <size>`: size of cursor cache

`--output-file <filename>`: write output to this file

`--output-path <path>`: write output to this directory

`--gzip`: compress output using gzip

`--bzip2`: compress output using bzip2

`--output-buffer-size <size>`: size of output-buffer, 0...none

`--disable-multithreading`: disable multithreading

`--info`: print info about run

`--spotgroups`: show spotgroups

`--merge-ranges`: merge and sort row-ranges

`--spread`: show spread of integer values

`-a|--append`: append to output-file, if output-file used

`--ngc <path>`: path to ngc file

`--view <view>`: view-name

`--inspect`: inspect data usage inside object

`-h|--help`: Output brief explanation for the program.

`-V|--version`: Display the version of the program then quit.

`-L|--log-level <level>`: Logging level as number or enum string.
One of (`fatal`|`sys`|`int`|`err`|`warn`|`info`|`debug`) or (`0`-`6`).
**Default:** is `warn`.

`-v|--verbose`: Increase the verbosity of the program status messages.
Use multiple times for more verbosity.
Negates quiet.

`-q|--quiet`: Turn off all status messages for the program.
Negated by verbose.

`--option-file <file>`: Read more options and parameters from the file.
