from setuptools import setup, find_packages
import re
import os

exec(open('rony/_version.py').read())

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rony',
    version=__version__,
    author='A3Data',
    author_email='rony@a3data.com.br',
    url='https://github.com/A3Data/rony',
    description='An opinionated Data Engineering framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development'
      ],
      keywords='data engineering mlops devops pipelines',
      license='Apache License 2.0',
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        rony=rony.cli:cli
    ''',
    python_requires='>=3.6'
)
