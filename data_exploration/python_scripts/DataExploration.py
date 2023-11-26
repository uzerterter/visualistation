# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
##############################################PATHS OF THE DATASETS#####################################################
genesis = 'Daten/genesis_traffic/genesis_traffic.csv'
income2021 = ('Daten/income/statistic_id209211_bruttomonatsverdienst-nach-bundeslaendern-und-geschlecht-in-deutschland'
              '-2021.csv')
income2016 = ('Daten/income/statistic_id806476_median-des-bruttomonatsverdienstes-von-maennern-und-frauen-nach'
              '-bundeslaendern-2016.csv')
unemployment_sh = 'Daten/unemployment/statistic_id2509_arbeitslosenquote-in-schleswig-holstein-bis-2022.csv'
unemployment_ham = 'Daten/unemployment/statistic_id2510_arbeitslosenquote-in-hamburg-bis-2022.csv'
unemployment_ns = 'Daten/unemployment/statistic_id2511_arbeitslosenquote-in-niedersachsen-bis-2022.csv'
unemployment_br = 'Daten/unemployment/statistic_id2512_arbeitslosenquote-in-bremen-bis-2022.csv'
unemployment_nrw = 'Daten/unemployment/statistic_id2513_arbeitslosenquote-in-nordrhein-westfalen-bis-2022.csv'
unemployment_hes = 'Daten/unemployment/statistic_id2514_arbeitslosenquote-in-hessen-bis-2022.csv'
unemployment_rp = 'Daten/unemployment/statistic_id2515_arbeitslosenquote-in-rheinland-pfalz-bis-2022.csv'
unemployment_bawu = 'Daten/unemployment/statistic_id2516_arbeitslosenquote-in-baden-wuerttemberg-bis-2022.csv'
unemployment_ba = 'Daten/unemployment/statistic_id2517_arbeitslosenquote-in-bayern-bis-2022.csv'
unemployment_saa = 'Daten/unemployment/statistic_id2518_arbeitslosenquote-im-saarland-bis-2022.csv'
unemployment_ber = 'Daten/unemployment/statistic_id2519_arbeitslosenquote-in-berlin-bis-2022.csv'
unemployment_bburg = 'Daten/unemployment/statistic_id2520_arbeitslosenquote-in-brandenburg-bis-2022.csv'
unemployment_mp = 'Daten/unemployment/statistic_id2521_arbeitslosenquote-in-mecklenburg-vorpommern-bis-2022.csv'
unemployment_s = 'Daten/unemployment/statistic_id2522_arbeitslosenquote-in-sachsen-bis-2022.csv'
unemployment_sa = 'Daten/unemployment/statistic_id2523_arbeitslosenquote-in-sachsen-anhalt-bis-2022.csv'
unemployment_t = 'Daten/unemployment/statistic_id2524_arbeitslosenquote-in-thueringen-bis-2022.csv'

rent_ba = 'Daten/rent_development/statistic_id975191_index-der-nettokaltmieten-fuer-bayern-bis-2022.csv'
rent_bawu = 'Daten/rent_development/statistic_id975192_index-der-nettokaltmieten-fuer-baden-wuerttemberg-bis-2022.csv'
rent_ber = 'Daten/rent_development/statistic_id975194_index-der-nettokaltmieten-fuer-berlin-bis-2022.csv'
rent_br = 'Daten/rent_development/statistic_id975195_index-der-nettokaltmieten-fuer-bremen-bis-2022.csv'
rent_bburg = 'Daten/rent_development/statistic_id975198_index-der-nettokaltmieten-fuer-brandenburg-bis-2022.csv'
rent_hes = 'Daten/rent_development/statistic_id975199_index-der-nettokaltmieten-fuer-hessen-bis-2022.csv'
rent_mp = 'Daten/rent_development/statistic_id975203_index-der-nettokaltmieten-fuer-mecklenburg-vorpommern-bis-2022.csv'
rent_ns = 'Daten/rent_development/statistic_id975204_index-der-nettokaltmieten-fuer-niedersachsen-bis-2022.csv'
rent_nrw = 'Daten/rent_development/statistic_id975205_index-der-nettokaltmieten-fuer-nordrhein-westfalen-bis-2022.csv'
rent_rp = 'Daten/rent_development/statistic_id975207_index-der-nettokaltmieten-fuer-rheinland-pfalz-bis-2022.csv'
rent_saa = 'Daten/rent_development/statistic_id975212_index-der-nettokaltmieten-fuer-das-saarland-bis-2022.csv'
rent_s = 'Daten/rent_development/statistic_id975214_index-der-nettokaltmieten-fuer-sachsen-bis-2022.csv'
rent_sa = 'Daten/rent_development/statistic_id975215_index-der-nettokaltmieten-fuer-sachsen-anhalt-bis-2022.csv'
rent_t = 'Daten/rent_development/statistic_id975216_index-der-nettokaltmieten-fuer-thueringen-bis-2022.csv'
rent_ham = 'Daten/rent_development/statistic_id975217_index-der-nettokaltmieten-fuer-hamburg-bis-2022.csv'
rent_sw = 'Daten/rent_development/statistic_id1028723_index-der-nettokaltmieten-fuer-schleswig-holstein-bis-2022.csv'

