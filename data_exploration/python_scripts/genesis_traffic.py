# %%
from data_exploration.python_scripts.functions import *
import pandas as pd

# %%
genesis = 'data_exploration/Daten/genesis_traffic/genesis_traffic.csv'

# Export NaN values in genesis traffic dataset as csv-file with percentage of their occurence
genesis_traffic = pd.read_csv(genesis, sep=";", encoding="ISO-8859-9")
set_name(genesis_traffic, "genesis_traffic")
genesis_cols = ['1. Quartal Unternehmen Anzahl',
                '1. Quartal Beförderte Personen 1000',
                '1. Quartal Personenkilometer 1000', '2. Quartal Unternehmen Anzahl',
                '2. Quartal Beförderte Personen 1000',
                '2. Quartal Personenkilometer 1000', '3. Quartal Unternehmen Anzahl',
                '3. Quartal Beförderte Personen 1000',
                '3. Quartal Personenkilometer 1000', '4. Quartal Unternehmen Anzahl',
                '4. Quartal Beförderte Personen 1000',
                '4. Quartal Personenkilometer 1000']
genesis_nans = ['-', 'x', '.', '...', '..']

count_NaNs_and_export(genesis_cols, genesis_nans, genesis_traffic, "genesis_traffic_NaNs")

# %%
#  Deleting NaN Values [x, -, ..., .] From Genesis Data Set
for col in genesis_cols:
    for nan in genesis_nans:
        genesis_traffic = genesis_traffic[genesis_traffic[col] != nan]

# %%
#  Converting Numeral-Value Columns to int46 in Genesis Data Set
conversion_dict = {col: 'int64' for col in genesis_cols}
genesis_traffic = genesis_traffic.astype(conversion_dict)

# %%
# Create a new DataFrame containing selected columns from the original DataFrame
final_genesis_traffic = genesis_traffic[["Jahr", "Art", "Bundesland"]].copy()

# Calculate total number of companies across quarters and add it as a new column
final_genesis_traffic["Anzahl_Unternehmen"] = (genesis_traffic['1. Quartal Unternehmen Anzahl'] +
                                               genesis_traffic['2. Quartal Unternehmen Anzahl'] +
                                               genesis_traffic['3. Quartal Unternehmen Anzahl'] +
                                               genesis_traffic['4. Quartal Unternehmen Anzahl'])

# Calculate total transported persons across quarters and add it as a new column
final_genesis_traffic["Befoerderte_Personen_in_1000"] = (genesis_traffic['1. Quartal Beförderte Personen 1000'] +
                                                         genesis_traffic['2. Quartal Beförderte Personen 1000'] +
                                                         genesis_traffic['3. Quartal Beförderte Personen 1000'] +
                                                         genesis_traffic['4. Quartal Beförderte Personen 1000'])

# Convert transported persons to million units and add it as a new column
final_genesis_traffic["Befoerderte_Personen_in_Mio"] = (
    final_genesis_traffic["Befoerderte_Personen_in_1000"].apply(lambda x: round((x / 1000), 3)))

# Calculate total person kilometers across quarters and add it as a new column
final_genesis_traffic["Personenkilometer_in_1000"] = (genesis_traffic['1. Quartal Personenkilometer 1000'] +
                                                      genesis_traffic['2. Quartal Personenkilometer 1000'] +
                                                      genesis_traffic['3. Quartal Personenkilometer 1000'] +
                                                      genesis_traffic['4. Quartal Personenkilometer 1000'])

# Convert person kilometers to million units and add it as a new column
final_genesis_traffic["Personenkilometer_in_Mio"] = (
    final_genesis_traffic["Personenkilometer_in_1000"].apply(lambda x: round((x / 1000), 3)))

# Filter and save data related to 'Liniennahverkehr insgesamt' into a separate DataFrame
deutschland_gesamt_values = final_genesis_traffic[final_genesis_traffic['Art'] == 'Liniennahverkehr insgesamt']
final_genesis_traffic = final_genesis_traffic[final_genesis_traffic['Art'] != 'Liniennahverkehr insgesamt']

# Save the modified DataFrame to a CSV file
final_genesis_traffic.to_csv(f"data_exploration/Daten/genesis_traffic/final_genesis_traffic.csv", index=True)

# Aggregate and merge data based on different groupings (Jahr/Art, Jahr/Bundesland, Jahr)
# and create summary rows for Germany, individual Bundesland, and overall Deutschland values

# Combine summarized Germany data based on 'Jahr' and 'Art'
merge_df = pd.DataFrame()

# Summarize Germany values based on 'Jahr' and 'Art'
# Concatenate the summarized data with the 'merge_df' DataFrame
# Repeat the same process for Bundesland and overall Deutschland values

# Concatenate all the individual DataFrames to create the final DataFrame with aggregated data
germany_df = final_genesis_traffic.groupby(['Jahr', 'Art']).agg({
    'Anzahl_Unternehmen': 'sum',
    'Befoerderte_Personen_in_1000': 'sum',
    "Befoerderte_Personen_in_Mio": 'sum',
    'Personenkilometer_in_1000': 'sum',
    "Personenkilometer_in_Mio": 'sum',
}).reset_index()

germany_row = pd.DataFrame(
    {'Jahr': germany_df['Jahr'], 'Art': germany_df['Art'],
     'Bundesland': 'Deutschland',
     'Anzahl_Unternehmen': germany_df['Anzahl_Unternehmen'],
     'Befoerderte_Personen_in_1000': germany_df['Befoerderte_Personen_in_1000'],
     'Befoerderte_Personen_in_Mio': germany_df['Befoerderte_Personen_in_Mio'],
     'Personenkilometer_in_1000': germany_df['Personenkilometer_in_1000'],
     'Personenkilometer_in_Mio': germany_df['Personenkilometer_in_Mio'],
     })

