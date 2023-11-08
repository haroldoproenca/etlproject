"""Module for extracting data from Excel files into pandas DataFrames."""

import glob
import os
from typing import List

import pandas as pd

# Constante para o caminho do diretório de entrada dos arquivos Excel.
INPUT_PATH = "../../data/input"


def extract_dataframes_from_excel(input_path: str) -> List[pd.DataFrame]:
    """Read all Excel files.

    Read all Excel files in a given directory and return a list of DataFrames.

    Args:
        input_path (str): The path to the directory containing Excel files.

    Returns
    -------
        List[pd.DataFrame]: A list of DataFrames, each representing an Excel file.

    """
    # Constrói o caminho de busca e encontra todos os arquivos Excel no diretório.
    excel_files = glob.glob(os.path.join(input_path, "*.xlsx"))
    # Usa compreensão de lista para ler cada arquivo Excel e coletá-los em uma lista.
    try:
        data_frames = [pd.read_excel(file) for file in excel_files]
    except Exception as e:
        # Tratamento de exceções para lidar com erros ao ler os arquivos Excel.
        print(f"An error occurred: {e}")
        data_frames = []

    return data_frames


if __name__ == "__main__":
    # Chama a função e imprime os DataFrames extraídos.
    extracted_data_frames = extract_dataframes_from_excel(INPUT_PATH)
    for df in extracted_data_frames:
        print(df)
