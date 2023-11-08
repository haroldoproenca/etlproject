"""Module for unit and integration testing of the ETL project pipeline."""

import pandas as pd

from etlproject.pipeline.transform import concat_data_frames

# DataFrames de teste
df_1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
df_2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})


def test_concatenation_of_dataframe_list():
    """Test the concatenation of a list of DataFrames."""

    # Prepara os dados esperados
    expected_df = pd.DataFrame({"col1": [1, 2, 5, 6], "col2": [3, 4, 7, 8]})

    # Executa a função de concatenação
    concatenated_df = concat_data_frames([df_1, df_2])

    # Verifica se o tamanho do DataFrame resultante é o esperado
    assert concatenated_df.shape == (
        4,
        2,
    ), "The shape of the concatenated DataFrame is incorrect."

    # Verifica se os dados do DataFrame resultante são os esperados
    pd.testing.assert_frame_equal(
        concatenated_df,
        expected_df,
        "The data in the concatenated DataFrame is incorrect.",
    )
