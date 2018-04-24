#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='meteorflux',
      description="Powers meteorflux.io.",
      author='Geert Barentsen',
      author_email='hello@geert.io',
      license='MIT',
      url='http://meteorflux.io',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['numpy',
                        'matplotlib',
                        'astropy',
                        'psycopg2',
                        'flask'],
      keywords="meteors astronomy",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Astronomy",
      ],
      )
