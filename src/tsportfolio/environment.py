"""Utilities for reporting the reproducibility environment."""

from __future__ import annotations

import importlib.metadata
import subprocess

PACKAGES = [
    "numpy",
    "pandas",
    "polars",
    "pyarrow",
    "duckdb",
    "scipy",
    "statsmodels",
    "scikit-learn",
    "matplotlib",
]


def git_output(*args: str) -> str:
    """Return output from a git command, or 'unavailable' on failure."""
    try:
        result = subprocess.run(
            ["git", *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unavailable"


def package_version(name: str) -> str:
    """Return an installed package version."""
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return "not installed"
