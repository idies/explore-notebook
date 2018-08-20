# coding: utf-8
#!/usr/bin/env python

'''
Python file that contains all the packages needed to execute the explore tool.
It's all in one file so that importing modules runs smoother.
'''

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
from SciServer import Config, Authentication, SkyServer, SkyQuery, CasJobs
import argparse
import html
from IPython.display import HTML
'''Data Release version is currently set to DR14. DR15 rolls out 11/2018'''
data_release="DR14"
