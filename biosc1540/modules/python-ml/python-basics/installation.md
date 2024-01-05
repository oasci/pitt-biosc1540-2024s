!!! important

    This is just included for completeness.
    We will always be using [Google Colab](https://colab.google/) in this class.

The most common and reproducible ways to getting Python on your system is with [conda](https://docs.conda.io/projects/conda/en/latest/index.html).

=== "Windows"

    [Download](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) the `Windows installer` for your desired Python version.
    Or run the following commands to automatically perform the installation.

    ```bash
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe \
    start /wait "" miniconda.exe /S \
    del miniconda.exe
    ```

=== "MacOS"

    These commands will install [miniconda][miniconda] on the latest M1 macOS.

    ```bash
    mkdir -p ~/miniconda3 \
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 \
    rm -rf ~/miniconda3/miniconda.sh
    ```

    After installing, initialize your newly-installed [Miniconda][miniconda]. The following commands initialize for bash and zsh shells:

    ```bash
    ~/miniconda3/bin/conda init bash \
    ~/miniconda3/bin/conda init zsh
    ```

=== "Ubuntu"

    These commands will install [miniconda][miniconda] on linux machines.

    ```bash
    mkdir -p ~/miniconda3 \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda3/miniconda.sh \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 \
    rm -rf ~/miniconda3/miniconda.sh
    ```

    After installing, initialize your newly-installed [Miniconda][miniconda]. The following commands initialize for bash and zsh shells:

    ```bash
    ~/miniconda3/bin/conda init bash \
    ~/miniconda3/bin/conda init zsh
    ```

---

Once we have conda installed, we are ready to create an [environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) for running arbitrary Python code.

=== "Input"

    ```bash
    conda create --name biosc1540-2024s
    ```

=== "Output"

    ```text
    Channels:
    - defaults
    Platform: linux-64
    Collecting package metadata (repodata.json): done
    Solving environment: done

    ## Package Plan ##

    environment location: /home/alex/miniconda3/envs/biosc1540-2024s



    Proceed ([y]/n)? y

    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate biosc1540-2024s
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    ```

---

Now that we have created our Conda environment, the next step is to activate it. Activating the environment ensures that any software or packages installed will be specific to this environment, avoiding conflicts with other environments or the system-wide installation.

```bash
conda activate biosc1540-2024s
```

Once activated, your command prompt should indicate the active environment.
Now, if you try to run Python with the `python` command, you might encounter an error similar to the one below:

```shell
$ python
Command 'python' not found
```

This is because our environment is currently empty, and Python is not installed in it.
In this course, we will use [Python 3.11.7](https://www.python.org/downloads/release/python-3117/).
To install Python within our Conda environment, follow these steps.

It is generally a good idea to update conda first.

=== "Input"

    ```bash
    conda update --all
    ```

=== "Output"

    ```text
    Channels:
    - defaults
    Platform: linux-64
    Collecting package metadata (repodata.json): done
    Solving environment: done

    # All requested packages already installed.
    ```

---

=== "Input"

    ```bash
    conda install python=3.11.7 -c conda-forge
    ```

=== "Output"

    ```text
    Channels:
    - conda-forge
    - defaults
    Platform: linux-64
    Collecting package metadata (repodata.json): done
    Solving environment: done

    ## Package Plan ##

    environment location: /home/alex/miniconda3/envs/biosc1540-2024s

    added / updated specs:
        - python=3.11.7


    The following NEW packages will be INSTALLED:

    _libgcc_mutex      conda-forge/linux-64::_libgcc_mutex-0.1-conda_forge
    _openmp_mutex      conda-forge/linux-64::_openmp_mutex-4.5-2_gnu
    bzip2              conda-forge/linux-64::bzip2-1.0.8-hd590300_5
    ca-certificates    conda-forge/linux-64::ca-certificates-2023.11.17-hbcca054_0
    ld_impl_linux-64   conda-forge/linux-64::ld_impl_linux-64-2.40-h41732ed_0
    libexpat           conda-forge/linux-64::libexpat-2.5.0-hcb278e6_1
    libffi             conda-forge/linux-64::libffi-3.4.2-h7f98852_5
    libgcc-ng          conda-forge/linux-64::libgcc-ng-13.2.0-h807b86a_3
    libgomp            conda-forge/linux-64::libgomp-13.2.0-h807b86a_3
    libnsl             conda-forge/linux-64::libnsl-2.0.1-hd590300_0
    libsqlite          conda-forge/linux-64::libsqlite-3.44.2-h2797004_0
    libuuid            conda-forge/linux-64::libuuid-2.38.1-h0b41bf4_0
    libxcrypt          conda-forge/linux-64::libxcrypt-4.4.36-hd590300_1
    libzlib            conda-forge/linux-64::libzlib-1.2.13-hd590300_5
    ncurses            conda-forge/linux-64::ncurses-6.4-h59595ed_2
    openssl            conda-forge/linux-64::openssl-3.2.0-hd590300_1
    pip                conda-forge/noarch::pip-23.3.2-pyhd8ed1ab_0
    python             conda-forge/linux-64::python-3.11.7-hab00c5b_1_cpython
    readline           conda-forge/linux-64::readline-8.2-h8228510_1
    setuptools         conda-forge/noarch::setuptools-68.2.2-pyhd8ed1ab_0
    tk                 conda-forge/linux-64::tk-8.6.13-noxft_h4845f30_101
    tzdata             conda-forge/noarch::tzdata-2023d-h0c530f3_0
    wheel              conda-forge/noarch::wheel-0.42.0-pyhd8ed1ab_0
    xz                 conda-forge/linux-64::xz-5.2.6-h166bdaf_0


    Proceed ([y]/n)? y


    Downloading and Extracting Packages:

    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    ```

---

??? note "What is `-c conda-forge`?"

    The additional `-c conda-forge` in the command `conda install python=3.11.7 -c conda-forge` specifies the channel from which Conda should retrieve the Python package.

    In Conda, a channel is a repository of packages.
    The default channel is the Anaconda repository, but the `-c conda-forge` option instructs Conda to look for the specified package in the [conda-forge channel](https://conda-forge.org/).
    Conda-forge is a [community-maintained collection of conda packages](https://anaconda.org/conda-forge).

    Including this option in the command is beneficial for a couple of reasons:

    -   Conda-forge often provides more up-to-date versions of packages, including Python, as it is maintained by the community.
        This can be advantageous if you want the latest features or bug fixes.
    -   Some packages or specific versions might be available on conda-forge but not in the default Anaconda repository.
        Adding the conda-forge channel increases the pool of available packages.
