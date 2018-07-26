import os
import sys
import warnings
import getpass

#fix authentication here so it won't be an issue later.

'''Default data release version in use is set to DR14 '''

data_release="DR14"

try:
    if(Authentication.getToken==None):
        Auth()
except (warnings.warn("Authentication Failed. Please verify your username and password")) as e:
    Auth()
else:
    token=Authentication.getToken()
    
    
def Auth():
## Authentication token for SciServer ##
    Auth_username=getpass.getpass('User Name: ')
    Auth_pass=getpass.getpass('Password: ')
    token1=Authentication.login(Auth_username,Auth_pass)
    token=Authentication.getToken()