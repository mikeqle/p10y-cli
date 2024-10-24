# setup.py
from setuptools import setup, find_packages

setup(
    name='p10y',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        p10y=p10y.cli:cli
    ''',
    author='Mike Le',
    author_email='your.email@example.com',
    description='A versatile personal productivity CLI tool with multiple utilities.',
    url='https://github.com/mikeqle/p10y',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)