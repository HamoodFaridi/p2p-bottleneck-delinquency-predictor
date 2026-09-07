"""
Data loading utilities.

Provides standard methods for loading datasets.
"""

from pathlib import Path
from typing import Union

import pandas as pd 

def load_invoice_data(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load the invoice raw dataset from a CSV file into a pandas Dataframe.

    Parameters
    ----------
    file_path: str | Path
        Path to the raw invoice CSV file.

    Returns
    -------
    pd.Dataframe
        Loaded dataset.
    
    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    ValueError
        If the file does not have a CSV extension.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Invoice dataset not found: {file_path}"
        )
    
    if file_path.suffix.lower() != ".csv":
        raise ValueError(
            f"Expected a CSV file, received: {file_path.suffix}"
        )
    

    return pd.read_csv(file_path)