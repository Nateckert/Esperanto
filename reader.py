import os
import re

def scan_languages(path_dir):
    """
        Scan the directory for files following the pattern ESPERANTO_ENGLISH.xlsx
        and return a list of the available languages, and the full path_files
        For exemple, files ESPERANTO_ENGLISH.xlsx and ESPERANTO_FRENCH.xlsx would return 
            ['ENGLISH', 'FRENCH'] and ['ESPERANTO_ENGLISH.xlsx', 'ESPERANTO_FRENCH.xlsx']
    """
    files = os.listdir(path_dir)

    pattern = re.compile(r'^ESPERANTO_(\w+).xlsx$')
    languages = list()
    path_files = list()
    for file in files:
        match = pattern.match(file)
        if match is not None:
            languages.append(match.group(1))
            path_files.append(match.group(0))
    return languages, path_files




import pandas as pd

def join_languages(path_dir, *languages):
    languages_files, path_files = scan_languages(path_dir)
    df = None
    for language in languages:
        if language not in languages_files:
            raise ValueError('The file for the language {} is not found in the directory {}, warning, the case matters'.format(language, path_dir))
        index = languages_files.index(language)
        path_language = path_files[index]
        path_tot = path_dir + path_language
        xls = pd.ExcelFile(path_tot)

        if len(xls.sheet_names) != 1:
            raise ValueError('There are several worksheet in the file {}'.format(path_tot))
        df_language = pd.read_excel(path_tot, usecols=[0,1,2])
        
        if df_language.columns[0] != 'ID':
            raise ValueError('The first column of the file {} should be named ID, the current name is {}'.format(path_language, df_language.columns[0]))
        if df_language.columns[1] != 'esperanto':
            raise ValueError('The second column of the file {} should be named esperanto, the current name is {}'.format(path_language, df_language.columns[1]))

        if df is not None:
            df = df.join(df_language, lsuffix='', rsuffix='_other')
            df = df.drop('ID_other', axis=1)
            df = df.drop('esperanto_other', axis=1)
        else:
            df = df_language.copy()
    return df

def to_excel(df, path_output):
    df = df.drop('ID', axis=1)
    df.to_excel(path_output, index=False)