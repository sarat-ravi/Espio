#!/usr/bin/env python
# -----------------------------------------------------------------------------------------------
#
#  setup.py - Python script to build the project
#
#  Created by Sarat Tallamraju
#
# -----------------------------------------------------------------------------------------------

import sys
import os
from setuptools import setup

# PACKAGE CONFIGURATION
# -----------------------------------------------------------------------------------------------
PACKAGE_NAME = "espio"
DESCRIPTION = "import agent; agent.spy()"
VERSION = "0.0.1" 

def find_packages():
    packages = []
    packages.append("espio")
    packages.append("espio.agents")
    packages.append("espio.handlers")
    packages.append("espio.common")
    return packages

# SETUP 
# -----------------------------------------------------------------------------------------------

setup(name = PACKAGE_NAME,
        version = VERSION,
        package_dir = {'espio': 'lib'},
        packages = find_packages(),
        description = DESCRIPTION,
        scripts = [
            'espio-manage',
            ],
        )



