from tsportfolio.environment import package_version


def test_package_version_for_installed_package():
    assert package_version("numpy") != "not installed"


def test_package_version_for_missing_package():
    assert package_version("definitely-not-a-real-package") == "not installed"
