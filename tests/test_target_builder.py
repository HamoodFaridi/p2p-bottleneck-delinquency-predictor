import pandas as pd
import pytest 
from src.features.target_builder import (
    split_closed_and_open_invoices,
    build_targets,
)

def create_test_invoice_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "posting_date": pd.to_datetime(
                [
                    "2020-01-01",
                    "2020-01-05",
                    "2020-01-10",
                ]
            ),
            "due_in_date": pd.to_datetime(
                [
                    "2020-01-10",
                    "2020-01-15",
                    "2020-01-20",
                ]
            ),
            "clear_date": pd.to_datetime(
                [
                    "2020-01-08",
                    "2020-01-20",
                    None,
                ]
            ),
        }
    )


def test_split_closed_and_open_invoices():
    df = create_test_invoice_data()

    closed_df, open_df = split_closed_and_open_invoices(df)

    assert len(closed_df) == 2
    assert len(open_df) == 1

    assert closed_df["clear_date"].notna().all()
    assert open_df["clear_date"].isna().all()


def test_build_targets():
    df = create_test_invoice_data()

    closed_df, _ = split_closed_and_open_invoices(df)

    required_columns = [
        "clear_date",
        "due_in_date",
        "posting_date",
    ]

    target_df = build_targets(closed_df, required_columns)

    assert target_df["days_late"].tolist() == [-2, 5]
    assert target_df["is_delayed"].tolist() == [0, 1]
    assert target_df["days_to_payment"].tolist() == [7, 15]


def test_build_targets_requires_required_columns():
    df = pd.DataFrame(
        {
            "posting_date": pd.to_datetime(
                ["2020-01-01"]
            ),
            "clear_date": pd.to_datetime(
                ["2020-01-10"]
            ),
        }
    )

    required_columns = [
        "clear_date",
        "due_in_date",
        "posting_date",
    ]
    with pytest.raises(
        ValueError,
        match = "Missing required columns",
    ): 
        build_targets(df, required_columns)