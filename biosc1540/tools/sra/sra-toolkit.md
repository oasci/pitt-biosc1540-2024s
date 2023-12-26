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
