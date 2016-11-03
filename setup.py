#!/usr/bin/env python
from setuptools import setup

setup(name='ag_frame',
      version='0.1',
      description='Genetic Algorithms',
      author='Micu Matei-Marius',
      author_email='micumatei@gmail.com',
      license='MIT',
      packages=['ag_frame'],
      entry_points = {
        'console_scripts': ['ag_frame=ag_frame.command_line:main'],
      },
      zip_safe=False)
