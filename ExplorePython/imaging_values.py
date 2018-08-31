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
import new
token=Authentication.getToken()

def display_image(ob_id=1237668296598749280, ra=197.614455635, dec=18.438168849):
    '''

    :Display:: Primary values for the imaging portion of the query.
    :param:: No input parameters.
    :Return:: A pandas' data frame, 'imgval'.
    :Raise:: Exception for a KeyboardInterrupt.
    
    ..seealso:: imaging_values.__doc__
    '''
    print("Imaging")
    I=0
    dec=new.dec
    print(dec)

    imgval=pd.DataFrame(index=[0], columns=['N','V'])
    try:   
        sql_query=("select p.clean, p.type, p.u, p.g, p.r , p.I, p.z, p.err_u, p.err_g," + " p.err_r, p.err_i, p.err_z from PhotoObjAll p where p.objID= " + str(ob_id))
        a=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release)))
        print(a)
        try:
            if a.empty:
                print("Warning: There is no imaging data for this object. " + 
                      "Indistinct features hinder observations. Check input and try again ")
                return 0
            else:
                for index,row in a.iterrows():
                    imgval.loc[I]=((row.name,row[0]))
                    I+=1
        except Exception:
            print("Unexpected error: "+ str(sys.exc_info()[0]))
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
            imgval.iloc[I]=('Morphology','Spiral')
            I+=1
        elif ((e==1) or (e>s)) :
            imgval.iloc[I]=('Morphology','Elliptical')
            I+=1
        else:
            imgval.iloc[I]=('Morphology','Uncertain')
            I+=1
        return imgval
    except TimeoutError as e:
        print("Server timed out. Please verify your query or increase queue")
        return ""
#         if (e==500):
#             pass
#         else:
#             raise ErrorCode("The server is unable to process your request. Please try again later")



