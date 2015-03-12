# -*- coding: utf-8 -*-
'''
Created on fevr. 2015

@author: sd-libre
'''

from setuptools import setup
from lucterios.standard import __version__

setup(
    name="Lucterios_standard",
    version=__version__,
    author="Lucterios",
    author_email="support@lucterios.org",
    url="http://www.lucterios.org",
    description="Standard application for Lucterios.",
    long_description="""
    Standard application for Lucterios.
    """,
    include_package_data=True,
    platforms=('Any',),
    license="GNU General Public License v2",
    # Packages
    packages=["lucterios", "lucterios.standard"],
    package_data={
       "lucterios.standard":['build', 'logo.gif', 'locale/*/*/*', 'help/*'],
    },
    install_requires=["Lucterios >=2.0b1"],
)