civ_bawu = 'Daten/inhabitants/statistic_id154878_einwohnerzahl-in-baden-wuerttemberg-bis-2022.csv'
civ_ba = 'Daten/inhabitants/statistic_id154879_einwohnerzahl-in-bayern-bis-2022.csv'
civ_ber = 'Daten/inhabitants/statistic_id154880_einwohnerzahl-in-berlin-bis-2022.csv'
civ_bburg = 'Daten/inhabitants/statistic_id155142_einwohnerzahl-in-brandenburg-bis-2022.csv'
civ_br = 'Daten/inhabitants/statistic_id155144_einwohnerzahl-in-bremen--bundesland--bis-2022.csv'
civ_ham = 'Daten/inhabitants/statistic_id155147_einwohnerzahl-in-hamburg-bis-2022.csv'
civ_hes = 'Daten/inhabitants/statistic_id155150_einwohnerzahl-in-hessen-bis-2022.csv'
civ_mp = 'Daten/inhabitants/statistic_id155151_einwohnerzahl-in-mecklenburg-vorpommern-bis-2022.csv'
civ_ns = 'Daten/inhabitants/statistic_id155154_einwohnerzahl-in-niedersachsen-bis-2022.csv'
civ_nrw = 'Daten/inhabitants/statistic_id155156_einwohnerzahl-in-nordrhein-westfalen-bis-2022.csv'
civ_rp = 'Daten/inhabitants/statistic_id155158_einwohnerzahl-in-rheinland-pfalz-bis-2022.csv'
civ_saa = 'Daten/inhabitants/statistic_id155163_einwohnerzahl-im-saarland-bis-2022.csv'
civ_s = 'Daten/inhabitants/statistic_id155167_einwohnerzahl-in-sachsen-bis-2022.csv'
civ_sa = 'Daten/inhabitants/statistic_id155169_einwohnerzahl-in-sachsen-anhalt-bis-2022.csv'
civ_sh = 'Daten/inhabitants/statistic_id155171_einwohnerzahl-in-schleswig-holstein-bis-2022.csv'
civ_t = 'Daten/inhabitants/statistic_id155172_einwohnerzahl-in-thueringen-bis-2022.csv'


