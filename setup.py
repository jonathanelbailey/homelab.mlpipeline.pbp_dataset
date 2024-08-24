from setuptools import setup, find_packages

requirements = [
  'clearml',
  'nfl-data-py',
  'pandas'
]

setup(
    name='pbp-data-import',
    version='0.0.1',
    author='Jonathan Bailey',
    author_email='jonathan@jelbailey.com',
    description='Import Play-by-Play Data from nfl_data_py',
    entrypointts={
        'console_scripts': [
            'dataset-cli=src.import_pbp_data:main'
        ]
    },
    packages=find_packages(exclude=['tests']),
    install_requires=requirements
)