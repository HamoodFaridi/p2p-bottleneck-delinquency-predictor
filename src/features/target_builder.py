"""
Utilities for creating ML targets from invoice data.
"""

import pandas as pd
from typing import List

def split_closed_and_open_invoices(
        df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split invoices into open and closed populations based on clear_date.

    Closed invoices have a known payment outcome and can be used
    for model training and evaluation.

    Open invoices do not have known payment outcome and 
    are reserved for future prediction.
    """

    closed_df = df[df["clear_date"].notna()].copy()
    open_df = df[df["clear_date"].isna()].copy()

    return closed_df, open_df


def build_targets(
        closed_df: pd.DataFrame,
        required_columns: List[str],
) -> pd.DataFrame:
    """
    Create classification and regresion targets for closed invoices.

    Targets:
        days_late:
            Number of days between clear_date and due_in_date.
        
        is_delayed:
            1 when the invoice was paid after the due_date,
            Otherwise 0.
        
        days_to_payment:
            Number of days between posting_date and clear_date.
    
    The input DataFrame must contain only closed invoices.
    """

    missing_columns = [
        column
        for column in required_columns
        if column not in closed_df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns for target creation: "
            f"{missing_columns}"
        )
    
    if closed_df["clear_date"].isna().any():
            raise ValueError(
            "build targets() requires closed invoices only."
            "Found rows with missing clear_date."      
            )
    
    target_df = closed_df.copy()

    target_df["days_late"] = (
        target_df["clear_date"] - target_df["due_in_date"]
    ).dt.days

    target_df["is_delayed"] =(
        target_df["days_late"] > 0
    ).astype(int)

    target_df["days_to_payment"] = (
        target_df["clear_date"] - target_df["posting_date"]
    ).dt.days

    return target_df
                    