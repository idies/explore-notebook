#coding: utf-8
#!/usr/bin/env python import *

from SciServer import Authentication, LoginPortal
'''
python file containing miscellaneous functions
this file can be accessed by all other display functions
'''
try:
    token=Authentication.getToken()
    if token is None:
        mv.Auth()
except (NameError, TypeError) as e:
    print(str(e)+" Please verify your credentials and try again")
    mv.Auth()
else:
    token = Authentication.getToken()
    
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
        token=Authentication.login(auth_username,auth_pass)
    except (ValueError, TypeError) as e:
        print(str(e) + "Please verify your username and password and try again")
        Auth()
    else:
        token=Authentication.getToken()
        return 0
    

def display_image(ra=197.614455635, dec=18.438168849):
    ra1=ra; dec1=dec
    pixel_scale=0.2
    img = SkyServer.getJpegImgCutout(ra=ra1, dec=dec1, scale = pixel_scale) 
    #plt.savefig(plt.imshow(img), bbox_inches='tight')
    #img, (a, b) = plt.subplots()
    fig=plt.imshow(img, interpolation = 'nearest')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    #fig.set_axisbelow(True)
    #plt.yaxis.grid(linestyle='dashed')
    #plt.grid(b=True, which='major', axis='both', ls='-')
    plt.show()
        
