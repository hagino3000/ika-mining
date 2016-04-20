import os
from setuptools import setup, find_packages

version = '0.0.1'
name = 'ika-mining'
short_description = 'ika'

setup(
    name=name,
    version=version,
    author='',
    author_email="",
    description=short_description,
    install_requires=open('requirements.txt').read().splitlines(),
    url='',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
