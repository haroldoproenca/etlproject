# Load

Abaixo, você encontrará detalhes sobre as funções e módulos do nosso projeto.

## Módulo `consolidador`


### `load`

```python
def load(df: pd.DataFrame, output_folder: str, filename: str) -> None:
    """
    Função para carregar (ou salvar) um DataFrame em um arquivo Excel.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        output_folder (str): Diretório onde o arquivo será salvo.
        filename (str): Nome do arquivo Excel.

    Returns:
        None
    """
```

### `consolidate_excels`

```python
def consolidate_excels(input_folder: str, output_folder: str, filename: str) -> None:
    """
    Função para consolidar múltiplos arquivos Excel em um único arquivo.

    Args:
        input_folder (str): Pasta contendo arquivos Excel.
        output_folder (str): Pasta onde o arquivo consolidado será salvo.
        filename (str): Nome do arquivo Excel consolidado.

    Returns:
        None
    """
