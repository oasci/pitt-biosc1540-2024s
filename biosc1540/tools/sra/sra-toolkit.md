# SRA toolkit

The SRA Toolkit and SDK from NCBI is a collection of tools and libraries for using data in the INSDC Sequence Read Archives.

[GitHub](https://github.com/ncbi/sra-tools) &nbsp; &nbsp; &nbsp; [Documentation](https://github.com/ncbi/sra-tools/wiki)

## Download

You can download the toolkit from the [GitHub wiki](https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit#sra-toolkit) or click on one of the following links for v3.0.10.

=== "Windows"

    [Download for Windows 64 bit](https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.0.10/sratoolkit.3.0.10-win64.zip)

=== "MacOS"

    [Download for MacOS x86-64 bit](https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.0.10/sratoolkit.3.0.10-mac-x86_64.tar.gz)

=== "Ubuntu"

    [Download for Ubuntu Linux 64 bit](https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.0.10/sratoolkit.3.0.10-ubuntu64.tar.gz)

## Installation

=== "Windows"

    1.  Extract the `sratoolkit.3.0.10-win64.zip` file somewhere in your user directory.
    2.  Open a command shell in the same directory as your `sratoolkit.3.0.10-win64.zip` file by pressing :fontawesome-brands-windows: + `R` and type

        ```
        cmd.exe
        ```

        and then hit `ENTER`.

        !!! tip

            You can change directories using the `cd` command.

    3.  Move into the `bin` directory.

        ```
        cd bin
        ```

=== "MacOS"

    1.  Extract the contents of `sratoolkit.3.0.10-mac-x86_64.tar.gz`.

        ``` bash
        tar -vxzf sratoolkit.3.0.10-mac-x86_64.tar.gz
        ```

=== "Ubuntu"

    1.  Extract the contents of `sratoolkit.3.0.10-ubuntu64.tar.gz`.

        ``` sh
        tar -vxzf sratoolkit.3.0.10-ubuntu64.tar.gz
        ```

        This will create a directory called `sratoolkit.3.0.10-ubuntu64` with the following contents.

        ``` console
        $ ls
        bin/  CHANGES  example/  README-blastn  README.md  README-vdb-config  schema/
        ```

    2.  Move `sratoolkit.3.0.10-ubuntu64` to a directory where you store your third-party software.
        If you have `sudo` access, this is normally `/opt`.
        Otherwise, you can use something like `~/codes`.

        ``` bash
        sudo cp -r sratoolkit.3.0.10-ubuntu64 /opt # (1)!
        ```

        1.  If you are using `~/codes` then you do not need `sudo`.
    3.  Add `/opt/sratoolkit.3.0.10-ubuntu64/bin` to your path.

        ```bash
        echo 'export PATH=$PATH:/opt/sratoolkit.3.0.10-ubuntu64/bin' >> ~/.bashrc \
        source ~/.bashrc
        ```
    4.  Test that `bash` can find `fastq-dump`.

        ``` console
        $ which fastq-dump
        /opt/sratoolkit.3.0.10-ubuntu64/bin/fastq-dump
        ```

## Configuration

=== "Windows"

    TODO:

=== "MacOS"

    TODO:

=== "Ubuntu"

    1.  Open up a terminal and run.

        ``` bash
        vdb-config -i
        ```

        You will see something like the following screen.

        ![](/files/img/sra/setup/vdb-config-i.png)

        You can use `TAB` or click on options to select them and press `ENTER` to toggle them.
    2.  Under `MAIN`, ensure that you have `[X] Enable Remote Access` enabled.
    3.  Under `CACHE`, ensure that you have `[X] enable local file-caching` enabled.
        Select a `location of user-repository` such as `~/sra-cache`.
        This directory needs to be empty
    4.  Hit `[ save ]` and then `[ exit ]`.

## Retrieving SRA runs

The combination of `prefetch` and `fasterq-dump` is the fastest way to extract FASTQ-files from SRA-accessions.
The `prefetch` tool downloads all necessary files to your computer and can be invoked multiple times if the download failed.
It will not start from the beginning every time; instead, it will pick up from where the last invocation failed.

### Example

Suppose we want to download run [`SRR000001`][SRR000001] from experiment [`SRX000007`][SRX000007].

First, we should get information about

``` console
$ vdb-dump SRR000001 --info
acc    : SRR000001
path   : /home/alex/sra-cache/sra/SRR000001.sra
remote : https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR000001/SRR000001
size   : 312,527,083
type   : Table
platf  : SRA_PLATFORM_454
SEQ    : 470,985
SCHEMA : NCBI:SRA:_454_:tbl:v2#1.0.7
TIME   : 0x0000000055248a41 (04/07/2015 21:54)
FMT    : SFF
FMTVER : 2.4.5
LDR    : sff-load.2.4.5
LDRVER : 2.4.5
LDRDATE: Feb 25 2015 (2/25/2015 0:0)
```

This download will take up 312.5 MB of space.

Next use [`prefetch`](#prefetch) to download the data.

``` console
$ prefetch SRR000001

2023-12-26T20:16:17 prefetch.3.0.10: Current preference is set to retrieve SRA
Normalized Format files with full base quality scores.
2023-12-26T20:16:18 prefetch.3.0.10: 1) Downloading 'SRR000001'...
2023-12-26T20:16:18 prefetch.3.0.10: SRA Normalized Format file is being retrieved,
if this is different from your preference, it may be due to current file availability.
2023-12-26T20:16:18 prefetch.3.0.10:  Downloading via HTTPS...
2023-12-26T20:16:26 prefetch.3.0.10:  HTTPS download succeed
2023-12-26T20:16:26 prefetch.3.0.10:  'SRR000001' is valid
2023-12-26T20:16:26 prefetch.3.0.10: 1) 'SRR000001' was downloaded successfully
```

Since we did not specify where to store the files it defaulted to the cache directory at `~/sra-cache/`.
We could have specified a different directory.

``` bash
prefetch --output-directory ~/test/SRR000001 SRR000001
```

!!! tip

    [`prefetch`](#prefetch) will automatically create the directory if it does not exist.

### `prefetch`

#### Usage

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

#### Options

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

### `fasterq-dump`

The fasterq-dump tool extracts data in FASTQ- or FASTA-format from SRA-accessions.
It is a commandline-tool that is available for Linux, macOS, and Windows.

[Documentation](https://github.com/ncbi/sra-tools/wiki/HowTo:-fasterq-dump)

#### Usage

`fasterq-dump <path> [options]`

`fasterq-dump <accession> [options]`

#### Options

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

## Validating downloads

After the download, you have the option to test the downloaded data with the `vdb-validate` tool.
After the successful download, there is no need for network-connectivity.
You can move the folder created by prefetch to a different location to perform the conversion to the fastq-format somewhere else (for instance to a compute-cluster without internet access).

[SRR000001]: https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR000001&display=metadata
[SRX000007]: https://www.ncbi.nlm.nih.gov/sra/SRX000007
