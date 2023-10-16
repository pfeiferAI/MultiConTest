<img src="res/multicontest_icon.png" alt="MultiConTest logo" width="150">

# MultiConTest

The MultiConTest GUI application provides easy access to identifying confounding factors in multi-view biomedical data
using the statistical analyses described by [Wallner et al. (2022)](https://doi.org/10.1101/2022.10.14.512210). The detection of potential confounding factors
in multiple data modalities is carried out based on a joint multi-view clustering of primary data.

If your multi-view data is not clustered yet, you may consider using an appropriate clustering method such as the easily
accessible [web-rMKL](https://web-rmkl.org/) webserver by [Röder et al. (2019)](https://doi.org/10.1093/nar/gkz422) which
delivers state-of-the-art clustering results for multi-view data.

## Installation

Binary versions of MultiConTest can be found under [releases](https://github.com/pfeiferAI/MultiConTest/releases).
These binaries come bundled with a recent version of Python and all necessary packages (see license information in the
_About_ dialog of the App). This means that files may be executed directly without installation.

`Windows` and `Linux` executables (.exe or .bin) are compiled for x86_64 systems. Their functionality on arm64 systems
has not been evaluated. If you encounter compatibility issues, you may try to run the application from source as
described below.

For `macOS`, the application is bundled in a DMG and may either be dragged to the Programs folder or executed directly
from within the DMG or any other location. Please make sure that you select the correct version of the application, 
Intel (x86_64) or Apple Silicon (arm64), for your system.

### Running the application from source

You may also run the application from source. We recommend using Python 3.11.3 since MultiConTest was
developed with this version. To run the application from source, please follow these steps:
- Clone this repository
- [optional] Create a virtual environment, e.g., with `python -m venv mutlicontest_venv`
- Install the MultiConTest package with `pip install {path_to_repository}`. All necessary dependencies will be
  installed automatically.
- Installing the package will automatically add a command line entry point for MultiConTest. You may run the
  application with `MultiConTest` from the command line in any directory.
- Alternatively, you can launch the application from the project root by running `python -m multicontest`.

## Usage

### Input data

MultiConTest requires a file containing sample-cluster assignments and a file that contains sample label metadata:
- Sample-cluster assignment file:
  - `.csv` or `.txt` file containing sample names in the first column and cluster labels
    in the second column (separated by commas).
  - The file may contain a header row.
- Sample label file (metadata):
  - `.csv` file containing samples (rows) and sample labels (columns). The file must be comma-separated.
  - Sample names must be identical to the sample-cluster assignment file. Only samples that are present in both files
    will be considered.
  - All columns must contain a header row with a unique name of the sample label. Multiple label columns can be included.
  - MultiConTest will only consider categorical labels. A filtering method is provided for selecting categorical
    labels based on their number of unique values (see below).
  - The data may contain missing values. Such values can either be dropped automatically or included as an additional
    category.

**Label selection and filtering:**

We strongly advise using only labels with a large number of overlapping samples, since sparse data will reduce the 
statistical power of the confounding detection (i.e., the distribution of sample label categories among clusters might 
be shifted due to missing values).

By clicking _Adjust categories_, the automatic filtering threshold can be set manually. This threshold is used to
determine whether a label is likely to be numerical or categorical. The default value is 10, which means that all
labels with 10 or less unique values are considered categorical. The threshold can be adjusted to values between 2
and 20. Please confirm that the selected potential confounding factors are categorical by inspecting the table in the 
_Sample labels_ tab as well as the visualization in the _Confounding test_ tab.

By default, missing values are dropped from the data. This means that samples with missing values for the selected
label will be excluded from the confounding test. If you wish to include missing values as an additional category, you
may do so by unselecting the _drop missing values_ checkbox. This is only recommended if missing data provides
meaningful information for the selected label.

### Confounding test

After importing all necessary data as described above, MultiConTest provides an overview of available samples, sample
labels and the number of overlapping samples for the selected label. Since only categorical labels are suitable for
the confounding test, the software will automatically filter labels that are likely to be numerical labels. Upon
selecting a sample label in the _Sample labels_ tab, the according sample overlap will be shown. Simultaneously, a 
visualization of the per-cluster label distribution and the corresponding contingency table shown in the 
_Confounding test_ tab. Furthermore, a contingency table can be displayed to show the distribution of samples among
clusters and label categories. The _compute_ button will start the confounding test for the selected label and
display the results in the _Confounding test_ tab upon completion.

**Test results:**

The main test results (displayed in the _Confounding test_ tab) include the final p-value of the confounding test that
is corrected by permutation testing. Furthermore, the results include the _original p-value_ of the chi-square test,
and the percentage of redrawn permutations. The latter is an indicator of the statistical power of the confounding test.
If the percentage of redrawn permutations is high, the statistical power of the test may be marginal since chi-square
test assumptions were not met in many permutations.

Further details regarding the confounding test can be found in the original publication:
[Wallner et al. (2022)](https://doi.org/10.1101/2022.10.14.512210)

If the confounding test is computed for multiple labels, the results for all tested labels will be displayed in a table
in the _Test results_ tab. The table contains all information from the _Confounding test_ tab as well as the error
messages for failed tests. The table can be exported as a `.csv` file.

**Note: The table only contains a collection of all test results. These results are not corrected for multiple testing!**



## Troubleshooting:

- If you encounter issues with the data import, please verify that your `.csv` files are comma-separated. You may need
  to convert your files to utf-8 encoding if they cannot be imported otherwise.
- If you encounter issues with the export, please verify that you have write permissions for the selected export
  directory.
- If you encounter issues with the confounding test, please verify that the selected label is categorical and that
  there are enough overlapping samples for the selected label.
- If confounding tests fail due to chi-square test errors, please check the distribution of samples among clusters
  for the selected label. If the number of samples in one or more clusters is too small, the chi-square test will fail.
  You may also consider looking at the sample overlap for the selected label as it may hint at missing information that
  may have been lost due to a different sample labeling scheme.

## Citing

If you use MultiConTest, please cite the original publication:
```
Wallner, M. A., Kersten, N., & Pfeifer, N. (2022). Multi-view confounder detection for biomedical studies.
bioRxiv 2022.10.14.512210; doi: https://doi.org/10.1101/2022.10.14.512210
```

---

Copyright &copy; 2023 University of Tübingen, Nicolas Kersten
