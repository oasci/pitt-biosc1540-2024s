# Tutorials

The combination of `prefetch` and `fasterq-dump` is the fastest way to extract FASTQ-files from SRA-accessions.
The `prefetch` tool downloads all necessary files to your computer and can be invoked multiple times if the download failed.
It will not start from the beginning every time; instead, it will pick up from where the last invocation failed.

In the following content, we will use the SRA run [`SRR000001`][SRR000001] from experiment [`SRX000007`][SRX000007] as an example.
The same workflow can be used for any other accession number.

## Getting metadata

First, we should get information about the run using the command [`vbd-dump`](./scripts.md#vdb-dump).

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

-   `acc`: Accession number for our request.
-   `path`: Local path to the SRA run.
-   `remote`: Remote path where the SRA run is stored.
-   `size`: File size of SRA run in bytes.
    Divide by 1,000,000 to convert this into MB.
-   `type`: TODO:
-   `platf`: TODO:
-   `SEQ`: TODO:
-   `FMT`: TODO:
-   `FMTVER`: Format version
-   `LDR`: TODO:
-   `LDRVER`: TODO:
-   `LDRDATE`: TODO:

One key metric is the size, which for this example would be 312.5 MB of space.

## Downloading SRA run

Now, we can use [`prefetch`](./scripts.md#prefetch) to download the data.

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

    [`prefetch`](./scripts.md#prefetch) will automatically create the directory if it does not exist.

## Extract data

We need to use [`fasterq-dump`](./scripts.md#fasterq-dump) to retrieve the FASTA- or FASTQ-files from the SRA-accession.
The tool will use the current directory as scratch-space and will also put the output-files there.
When finished, the tool will delete all temporary files it created.

``` console
$ fasterq-dump SRR000001
spots read      : 470,985
reads read      : 1,883,940
reads written   : 707,026
reads 0-length  : 468,635
technical reads : 708,279
```

If you want to have the output files created in a different directory, use the `--outdir` option.
The `fasterq-dump` tool performs a `split-3` operation by default.

You will now have three files in your working directory:

-   `SRR000001.fastq` (147.5 MB)
-   `SRR000001_1.fastq` (70.8 MB)
-   `SRR000001_2.fastq` (78.8 MB)


[SRR000001]: https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR000001&display=metadata
[SRX000007]: https://www.ncbi.nlm.nih.gov/sra/SRX000007
