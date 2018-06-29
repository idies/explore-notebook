
#!/usr/bin/env python

import os
import sys

from __main__ import *



x = ob_id
token=Authentication.getToken()
          

ex=pd.DataFrame(index=[1,2,3,4,5,6,7,8])  
print("Imaging ")

  
i=1
             ### getting values from table PhotoTag  ###

      
        
    
             ### getting values from table photoobjall ###
          
        
sql_query="select p.clean, p.type, p.u, p.g, p.r , p.I, p.z, p.err_u, p.err_g, p.err_r, p.err_i, p.err_z from PhotoObjAll p where p.objID=x"
ex.loc[i]=['clean', 'type', 'u', 'g', 'r' ,'I','z,err_u', 'err_g,err_r','err_i,err_z']
i+=i
ex.loc[i]=[SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14")]
i+=i
        
    
             ### getting values from table PhotoObj and Photoz ###
        
        
ex.loc[i]=['mode', 'mdj','nDetect-1','parentID','nChild','extinction_r','petroRad','petroRadErr_r']
i+=i
ex.loc[i]=[SkyServer.sqlSearch(sql="select b.mode, b.mdj, b.nDetect-1, b.parentID, b.nChild, b.extinction_r, b.petroRad, b.petroRadErr_r, from PhotoObj b where b.objID=x", dataRelease="DR14")]
i+=i 
ex.loc[i]= ['z','zerr']
i+=i
ex.loc[i]=[SkyServer.sqlSearch(sql="select h.z,h.zerr from Photoz h where h.objID=x", dataRelease="DR14")]         
i+=i        
        
    
        ### getting values from table zooSpec on shape of object  ###
ex.loc[i]=['Morphology']
i+=i

s=(SkyServer.sqlSearch(sql="select z.spiral from zooSpec z where z.objID=x", dataRelease="DR14"))
e=(SkyServer.sqlSearch(sql="select z.elliptical from zooSpec z where z.objID=x", dataRelease="DR14"))
u=(SkyServer.sqlSearch(sql="select z.uncertain from zooSpec z where z.objID=x", dataRelease="DR14"))
if (s):
    ex.loc[i]=['Spiral']
    i+=i
elif (e) :
    ex.loc=['Elliptical']
    i+=i
else:
    ex.loc[i]=['Uncertain']
    i+=i
    
    

print(ex)    
    
    


