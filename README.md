# Solutions to Niklas Linde's Homework for LAPIS 2019

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/santisoler/lapis2019-linde-homework/master)

This repo contains a Jupyter notebook that performs the tasks left as homework by Niklas
Linde on the LAPIS 2019 School.

It contains:

- `Solution to Homework.ipynb`: Jupyter notebook with the solutions to the homework.
- `data.mat`: Matlab data file containing measured GPR arrival times.
- `environment.yml`: Configuration file for creating Anaconda environment.

The `Solution to Homework.ipynb` notebook has been written by
[Santiago Soler](https://github.com/santisoler) and
[Sebastian Correa-Otto](https://github.com/sacaliza)
in order to pass the LAPIS 2019 assignments.


## How to run?

### Use Binder

The easiest way to run the notebook is through [Binder](https://mybinder.org).
Just follow
[this link](https://mybinder.org/v2/gh/santisoler/lapis2019-linde-homework/master)
and wait until Binder loads the notebook.

### Download the repo and run it locally

You'll need a Python distribution to make it run with the following dependencies:
- numpy
- numba
- scipy
- matplotlib

The easiest way to get Python and all of these dependencies installed is through
[Anaconda](https://www.anaconda.com/).
Download the latest Anaconda 3 distribution for your OS.

Then clone the repo:

```
git clone https://github.com/santisoler/lapis2019-linde-homework
```

or
[download it](https://github.com/santisoler/lapis2019-linde-homework/archive/master.zip)
as a zip file.

Change your working directory to the cloned repo and create the conda environment to get
all the dependencies:
```
cd lapis2019-linde-homework
conda env create
```

Once all the packages have been downloaded and installed, activate the repository:
```
conda activate lapis2019-linde-homework
```

Finally, start a Jupyter Notebook kernel:
```
jupyter-notebook
```
This will open a new page on your web browser where you will be able to find the
`Solutions to Homework.ipynb` notebook.
You'll be able to open it and run any cell.
If you want to reproduce our results, run all cells in order.