##############################################PATHS OF THE DATASETS#####################################################
# %%
def count_NaNs_and_export(column_list, NaN_values_list, dataframe, name):
    """
    Counts occurrences and calculates percentages of specified NaN values in the given DataFrame columns.

    Parameters:
    - column_list (list): List of column names in the DataFrame to analyze.
    - NaN_values_list (list): List of NaN values to count occurrences and calculate percentages for.
    - dataframe (pd.DataFrame): The DataFrame to analyze.
    - name (str): The name used for exporting the results to a CSV file.

    Returns:
    - pd.DataFrame: A DataFrame containing the counts and percentages of NaN values in each specified column.
                   The DataFrame is also exported to a CSV file with the given 'name'.
    """

    columns = ['Column'] + [f"Occurrences of {value}" for value in NaN_values_list] + [f"Percentage of {value}" for
                                                                                       value in NaN_values_list]
    percentage_occurrences_df = pd.DataFrame(columns=columns)

    data_to_concat = []

    for col in column_list:
        row_data = {'Column': col}
        for value in NaN_values_list:
            count_value = (dataframe[col] == value).sum()
            percentage_value = count_value / len(dataframe[col]) * 100
            row_data[f"Occurrences of {value}"] = count_value
            row_data[f"Percentage of {value}"] = round(percentage_value, 2)

        data_to_concat.append(row_data)

        percentage_occurrences_df = pd.concat([pd.DataFrame([row_data]) for row_data in data_to_concat],
                                              ignore_index=True)
    percentage_occurrences_df.to_csv(f"Daten/{name}.csv", index=True)

    return percentage_occurrences_df


# %%
def process_csv_data(csv_data, skip_last_rows=0, skip_first_columns=0, skip_last_columns=0, column_names=[],
                     skip_rows=0):
    """
    Process CSV data and create a DataFrame with specified configurations.

    Parameters:
    - csv_data (str): The CSV data or the path to the CSV file to be processed.
    - skip_last_rows (int): Number of rows to skip from the end of the CSV data.
    - skip_first_columns (int): Number of columns to skip from the beginning of the CSV data.
    - skip_last_columns (int): Number of columns to skip from the end of the CSV data.
    - column_names (list): List of column names to use for the DataFrame.
    - skip_rows (int): Number of rows to skip from the beginning of the CSV data.

    Returns:
    - pd.DataFrame: A DataFrame containing the processed CSV data based on the specified configurations.
    """

    csv_data = csv_data.replace(',"', ',').replace('",', ',')
    dataframe = pd.read_csv(csv_data, delimiter=',', thousands=None, decimal=',', skiprows=skip_rows)

    if skip_last_rows > 0:
        dataframe = dataframe.iloc[:-skip_last_rows, :]
    if skip_first_columns > 0:
        dataframe = dataframe.iloc[:, skip_first_columns:]
    if skip_last_columns > 0:
        dataframe = dataframe.iloc[:, :-skip_last_columns]

    dataframe.columns = column_names

    return dataframe


# %%

def set_name(df, name):
    """
    Set a name attribute for a pandas DataFrame.

    Parameters:
    - df (pd.DataFrame): The pandas DataFrame to which the name attribute will be assigned.
    - name (str): The name to be assigned to the DataFrame.

    Returns:
    None
    """
    df.name = name


# %%

def fill_up_strings(dataframe, column_name, target_length):
    """
    Fill up string values in a column by left-padding or appending ".000".

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing the column to be modified.
    - column_name (str): The name of the column to be modified.
    - target_length (int): The target length for the strings.

    Returns:
    - pd.DataFrame: The modified DataFrame.
    """

    dataframe[column_name] = dataframe[column_name].apply(
        lambda x: x if len(str(x)) > target_length else str(x) + ".000"
    )

    return dataframe


# %%
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
################################################  READING IN DATASETS   ################################################
brutto_income_2021 = pd.read_csv(income2021, sep=",")
set_name(brutto_income_2021, "brutto_income_2021")

brutto_income_2016 = pd.read_csv(income2016, sep=",")
set_name(brutto_income_2016, "brutto_income_2016")

# %%
df_unemployment_sh = process_csv_data(unemployment_sh, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                      column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_sh, "df_unemployment_sh")

df_unemployment_ham = process_csv_data(unemployment_ham, skip_rows=4, skip_last_rows=2, skip_first_columns=1,
                                       column_names=["Jahr", "Prozent"], skip_last_columns=1)
set_name(df_unemployment_ham, "df_unemployment_ham")

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

################################################  READING IN DATASETS   ################################################

# %%
################################################  PREPROCESSING   ######################################################

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

# list of all datasets with unemployment data
datasets_unemployment = [
    df_unemployment_sh,
    df_unemployment_ham,
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
]

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
]

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

