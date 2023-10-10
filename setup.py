# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:14:41 2023

@author: akomarla
"""

from setuptools import setup, find_packages

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ExpSmoothing", 
        version='0.0.1',
        author="Aparna Komarla",
        author_email="<aparna.komarla@email.com>",
        description='Exponential smoothing forecast model',
        long_description='Training and testing an exponential smoothing forecast model for time-series data using statistical learning',
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        licenses='MIT',
        url= 'https://github.com/akomarla/ExpSmoothing',
        keywords=['python', 'time-series'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)