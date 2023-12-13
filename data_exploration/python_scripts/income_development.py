# %%
from data_exploration.python_scripts.functions import *

# %%
# define paths of datasets
income_ham = 'data_exploration/Daten/income/statistic_id252383_arbeitnehmerentgelt-je-arbeitnehmer-in-hamburg-bis-2022.csv'
income_bawu = 'data_exploration/Daten/income/statistic_id252496_arbeitnehmerentgelt-je-arbeitnehmer-in-baden-wuerttemberg-bis-2022.csv'
income_ba = 'data_exploration/Daten/income/statistic_id253200_arbeitnehmerentgelt-je-arbeitnehmer-in-bayern-bis-2022.csv'
income_ber = 'data_exploration/Daten/income/statistic_id253201_arbeitnehmerentgelt-je-arbeitnehmer-in-berlin-bis-2022.csv'
income_bburg = 'data_exploration/Daten/income/statistic_id253202_arbeitnehmerentgelt-je-arbeitnehmer-in-brandenburg-bis-2022.csv'
income_br = 'data_exploration/Daten/income/statistic_id253203_arbeitnehmerentgelt-je-arbeitnehmer-in-bremen-bis-2022.csv'
income_hes = 'data_exploration/Daten/income/statistic_id253204_arbeitnehmerentgelt-je-arbeitnehmer-in-hessen-bis-2022.csv'
income_mp = 'data_exploration/Daten/income/statistic_id253205_arbeitnehmerentgelt-je-arbeitnehmer-in-mecklenburg-vorpommern-bis-2022.csv'
income_ns = 'data_exploration/Daten/income/statistic_id253206_arbeitnehmerentgelt-je-arbeitnehmer-in-niedersachsen-bis-2022.csv'
income_nrw = 'data_exploration/Daten/income/statistic_id253207_arbeitnehmerentgelt-je-arbeitnehmer-in-nordrhein-westfalen-bis-2022.csv'
income_rp = 'data_exploration/Daten/income/statistic_id253208_arbeitnehmerentgelt-je-arbeitnehmer-in-rheinland-pfalz-bis-2022.csv'
income_saa = 'data_exploration/Daten/income/statistic_id253209_arbeitnehmerentgelt-je-arbeitnehmer-im-saarland-bis-2022.csv'
income_sa = 'data_exploration/Daten/income/statistic_id253211_arbeitnehmerentgelt-je-arbeitnehmer-in-sachsen-anhalt-bis-2022.csv'
income_s = 'data_exploration/Daten/income/statistic_id253210_arbeitnehmerentgelt-je-arbeitnehmer-in-sachsen-bis-2022.csv'
income_sh = 'data_exploration/Daten/income/statistic_id253212_arbeitnehmerentgelt-je-arbeitnehmer-in-schleswig-holstein-bis-2022.csv'
income_t = 'data_exploration/Daten/income/statistic_id253213_arbeitnehmerentgelt-je-arbeitnehmer-in-thueringen-bis-2022.csv'
income_de = 'data_exploration/Daten/income/statistic_id440525_arbeitnehmerentgelte-je-arbeitnehmer-in-deutschland-bis-2022.csv'

# %%
# Reading in Datasets
df_income_ba = process_csv_data(income_ba, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_ba, "df_income_ba")
df_income_ham = process_csv_data(income_ham, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_ham, "df_income_ham")
df_income_bburg = process_csv_data(income_bburg, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_bburg, "df_income_bburg")
df_income_br = process_csv_data(income_br, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_br, "df_income_br")
df_income_ber = process_csv_data(income_ber, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_ber, "df_income_ber")
df_income_bawu = process_csv_data(income_bawu, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_bawu, "df_income_bawu")
df_income_hes = process_csv_data(income_hes, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_hes, "df_income_hes")
df_income_mp = process_csv_data(income_mp, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_mp, "df_income_mp")
df_income_rp = process_csv_data(income_rp, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_rp, "df_income_rp")
df_income_nrw = process_csv_data(income_nrw, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_nrw, "df_income_nrw")
df_income_saa = process_csv_data(income_saa, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_saa, "df_income_saa")
df_income_sa = process_csv_data(income_sa, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_sa, "df_income_sa")
df_income_s = process_csv_data(income_s, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_s, "df_income_s")
df_income_ns = process_csv_data(income_ns, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_ns, "df_income_ns")
df_income_t = process_csv_data(income_t, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_t, "df_income_t")
df_income_sh = process_csv_data(income_sh, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_sh, "df_income_sh")
df_income_de = process_csv_data(income_de, skip_rows=4, skip_first_columns=1, skip_last_rows=2, skip_last_columns=1,
                             column_names=["Jahr", "Income"])
set_name(df_income_de, "df_income_de")

# %%
# list of all datasets with population development data
datasets_income = [
    df_income_ba,
    df_income_bawu,
    df_income_ber,
    df_income_br,
    df_income_bburg,
    df_income_hes,
    df_income_mp,
    df_income_ns,
    df_income_nrw,
    df_income_rp,
    df_income_saa,
    df_income_s,
    df_income_sa,
    df_income_t,
    df_income_ham,
    df_income_sh,
    df_income_de
]

# %%
# Add Federal State in own column to datasets in lists of datasets
add_bundesland(datasets_income, bundeslaender)

# %%
# Merge all datasets in list above into one dataset
df_income = pd.concat(datasets_income, ignore_index=True)

# %%
# Exporting dataset as csv
df_income.to_csv(f"data_exploration/Daten/income/income.csv", index=True)
# Exporting datasets as jsons
df_income.to_json(f"data_exploration/Daten/jsons/income.json", index=True, orient="table",
               force_ascii=False)

