# Code Analysis

Using a CNN to analyze suspicious scripts found online

## Conda Environment

`conda env create -f keras-code.condaenv`
`conda activate keras-code`

## Importing the Data

Credit to Offensive Security's [Exploit DB](https://github.com/offensive-security/exploitdb). Clone their repo down (large repo) and this one alongside it:

```
git clone https://github.com/offensive-security/exploitdb
git clone https://github.com/tangenttonothing/code_analysis
```

`exploitdb_import.py` build a pandas-compatible CSV filled with the exploitdb files as well as a random assortment of system files (this is not a good source of clean files, working on finding the best assortment of clean data files). After running this script, you should have a `data.csv` floating around for use with the models.

