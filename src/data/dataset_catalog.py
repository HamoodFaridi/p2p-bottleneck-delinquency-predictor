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
from typing import List


@dataclass
class DatasetInfo:
    """
    Represents metadata about a dataset.
    """

    name: str
    source: str 
    domain: str 
    description: str 
    estimated_rows: int | None 
    target_column: str | None 
    license: str 
    status: str 
    notes: str 

# Candidate datasets 
DATASETS: List[DatasetInfo] = []