# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:14:41 2023

@author: akomarla
"""

from setuptools import setup, find_packages
from pathlib import Path

# Getting directory info
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Setting up
setup(
        name="ExpSmoothing", 
        version='0.1.5',
        author="Aparna Komarla",
        author_email="<aparna.komarla@email.com>",
        description='Exponential smoothing forecast model',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(include = ['ExpSmoothing', 'ExpSmoothing.*']),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        licenses='MIT',
        url= 'https://github.com/akomarla/ExpSmoothing',
        keywords=['python', 'time-series', 'forecasting', 'exponential smoothing', 'error metrics'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)