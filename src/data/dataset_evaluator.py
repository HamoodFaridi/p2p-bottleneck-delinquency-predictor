"""
Dataset evaluation utilities

This module contains helper functions for comparing candidate datasets.
"""

from src.data.dataset_catalog import DatasetInfo


def evaluate_dataset(dataset: DatasetInfo) -> dict:
    """
    Perform an initial qualitative evaluation of a dataset.

    Returns a dictionary that can later be expanded into 
    a weighted scoring framework.
    """

    return {
        "name": dataset.name,
        "has_target": dataset.target_column is not None,
        "known_size": dataset.estimated_rows is not None,
        "license": dataset.license,
        "status": dataset.status.value
    }
