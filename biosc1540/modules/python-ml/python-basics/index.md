# Python basics

!!! danger "DRAFT"

    This page is a work in progress and is subject to change at any moment.

## Google Colab

Managing local Python installations can be troublesome with a large class.
Different versions, dependencies, and system setups could mean it runs on your computer but not elsewhere.
To minimize these issues, we will be using [Google Colab](https://colab.google/) to write, run, and distribute Python code in [Jupyter Notebooks](https://jupyter.org/).

### Features

-   Google Colab runs in the cloud on Google's servers.
    This means you don't need to install any software on your local machine, and you can access it from anywhere with an internet connection.
-   One of the notable features of Google Colab is that it provides free access to Graphics Processing Units (GPUs) and Tensor Processing Units (TPUs).
    This can be especially beneficial for machine learning tasks that require significant computational power.
-   Multiple users can collaborate in real-time on a Colab Notebook. This makes it easy for teams to work together on coding projects, share insights, and provide feedback.
-   Colab integrates seamlessly with Google Drive.
    You can save your Colab Notebooks directly to your Google Drive, share them, and access them from any device.
-   Colab Notebooks run on virtual machines in the cloud, and your session state persists as long as the virtual machine is active.
    However, if there is inactivity for too long, the session may be disconnected.

## Usage

When you see a ![colab logo](/img/launchy/colab.svg){ width=18px } symbol in the upper right corner of a page, you can click on it to open up that file directly in [Google Colab](https://colab.google/).

!!! example

    Go to [this page](../../python-ml/regression/introduction.ipynb) to see an example.
    If you click ![colab logo](/img/launchy/colab.svg){ width=18px } then you will be taken [here](https://colab.research.google.com/github/oasci/pitt-biosc1540-2024s-website/blob/main/biosc1540/modules/python-ml/regression/introduction.ipynb).

How does this work?
Well, [Google Colab](https://colab.google/) has an import mechanism for Jupyter Notebooks in [GitHub](https://github.com/) repositories.
Adding an import link is all it takes.

Opening it, however, does not create a copy in your Google Drive.
When running code, working on assignments, etc. you should always save a copy in your Google Drive.
The ![colab logo](/img/launchy/colab.svg){ width=18px } button just opens up a copy without saving it.
We recommend keeping these files in a class directory.

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

## Learn Python

There are a ton of resources to learn the basics of Python and I cannot necessarily write better ones.
Here are some options I recommend&mdash;in decreasing order&mdash;along with what sections will be relevant for this course.

-   [kaggle learn](https://www.kaggle.com/learn/): "Intro to Programming", "Intro to Machine Learning", "Python", and "Pandas" courses.
-   [learnpython.org](https://www.learnpython.org/): "Learn the Basics" and "Data Science Tutorials".
-   [Google's Python Class](https://developers.google.com/edu/python): Everything.
-   [Byte of Python](https://python.oasci.org/external/byte-of-python/): Everything

I know this is not a Python course, and you will never be graded on how good your Python code is.
All that matters is that it runs in a reasonable amount of time and I can understand what your code is trying to do.

## Installation

{% include "/modules/python-ml/python-basics/installation.md" %}

<!-- LINKS -->

[miniconda]: https://docs.conda.io/projects/miniconda/en/latest/#
