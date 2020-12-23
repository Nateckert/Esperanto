# Esperanto

https://github.com/Nateckert/Esperanto_dictionary


## Installation

1. Clone the Github repository, than run in the terminal the following commands
2. `cd path/to/folder` (`cd Desktop/Python/Esperanto_dictionary`)
3. `python3 -m venv venv`
4. `source ./venv/bin/activate`
5. `pip install --upgrade pip`
6. `pip install -r requirements.txt`
7. `deactivate`

## Start-up

1. `cd path/to/folder` (`cd Desktop/Python/Esperanto_dictionary`)
2. `source ./venv/bin/activate`
3. `jupyter notebook`


## `create_dictionary.ipynb`

- create a `data` folder and an `output` folder
- add to the `data` folder the .xlsx files for each language with the appropriate format (see Data format section)
- the script scans the `data` for each language
- it outputs an `output.xlsx` in the `output` folder with the concatenation of the translation

### Data format

One file per language, in the data folder, with the naming convention `ESPERANTO_OTHERLANGUAGE.xlsx`

The excel file must have 3 columns:

- `ID`
- `esperanto`
- `otherLanguageName`

## `filter_dictionary.ipynb`

Select :

- a subset of columns
- a subset of rows based on a non empty condition of two columns