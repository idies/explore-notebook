# coding: utf-8
#!/usr/bin/env python import *
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Photometric values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Photometric aspects of the celestial body in question.

:param:: 'a' - temporary data frame; arranges query o/p  
:param:: I(capital i["eye"]) is the counter; indicating the next row of the data frame. 
'''

import os
import sys
from Image_Cut_Out import *
from __main__ import *

token=Authentication.getToken()

def display_image():
    '''

    :Display:: Primary values for the imaging portion of the query.
    :Return:: A pandas' data frame, 'Answer' 
    :Raise:: an exception in the event of a erroneous object ID.
    
    ..seealso:: Imaging_values.__doc__
    '''
    print("Imaging ")
    I=0       
    Answer=pd.DataFrame(index=[0], columns=['N','V'])
        
    sql_query=("select p.clean, p.type, p.u, p.g, p.r , p.I, p.z, p.err_u, p.err_g, p.err_r, p.err_i, p.err_z from PhotoObjAll p where p.objID= " + str(ob_id))
    a=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14")))
    if a.empty:
        print("There are no imaging values for this object")
    else:
        for index,row in a.iterrows():
            Answer.loc[I]=((row.name,row[0]))
            I+=1
        Answer.loc[I]=('*','*')
        I+=1
    
    sql_query=("select z.spiral from zooSpec z where z.objid="+ str(ob_id))
    a=(SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14"))
    if a.empty:
        s=0
    else:
        s=a.index[0]
    sql_query=("select z.elliptical from zooSpec z where z.objid="+ str(ob_id))
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
    :Return:: A pandas data frame 'Phobj' with organized values
    :Raises a warning in the event of an distorted image
    
    ..seealso:: Imaging_values.__doc__
    """
    sql_query=("select b.mode, b.mdj, b.nDetect-1, b.parentID, b.nChild, b.extinction_r, b.petroRad, b.petroRadErr_r from PhotoObj b where b.objID="+ str(ob_id))
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
    sql_query=("select * from PhotoTag g where g.objID=" + str(ob_id))
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

    sql_query=("select h.z,h.zerr from Photoz h where h.objID ="+ str(ob_id))
    Phz=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14")))
    if Phz.empty:
        print("There are no Photoz values for this object")
    else:
        return Phz
