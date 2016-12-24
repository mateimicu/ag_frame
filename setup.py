#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

setup(name='ag_frame',
      version='0.2',
      description='Genetic Algorithms',
      author='Micu Matei-Marius',
      author_email='micumatei@gmail.com',
      license='MIT',
      packages=find_packages(),
      entry_points = {
        'console_scripts': ['ag_frame=ag_frame.command_line:main'],
      },
      zip_safe=False)
