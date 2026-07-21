"""
Dataset catalog

This module maintains metadata about all datasets evaluated for this project.

Eventually, it will also support:
- Dataset downloads
- Version tracking
- Validation
- Checksums
"""

from dataclasses import dataclass
from typing import List, Optional

from src.constants import DatasetStatus


@dataclass
class DatasetInfo:
    """
    Represents metadata about a dataset.
    """

    name: str
    source: str 
    domain: str 
    description: str 
    estimated_rows: Optional[int]
    target_column: Optional[str] 
    license: str 
    priority: int
    status: DatasetStatus
    notes: str 

    def is_selected(self) -> bool:
        """Return True if this dataset has been selected."""
        return self.status == DatasetStatus.SELECTED
    
    def summary(self) -> str:
        """Return a readable summary of the dataset."""
        return (
            f"{self.name} | "
            f"Domain: {self.domain} | "
            f"Rows: {self.estimated_rows or 'Unknown'} | "
            f"Status: {self.status.value}"

        )

# Candidate datasets 
DATASETS: List[DatasetInfo] = []