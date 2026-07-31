"""
Dataset Evaluation Module

This module provides utilies for:

1. Inspecting dataset metadata.
2. Scoring candidate datasets.
3. Ranking datasets for selection.

As the project evolves, this module will support 
automatic scoring based on dataset profiling
"""


from dataclasses import dataclass 
from src.constants import DatasetStatus
from src.data.dataset_catalog import DatasetInfo


@dataclass
class DatasetScore:
    """
    Stores the evaluation score for a dataset.
    """

    business_relevance_score: int
    feature_completeness_score: int
    data_quality_score: int
    scalability_score: int
    licensing_score: int
    overall_recommendation: str

    @property
    def total_score(self) -> int:
        """
        Return the total weighted score.
        """

        return (
            self.business_relevance_score
            + self.feature_completeness_score
            + self.data_quality_score
            + self.scalability_score
            + self.licensing_score
        )
    
def inspect_dataset(dataset: DatasetInfo) -> dict:
    """
    Returns factual metadata about a dataset.

    Returns a dictionary that can later be expanded into 
    a weighted scoring framework.
    No scoring or business judgement is performed here.
    """

    return {
        "name": dataset.name,
        "domain": dataset.domain,
        "description": dataset.description,
        "estimated_rows": dataset.estimated_rows is not None,
        "has_target": dataset.target_column is not None,
        "target_column": dataset.target_column,
        "license": dataset.license,
        "status": dataset.status.value,
        "priority": dataset.priority,
        "notes": dataset.notes
    }
    
def score_dataset(dataset: DatasetInfo) -> DatasetScore:
    """
    Perform an initial qualitative evaluation of a dataset.
    
    Version 1: 
        Placeholder evaluation.

    Future versions will calculate scores automatically
    based on dataset profiling and business rules.
    """

    return DatasetScore(
        business_relevance_score = 0,
        feature_completeness_score = 0,
        data_quality_score = 0,
        scalability_score = 0,
        licensing_score = 0,
        overall_recommendation = "Not Evaluated"
    )