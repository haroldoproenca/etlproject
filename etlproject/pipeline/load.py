"""Module for loading data into Excel format."""

import os
from typing import NoReturn

import pandas as pd


def save_dataframe_to_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> NoReturn:
    """Save Dataframe.

    Save a given DataFrame to an Excel file.

    Args:
        data_frame (pd.DataFrame): DataFrame to be saved to Excel.
        output_path (str): Path where the Excel file will be saved.
        file_name (str): Name of the Excel file to be saved.

    Returns
    -------
        NoReturn: This function does not return anything.

    """
    complete_path = os.path.join(output_path, f"{file_name}.xlsx")
    os.makedirs(output_path, exist_ok=True)
    with pd.ExcelWriter(complete_path, engine="openpyxl") as writer:
        data_frame.to_excel(writer, index=False)
    print("File saved successfully.")


def main() -> NoReturn:
    """Main function to demonstrate saving a DataFrame to an Excel file."""
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    save_dataframe_to_excel(df, "data/output", "test")


if __name__ == "__main__":
    main()
