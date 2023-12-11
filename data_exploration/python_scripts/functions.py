# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
    percentage_occurrences_df.to_csv(f"data_exploration/Daten/genesis_traffic/{name}.csv", index=True)

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
        'Bundesland': ['Deutschland_mean'] * len(aggregate_values),
        target: aggregate_values[f"{target}_mean"].astype(int)
    })

    germany_median_rows = pd.DataFrame({
        helper: aggregate_values[helper],
        'Bundesland': ['Deutschland_median'] * len(aggregate_values),
        target: aggregate_values[f"{target}_median"].astype(int)
    })

    germany_std_rows = pd.DataFrame({
        helper: aggregate_values[helper],
        'Bundesland': ['Deutschland_std'] * len(aggregate_values),
        target: aggregate_values[f"{target}_std"].astype(int)
    })

    dataframe = pd.concat([dataframe, germany_median_rows, germany_mean_rows, germany_std_rows], ignore_index=True)

    return dataframe


# %%

def set_first_row_as_header(dataframe):
    dataframe.columns = dataframe.iloc[0]
    dataframe = dataframe[1:]

    return dataframe


# %%
def get_EW(year, bundesland, pandas_df, target):
    val = pandas_df.loc[(pandas_df["Jahr"] == year) & (pandas_df["Bundesland"] == bundesland), target].iloc[0]
    return val
