from setuptools import find_packages, setup

requirements = ["clearml", "nfl-data-py", "pandas", "numpy<2.0.0"]

dev_requirements = ["pre-commit", "black", "flake8", "isort"]

setup(
    name="pbp-data-import",
    version="0.0.1",
    author="Jonathan Bailey",
    author_email="jonathan@jelbailey.com",
    description="Import Play-by-Play Data from nfl_data_py",
    entry_points={"console_scripts": ["pbp-data-import = src.import_pbp_data:main"]},
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
)
