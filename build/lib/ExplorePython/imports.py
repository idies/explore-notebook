# coding: utf-8
#!/usr/bin/env python

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from setuptools import setup, find_packages
setup(
    name = "SciServer",
    version = "1.10.2",
    packages = find_packages(),
)

import numpy as np
import io
from io import StringIO, BytesIO
import scipy
import pandas as pd
import skimage
import matplotlib.pyplot as plt
import matplotlib.img as imgm
import json
import warnings
import re
# import SciScript_Python
# from SciScript_Python import py3
# from SciScript_Python.py3 import SciServer
from SciServer import Config, Authentication, SkyServer, SkyQuery, CasJobs

