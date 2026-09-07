from pathlib import Path

from src.data.loader import load_invoice_data
from src.data.cleaner import (
    standardize_column_names,
    validate_invoice_data,
    remove_unusable_columns,
    standardize_date_columns,
    validate_date_quality,
    compare_document_and_posting_dates,
    investigate_secondary_document_dates,
    remove_redundant_columns,
    investigate_invoice_identifiers,
    remove_duplicate_records,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "src"
    / "data"
    / "raw"
    / "customer_invoices"
    / "dataset.csv"
)

def main():
    # ---------------------------------------------------------
    # 1. Load raw data
    # ---------------------------------------------------------
    df = load_invoice_data(DATA_PATH)

    print(f"Loaded dataset: {df.shape}")

    # ---------------------------------------------------------
    # 2. Validate raw data
    # ---------------------------------------------------------
    validate_invoice_data(df)

    print("Dataset validation passed.")

    # ---------------------------------------------------------
    # 3. Standardize column names
    # ---------------------------------------------------------
    cleaned_df = standardize_column_names(df)

    print("\nStandardized columns:")
    print(cleaned_df.columns.tolist())

    # ---------------------------------------------------------
    # 4. Remove unusable columns
    # ---------------------------------------------------------
    columns_to_remove = [
        "area_business",
        "posting_id",
    ]

    cleaned_df = remove_unusable_columns(cleaned_df, columns_to_remove=columns_to_remove,)

    print("\nDataset shape after removing unusable columns:")
    print(cleaned_df.shape)

    print("\nRemaining columns:")
    print(cleaned_df.columns.tolist())

    # ---------------------------------------------------------
    # 5. Standardize date columns
    # ---------------------------------------------------------

    cleaned_df = standardize_date_columns(cleaned_df)

    print("\nDate column data types:")

    date_columns = [
        "posting_date",
        "document_create_date",
        "document_create_date_secondary",
        "due_in_date",
        "baseline_create_date",
        "clear_date",
    ]

    print(cleaned_df[date_columns].dtypes)

    print("\nDate column missing values:")

    print(
        cleaned_df[date_columns]
        .isna()
        .sum()
    )

    print("\nDate samples:")

    print(
        cleaned_df[date_columns]
        .head()
        .to_string(index=False)
    )

    # ---------------------------------------------------------
    # 6. Validate date quality
    # ---------------------------------------------------------

    validate_date_quality(cleaned_df)


    # ---------------------------------------------------------
    # 7. Compare document and posting dates
    # ---------------------------------------------------------    

    compare_document_and_posting_dates(cleaned_df)

    # ---------------------------------------------------------
    # 8. Investigate secondary document dates
    # --------------------------------------------------------- 

    mismatches = investigate_secondary_document_dates(cleaned_df)

    print("\nRows where secondary document dates differs:")
    print(mismatches)

    # ---------------------------------------------------------
    # 9. Remove redundant columns
    # --------------------------------------------------------- 

    columns_to_remove = [
        "document_create_date_secondary"
    ]
    # cleaned_df = remove_redundant_columns(cleaned_df, columns_to_remove=columns_to_remove)
    cleaned_df = remove_unusable_columns(cleaned_df, columns_to_remove=columns_to_remove,)

    print("\nDataset shape after removing redundant columns:")
    print(cleaned_df.shape)

    print("\nRemaining columns:")
    print(cleaned_df.columns.tolist())

    # ---------------------------------------------------------
    # 10. Investigate Invoice identifiers
    # --------------------------------------------------------- 

    investigate_invoice_identifiers(cleaned_df)

    # ---------------------------------------------------------
    # 11. Remove duplicate records from dataset
    # --------------------------------------------------------- 

    print("Shape before deduplication:", cleaned_df.shape)

    cleaned_df = remove_duplicate_records(cleaned_df)

    print("Shape after deduplication:", cleaned_df.shape)

    print("Shape")

    # ---------------------------------------------------------
    # 12. Remove invoice_id column from dataset as doc_id and 
    # invoice_id represent the same identifier in this dataset, 
    # and doc_id is the more complete field.
    # --------------------------------------------------------- 
    columns_to_remove = ["invoice_id"]

    cleaned_df = remove_unusable_columns(cleaned_df, columns_to_remove=columns_to_remove,)

    print("\nDataset shape after removing redundant columns:")
    print(cleaned_df.shape)

    print("\nRemaining columns:")
    print(cleaned_df.columns.tolist())

if __name__ == "__main__":
    main()

