import os
import sys
import warnings
import getpass
from SciServer import Authentication, LoginPortal

'''Default data release version in use is set to DR14 '''

data_release="DR14"

def Auth():
	"""Validating an Authentication token for SciServer"""
	Auth_username=getpass.getpass('User Name: ');
	Auth_pass=getpass.getpass('Password: ');
	token1=Authentication.login(Auth_username,Auth_pass)
	token=Authentication.getToken()

try:
	if(Authentication.getToken==None):
		Auth()
except (TypeError, None) as e:
	print("Authentication failed. Please verify your username and password and try again.");
	Auth()
else:
	token=Authentication.getToken()
    
    