def add_bundesland(dataset_list, bundeslaender_dict):
    """
    Add a 'Bundesland' column to each DataFrame in the given list based on a provided dictionary.

    Parameters:
    - dataset_list (list): List of pandas DataFrames to which the 'Bundesland' column will be added.
    - bundeslaender_dict (dict): Dictionary mapping the last part of DataFrame names to corresponding 'Bundesland' values.

    Returns:
    None
    """
    for dataset in dataset_list:
        df_bundesland = dataset.name.split('_')[-1]
        dataset['Bundesland'] = bundeslaender_dict[df_bundesland]


# %%
# Add Federal State in own column to datasets in lists of datasets
# 1. Population Development
# 2. Unemplyoment Development
# 3. Rent-Index Development
add_bundesland(datasets_civ, bundeslaender)
add_bundesland(datasets_unemployment, bundeslaender)
add_bundesland(datasets_rent, bundeslaender)

# %%
# Merge all the datasets in the lists from above into one dataset for each list
df_unemployment = pd.concat(datasets_unemployment, ignore_index=True)
df_rent = pd.concat(datasets_rent, ignore_index=True)
df_civ = pd.concat(datasets_civ, ignore_index=True)

# %%
# Converting numeral-values in columns into int64 format in unemployment dataset
df_unemployment_cols = {'Jahr'}
conversion_dict = {col: 'int64' for col in df_unemployment_cols}
df_unemployment = df_unemployment.astype(conversion_dict)

# %%
# Converting numeral-values in columns into int64 format in population development dataset
df_civ['Einwohner'] = df_civ['Einwohner'].str.replace('.', '')
df_civ_cols = {'Jahr', 'Einwohner'}
conversion_dict = {col: 'int64' for col in df_civ_cols}
df_civ = df_civ.astype(conversion_dict)

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
################################################ VISUALIZATION #########################################################

def plot_percentage_over_years(dataframe, title='', y_name='', plot_filename=None):
    """
        Plot percentage data over the years for different Bundesländer (states).

        Parameters:
        - dataframe (pd.DataFrame): The input DataFrame containing the data to be plotted.
        - title (str, optional): Title for the plot. Defaults to an empty string.
        - y_name (str): The column name representing the variable to be plotted on the y-axis.
        - plot_filename (str, optional): If provided, the plot will be saved to this file. Defaults to None.

        Returns:
        - None: Displays the plot using Matplotlib.

        Note:
        - This function uses Seaborn and Matplotlib for plotting.
        - The input DataFrame should have columns 'Jahr' (Year), 'Bundesland' (State), and 'Einwohner' (Population).
        - The plot is a bar plot with years on the x-axis, population on the y-axis, and different states represented by colors.
        - The legend is placed to the right of the plot.
        - The plot can be saved to a file if 'plot_filename' is provided.
    """

    sns.set(style="whitegrid")

    plt.figure(figsize=(35, 15))

    sns.barplot(x='Jahr', y=y_name, hue='Bundesland', data=dataframe)
    sns.despine(left=True)

    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Einwohner')
    plt.ticklabel_format(style='plain', axis='y')

    plt.legend(title='Bundesland', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=90)
    plt.tight_layout()
    if plot_filename:
        plt.savefig(plot_filename, bbox_inches='tight')

    plt.show()


# %%

plot_percentage_over_years(df_unemployment,
                           title='Percentage of Unemployment Rates Over the Years (1994-2022) for Each Bundesland',
                           y_name='Prozent', plot_filename="unemployment")

# %%

plot_percentage_over_years(df_rent,
                           title='Percentage of Index-linked Rent Over the Years (2006-2022) for Each Bundesland',
                           y_name='Index', plot_filename="rent")

# %%
plot_percentage_over_years(df_civ,
                           title='Population Development Over the Years (1961-2022) for Each Bundesland',
                           y_name='Einwohner', plot_filename="population")


