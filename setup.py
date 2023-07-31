#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="Log10",
    version="0.2.3",
    description="Log10 LLM data management",
    author="Log10 team",
    author_email="team@log10.io",
    url="",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
    ],
    dev_requires=[
        "chromadb"
    ],
    extras_require={
        "bigquery": ["google-cloud-bigquery"],
    },
)
