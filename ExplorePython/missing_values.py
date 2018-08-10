#coding: utf-8
#!/usr/bin/env python import *

import os, sys, pandas, getpass
from SciServer import CasJobs, Authentication

'''
python file containing miscellaneous functions
this file can be accessed by all other display functions
'''
token=Authentication.getToken()

def get_objid(ra=0, dec=0):
    '''
    Returns:: big int object_id from given ra and dec of the object
    input:: ra(right ascension), dec(declination)
    param:: 'x' is a pandas data frame used to store query values
    '''
    if(ra==0 or dec==0):
        print("Missing: function arguments(ra,dec)")
        return 0
    x=pd.DataFrame(index=[0], columns=["N","V"])
    x["N"]=pd.Series([], dtype=str)
    x["V"]=pd.Series([], dtype=object)

    sql_query='select * from fGetNearestObjEq(' + str(ra) + ',' + str(dec)+ ', 0.2)'

    x=CasJobs.executeQuery(sql=sql_query, context=data_release, format='pandas')
    objid=(x.iloc[0])
    if (objid==None):
        print("No object id found. Please verify values and try again")
        return 0
    return objid

def get_specid(ra=0, dec=0):
    '''
    Derives spectral id when just ra and dec are available
    Returns:: big int specid storing the IR and optical spectrum values for the chosen object
    input:: ra(right ascension), dec(declination) of the celestial body in question; both initialized to 0
    param:: 'x' is a pandas data frame used to store query values
    '''
    if (ra==0 or dec==0):
        print("Missing: function arguments (ra,dec)")
        return 0
    x=pd.DataFrame(index=[0], columns=["N","V"])
    x["N"]=pd.Series([], dtype=str)
    x["V"]=pd.Series([], dtype=object)

    sql_query="select * from fGetNearestSpecObjEq(" + str(ra) + "," + str(dec)+  ", 0.2)"
    x=CasJobs.executeQuery(sql=sql_query, context=data_release, format='pandas')
    specid=x.iloc[0]
    if (specid==None):
        print("No spectrum id found. Please verify values and try again")
        return 0
    return specid

def Auth():
    '''
    Creates a temporary token to help access the SciServer database
    No output
    No arguments
    param:: token - SciServer login token.
    input:: auth_username, auth_password - username and password values for sciserver
    Raise:: Exception for TyperError
    '''
## Authentication token for SciServer ##
    try:
        auth_username=getpass.getpass('User Name: ')
        auth_pass=getpass.getpass('Password: ')
        token3=Authentication.login(auth_username,auth_pass)
        token=Authentication.getToken()
    except (ValueError, TypeError) as e:
        print(str(e) + "Please verify your username and password and try again")
        Auth()

    return 0
