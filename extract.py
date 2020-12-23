import pandas as pd

def extract_columns(path, columnsToKeep, nonEmptyConditionOnRowsToKeep):
    df = pd.read_excel(path)
    df = df[columnsToKeep]

    languageCondition = [columnsToKeep[i] for i in nonEmptyConditionOnRowsToKeep]
    df = df[(pd.notnull(df[languageCondition[0]])) & (pd.notnull(df[languageCondition[1]]))]

    return df