# %%
from data_exploration.python_scripts.functions import *

# %%
civ_bawu = 'data_exploration/Daten/inhabitants/statistic_id154878_einwohnerzahl-in-baden-wuerttemberg-bis-2022.csv'
civ_ba = 'data_exploration/Daten/inhabitants/statistic_id154879_einwohnerzahl-in-bayern-bis-2022.csv'
civ_ber = 'data_exploration/Daten/inhabitants/statistic_id154880_einwohnerzahl-in-berlin-bis-2022.csv'
civ_bburg = 'data_exploration/Daten/inhabitants/statistic_id155142_einwohnerzahl-in-brandenburg-bis-2022.csv'
civ_br = 'data_exploration/Daten/inhabitants/statistic_id155144_einwohnerzahl-in-bremen--bundesland--bis-2022.csv'
civ_ham = 'data_exploration/Daten/inhabitants/statistic_id155147_einwohnerzahl-in-hamburg-bis-2022.csv'
civ_hes = 'data_exploration/Daten/inhabitants/statistic_id155150_einwohnerzahl-in-hessen-bis-2022.csv'
civ_mp = 'data_exploration/Daten/inhabitants/statistic_id155151_einwohnerzahl-in-mecklenburg-vorpommern-bis-2022.csv'
civ_ns = 'data_exploration/Daten/inhabitants/statistic_id155154_einwohnerzahl-in-niedersachsen-bis-2022.csv'
civ_nrw = 'data_exploration/Daten/inhabitants/statistic_id155156_einwohnerzahl-in-nordrhein-westfalen-bis-2022.csv'
civ_rp = 'data_exploration/Daten/inhabitants/statistic_id155158_einwohnerzahl-in-rheinland-pfalz-bis-2022.csv'
civ_saa = 'data_exploration/Daten/inhabitants/statistic_id155163_einwohnerzahl-im-saarland-bis-2022.csv'
civ_s = 'data_exploration/Daten/inhabitants/statistic_id155167_einwohnerzahl-in-sachsen-bis-2022.csv'
civ_sa = 'data_exploration/Daten/inhabitants/statistic_id155169_einwohnerzahl-in-sachsen-anhalt-bis-2022.csv'
civ_sh = 'data_exploration/Daten/inhabitants/statistic_id155171_einwohnerzahl-in-schleswig-holstein-bis-2022.csv'
civ_t = 'data_exploration/Daten/inhabitants/statistic_id155172_einwohnerzahl-in-thueringen-bis-2022.csv'

# %%

df_civ_ba = process_csv_data(civ_ba, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                             column_names=["Jahr", "Einwohner"])
set_name(df_civ_ba, "df_civ_ba")

df_civ_bawu = process_csv_data(civ_bawu, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                               column_names=["Jahr", "Einwohner"])
set_name(df_civ_bawu, "df_civ_bawu")

df_civ_ber = process_csv_data(civ_ber, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                              column_names=["Jahr", "Einwohner"])
set_name(df_civ_ber, "df_civ_ber")

df_civ_br = process_csv_data(civ_br, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                             column_names=["Jahr", "Einwohner"])
set_name(df_civ_br, "df_civ_br")

df_civ_bburg = process_csv_data(civ_bburg, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                                column_names=["Jahr", "Einwohner"])
set_name(df_civ_bburg, "df_civ_bburg")
fill_up_strings(df_civ_bburg, "Einwohner", 6)

df_civ_hes = process_csv_data(civ_hes, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                              column_names=["Jahr", "Einwohner"])
set_name(df_civ_hes, "df_civ_hes")

df_civ_mp = process_csv_data(civ_mp, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                             column_names=["Jahr", "Einwohner"])
set_name(df_civ_mp, "df_civ_mp")
fill_up_strings(df_civ_mp, "Einwohner", 6)

df_civ_ns = process_csv_data(civ_ns, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                             column_names=["Jahr", "Einwohner"])
set_name(df_civ_ns, "df_civ_ns")

df_civ_nrw = process_csv_data(civ_nrw, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                              column_names=["Jahr", "Einwohner"])
set_name(df_civ_nrw, "df_civ_nrw")

df_civ_rp = process_csv_data(civ_rp, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                             column_names=["Jahr", "Einwohner"])
set_name(df_civ_rp, "df_civ_rp")

df_civ_saa = process_csv_data(civ_saa, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                              column_names=["Jahr", "Einwohner"])
set_name(df_civ_saa, "df_civ_saa")

df_civ_s = process_csv_data(civ_s, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                            column_names=["Jahr", "Einwohner"])
set_name(df_civ_s, "df_civ_s")
fill_up_strings(df_civ_s, "Einwohner", 6)

df_civ_sa = process_csv_data(civ_sa, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                             column_names=["Jahr", "Einwohner"])
set_name(df_civ_sa, "df_civ_sa")

df_civ_t = process_csv_data(civ_t, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                            column_names=["Jahr", "Einwohner"])
set_name(df_civ_t, "df_civ_t")
fill_up_strings(df_civ_t, "Einwohner", 6)

df_civ_ham = process_csv_data(civ_ham, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                              column_names=["Jahr", "Einwohner"])
set_name(df_civ_ham, "df_civ_ham")

df_civ_sh = process_csv_data(civ_sh, skip_rows=4, skip_first_columns=1, skip_last_rows=2,
                             column_names=["Jahr", "Einwohner"])
set_name(df_civ_sh, "df_civ_sh")

# Dictionary with Federal States Abbrevations and Federal State Names
bundeslaender = {
    "ba": "Bayern",
    "bawu": "Baden-Wuerttemberg",
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
    "t": "Thueringen",
    "ham": "Hamburg",
    "sh": "Schleswig-Holstein",
}

# list of all datasets with population development data
datasets_civ = [
    df_civ_ba,
    df_civ_bawu,
    df_civ_ber,
    df_civ_br,
    df_civ_bburg,
    df_civ_hes,
    df_civ_mp,
    df_civ_ns,
    df_civ_nrw,
    df_civ_rp,
    df_civ_saa,
    df_civ_s,
    df_civ_sa,
    df_civ_t,
    df_civ_ham,
    df_civ_sh,
]

# %%
# Add Federal State in own column to datasets in lists of datasets
add_bundesland(datasets_civ, bundeslaender)

# %%
# Merge all the datasets in the lists from above into one dataset for each list
df_civ = pd.concat(datasets_civ, ignore_index=True)

# %%
# Converting numeral-values in columns into int64 format in population development dataset
df_civ['Einwohner'] = df_civ['Einwohner'].str.replace('.', '')
df_civ_cols = {'Jahr', 'Einwohner'}
conversion_dict = {col: 'int64' for col in df_civ_cols}
df_civ = df_civ.astype(conversion_dict)

# %%
plot_percentage_over_years(df_civ,
                           title='Population Development Over the Years (1961-2022) for Each Bundesland',
                           y_name='Einwohner', plot_filename="population")

# %%
# Adding mean, median and std to the population development dataset, rent index dataset, unemployment rate dataset
df_civ = add_mean_median_std(df_civ, 'Einwohner', 'Jahr')
df_civ.to_csv(f"data_exploration/Daten/inhabitants/bevoelkerungsentwicklung.csv", index=True)

# %%
# Exporting datasets as jsons
df_civ.to_json(f"data_exploration/Daten/jsons/population_development.json", index=True, orient="table", force_ascii=False)
