# coding: utf-8
#!/usr/bin/env python

import sys
import os
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
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
# import SciScript_Python
# from SciScript_Python import py3
# from SciScript_Python.py3 import SciServer
from SciServer import Config, Authentication, SkyServer, SkyQuery, CasJobs

