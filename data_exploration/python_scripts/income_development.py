# %%
import pandas as pd
from data_exploration.python_scripts.functions import *

# %%
# define paths of datasets
income2021 = (
    'data_exploration/Daten/income/statistic_id209211_bruttomonatsverdienst-nach-bundeslaendern-und-geschlecht-in'
    '-deutschland-2021.csv')
income2016 = (
    'data_exploration/Daten/income/statistic_id806476_median-des-bruttomonatsverdienstes-von-maennern-und-frauen-nach'
    '-bundeslaendern-2016.csv')

# %%
# Reding in Datasets
brutto_income_2021 = pd.read_csv(income2021, sep=",")
set_name(brutto_income_2021, "brutto_income_2021")

brutto_income_2016 = pd.read_csv(income2016, sep=",")
set_name(brutto_income_2016, "brutto_income_2016")

# %%
# Converting numeral-values in columns into int64 format in brutto income 2021 dataset
# 1. Converting to string without losing trailing 0
# 2. Deleting german format '.' for thousands
# 3. converting back to int64
brutto_income_2021['Männer'] = brutto_income_2021['Männer'].apply(lambda x: "{:.3f}".format(x))
brutto_income_2021['Männer'] = brutto_income_2021['Männer'].str.replace('.', '')
brutto_income_2021['Männer'] = brutto_income_2021['Männer'].astype(int)

brutto_income_2021['Frauen'] = brutto_income_2021['Frauen'].apply(lambda x: "{:.3f}".format(x))
brutto_income_2021['Frauen'] = brutto_income_2021['Frauen'].str.replace('.', '')
brutto_income_2021['Frauen'] = brutto_income_2021['Frauen'].astype(int)

brutto_income_2021['Insgesamt'] = brutto_income_2021['Insgesamt'].apply(lambda x: "{:.3f}".format(x))
brutto_income_2021['Insgesamt'] = brutto_income_2021['Insgesamt'].str.replace('.', '')
brutto_income_2021['Insgesamt'] = brutto_income_2021['Insgesamt'].astype(int)
print(brutto_income_2021)

# %%
# Converting numeral-values in columns into int64 format in brutto income 2016 dataset
# 1. Converting to string without losing trailing 0
# 2. Deleting german format '.' for thousands
# 3. converting back to int64
brutto_income_2016['Männer'] = brutto_income_2016['Männer'].apply(lambda x: "{:.3f}".format(x))
brutto_income_2016['Männer'] = brutto_income_2016['Männer'].str.replace('.', '')
brutto_income_2016['Männer'] = brutto_income_2016['Männer'].astype(int)

brutto_income_2016['Frauen'] = brutto_income_2016['Frauen'].apply(lambda x: "{:.3f}".format(x))
brutto_income_2016['Frauen'] = brutto_income_2016['Frauen'].str.replace('.', '')
brutto_income_2016['Frauen'] = brutto_income_2016['Frauen'].astype(int)
print(brutto_income_2016)

# %%
# Deleting Währung column in income dataset
brutto_income_2016.drop([' Währung'], axis=1, inplace=True)
brutto_income_2021.drop([' Währung'], axis=1, inplace=True)

brutto_income_2021['Jahr'] = [2021] * len(brutto_income_2021)
brutto_income_2016['Jahr'] = [2016] * len(brutto_income_2016)

# %%
# Add 'Insgesamt' column in income dataset
brutto_income_2016['Insgesamt'] = ((brutto_income_2016['Männer'] + brutto_income_2016['Frauen']) / 2)
brutto_income_2016['Insgesamt'] = brutto_income_2016['Insgesamt'].round().astype('int64')

# %%
# Adding mean, median and std to income dataset
median_income = {
    "Bundesland": "Deutschland median",
    "Männer": brutto_income_2021.Männer.median(),
    "Frauen": brutto_income_2021.Frauen.median(),
    "Insgesamt": brutto_income_2021.Insgesamt.median(),
    "Jahr": 2021
}

mean_income = {
    "Bundesland": "Deutschland mean",
    "Männer": brutto_income_2021.Männer.mean(),
    "Frauen": brutto_income_2021.Frauen.mean(),
    "Insgesamt": brutto_income_2021.Insgesamt.mean(),
    "Jahr": 2021
}

std_income = {
    "Bundesland": "Deutschland std",
    "Männer": brutto_income_2021.Männer.std(),
    "Frauen": brutto_income_2021.Frauen.std(),
    "Insgesamt": brutto_income_2021.Insgesamt.std(),
    "Jahr": 2021
}

for row in [median_income, mean_income, std_income]:
    brutto_income_2021.loc[len(brutto_income_2021)] = row

# %%
# Adding mean, median and std to income dataset
brutto_income_2016.loc[len(brutto_income_2016)] = [
    "Deutschland median",
    brutto_income_2016.Männer.median(),
    brutto_income_2016.Frauen.median(),
    2016,
    brutto_income_2016.Insgesamt.median(),
]

brutto_income_2016.loc[len(brutto_income_2016)] = [
    "Deutschland mean",
    brutto_income_2016.Männer.mean(),
    brutto_income_2016.Frauen.mean(),
    2016,
    brutto_income_2016.Insgesamt.mean(),
]

brutto_income_2016.loc[len(brutto_income_2016)] = [
    "Deutschland std",
    brutto_income_2016.Männer.std(),
    brutto_income_2016.Frauen.std(),
    2016,
    brutto_income_2016.Insgesamt.std(),
]

# %%
brutto_income_2016 = brutto_income_2016.rename(columns={'Bundesland ': 'Bundesland'})
df_income = pd.concat([brutto_income_2021, brutto_income_2016], ignore_index=True)

# %%

for col in ['Männer', 'Frauen', 'Insgesamt', 'Jahr']:
    df_income[col] = df_income[col].round().astype('int64')

df_income.to_csv(f"data_exploration/Daten/income/income.csv", index=True)
df_income.to_json(f"data_exploration/Daten/jsons/income.json", index=True, orient="table", force_ascii=False)

