# Google Colab

!!! danger "DRAFT"

    This page is a work in progress and is subject to change at any moment.

Managing local Python installations can be troublesome with a large class.
Different versions, dependencies, and system setups could mean it runs on your computer but not elsewhere.
To minimize these issues, we will be using [Google Colab](https://colab.google/) to write, run, and distribute Python code in [Jupyter Notebooks](https://jupyter.org/).

## Features

-   Google Colab runs in the cloud on Google's servers.
    This means you don't need to install any software on your local machine, and you can access it from anywhere with an internet connection.
-   One of the notable features of Google Colab is that it provides free access to Graphics Processing Units (GPUs) and Tensor Processing Units (TPUs).
    This can be especially beneficial for machine learning tasks that require significant computational power.
-   Multiple users can collaborate in real-time on a Colab Notebook. This makes it easy for teams to work together on coding projects, share insights, and provide feedback.
-   Colab integrates seamlessly with Google Drive.
    You can save your Colab Notebooks directly to your Google Drive, share them, and access them from any device.
-   Colab Notebooks run on virtual machines in the cloud, and your session state persists as long as the virtual machine is active.
    However, if there is inactivity for too long, the session may be disconnected.

## Opening files in Colab

When you see a ![colab logo](/img/launchy/colab.svg){ width=18px } symbol in the upper right corner on a page of this website, you can click on it to open up that file directly in [Google Colab](https://colab.google/).

!!! example

    Go to [this page](../../intro/regression/introduction.ipynb) to see an example.
    If you click ![colab logo](/img/launchy/colab.svg){ width=18px } then you will be taken [here](https://colab.research.google.com/github/oasci/pitt-biosc1540-2024s-website/blob/main/biosc1540/modules/intro/regression/introduction.ipynb).

How does this work?
Well, [Google Colab](https://colab.google/) has an import mechanism for Jupyter Notebooks in [GitHub](https://github.com/) repositories.
Adding an import link is all it takes.

!!! quote "**Figure 1**"

    When you open up our Jupyter notebooks in Google colab, you will be met with this screen.

    <figure markdown>
    ![](/img/colab/gui.svg){ width=600 }
    </figure>

    Jupyter notebooks are made up of <font color="#ff2a2a"><b>blocks</b></font> which can be thought of as paragraphs that can change types.
    [Markdown](https://www.markdownguide.org/) is simply text like you would put in a Word document, email, etc.
    The only difference is how you specify things like a list, link, etc.

    When you see a `[ ]` with a greyed out background, this is a Python block.
    You can put any Python code here and run it.
    We will get to this later.

    When working on Jupyter notebooks from this website, you should always <font color="#37c871"><b>save a copy to your Google Drive</b></font>.

    To run Python code, you have to <font color="#0066ff"><b>connect to Google's servers</b></font>.
    When you click this button, it will initiate a connection to Google's servers and will look like this once it is done.

    <figure markdown>
    ![](/img/colab/kernel-running.png){ width=200 }
    </figure>

## Python kernel

TODO:

## Saving

Opening it, however, does not create a copy in your Google Drive.
When running code, working on assignments, etc. you should always save a copy in your Google Drive.
The ![colab logo](/img/launchy/colab.svg){ width=18px } button just opens up a copy without saving it.
We recommend keeping these files in a class directory.

## Reproducibility

As mentioned above, the version of Python can affect its reproducibility.
We include the following code block as the first code cell.

```python
import sys
IN_COLAB = 'google.colab' in sys.modules
if IN_COLAB:
    !sudo apt-get update -y > /dev/null 2>&1
    !sudo apt-get install python3.11 python3.11-dev python3.11-distutils libpython3.11-dev > /dev/null 2>&1
    !sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2 > /dev/null 2>&1
```

All this does is check if the Jupyter Notebook is running and install the version of Python used to develop this course: 3.11.

You can technically remove this.
The version of Python usually has small changes that are backward compatible.
The main issue is the dependencies that we install; some have very specific version requirements that could affect which versions get installed.
