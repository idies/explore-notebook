
#!/usr/bin/env python import *

from Image_Cut_Out import ob_id, ra, dec
from __main__ import *
from imports import *

Opt_Sp=pd.DataFrame()
    
j=0

z=ob_id
zra=ra
zdec=dec
token=Authentication.getToken()   

plate=SkyServer.sqlSearch(sql='select * from PlateX l where l.ra=zra AND l.dec=zdec', dataRelease='DR14')
plate=np.transpose(plate)
### ***************** Function Plate on the LEFT sidebar *****************###

    ##getting values form SpecObjAll##
a=SkyServer.sqlSearch(sql='select a.specObjID, a.fiberID, a.mjd, a.plate, a.survey, a.programname, a.instrument,a.sourceType,a.z, a.zErr, a.class, a.velDisp, a.velDispErr from SpecObjAll a where a.ra=zra and a.dec=zdec', dataRelease='DR14')
b=SkyServer.sqlSearch(sql='select img from SpecObjAll a where a.ra=zra and a.dec=zdec', dataRelease='DR14')
a=np.transpose(a)
Opt_Sp.loc[j]=[a]
j+=1


##add flag check##