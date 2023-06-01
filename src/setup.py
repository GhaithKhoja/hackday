"""
hackday python package configuration.
"""

from setuptools import setup

setup(
    name='hackday',
    version='0.1.0',
    packages=['hackday'],
    include_package_data=True,
    install_requires=[
        'bs4',
        'Flask',
        'requests',
    ],
    python_requires='>=3.8',
)
