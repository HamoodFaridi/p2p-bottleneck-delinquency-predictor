"""
Data loading utilities.

Provides standard methods for loading datasets.
"""

from pathlib import Path

import pandas as pd 

def load_csv(file_path: str | Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas Dataframe.

    Parameters
    ----------
    file_path: str | Path
        Path to the CSV file.

    Returns
    -------
    pd.Dataframe
        Loaded dataset.
    """

    return pd.read_csv(file_path)