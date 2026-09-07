"""
Utilities for validating and cleaning invoice data
"""

from typing import List
import pandas as pd 

def validate_required_columns(
        df: pd.DataFrame,
        required_columns: List[str],
) -> None:
    """
    Validate that required columns exist in the dataset.

    Parameters
    ----------
    df: pd.DataFrame
        Input dataset.

    required_columns: list[str]
        Columns required by the pipeline.

    Raises
    ------
    ValueError
        If oen or more required colummns are missing.
    """

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )
    

def validate_dataset_not_empty(
        df: pd.DataFrame
) -> None:
    """
    Validate that the dataset contains atleast one row.

    Parameters
    ----------
    df: pd.DataFrame
        Input dataset.

    Raises
    ------
    ValueError
        If dataset contains zero rows.
    """

    if df.empty:
        raise ValueError("Dataset is empty.")
    

def validate_invoice_data(
        df: pd.DataFrame
) -> None:
    """
    Run basic validation checks on the invoice dataset.

    Parameters
    ----------
    df: pd.DataFrame
        Input invoice dataset
    """

    required_columns = [
        "business_code",
        "cust_number",
        "clear_date",
        "posting_date",
        "due_in_date",
        "total_open_amount",
        "cust_payment_terms",
        "isOpen",
    ]

    validate_dataset_not_empty(df)

    validate_required_columns(df, required_columns)


def standardize_column_names(
        df: pd.DataFrame
) -> pd.DataFrame:
    """
    Standardize dataset column names.

    The function:
    - Converts column names to lowercase.
    - Replaces spaces with underscores.
    - Corrects known spelling inconsistencies.
    - Renames ambiguous duplicate columns.

    Parameters
    ----------
    df: pd.DataFrame
        Input dataset.
    
    Returns
    -------
    pd.DataFrame
        Dataset with standardize column names.
    """

    cleaned_df = df.copy()

    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    column_renames = {
        "buisness_year": "business_year",
        "document_create_date.1": "document_create_date_secondary",
        "isopen": "isOpen",

    }

    cleaned_df = cleaned_df.rename(
        columns=column_renames
    )
    
    return cleaned_df


def remove_unusable_columns(
        df: pd.DataFrame,
        columns_to_remove: List[str],
) -> pd.DataFrame:
    """
    Remove columns that provide o useful information for the modeling.

    Currently removes:
    - area_business: 100% missing values
    - posting_id: contains only 1 unique value.

    Parameters
    ----------
    df: pd.DataFrame
        Input dataset.
    columns_to_remove: List[str]
        Input list of column names to be removed 

    Returns
    -------
    pd.DataFrame
        Dataset with unusable columns removed.
    """

    cleaned_df = df.copy()

    # columns_to_remove = [
    #     "area_business",
    #     "posting_id",
    # ]

    cleaned_df = cleaned_df.drop(
        columns=columns_to_remove,
        errors="ignore",
    )

    return cleaned_df



def convert_yyyymmdd_column(
        series: pd.Series,
) -> pd.Series:
    """
    Convert a YYYYMMDD numeric column into datetime.

    Invalid or missing values are converted to NaT
    """

    numeric_series = pd.to_numeric(
        series,
        errors="coerce",
    )

    string_series = (
        numeric_series
        .astype("Int64")
        .astype("string")
    )

    return pd.to_datetime(
        string_series,
        format="%Y%m%d",
        errors="coerce",
    )


def standardize_date_columns(
        df: pd.DataFrame,
) -> pd.DataFrame:
    """"
    Convert all invoice date columns to datetime.

    Numeric YYYYMMDD columns are explicitly parsed
    using the YYYYMMDD format.

    String-based dates are parsed using pandas'
    datetime parser.

    Missing clear_date values are preserved as NaT
    because they represent open invoices.
    """

    cleaned_df = df.copy()

    yyyymmdd_columns = [
        "document_create_date",
        "document_create_date_secondary",
        "due_in_date",
        "baseline_create_date",
    ]

    for column in yyyymmdd_columns:
        if column in cleaned_df.columns:
            cleaned_df[column] = convert_yyyymmdd_column(
                cleaned_df[column]
            )

    string_date_columns = [
        "posting_date",
        "clear_date",
    ]

    for colummn in string_date_columns:
        if colummn in cleaned_df.columns:
            cleaned_df[colummn] = pd.to_datetime(
                cleaned_df[colummn],
                errors="coerce",
            )

    return cleaned_df


