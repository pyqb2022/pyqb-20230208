# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: February 8, 2023
#
# You can solve the exercises below by using standard Python 3.10 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.10/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC](https://docs.pymc.io).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2223/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.**
#
#
#
#

import numpy as np
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore
import arviz as az   # type: ignore

# ### Exercise 1 (max 3 points)
#
# The file [Plant_data.csv](./Plant_data.csv) (Vesala, Risto, Rikkinen, Aleksi, Pellikka, Petri, Rikkinen, Jouko, & Arppe, Laura. (2023). You eat what you find – local patterns in vegetation structure control diets of African fungus-growing termites [Data set]. https://doi.org/10.5061/dryad.2ngf1vhq0) contains data about a stable isotope values and C/N content in for some plants under examination.
#
# - Site: study site where the plant sample was collected from (Maktau or Sanctuary)
# - Plant_type: C3 or C4 photosynthesizing plant corresponding trees/shrubs and savanna grasses, respectively
# - Plant_part: plant part that was analyzed
# - Species: name of the studied plant
# - d13C: d13C mean of the analyzed sample (in cases where standard deviation is reported, value is average of two replicate measurements)
# - d13C_sd: standard deviation of two replicate measurements (d13C) of the same sample (NA means that the sample was measured only once)
# - C_cont: carbon content (%, w/w) of the analyzed sample (in cases where standard deviation is reported, value is average of two replicate measurements)
# - C_cont_sd: standard deviation of two replicate measurements (C_cont) of the same sample (NA means that the sample was measured only once)
# - d15N: d15N mean of the analyzed sample (in cases where standard deviation is reported, value is average of two replicate measurements)
# - d15N_sd: standard deviation of two replicate measurements (d15N) of the same sample (NA means that the sample was measured only once)
# - N_cont: nitrogen content (%, w/w) of the analyzed sample (in cases where standard deviation is reported, value is average of two replicate measurements)
# - N_cont_sd: standard deviation of two replicate measurements (N_cont) of the same sample (NA means that the sample was measured only once)
#
#
# Load the data in a pandas dataframe and make a `bool` column `wooden` which is `True` iff the plant part is "wood" or "bark".

pass

# ### Exercise 2 (max 6 points)
#
# Define a proper Gaussian function and plot the Gaussians defined by all the pairs d15N (mean), d15N_sd (standard deviation). If the standard deviation is NA ignore the line: in total you should have 18 plots. Remember that a Gaussian with mean $\mu$ and standard deviation $\sigma$ is defined as:
#
#
# $g(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left( -\frac{1}{2} \frac{(x - \mu)^2}{\sigma^2} \right)$
#

pass

# ### Exercise 3 (max 6 points)
#
# Define a function `secret_sauce` that takes a plant type (a string), a d13C (a float) and percentage (a float between 0 and 1): the result should be the percentage applied to d13C if the plant type is "C3" and (1 - percentage) of d13C if the plant type is "C4". For example, secret_sauce("C3", 30, .1) should be 3.0, and secret_sauce("C4", 30, .1) should be 27.0. 
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

pass

# ### Exercise 4 (max 4 points)
#
# Add a column to the data with the `secret_sauce` computed in the previous exercise, using `d13C` and `C_cont` as the percentage (scale it properly!).
#
# To get the full marks avoid the use of explicit loops.

pass

# ### Exercise 5 (max 2 points)
#
# Print the mean d15N for each type of plant part. 

pass

# ### Exercise 6 (max 3 points)
#
# Make a scatter plot of `d13C` vs. `d15N`, using different colors for each plant part.

pass

# ### Exercise 7 (max 3 points)
#
# Compute the mean and the standard deviation of the sum of `d13C` and `d15N` when taking into account only the acaciae (all the types included in the data).

pass

# ### Exercise 8 (max 6 points)
#
# Consider this statistical model:
#
# - a parameter $\alpha$ is normally distributed with mean 0 and standard deviation 5
# - a parameter $\beta$ is normally distributed with mean 0 and standard deviation 5
# - $\sigma$ is exponentially distributed with $\lambda = 1$
# - the observed `N_cont` is normally distributed with a mean given by $\alpha + \beta\cdot C$, where $C$ is the corresponding `C_cont`
#
# Code this model with pymc, sample the model, and plot the summary of the resulting estimation by using `az.plot_posterior`.
#
#
#
#

pass