################################################ VISUALIZATION #########################################################
# %%
def add_mean_median_std(dataframe, target, helper):
    """
    Add mean, median, and standard deviation values to the DataFrame based on a grouping variable.

    Parameters:
    - dataframe (pd.DataFrame): The input DataFrame to which statistics will be added.
    - target (str): The column name representing the variable for which statistics will be calculated.
    - helper (str): The column name used for grouping the data.

    Returns:
    - pd.DataFrame: A new DataFrame with additional rows representing mean, median, and standard deviation values.

    Notes:
    - This function groups the DataFrame by the 'helper' column and calculates mean, median, and standard deviation
      for the 'target' column within each group.
    - Three new rows are added to the DataFrame for each group, representing the mean, median, and standard deviation.
    - The 'Bundesland' column is set to 'Deutschland mean', 'Deutschland median', and 'Deutschland std' for the added rows.
    - The resulting DataFrame includes the original data and the added mean, median, and standard deviation rows.
    """
    aggregate_values = dataframe.groupby(helper)[target].agg(['mean', 'median', 'std']).reset_index()
    aggregate_values.columns = [f"{helper}", f"{target}_mean", f"{target}_median", f"{target}_std"]

    germany_mean_rows = pd.DataFrame({
        helper: aggregate_values[helper],
        'Bundesland': ['Deutschland mean'] * len(aggregate_values),
        target: aggregate_values[f"{target}_mean"].astype(int)
    })

    germany_median_rows = pd.DataFrame({
        helper: aggregate_values[helper],
        'Bundesland': ['Deutschland median'] * len(aggregate_values),
        target: aggregate_values[f"{target}_median"].astype(int)
    })

    germany_std_rows = pd.DataFrame({
        helper: aggregate_values[helper],
        'Bundesland': ['Deutschland std'] * len(aggregate_values),
        target: aggregate_values[f"{target}_std"].astype(int)
    })

    dataframe = pd.concat([dataframe, germany_median_rows, germany_mean_rows, germany_std_rows], ignore_index=True)

    return dataframe


# %%
# Adding mean, median and std to the population development dataset, rent index dataset, unemployment rate dataset
df_civ = add_mean_median_std(df_civ, 'Einwohner', 'Jahr')
df_rent = add_mean_median_std(df_rent, 'Index', 'Jahr')
df_unemployment = add_mean_median_std(df_unemployment, 'Prozent', 'Jahr')

df_rent.to_csv(f"Daten/mietindex.csv", index=True)
df_unemployment.to_csv(f"Daten/arbeitslosenquote.csv", index=True)
df_civ.to_csv(f"Daten/bevoelkerungsentwicklung.csv", index=True)

# %%
# Exporting datasets as jsons
df_civ.to_json(f"Daten/population_development.json", index=True, orient="table", force_ascii=False)
df_rent.to_json(f"Daten/index_rent_development.json", index=True, orient="table", force_ascii=False)
df_unemployment.to_json("Daten/unemployment_rate.json", index=True, orient="table", force_ascii=False)

# %%
# Deleting Währung column in income dataset
brutto_income_2016.drop([' Währung'], axis=1, inplace=True)
brutto_income_2021.drop([' Währung'], axis=1, inplace=True)

brutto_income_2021['Jahr'] = [2021]*len(brutto_income_2021)
brutto_income_2016['Jahr'] = [2016]*len(brutto_income_2016)

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

df_income.to_csv(f"Daten/income.csv", index=True)
df_income.to_json(f"Daten/income.json", index=True, orient="table", force_ascii=False)

# %%
############################################### GENESIS TRAFFIC DATASET ################################################
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
final_genesis_traffic.to_csv(f"Daten/final_genesis_traffic.csv", index=True)

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
    {'Jahr': germany_df['Jahr'], 'Art': 'Nahverkehr insgesamt',
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
    {'Jahr': germany_df['Jahr'], 'Art': 'Nahverkehr insgesamt',
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

# Save the final DataFrame to a CSV file
final_genesis_traffic.to_csv(f"Daten/final_genesis_traffic.csv", index=True)

# Save the final DataFrame to a JSON file using table orientation
final_genesis_traffic.to_json(f"Daten/final_genesis_traffic.json", index=True, orient="table", force_ascii=False)

############################################### GENESIS TRAFFIC DATASET ################################################