def validate_date_quality(
        df: pd.DataFrame,
) -> None:
    """
    Validate basic date quality and relationships.
    """

    date_columns = [
        "posting_date",
        "document_create_date",
        "document_create_date_secondary",
        "due_in_date",
        "baseline_create_date",
        "clear_date",
    ]

    for column in date_columns:
        if column in df.columns:
            if not pd.api.types.is_datetime64_any_dtype(
                df[column]
            ):
                raise ValueError(
                    f"{column} is not a datetime column"
                )
            
    
    if "clear_date" in df.columns and "posting_date" in df.columns:
        invalid_clear_dates = (
            df["clear_date"].notna()
            & (
                df["clear_date"]
                < df["posting_date"]
            )
        )

        print(
            "\nClear date before posting date:",
            invalid_clear_dates.sum()
        )


def compare_document_and_posting_dates(
        df: pd.DataFrame
) -> None:
    """"
    Compare document creation date with posting dates.
    """

    comparison = (
        df["document_create_date_secondary"]
        == df["posting_date"]
    )

    print("\nSecondary document date vs posting date:")

    print(
        "Matching:",
        comparison.sum(),
    )

    print(
        "Different:",
        (~comparison).sum(),
    )

    print(
        "Match percentage:",
        round(comparison.mean() * 100, 3),
        "%",
    )

def investigate_secondary_document_dates(
        df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Identify rows where the secondary document ceration date
    differs from the posting date
    """

    mismatch_mask = (
        df["document_create_date_secondary"]
        != df["posting_date"]
    )

    mismatches = df.loc[
        mismatch_mask,
        [
            "business_code",
            "cust_number",
            "doc_id",
            "document_create_date",
            "document_create_date_secondary",
            "posting_date",
            "due_in_date",
            "clear_date",       
        ] ,          
    ].copy()

    return mismatches


def remove_redundant_columns(
        df: pd.DataFrame,
        columns_to_remove: List[str],
) -> pd.DataFrame:
    """
    Remove columns that are redundant or not required 
    for downstream modeling
    """

    cleaned_df = df.copy()

    # columns_to_remove = [
    #     "document_create_date_secondary"
    # ]

    cleaned_df = cleaned_df.drop(
        columns=columns_to_remove,
        errors="ignore",
    )

    return cleaned_df


def investigate_invoice_identifiers(
        df: pd.DataFrame,
) -> None:
    """
    Investigate invoice and document identifiers, including missingand duplicate values.
    """

    print("\n--- Invoice Identifier Investigation ---")

    for column in ["invoice_id", "doc_id"]:
        if column not in df.columns:
            continue
    
        print(f"\n{column}")

        print(
            "Missing:",
            df[column].isna().sum()
        )

        print(
            "Unique:",
            df[column].nunique(dropna=True)
            )
        
        print(
            "Duplicated rows:",
            df[column].duplicated(
                keep=False
            ).sum()
        )

    if "invoice_id" in df.columns:
        duplicated_invoice_ids = (
            df[
                df["invoice_id"].duplicated(
                    keep=False
                )
                & df["invoice_id"].notna()
            ]
            .sort_values("invoice_id")
        )

        print("\nDuplicate invoice_id records:")

        print(
            duplicated_invoice_ids[
                [
                    "invoice_id",
                    "doc_id",
                    "cust_number",
                    "posting_date",
                    "due_in_date",
                    "total_open_amount",
                    "isOpen",
                ]
            ].head(30)
        )



def remove_duplicate_records(
        df: pd.DataFrame
) -> pd.DataFrame:
    """
    Remove exact duplicate records from the dataset
    """

    cleaned_df = df.copy()

    cleaned_df = cleaned_df.drop_duplicates()

    return cleaned_df