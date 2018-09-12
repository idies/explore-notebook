#coding: utf-8
#!/usr/bin/env python import *
import getpass
from imports import *

'''
python file containing miscellaneous functions
this file can be accessed by all other display functions
'''

def get_radec_obj(objid):
    
    
    x=pd.DataFrame(index=[0], columns=["N","V"])
    x["N"]=pd.Series([], dtype=str)
    x["V"]=pd.Series([], dtype=object)
    sql_query="select * from FIRST where objID= " +str(objid)
    x=CasJobs.executeQuery(sql=sql_query, context=data_release, format="pandas") 
    if (x.empty):
        print("There are currently no objects with this object ID. Please verify your input an try again")
        raise ValueError
        
    ra=format(x[0]['ra'],'f')
    dec=format([0]['dec'],'f')
    return((ra),(dec))
    
def get_radec_spec(specid):
    x=pd.DataFrame(index=[0], columns=["N","V"])
    x["N"]=pd.Series([], dtype=str)
    x["V"]=pd.Series([], dtype=object)
    sql_query='Select ra,dec from SpecObjAll where specObjID='+str(specid)
    x=CasJobs.executeQuery(sql=sql_query, context=data_release, format="pandas") 
    if(x.empty):
        print("There are currently no objects with this optical spetcral ID. Please verify your input an try again")
        raise ValueError
    ra=format(x[0]['ra'],'f')
    dec=format([0]['dec'],'ra')
    return((ra),(dec))


def get_objid(ra=197.614455635, dec=18.438168849):
    '''
    Returns:: big int object_id from given ra and dec of the object
    input(optional):: ra(right ascension), dec(declination)
    param:: 'x' is a pandas data frame used to store query values
    '''
    try:
        
        if(ra is 197.614455635 and dec is 18.438168849): 
            print("default specs displayed")
        else: 
            pass
        
        x=pd.DataFrame(index=[0], columns=["N","V"])
        x["N"]=pd.Series([], dtype=str)
        x["V"]=pd.Series([], dtype=object)

        sql_query="select * from fGetNearestObjIdEq(" +str(ra)+ "," +str(dec)+ ",0.2)"
        x=CasJobs.executeQuery(sql=sql_query, context=data_release, format="pandas")
        objid=format(x.iloc[0]['objID'],'f')
        if (bool(objid) is False):
            raise ValueError("No object id found. Please verify argument parameters and try again")
            pass
        else:
            return objid

    except (NameError,ValueError,TimeoutError) as e:
        print(str(e)+ "occured. Please verify your values and try again")

def get_specid(ra=197.614455635 , dec=18.438168849):
    '''
    Derives spectral id when just ra and dec are available
    Returns:: big int specid storing the IR and optical spectrum values for the chosen object
    input(optional):: ra(right ascension), dec(declination) of the celestial body in question; both initialized to 0
    param:: 'x' is a pandas data frame used to store query values
    '''
    try:

       
        if (ra is 0 and dec is 0):
            print("Missing: function arguments(ra,dec)")
            return 0
        elif (ra is 197.614455635 and dec is 18.438168849):
            print("Invalid input argument. Display: Default object specs displayed")
            return ((2947691243863304192.0))
        else:
            x=pd.DataFrame(index=[0], columns=["N","V"])
            x["N"]=pd.Series([], dtype=str)
            x["V"]=pd.Series([], dtype=object)

            sql_query="select * from fGetNearestSpecObjIdAllEq(" + str(ra) + "," + str(dec)+  ", 0.2)"
            x=CasJobs.executeQuery(sql=sql_query, context=data_release, format='pandas')
            specid=format(x.iloc[0]['specObjID'],'f')
#             specid=x.iloc[0]['specObjID'] 
        if (bool(specid) is False):
            raise ValueError("No spectrum id found. Please verify argument parameters and try again")
            pass
        else:
            return specid
    except (NameError,ValueError,TimeoutError) as e:
        print(str(e)+ "has occurred. Please verify your values and try again")

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
        return 2
    

def display_obj_image(ra=197.614455635 , dec=18.438168849):
    try:
        
        if(ra is 0 and dec is 0):
            print("Missing: function arguments(ra,dec)")
            return 0
        elif (ra is 197.614455635 and dec is 18.438168849):
            print("Invalid input argument. Display: Default object specs")    
            pass
        else:
            pass
        
        ra1=ra; dec1=dec;
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
    except:
        print("Unexpected Error. Pleae try again")
    
def view(df):
    css = """<style>
    table { border-collapse: collapse; border: 3px solid #eee; }
    table tr th:first-child { background-color: #eee; color: #333; font-weight: bold }
    table thead th { background-color: #eee; color: #000; }
    tr, th, td { border: 1px solid #ccc; border-width: 1px 0 0 1px; border-collapse: collapse;
    padding: 3px; font-family: monospace; font-size: 10px }</style>
    """
    s  = '<script type="text/Javascript">'
    s += 'var win = window.open("", "Title", "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=780, height=200, top="+(screen.height-400)+", left="+(screen.width-840));'
    s += 'win.document.body.innerHTML = \'' + (df.to_html() + css).replace("\n",'\\') + '\';'
    s += '</script>'

    return(HTML(s+css))
        
