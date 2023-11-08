"""Transform.py - Module for data transformation utilities."""

from typing import List, Union

import pandas as pd


def concat_data_frames(
    data_frame_list: List[pd.DataFrame],
) -> Union[pd.DataFrame, None]:
    """Concatenate Dataframes.

    Concatenate a list of pandas DataFrames into a single DataFrame.

    Args:
        data_frame_list (List[pd.DataFrame]): List of DataFrames to concatenate.

    Returns
    -------
        pd.DataFrame: The concatenated DataFrame if the list is not empty, None otherwise.

    """
    if not data_frame_list:  # Verifica se a lista está vazia
        print("The provided list of DataFrames is empty.")
        return None

    try:
        # Concatena os DataFrames, ignorando os índices originais.
        return pd.concat(data_frame_list, ignore_index=True)
    except ValueError as e:
        # Tratamento de exceções para lidar com erros durante a concatenação.
        print(f"An error occurred while concatenating DataFrames: {e}")
        return None
