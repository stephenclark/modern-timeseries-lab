"""Report the runtime environment for reproducibility."""

from __future__ import annotations

import platform
import sys
from pathlib import Path

from tsportfolio.environment import PACKAGES, git_output, package_version


def main() -> None:
    """Print a compact project environment report."""
    repo_root = Path(__file__).resolve().parents[1]

    print("Modern Time Series Lab - Environment Report")
    print("=" * 48)
    print(f"Repository:   {repo_root}")
    print(f"Python:       {sys.version.split()[0]}")
    print(f"Executable:   {sys.executable}")
    print(f"Platform:     {platform.platform()}")
    print(f"Architecture: {platform.machine()}")
    print()
    print("Git")
    print("---")
    print(f"Branch:       {git_output('branch', '--show-current')}")
    print(f"Commit:       {git_output('rev-parse', '--short', 'HEAD')}")

    dirty = git_output("status", "--porcelain")
    print(f"Working tree: {'dirty' if dirty else 'clean'}")

    print()
    print("Key packages")
    print("------------")
    for package in PACKAGES:
        print(f"{package:<16} {package_version(package)}")


if __name__ == "__main__":
    main()
