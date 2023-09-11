# EIAOpenData v0.1.1

## Description

`EIAOpenData` is a Python package that provides easy access to various energy-related data obtained from the Energy Information Administration (EIA) API.

*** WARNING ***

To get your API key, please visit: https://www.eia.gov/opendata/

### Supported Categories

This package provides access to a wide range of energy-related data categories, including:

* Coal
* Crude Oil Imports
* Electricity
* International
* Natural Gas
* Nuclear Outages
* Petroleum
* State Energy Data System (SEDS)
* Short Term Energy Outlook
* Densified Biomass
* Total Energy
* Annual Energy Outlook
* International Energy Outlook
* State CO2 Emissions

## Installation

Follow the steps below to use the library:

1. Install Python on your system: https://www.python.org/downloads/
2. Open the terminal and run the following command to install the package:

```bash
pip install EIAOpenData
```

If you want to install a specific version, you can run the command as in the example below.

```bash
pip install EIAOpenData==0.1.1
```

You can find the version of the installed package with the following command.

```bash
pip show EIAOpenData
```

## Usage

### Importing the Library

```python
from EIAOpenData import EIAOpenData
```

### The EIAOpenData Class and Its Methods:

#### `EIAOpenData`

This class is designed for retrieving data from the EIA (Energy Information Administration) API.

* Description: Initializes the EIAOpenData class with your EIA API key.
* Parameters:
  * `api_key` (str): Your EIA API key. It is required to make API requests.

`get_data(route, data_param, frequency=None, start_date=None, end_date=None, facet_name=None, facet_values=None)`

* Description: Fetches data from the API.
* Parameters:
  * `route` (str): The target route for the API request (e.g., "petroleum/crd/crpdn").
  * `data_param` (str): The data parameter to include in the URL (e.g., "value").
  * `frequency` (str, optional): The frequency parameter to include in the URL (e.g., "monthly").
  * `start_date` (str, optional): The start date in a valid date format (e.g., "2005-03").
  * `end_date` (str, optional): The end date in a valid date format (e.g., "2022-11").
  * `facet_name` (str, optional): The facet name to filter the data (e.g., "product").
  * `facet_values` (list, optional): The facet values to filter the data (e.g., ["EPC0"]).
* Returns: DataFrame.

`filter_and_select_columns(df, filter_columns=None, filter_values=None, selected_columns=None)`

* Description: Filters a DataFrame by specific columns and their corresponding values, and selects columns.
* Parameters:
  * `df` (Pandas DataFrame): DataFrame to filter.
  * `filter_columns` (list, optional): List of column names to filter.
  * `filter_values` (list, optional): List of filter values corresponding to the filter_columns.
  * `selected_columns` (list, optional): List of column names to select.
* Returns: Filtered DataFrame with selected columns.

`save_to_excel(df, file_name)`

* Description: Saves a DataFrame to an Excel file with a .xlsx extension.
* Parameters:
  * `df` (Pandas DataFrame): DataFrame to save.
  * `file_name` (str): Name of the Excel file (without the .xlsx extension).
* Returns: True if the DataFrame is saved successfully, False otherwise.

### Examples

```python
my_api_key = 'your_api_key' # Replace 'your_api_key' with your actual API key.
eia = EIAOpenData(my_api_key) # Initialize EIAOpenData with your API key.

# Visit the EIA Open Data API Dashboard: https://www.eia.gov/opendata/

# Select your desired dataset and parameters from the API Dashboard.
# For example, let's choose "Petroleum/Imports/Exports And Movements/Weekly Imports & Exports."

# Examine the URL of the selected dataset. An example URL might look like this:
# https://www.eia.gov/opendata/browser/petroleum/move/wkly?frequency=weekly&data=value;&sortColumn=period;&sortDirection=desc;

# By inspecting the URL, you can determine the appropriate values for 'route' and 'data_param.'
# In the example URL above:
# - 'route' can be set to 'petroleum/move/wkly' based on the path in the URL.
# - 'data_param' can be set to 'value' based on the 'data' parameter in the URL.

# Optionally, you can further customize your data retrieval by specifying:
# - 'frequency' to set the desired data frequency (e.g., 'weekly', 'monthly', 'annual').
# - 'start_date' to specify the beginning date for the data you want to retrieve.
# - 'end_date' to specify the end date for the data you want to retrieve.
# - 'facet_name' to define the facet by which you want to filter the data.
# - 'facet_values' to specify the values within the chosen facet by which to filter the data.

# Define the API route for fetching data related to weekly petroleum imports and exports.
# Adjust this value according to the dataset path from the URL.
# You can add a "/" at the beginning and/or end.
route = 'petroleum/move/wkly'

# Define the data parameter that specifies what type of data to retrieve.
# Adjust this value based on the 'data' parameter from the URL.
data_param = 'value'

# Specify the data retrieval parameters.
frequency='four-week-average' # Data frequency.
start_date='2018-01-01' # Start date for data retrieval.
end_date='2023-08-25' # End date for data retrieval.

# Specify the facet parameters for data filtering.
facet_name = 'product' # Name of the facet to filter by.
facet_values = ['EPC0','EPJK'] # Values to filter within the facet.

# Fetch data from the EIA API
my_data = eia.get_data(
  route,
  data_param,
  frequency=frequency,
  start_date=start_date,
  end_date=end_date,
  facet_name=facet_name,
  facet_values=facet_values
)

# Save the retrieved data to an Excel file named 'my_data'
eia.save_to_excel(my_data, 'my_data')

# Filter the data to select only records where 'product-name' is 'Crude Oil'
# and select columns 'period', 'product-name', and 'value'
my_new_data = eia.filter_and_select_columns(
  my_data,
  filter_columns=['product-name'],
  filter_values=['Crude Oil'],
  selected_columns=['period', 'product-name', 'value']
)

# Save the filtered and selected data to an Excel file named 'my_new_data'
eia.save_to_excel(my_new_data, 'my_new_data')
```

## Notes

* The EIAOpenData library relies on data from the Energy Information Administration (EIA). To ensure the accuracy and continuity of the data, please check the relevant website: [The U.S. Energy Information Administration Open Data](https://www.eia.gov/opendata/). You can visit the EIA's official website to verify the data and stay updated on any changes or updates to their datasets.
* I welcome your feedback for the development and improvement of the library. Contribute to the GitHub repo: [GitHub Repo](https://github.com/urazakgul/EIAOpenData)
* Please report any issues or suggestions by opening a new issue in the "Issue" section of the GitHub repo: [GitHub Issues](https://github.com/urazakgul/EIAOpenData/issues)

## Release Notes

### v0.1.0 - 02/09/2023

* First version released.

### v0.1.1 - 12/09/2023

* Added the ability to customize data retrieval by specifying `facet_name` and `facet_values` parameters for more precise filtering of dataset facets.

## License

This project is licensed under the MIT License.