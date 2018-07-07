#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="Bili-Kits",
    version="0.0.1",
    author="JLoeve",
    author_email="jianglufull@foxmail.com",
    description="A development suite based on Python3 and the API of BiliBili",
    long_description=open("README.md",encoding='utf-8').read(),
    license="MIT",
    url="https://github.com/LonelySteve/Bili-Kits",
    packages=['bili_kits'],
    install_requires=[
        "requests"
        ],
    classifiers=[
        "Environment :: Win32 (MS Windows)",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Chinese (Simplified)",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6"
    ],
)
