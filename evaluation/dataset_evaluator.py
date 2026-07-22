from dataclasses import dataclass 
from src.data.dataset_catalog import DatasetInfo


@dataclass
class DatasetScore:
    """
    Stores the evaluation score for a dataset.
    """

    business_relevance: int
    feature_completeness: int
    data_quality: int
    scalability: int
    licensing: int

    @property
    def total_score(self) -> int:
        """
        Return the total weighted score.
        """

        return (
            self.business_relevance
            + self.feature_completeness
            + self.data_quality
            + self.scalability
            + self.licensing
        )
    
def inspect_dataset(dataset: DatasetInfo) -> dict:
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
    
def score_dataset(dataset: DatasetInfo) -> DatasetScore:
    """
    Placeholder evaluation.

    Scores will become data driven as we analyze 
    real datasets.
    """

    return DatasetScore(
        business_relevance = 0,
        feature_completeness = 0,
        data_quality = 0,
        scalability = 0,
        licensing = 0
    )