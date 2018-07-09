
#!/usr/bin/env python import *

import os
import sys
from Image_Cut_Out import *
from __main__ import *
token=Authentication.getToken()

def display_opSpec():
    
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

    sql_query=('select * from PlateX l where l.specObjID='+ str(z))
    Plate=(np.transpose(SkyServer.sqlSearch(sql=sql_release, dataRelease='DR14')))
    if Plate.empty:
        print("There are no Plate values for this object")
    else:
        return Plate