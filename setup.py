#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['demjson', 'requests', 'lxml']


setuptools.setup(
    name='e_ok_api',
    version='0.1.1',
    author='dotEsuS',
    author_email='',
    description='Unofficial API wrapper for Liantis e-OK',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/dotEsuS/e_ok_api',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
        ],
    install_requires=requirements,
    license="GNU General Public License v3",
    keywords='e_ok_api',
)
