# coding: utf-8
#!/usr/bin/env python import *
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Photometric values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Photometric aspects of the celestial body in question.


:param:: 'a' - temporary data frame; consolidates o/p to a single format  
:param:: I(capital i["eye"]) is the counter; indicating the next row of the data frame. 
'''

#from img_cut import *
from imports import *

token=Authentication.getToken()

def display_image(val=[]):
    '''

    :Display:: Primary values for the imaging portion of the query.
    :param:: No input parameters.
    :Return:: A pandas' data frame, 'imgval'.
    :Raise:: Exception for a KeyboardInterrupt.
    
    ..seealso:: imaging_values.__doc__
    '''
    print("Imaging")
    I=0
    data_release=val[4]
    ob_id=val[0]
    imgval=pd.DataFrame(index=[0], columns=['N','V'])
    try:   
        sql_query=("select p.clean, p.type, p.u, p.g, p.r , p.I, p.z, p.err_u, p.err_g" + 
               "p.err_r, p.err_i, p.err_z from PhotoObjAll p where p.objID= " + str(ob_id))
        a=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release)))
        try:
            if a.empty:
                print("Warning: There is no imaging data for this object. " + 
                      "Indistinct features hinder observations. Check input and try again ")
                sys.exit()
            else:
                for index,row in a.iterrows():
                    imgval.loc[I]=((row.name,row[0]))
                    I+=1
        except:
            print("Unexpected error: "+ sys.exc_info()[0])
            sys.exit()
        sql_query=("select z.spiral from zooSpec z where z.objid="+ str(ob_id))
        a=(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release))
        if a.empty:
            s=0
        else:
            s=a.index[0]
        sql_query=("select z.elliptical from zooSpec z where z.objid="+ str(ob_id))
        a=(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release))
        if a.empty:
            e=0
        else:
            e=a.index[0]
        if ((s==1) or (s>e)):
            imgval.loc[I]=('Morphology','Spiral')
            I+=1
        elif ((e==1) or (e>s)) :
            imgval.loc[I]=('Morphology','Elliptical')
            I+=1
        else:
            imgval.loc[I]=('Morphology','Uncertain')
            I+=1
        return imgval
    except TimeoutError as e:
        print("Server timed out. Please verify your query or increase queue")
#         if (e==500):
#             pass
#         else:
#             raise ErrorCode("The server is unable to process your request. Please try again later")


def link_phobj():
    '''

    :Display:: Values for sidebar link, PhotoObj.
    :param:: No input parameters
    :Return:: A pandas' data frame, 'Phobj' 
    :Raise:: ValueError for missing or corrupted output.
    
    ..seealso:: imaging_values.__doc__
    '''
    sql_query=("select b.mode, b.mdj, b.nDetect-1, b.parentID, b.nChild" +
               "b.extinction_r, b.petroRad, b.petroRadErr_r from PhotoObj b where b.objID="+ str(test1.ob_id))
    Phobj=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release)))
    try:        
        if Phobj.empty:
            raise ValueError("There is no photo data corresponding to your object")
        else:
            return Phobj
    except:
        print("Unexpected error: " + sys.exc_info()[0])
        
def link_phtag():
    '''

    :Display:: Values for sidebar link, PhotoTag.
    :param:: No input parameters.
    :Return:: A pandas' data frame, 'Phtag' 
    :Raise:: ValueError for missing or corrupted data.
    
    ..seealso:: imaging_values.__doc__
    '''
    sql_query=("select * from PhotoTag g where g.objID=" + str(test1.ob_id))
    Phtag=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release)))     
    try:        
        if Phtag.empty:
            raise ValueError("There are no tags corresponding to your query")
        else:
            return Phtag
    except:
        print("Unexpected error: " + str(sys.exc_info()[0]))

def link_phz():
    '''

    :Display:: Values for sidebar link, PhotoZ.
    :param: No input parameters.
    :Return:: A pandas' data frame, 'Phz' 
    :Raise:: ValueError for missing or corrupted output.
    
    ..seealso:: imaging_values.__doc__
    '''

    sql_query=("select h.z,h.zerr from Photoz h where h.objID ="+ str(test1.ob_id))
    Phz=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release)))
    try:        
        if Phz.empty:
            raise ValueError("There is no data corresponding to your query")
        else:
            return Phz
    except:
        print("Unexpected error: "+ print(sys.exc_info()[0]))
