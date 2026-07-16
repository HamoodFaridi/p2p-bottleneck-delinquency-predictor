"""
Project-wide constants
"""

from enum import Enum


class DatasetStatus(str, Enum):
    CANDIDATE: "Candidate"
    SELECTED: "Selected"
    REJECTED: "Rejected"