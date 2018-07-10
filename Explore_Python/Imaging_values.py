#!/usr/bin/env python import *
Photometric values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import sys
from Image_Cut_Out import ob_id
from __main__ import *
token=Authentication.getToken()

def display_image():
    '''

    :Display the main values for the Imaging portion of the query.
    :Attributes:: No input needed.
    :Return:: Pandas data frame with organized values to be printed.
    Empty table and a warning that no values were found for that query
    :Raises an exception if the query is invalid.
    
    ..seealso::
    '''
    print("Imaging ")
    x=int(ob_id)
    I=0; i=0;          
    Answer=pd.DataFrame(index=[0], columns=['N','V'])
        
    sql_query=("select p.clean, p.type, p.u, p.g, p.r , p.I, p.z, p.err_u, p.err_g, p.err_r, p.err_i, p.err_z from PhotoObjAll p where p.objID= " + str(x))
    a=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14")))
    if a.empty:
        print("There are no imaging values for this object")
    else:
        for index,row in a.iterrows():
            Answer.loc[I]=((row.name,row[0]))
            I+=1
        Answer.loc[I]=('*','*')
        I+=1
    
    sql_query=("select z.spiral from zooSpec z where z.objid="+ str(x))
    a=(SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14"))
    if a.empty:
        s=0
    else:
        s=a.index[0]
    sql_query=("select z.elliptical from zooSpec z where z.objid="+ str(x))
    a=(SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14"))
    if a.empty:
        e=0
    else:
        e=a.index[0]
    if ((s==1) or (s>e)):
        Answer.loc[I]=('Morphology','Spiral')
        I+=1
    elif ((e==1) or (e>s)) :
        Answer.loc[I]=('Morphology','Elliptical')
        I+=1
    else:
        Answer.loc[I]=('Morphology','Uncertain')
        I+=1
    return Answer
                   
def link_phobj():
    """

    :Display information about the queried object's photo
    :Attributes:: No input needed. 
    :Return:: A pandas data frame 'Phobj' with organized values
    :Raises a warning in the event of an distorted image
    
    ..seealso::
    """
    sql_query=("select b.mode, b.mdj, b.nDetect-1, b.parentID, b.nChild, b.extinction_r, b.petroRad, b.petroRadErr_r from PhotoObj b where b.objID="+ str(x))
    Phobj=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14")))
    if Phobj.empty:
        print("There are no Photo Object values for this object")
    else:
        return Phobj

def link_phtag():
    """
    
    :Display information about the queried object's tags 
    :Attributes:: No input needed. 
    :Return:: A pandas data frame 'Phtag' with organized values
    :Raises a warning in the event of an distorted image
    
    ..seealso::
    """
    sql_query=("select * from PhotoTag g where g.objID=" + str(x))
    Phtag=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease='DR14')))     
    if Phtag.empty:
        print("There are no tags for this object")
    else:
        return Phtag

def link_phz():
    """
    
    :Display information about the queried object's redshift with an estimated error 
    :Attributes:: No input needed. 
    :Return:: A pandas data frame 'Phz' with organized values
    :Raises a warning in the event of an distorted image
    
    ..seealso::
    """

    sql_query=("select h.z,h.zerr from Photoz h where h.objID ="+ str(x))
    Phz=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14")))
    if Phz.empty:
        print("There are no Photoz values for this object")
    else:
        return Phz
