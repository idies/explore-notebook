# coding: utf-8
#!/usr/bin/env python import *
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Optical Spectrum values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optical spectrum aspects of the celestial body in question.

:param:: 'a' - temporary data frame; consolidates o/p to a single format  
:param:: I(capital i["eye"]) is the counter; indicating the next row of the data frame. 
'''

#from img_cut import *
from imports import *

token=Authentication.getToken

def display_opspec(specID=0, ra=0, dec=0):
    '''

    :Display:: Primary values for the optical spectrum portion of the query.
    :param:: No input parameters
    :Return:: A pandas' data frame, 'optspec' 
    :Raise:: Exception for keyboard interrupt
    
    ..seealso:: spectra_values.__doc__
    '''
    
    print("Optical Spectra")
    optspec=pd.DataFrame(index=[0], columns=['N','V'])
    I=0
    if(specID is 0 and ra is not 0):
        specID=mv.get_specid(ra,dec)
    
    try:
        sql_query=("select a.specObjID, a.fiberID, a.mjd, a.plate, a.survey, a.programname, a.instrument,a.sourceType,a.z, a.zErr, a.class, a.velDisp, a.velDispErr from SpecObjAll a where a.specObjID=" +str(specID))
        a=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release)))
        if a.empty:
            print("There are no Optical Spectra values for this object")
            pass
        else:
            for index,row in a.iterrows():
                optspec.loc[I]=((row.name,row[0]))
                I+=1
            return optspec
    
        sql_query=('select img from SpecObjAll a where a.specObjID='+str(specID))
        print(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release))
#         if b.empty:
#             print("There is no image for this object")
#             pass
#         else:
#             print(b)
    except TimeoutError as e:
        print("Request timed out. Please check the request or increase the queue")
#         if (e==500):
#             pass
#         else:
#             raise ErrorCode("The server is unable to process your request. Please try again later")

