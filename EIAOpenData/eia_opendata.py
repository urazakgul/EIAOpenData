import requests
import pandas as pd

class EIAOpenDataError(Exception):
    """
    Custom exception for EIAOpenData class errors.
    """
    pass

class EIAOpenData:
    """
    A class for retrieving data from the EIA (Energy Information Administration) API.
    """
    def __init__(self, api_key):
        """
        Initializes the EIAOpenData class.

        :param api_key: Your EIA API key.
        """
        if not api_key:
            error_msg = "API key is required. Please provide your EIA API key. Visit https://www.eia.gov/opendata/ to get one."
            raise EIAOpenDataError(error_msg)
        self.api_key = api_key
        self.base_url = "https://api.eia.gov/v2/"

    def build_url(self, route, data_param, frequency=None, start_date=None, end_date=None):
        """
        Builds the URL for the API request.

        :param route: The target route for the API request.
        :param data_param: The data parameter to include in the URL.
        :param frequency: The frequency parameter to include in the URL (e.g., "monthly").
        :param start_date: The start date in a valid date format (e.g., "2005-03").
        :param end_date: The end date in a valid date format (e.g., "2022-11").
        :return: The constructed URL.
        """
        url = f"{self.base_url}{route}/data?api_key={self.api_key}&data[0]={data_param}"
        if frequency:
            url += f"&frequency={frequency}"
        if start_date:
            url += f"&start={start_date}"
        if end_date:
            url += f"&end={end_date}"
        return url

    def get_data(self, route, data_param, frequency=None, start_date=None, end_date=None):
        """
        Fetches data from the API.

        :param route: The target route for the API request.
        :param data_param: The data parameter to include in the URL.
        :param frequency: The frequency parameter to include in the URL (e.g., "monthly").
        :param start_date: The start date in a valid date format (e.g., "2005-03").
        :param end_date: The end date in a valid date format (e.g., "2022-11").
        :return: DataFrame.
        """

        route = route.strip('/')

        url = self.build_url(route, data_param, frequency, start_date, end_date)

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                df = pd.DataFrame(data['response']['data'])
                return df
            else:
                error_msg = f"Error: {response.status_code} - {response.text}"
                raise EIAOpenDataError(error_msg)
        except Exception as e:
            error_msg = f"An error occurred: {e}"
            raise EIAOpenDataError(error_msg)

    def filter_and_select_columns(self, df, filter_columns=None, filter_values=None, selected_columns=None):
        """
        Filters a DataFrame by specific columns and their corresponding values, and selects columns.

        :param df: DataFrame to filter.
        :param filter_columns: List of column names to filter.
        :param filter_values: List of filter values corresponding to the filter_columns.
        :param selected_columns: List of column names to select.
        :return: Filtered DataFrame with selected columns.
        """

        filtered_df = df.copy()

        if filter_columns is not None and filter_values is not None:
            if not isinstance(filter_columns, list) or not isinstance(filter_values, list):
                raise ValueError("'filter_columns' and 'filter_values' must be lists.")

            if len(filter_columns) != len(filter_values):
                raise ValueError("'filter_columns' and 'filter_values' must have the same number of elements.")

            for column, value in zip(filter_columns, filter_values):
                filtered_df = filtered_df[filtered_df[column] == value]

        if selected_columns is not None:
            if not isinstance(selected_columns, list):
                raise ValueError("'selected_columns' must be a list.")
            else:
                filtered_df = filtered_df[selected_columns]

        return filtered_df

    def save_to_excel(self, df, file_name):
        """
        Saves a DataFrame to an Excel file with .xlsx extension.

        :param df: DataFrame to save.
        :param file_name: Name of the Excel file (without the .xlsx extension).
        :return: True if the DataFrame is saved successfully, False otherwise.
        """
        if isinstance(df, pd.DataFrame) and not df.empty:
            try:
                file_name = f"{file_name}.xlsx"
                df.to_excel(file_name, index=False)
                return True
            except Exception as e:
                raise EIAOpenDataError(f"An error occurred while saving the DataFrame to Excel: {e}")
        else:
            raise EIAOpenDataError("DataFrame is empty or not provided. Nothing to save to Excel.")