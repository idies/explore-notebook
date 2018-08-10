# coding: utf-8
#!/usr/bin/env python

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


import numpy as np
import io
from io import StringIO, BytesIO
import scipy
import pandas as pd
import skimage
import matplotlib.pyplot as plt
import matplotlib.image as imgm
import json
import warnings
import re
import SciServer
# from SciScript_Python import py3
# from SciScript_Python.py3 import SciServer
from SciServer import Config, Authentication, SkyServer, SkyQuery, CasJobs

from setuptools import setup, find_packages
setup(
    name = "ExplorePython",
    version = "2.0.0",
    packages = find_packages(),
)

