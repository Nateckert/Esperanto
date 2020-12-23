# Esperanto

## Installation

1. Clone the Github repository
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


## Use

Use the `main.ipynb` to run the script:

- it scans in the data folder at the root of the script the excel file for each language
- it outputs an output.xlsx in the output folder with the concatenation of the translation

## Data format

One file per language, in the data folder, with the naming convention `ESPERANTO_OTHERLANGUAGE.xlsx`

The excel file must have 3 columns:

- `ID`
- `esperanto`
- `otherLanguageName`