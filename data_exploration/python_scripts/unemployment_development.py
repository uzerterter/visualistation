# %%
from data_exploration.python_scripts.functions import *

# %%
unemployment_sh = ('data_exploration/Daten/unemployment/statistic_id2509_arbeitslosenquote-in-schleswig-holstein-bis'
                   '-2022.csv')
unemployment_ham = 'data_exploration/Daten/unemployment/statistic_id2510_arbeitslosenquote-in-hamburg-bis-2022.csv'
unemployment_ns = 'data_exploration/Daten/unemployment/statistic_id2511_arbeitslosenquote-in-niedersachsen-bis-2022.csv'
unemployment_br = 'data_exploration/Daten/unemployment/statistic_id2512_arbeitslosenquote-in-bremen-bis-2022.csv'
unemployment_nrw = ('data_exploration/Daten/unemployment/statistic_id2513_arbeitslosenquote-in-nordrhein-westfalen-bis'
                    '-2022.csv')
unemployment_hes = 'data_exploration/Daten/unemployment/statistic_id2514_arbeitslosenquote-in-hessen-bis-2022.csv'
unemployment_rp = ('data_exploration/Daten/unemployment/statistic_id2515_arbeitslosenquote-in-rheinland-pfalz-bis-2022'
                   '.csv')
unemployment_bawu = 'data_exploration/Daten/unemployment/statistic_id2516_arbeitslosenquote-in-baden-wuerttemberg-bis-2022.csv'
unemployment_ba = 'data_exploration/Daten/unemployment/statistic_id2517_arbeitslosenquote-in-bayern-bis-2022.csv'
unemployment_saa = 'data_exploration/Daten/unemployment/statistic_id2518_arbeitslosenquote-im-saarland-bis-2022.csv'
unemployment_ber = 'data_exploration/Daten/unemployment/statistic_id2519_arbeitslosenquote-in-berlin-bis-2022.csv'
unemployment_bburg = 'data_exploration/Daten/unemployment/statistic_id2520_arbeitslosenquote-in-brandenburg-bis-2022.csv'
unemployment_mp = 'data_exploration/Daten/unemployment/statistic_id2521_arbeitslosenquote-in-mecklenburg-vorpommern-bis-2022.csv'
unemployment_s = 'data_exploration/Daten/unemployment/statistic_id2522_arbeitslosenquote-in-sachsen-bis-2022.csv'
unemployment_sa = 'data_exploration/Daten/unemployment/statistic_id2523_arbeitslosenquote-in-sachsen-anhalt-bis-2022.csv'
unemployment_t = 'data_exploration/Daten/unemployment/statistic_id2524_arbeitslosenquote-in-thueringen-bis-2022.csv'
unemployment_de = 'data_exploration/Daten/unemployment/statistic_id1224_arbeitslosenquote-in-deutschland-bis-2023.csv'

# %%
df_unemployment_sh = process_csv_data(unemployment_sh, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                      column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_sh, "df_unemployment_sh")

df_unemployment_ham = process_csv_data(unemployment_ham, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                       column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_ham, "df_unemployment_ham")
df_unemployment_ns = process_csv_data(unemployment_ns, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                       column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_ns, "df_unemployment_ns")
df_unemployment_br = process_csv_data(unemployment_br, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                      column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_br, "df_unemployment_br")

df_unemployment_nrw = process_csv_data(unemployment_nrw, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                       column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_nrw, "df_unemployment_nrw")

df_unemployment_hes = process_csv_data(unemployment_hes, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                       column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_hes, "df_unemployment_hes")

df_unemployment_rp = process_csv_data(unemployment_rp, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                      column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_rp, "df_unemployment_rp")

df_unemployment_bawu = process_csv_data(unemployment_bawu, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                        column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_bawu, "df_unemployment_bawu")

df_unemployment_ba = process_csv_data(unemployment_ba, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                      column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_ba, "df_unemployment_ba")

df_unemployment_saa = process_csv_data(unemployment_saa, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                       column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_saa, "df_unemployment_saa")

df_unemployment_ber = process_csv_data(unemployment_ber, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                       column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_ber, "df_unemployment_ber")

df_unemployment_bburg = process_csv_data(unemployment_bburg, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                         column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_bburg, "df_unemployment_bburg")

df_unemployment_mp = process_csv_data(unemployment_mp, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                      column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_mp, "df_unemployment_mp")

df_unemployment_s = process_csv_data(unemployment_s, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                     column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_s, "df_unemployment_s")

df_unemployment_sa = process_csv_data(unemployment_sa, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                      column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_sa, "df_unemployment_sa")

df_unemployment_t = process_csv_data(unemployment_t, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                     column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_t, "df_unemployment_t")
df_unemployment_de = process_csv_data(unemployment_de, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                     column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_de, "df_unemployment_de")

# %%
# Dictionary with Federal States Abbrevations and Federal State Names
bundeslaender = {
    "ba": "Bayern",
    "bawu": "Baden-Württemberg",
    "ber": "Berlin",
    "br": "Bremen",
    "bburg": "Brandenburg",
    "hes": "Hessen",
    "mp": "Mecklenburg-Vorpommern",
    "ns": "Niedersachsen",
    "nrw": "Nordrhein-Westfalen",
    "rp": "Rheinland-Pfalz",
    "saa": "Saarland",
    "s": "Sachsen",
    "sa": "Sachsen-Anhalt",
    "t": "Thüringen",
    "ham": "Hamburg",
    "sh": "Schleswig-Holstein",
    "de": "Deutschland"
}

# list of all datasets with unemployment data
datasets_unemployment = [
    df_unemployment_sh,
    df_unemployment_ham,
    df_unemployment_ns,
    df_unemployment_br,
    df_unemployment_nrw,
    df_unemployment_hes,
    df_unemployment_rp,
    df_unemployment_bawu,
    df_unemployment_ba,
    df_unemployment_saa,
    df_unemployment_ber,
    df_unemployment_bburg,
    df_unemployment_mp,
    df_unemployment_s,
    df_unemployment_sa,
    df_unemployment_t,
    df_unemployment_de
]

# Add Federal State in own column to datasets in lists of datasets
add_bundesland(datasets_unemployment, bundeslaender)

# Merge all the datasets in the lists from above into one dataset for each list
df_unemployment = pd.concat(datasets_unemployment, ignore_index=True)

# %%
# Converting numeral-values in columns into int64 format in unemployment dataset
df_unemployment_cols = {'Jahr'}
conversion_dict = {col: 'int64' for col in df_unemployment_cols}
df_unemployment = df_unemployment.astype(conversion_dict)

# %%

plot_percentage_over_years(df_unemployment,
                           title='Percentage of Unemployment Rates Over the Years (1994-2022) for Each Bundesland',
                           y_name='Prozent', plot_filename="unemployment")

# %%
# Adding mean, median and std to the population development dataset, rent index dataset, unemployment rate dataset
# df_unemployment = add_mean_median_std(df_unemployment, 'Prozent', 'Jahr')

# %%
# exporting dataset as csv file
df_unemployment.to_csv(f"data_exploration/Daten/unemployment/arbeitslosenquote.csv", index=True)

# exporting dataset as json
df_unemployment.to_json("data_exploration/Daten/jsons/unemployment_rate.json", index=True, orient="table", force_ascii=False)
