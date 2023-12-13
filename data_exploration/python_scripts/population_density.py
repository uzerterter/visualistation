# %%
from data_exploration.python_scripts.functions import *

# %%
# Data Paths
pd_ham = 'data_exploration/Daten/population_density/statistic_id254514_bevoelkerungsdichte-in-hamburg-bis-2022.csv'
pd_bawu = 'data_exploration/Daten/population_density/statistic_id254840_bevoelkerungsdichte-in-baden-wuerttemberg-bis-2022.csv'
pd_ba = 'data_exploration/Daten/population_density/statistic_id254957_bevoelkerungsdichte-in-bayern-bis-2022.csv'
pd_ber = 'data_exploration/Daten/population_density/statistic_id255791_bevoelkerungsdichte-in-berlin-bis-2022.csv'
pd_bburg = 'data_exploration/Daten/population_density/statistic_id256068_bevoelkerungsdichte-in-brandenburg-bis-2022.csv'
pd_br = 'data_exploration/Daten/population_density/statistic_id256231_bevoelkerungsdichte-in-bremen-bis-2022.csv'
pd_nrw = 'data_exploration/Daten/population_density/statistic_id258069_bevoelkerungsdichte-in-nordrhein-westfalen-bis-2022.csv'
pd_hes = 'data_exploration/Daten/population_density/statistic_id258107_bevoelkerungsdichte-in-hessen-bis-2022.csv'
pd_mp = 'data_exploration/Daten/population_density/statistic_id258841_bevoelkerungsdichte-in-mecklenburg-vorpommern-bis-2022.csv'
pd_rp = 'data_exploration/Daten/population_density/statistic_id274542_bevoelkerungsdichte-in-rheinland-pfalz-bis-2022.csv'
pd_s = 'data_exploration/Daten/population_density/statistic_id274543_bevoelkerungsdichte-in-sachsen-bis-2022.csv'
pd_sa = 'data_exploration/Daten/population_density/statistic_id274544_bevoelkerungsdichte-in-sachsen-anhalt-bis-2022.csv'
pd_sh = 'data_exploration/Daten/population_density/statistic_id274545_bevoelkerungsdichte-in-schleswig-holstein-bis-2022.csv'
pd_t = 'data_exploration/Daten/population_density/statistic_id274546_bevoelkerungsdichte-in-thueringen-bis-2022.csv'
pd_saa = 'data_exploration/Daten/population_density/statistic_id274547_bevoelkerungsdichte-im-saarland-bis-2022.csv'
pd_de = 'data_exploration/Daten/population_density/statistic_id440766_bevoelkerungsdichte-in-deutschland-bis-2022.csv'
pd_ns = 'data_exploration/Daten/population_density/statistic_id258893_bevoelkerungsdichte-in-niedersachsen-bis-2022.csv'

# %%
df_ham = pd.read_csv(pd_ham, delimiter=',')
set_name(df_ham, 'df_ham')
df_bawu = pd.read_csv(pd_bawu, delimiter=',')
set_name(df_bawu, 'df_bawu')
df_ba = pd.read_csv(pd_ba, delimiter=',')
set_name(df_ba, 'df_ba')
df_ber = pd.read_csv(pd_ber, delimiter=',')
set_name(df_ber, 'df_ber')
df_bburg = pd.read_csv(pd_bburg, delimiter=',')
set_name(df_bburg, 'df_bburg')
df_br = pd.read_csv(pd_br, delimiter=',')
set_name(df_br, 'df_br')
df_nrw = pd.read_csv(pd_nrw, delimiter=',')
set_name(df_nrw, 'df_nrw')
df_hes = pd.read_csv(pd_hes, delimiter=',')
set_name(df_hes, 'df_hes')
df_mp = pd.read_csv(pd_mp, delimiter=',')
set_name(df_mp, 'df_mp')
df_rp = pd.read_csv(pd_rp, delimiter=',')
set_name(df_rp, 'df_rp')
df_s = pd.read_csv(pd_s, delimiter=',')
set_name(df_s, 'df_s')
df_sa = pd.read_csv(pd_sa, delimiter=',')
set_name(df_sa, 'df_sa')
df_sh = pd.read_csv(pd_sh, delimiter=',')
set_name(df_sh, 'df_sh')
df_t = pd.read_csv(pd_t, delimiter=',')
set_name(df_t, 'df_t')
df_saa = pd.read_csv(pd_saa, delimiter=',')
set_name(df_saa, 'df_saa')
df_de = pd.read_csv(pd_de, delimiter=',')
set_name(df_de, 'df_de')
df_ns = pd.read_csv(pd_ns, delimiter=',')
set_name(df_ns, 'df_ns')

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
    "de": "Deutschland",
}

population_density_list = [
    df_ham,
    df_t,
    df_s,
    df_de,
    df_sa,
    df_saa,
    df_ba,
    df_bawu,
    df_bburg,
    df_ber,
    df_br,
    df_hes,
    df_mp,
    df_nrw,
    df_rp,
    df_sh,
    df_ns
]

# add Federal State to dataset
add_bundesland(population_density_list, bundeslaender)

# Merge all the datasets in the lists from above into one dataset for each list
df_population_density = pd.concat(population_density_list, ignore_index=True)

# %%
# drop first column because it is undefined
df_population_density = df_population_density.iloc[:, 1:]

# %%
# convert column 'Jahr' to int64
df_population_density['Jahr'] = df_population_density['Jahr'].astype(int)

# %%
# Adding mean, median and std to the population development dataset, rent index dataset, unemployment rate dataset
df_germany = df_population_density[df_population_density['Bundesland'] == 'Deutschland']
df_rest = df_population_density[df_population_density['Bundesland'] != 'Deutschland']

# %%
# Adding mean, median and std to the population development dataset, rent index dataset, unemployment rate dataset
df_rest = add_mean_median_std(df_rest, 'EW_per_sqkm', 'Jahr')

# %%
# exporting dataset as csv file
df_population_density.to_csv(f"data_exploration/Daten/population_density/bevoelkerungsdichte.csv", index=True)

# exporting dataset as json
df_population_density.to_json("data_exploration/Daten/jsons/population_density.json", index=True, orient="table", force_ascii=False)