merge_df = pd.concat([merge_df, germany_row], ignore_index=True)

germany_df = final_genesis_traffic.groupby(['Jahr', 'Bundesland']).agg({
    'Anzahl_Unternehmen': 'sum',
    'Befoerderte_Personen_in_1000': 'sum',
    "Befoerderte_Personen_in_Mio": 'sum',
    'Personenkilometer_in_1000': 'sum',
    "Personenkilometer_in_Mio": 'sum',
}).reset_index()

germany_row = pd.DataFrame(
    {'Jahr': germany_df['Jahr'], 'Art': 'Liniennahverkehr insgesamt',
     'Bundesland': germany_df['Bundesland'],
     'Anzahl_Unternehmen': germany_df['Anzahl_Unternehmen'],
     'Befoerderte_Personen_in_1000': germany_df['Befoerderte_Personen_in_1000'],
     'Befoerderte_Personen_in_Mio': germany_df['Befoerderte_Personen_in_Mio'],
     'Personenkilometer_in_1000': germany_df['Personenkilometer_in_1000'],
     'Personenkilometer_in_Mio': germany_df['Personenkilometer_in_Mio'],
     })

merge_df = pd.concat([merge_df, germany_row], ignore_index=True)

germany_df = final_genesis_traffic.groupby(['Jahr']).agg({
    'Anzahl_Unternehmen': 'sum',
    'Befoerderte_Personen_in_1000': 'sum',
    "Befoerderte_Personen_in_Mio": 'sum',
    'Personenkilometer_in_1000': 'sum',
    "Personenkilometer_in_Mio": 'sum',
}).reset_index()

germany_row = pd.DataFrame(
    {'Jahr': germany_df['Jahr'], 'Art': 'Liniennahverkehr insgesamt',
     'Bundesland': 'Deutschland',
     'Anzahl_Unternehmen': germany_df['Anzahl_Unternehmen'],
     'Befoerderte_Personen_in_1000': germany_df['Befoerderte_Personen_in_1000'],
     'Befoerderte_Personen_in_Mio': germany_df['Befoerderte_Personen_in_Mio'],
     'Personenkilometer_in_1000': germany_df['Personenkilometer_in_1000'],
     'Personenkilometer_in_Mio': germany_df['Personenkilometer_in_Mio'],
     })

merge_df = pd.concat([merge_df, germany_row], ignore_index=True)

bundesland_df = final_genesis_traffic.groupby(['Jahr', 'Art']).agg({
    'Anzahl_Unternehmen': ['mean', 'median', 'std'],
    'Befoerderte_Personen_in_1000': ['mean', 'median', 'std'],
    'Befoerderte_Personen_in_Mio': ['mean', 'median', 'std'],
    'Personenkilometer_in_1000': ['mean', 'median', 'std'],
    'Personenkilometer_in_Mio': ['mean', 'median', 'std'],
}).reset_index()

mean = pd.DataFrame({'Jahr': bundesland_df['Jahr'], 'Art': bundesland_df['Art'], 'Bundesland': 'Deutschland_mean',
                     'Anzahl_Unternehmen': round(bundesland_df['Anzahl_Unternehmen']['mean'], 3),
                     'Befoerderte_Personen_in_1000': round(bundesland_df['Befoerderte_Personen_in_1000']['mean'], 3),
                     'Personenkilometer_in_1000': round(bundesland_df['Personenkilometer_in_1000']['mean'], 3)})

std = pd.DataFrame({'Jahr': bundesland_df['Jahr'], 'Art': bundesland_df['Art'], 'Bundesland': 'Deutschland_std',
                    'Anzahl_Unternehmen': round(bundesland_df['Anzahl_Unternehmen']['std'], 3),
                    'Befoerderte_Personen_in_1000': round(bundesland_df['Befoerderte_Personen_in_1000']['std'], 3),
                    'Personenkilometer_in_1000': round(bundesland_df['Personenkilometer_in_1000']['std'], 3)})

median = pd.DataFrame({'Jahr': bundesland_df['Jahr'], 'Art': bundesland_df['Art'], 'Bundesland': 'Deutschland_median',
                       'Anzahl_Unternehmen': round(bundesland_df['Anzahl_Unternehmen']['median'], 3),
                       'Befoerderte_Personen_in_1000': round(bundesland_df['Befoerderte_Personen_in_1000']['median'],
                                                             3),
                       'Personenkilometer_in_1000': round(bundesland_df['Personenkilometer_in_1000']['median'], 3)})

final_genesis_traffic = pd.concat([final_genesis_traffic, mean, std, median], ignore_index=True)

# Concatenate all the individual DataFrames to create the final DataFrame with aggregated data
final_genesis_traffic = pd.concat([final_genesis_traffic, merge_df], ignore_index=True)

# %%
# importing population development dataset for calculating relative numbers
population = 'data_exploration/Daten/inhabitants/bevoelkerungsentwicklung.csv'
population_df = pd.read_csv(population)

gen_df = final_genesis_traffic.copy()
gen_df["Relative_Befoerderte_Personen_in_1000"] = gen_df.apply(
    lambda x: x["Befoerderte_Personen_in_1000"] / get_EW(x["Jahr"], x["Bundesland"], population_df, "Einwohner"),
    axis=1)

# %%
# Save the final DataFrame to a CSV file
final_genesis_traffic.to_csv(f"data_exploration/Daten/genesis_traffic/final_genesis_traffic.csv", index=True)

# Save the final DataFrame to a JSON file using table orientation
final_genesis_traffic.to_json(f"data_exploration/Daten/jsons/final_genesis_traffic.json", index=True, orient="table",
                              force_ascii=False)
