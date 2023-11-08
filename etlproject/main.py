"""Main.py - Main script to run the ETL pipeline."""

from pipeline.extract import extract_dataframes_from_excel
from pipeline.load import save_dataframe_to_excel
from pipeline.transform import concat_data_frames


def main():
    """Main Function."""
    # Extrai DataFrames de arquivos Excel no diretório especificado.
    data_frame_list = extract_dataframes_from_excel("data/input")

    # Verifica se a extração retornou uma lista de DataFrames não vazia.
    if not data_frame_list:
        print("No DataFrames to process. Exiting the pipeline.")
        return

    # Concatena a lista de DataFrames em um único DataFrame.
    data_frame = concat_data_frames(data_frame_list)
    if data_frame is None:
        print("DataFrame concatenation failed. Exiting the pipeline.")
        return

    # Carrega o DataFrame concatenado em um arquivo Excel.
    try:
        save_dataframe_to_excel(data_frame, "data/output", "output")
        print("Data successfully loaded into Excel.")
    except Exception as e:
        print(f"Failed to load DataFrame into Excel: {e}")


if __name__ == "__main__":
    main()
