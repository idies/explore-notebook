
import os
import sys
from __main__ import *


#CASJOBS#

    ### getting all values under cross identification with OBJID###

tabel=pd.DataFrame[index=[1,2,3,4,5]]  
    
       
i=1        
y=ob_id
q=None

         #values from table USNO#

tabel.loc[i]=['proper_motion', 'mura_err', 'mudec_err', 'angle']
i+=1

tabel.loc[i]=[SciServer.CasJobs.executeQuery(sql="select propermotion, muraerr, mudecerr, angle from USNO n where n.OBJID=y", context='DR14', format='pandas')]
i+=i        
        
        #values from tables WISE_xmatch and WISE_allsky#

tabel.loc[i]=['wise_cntr','w1mag', 'w2mag', 'w3mag', 'w4mag']        
i+=i 

tabel.loc[i+1]=[SciServer.CasJobs.executeQuery(sql="select wise_cntr,w1mag, w2mag, w3mag, w4mag, from WISE_xmatch h and WISE_skyall t where h.OBJID=y and t.OBJID=y",context='DR14',format='pandas')]
i+=i       
        

    #values from ROSAT and RC3#
    
tabel.loc[i]=['cps', 'hr1', 'hr2', 'ext', hr1, hr2, ext]
i+=1

q= SciServer.CasJobs.executeQuery(sql="select cps, hr1, hr2, ext,cps, hr1, hr2, ext from RC3 c and ROSAT q where c.OBJID= q.OBJID= y", context='DR14', format='pandas')

if (q == NONE):
    print("There is no ROSAT, RC3 data for this object")
else:
    tabel.loc[i]=[q]
    i+=1
      
        
    #values from tables FIRST and TwoMASS #

tabel.loc[i]= ['j','h','k', 'phQual']    
i+=1    

tabel.loc[i] = [SciServer.CasJobs.executeQuery(sql="select j,h,k, phQual from TwoMASS s and First f where s.OBJID= f.OBJID= y", context='DR14', format='pandas')]
i+=1
    


print(tabel)
