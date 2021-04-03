"""Common utils for the project"""
from pathlib import Path


def get_project_root() -> Path:
    """Get project root path"""
    return Path(__file__).parent.parent