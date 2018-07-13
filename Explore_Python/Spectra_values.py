# coding: utf-8
#!/usr/bin/env python import *
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Optical Spectrum values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Optical spectrum aspects of the celestial body in question.

:param:: 'a' - temporary data frame; consolidates o/p to a single format  
:param:: I(capital i["eye"]) is the counter; indicating the next row of the data frame. 
'''

import os
import sys
from img_cut import *
from __main__ import *

token=Authentication.getToken()
#data_release="DR14"

def display_opSpec():
    '''

    :Display:: Primary values for the imaging portion of the query.
    :Return:: A pandas' data frame, 'Answer' 
    :Raise:: an exception in the event of a erroneous object ID.
    
    ..seealso:: imaging_values.__doc__
    '''
    
    print("Optical Spectra")
    optspec=pd.DataFrame(index=[0], columns=['N','V'])
    I=0
    z=spec_id
    zra=ra
    zdec=dec
    sql_query=("select a.specObjID, a.fiberID, a.mjd, a.plate, a.survey, a.programname, a.instrument,a.sourceType,a.z, a.zErr, a.class, a.velDisp, a.velDispErr from SpecObjAll a where a.specObjID=" +str(z))
    a=(np.transpose(SkyServer.sqlSearch(sql=sql_query, dataRelease='DR14')))
    if a.empty:
        print("There are no Optical Spectra values for this object")
    else:
        for index,row in a.iterrows():
            optspec.loc[I]=((row.name,row[0]))
            I+=1
        return optspec
    
    sql_query=('select img from SpecObjAll a where a.specObjID='+str(z))
    b=SkyServer.sqlSearch(sql=sql_query, dataRelease='DR14')
    if b.empty:
        print("There is no image for this object")
    else:
        print(b)
    
##add flag check##

def link_plate():    
    """
    
    :Display all attributes of the object observed from a particular image.
    :Attributes:: No input needed. 
    :Return:: A pandas data frame with organized values.
    :Raises a warning in the event of a indiscernible image.
    
    ..seealso::
    """
    sql_query=('select * from PlateX l where l.specObjID='+ str(z))
    Plate=(np.transpose(SkyServer.sqlSearch(sql=sql_release, dataRelease='DR14')))
    if Plate.empty:
        print("There are no Plate values for this object")
    else:
        return Plate
