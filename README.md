# crl-analysis

This repo contains my parsing and anylsis code for the certificate revocation list (CRL) question on
the CMSC711 midterm. There are three main steps to using this code:

1. Downloading the CRLs from the appropriate certificate authorities (CAs)
2. Parsing them into an easily managable format (csvs)
3. Performing the anylses and generating hte neccessary tables and plots

Steps 1 and 2 are handled automatically by the `makefile`; just use the `make` command to
set this process in motion. If the process fails, make sure to install any missing dependencies and
try it again.

For step 3, you'll need to run `plot-crls.ipynb`. This is an iPython notebook, so the easiest way to do
this is to open it in Jupyter by running the command `jupyter notebook` and open it in your browser
using one of the links printed to the terminal. Open the notebook from there and run all the cells
to generate all the tables and plots.
