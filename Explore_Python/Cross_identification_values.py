#!/usr/bin/env python import *

from __main__ import *
from imports import *  
from Image_Cut_Out import *

#CASJOBS#

    ### getting all values under cross identification with OBJID###

tabel=pd.DataFrame() 
       
i=0       
y=ob_id
yra=ra
ydec=dec
q=None

         #values from table USNO#

#tabel.loc[i]=['proper_motion', 'mura_err', 'mudec_err', 'angle']
#i+=1

a=SciServer.CasJobs.executeQuery(sql="select n.propermotion, n.muraerr, n.mudecerr, n.angle from USNO n where n.OBJID=y", context='DR14', format='pandas')
a=np.transpose(a)
tabel.loc[i]=[a]
i+=i        
        
        #values from tables WISE_xmatch and WISE_allsky#

#tabel.loc[i]=['wise_cntr','w1mag', 'w2mag', 'w3mag', 'w4mag']        
#i+=i 

a=SciServer.CasJobs.executeQuery(sql="select h.wise_cntr, t.w1mag, t.w2mag, t.w3mag, t.w4mag, from WISE_xmatch h and WISE_skyall t where h.sdss_objid=y and t.ra=yra and t.dec=ydec",context='DR14',format='pandas')
a=np.transpose(a)
tabel.loc[i]=[a]
i+=i       
        
    #values from ROSAT and RC3#
    
#tabel.loc[i]=['cps', 'hr1', 'hr2', 'ext', hr1, hr2, ext]
#i+=1

q= SciServer.CasJobs.executeQuery(sql="select q.CPS, q.HR1,q.HR2,q.EXT,q.CAT,  from RC3 c and ROSAT q where c.objID= q.OBJID= y", context='DR14', format='pandas')

if (q == NONE):
    print("There is no ROSAT, RC3 data for this object")
else:
    tabel.loc[i]=[np.transpose(q)]
    i+=1
      
        
    #values from tables FIRST and TwoMASS #

#tabel.loc[i]= ['j','h','k', 'phQual']    
#i+=1    

a=SciServer.CasJobs.executeQuery(sql="select j,h,k, phQual from TwoMASS s and First f where s.OBJID= f.OBJID= y", context='DR14', format='pandas')
tabel.loc[i]=[np.transpose(a)]
i+=1
    
