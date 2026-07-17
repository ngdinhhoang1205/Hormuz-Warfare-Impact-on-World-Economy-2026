import pandas as pd
from dbnomics import fetch_series


def fetch_imf_data(country_dict, metric_suffix="PCPI_IX", frequency="M"):
    """Fetch macroeconomic data from the IMF via DBnomics for multiple countries.

    Parameters:
    -----------
    country_dict : dict
        A dictionary containing country codes (keys) and display names (values).
        Example: {"VN": "Vietnam", "US": "United States"}
    metric_suffix : str, optional
        The IMF metric code. Default is 'PCPI_IX' (Consumer Price Index).
        Can be changed to other codes such as 'NGDP_XDC' (Nominal GDP).
    frequency : str, optional
        Data frequency: 'M' (Monthly), 'Q' (Quarterly), 'A' (Annual). Default is 'M'.

    Returns:
    --------
    pd.DataFrame
        A merged DataFrame containing data for all successfully fetched countries.
    """
    all_dfs = []

    for code, country_name in country_dict.items():
        series_id = f"IMF/CPI/{frequency}.{code}.{metric_suffix}"

        try:
            df = fetch_series(series_id)
            df["country_name"] = country_name
            df["country_code"] = code
            all_dfs.append(df)
        except Exception as e:
            print(f"Error {country_name} ({series_id}): {e}")

    if all_dfs:
        return pd.concat(all_dfs, ignore_index=True)
    else:
        print("No data was successfully loaded.")
        return pd.DataFrame()