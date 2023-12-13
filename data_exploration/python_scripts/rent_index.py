# %%
from data_exploration.python_scripts.functions import *

# %%
rent_ba = 'data_exploration/Daten/rent_development/statistic_id975191_index-der-nettokaltmieten-fuer-bayern-bis-2022.csv'
rent_bawu = 'data_exploration/Daten/rent_development/statistic_id975192_index-der-nettokaltmieten-fuer-baden-wuerttemberg-bis-2022.csv'
rent_ber = 'data_exploration/Daten/rent_development/statistic_id975194_index-der-nettokaltmieten-fuer-berlin-bis-2022.csv'
rent_br = ('data_exploration/Daten/rent_development/statistic_id975195_index-der-nettokaltmieten-fuer-bremen-bis-2022'
           '.csv')
rent_bburg = 'data_exploration/Daten/rent_development/statistic_id975198_index-der-nettokaltmieten-fuer-brandenburg-bis-2022.csv'
rent_hes = 'data_exploration/Daten/rent_development/statistic_id975199_index-der-nettokaltmieten-fuer-hessen-bis-2022.csv'
rent_mp = 'data_exploration/Daten/rent_development/statistic_id975203_index-der-nettokaltmieten-fuer-mecklenburg-vorpommern-bis-2022.csv'
rent_ns = 'data_exploration/Daten/rent_development/statistic_id975204_index-der-nettokaltmieten-fuer-niedersachsen-bis-2022.csv'
rent_nrw = 'data_exploration/Daten/rent_development/statistic_id975205_index-der-nettokaltmieten-fuer-nordrhein-westfalen-bis-2022.csv'
rent_rp = 'data_exploration/Daten/rent_development/statistic_id975207_index-der-nettokaltmieten-fuer-rheinland-pfalz-bis-2022.csv'
rent_saa = 'data_exploration/Daten/rent_development/statistic_id975212_index-der-nettokaltmieten-fuer-das-saarland-bis-2022.csv'
rent_s = 'data_exploration/Daten/rent_development/statistic_id975214_index-der-nettokaltmieten-fuer-sachsen-bis-2022.csv'
rent_sa = 'data_exploration/Daten/rent_development/statistic_id975215_index-der-nettokaltmieten-fuer-sachsen-anhalt-bis-2022.csv'
rent_t = 'data_exploration/Daten/rent_development/statistic_id975216_index-der-nettokaltmieten-fuer-thueringen-bis-2022.csv'
rent_ham = 'data_exploration/Daten/rent_development/statistic_id975217_index-der-nettokaltmieten-fuer-hamburg-bis-2022.csv'
rent_sw = 'data_exploration/Daten/rent_development/statistic_id1028723_index-der-nettokaltmieten-fuer-schleswig-holstein-bis-2022.csv'
rent_de = 'data_exploration/Daten/rent_development/statistic_id70132_wohnungsmietindex-fuer-deutschland-bis-2022.csv'
# %%
df_rent_ba = process_csv_data(rent_ba, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_ba, "df_rent_ba")

df_rent_bawu = process_csv_data(rent_bawu, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_bawu, "df_rent_bawu")

df_rent_ber = process_csv_data(rent_ber, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_ber, "df_rent_ber")

df_rent_br = process_csv_data(rent_br, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_br, "df_rent_br")

df_rent_bburg = process_csv_data(rent_bburg, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_bburg, "df_rent_bburg")

df_rent_hes = process_csv_data(rent_hes, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_hes, "df_rent_hes")

df_rent_mp = process_csv_data(rent_mp, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_mp, "df_rent_mp")

df_rent_ns = process_csv_data(rent_ns, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_ns, "df_rent_ns")

df_rent_nrw = process_csv_data(rent_nrw, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_nrw, "df_rent_nrw")

df_rent_rp = process_csv_data(rent_rp, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_rp, "df_rent_rp")

df_rent_saa = process_csv_data(rent_saa, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_saa, "df_rent_saa")

df_rent_s = process_csv_data(rent_s, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_s, "df_rent_s")

df_rent_sa = process_csv_data(rent_sa, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_sa, "df_rent_sa")

df_rent_t = process_csv_data(rent_t, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_t, "df_rent_t")

df_rent_ham = process_csv_data(rent_ham, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_ham, "df_rent_ham")

df_rent_sh = process_csv_data(rent_sw, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_sh, "df_rent_sh")
df_rent_de = process_csv_data(rent_de, skip_rows=4, skip_first_columns=1, column_names=["Jahr", "Index"])
set_name(df_rent_de, "df_rent_de")

# %%

# list of all datasets with rent-index data
datasets_rent = [
    df_rent_ba,
    df_rent_bawu,
    df_rent_ber,
    df_rent_br,
    df_rent_bburg,
    df_rent_hes,
    df_rent_mp,
    df_rent_ns,
    df_rent_nrw,
    df_rent_rp,
    df_rent_saa,
    df_rent_s,
    df_rent_sa,
    df_rent_t,
    df_rent_ham,
    df_rent_sh,
    df_rent_de
]

# %%
# Add Federal State in own column to datasets in lists of datasets
add_bundesland(datasets_rent, bundeslaender)

# %%
# Merge all the datasets in the lists from above into one dataset for each list
df_rent = pd.concat(datasets_rent, ignore_index=True)

# %%
# VISUALIZATION
plot_percentage_over_years(df_rent,
                           title='Percentage of Index-linked Rent Over the Years (2006-2022) for Each Bundesland',
                           y_name='Index', plot_filename="rent")

# %%
# Adding mean, median and std to the population development dataset, rent index dataset, unemployment rate dataset
#df_rent = add_mean_median_std(df_rent, 'Index', 'Jahr')

# exporting dataset as csv file
df_rent.to_csv(f"data_exploration/Daten/mietindex/mietindex.csv", index=True)

# exporting dataset as json
df_rent.to_json(f"data_exploration/Daten/jsons/index_rent_development.json", index=True, orient="table",
                force_ascii=False)
