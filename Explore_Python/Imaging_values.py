
#!/usr/bin/env python import *

import os
import sys

from Image_Cut_Out import ob_id
from __main__ import *



x = int(ob_id)
token=Authentication.getToken()
I=0          
Answer=pd.DataFrame()

print("Imaging ")

  
sql_query=('select * from PhotoTag g where g.objID='+x) 
             ### getting values from table PhotoTag  ###

Phtag=SkyServer.sqlSearch(sql=sql_query, dataRelease='DR14')     
Phtag= np.transpose(Phtag)       
### ***************** Function PhotoTag on the LEFT sidebar *****************###    
            
        ### getting values from table photoobjall ###
        
sql_query="select p.clean, p.type, p.u, p.g, p.r , p.I, p.z, p.err_u, p.err_g, p.err_r, p.err_i, p.err_z from PhotoObjAll p where p.objID= "+x)
#Answer.loc[I]=['clean', 'type', 'u', 'g', 'r' ,'I','z,err_u', 'err_g,err_r','err_i,err_z']
#I+=1
a=SkyServer.sqlSearch(sql=sql_query, dataRelease="DR14")
a=np.transpose(a)
Answer.loc[I]=[a]
I+=1
       
              ### getting values from table PhotoObj and Photoz ###
              
#Answer.loc[I]=['mode', 'mdj','nDetect1', 'parentID', 'nChild', 'extinction_r', 'petroRad', 'petroRadErr_r' 
#I+=1
a=SkyServer.sqlSearch(sql="select b.mode, b.mdj, b.nDetect-1, b.parentID, b.nChild, b.extinction_r, b.petroRad, b.petroRadErr_r, from PhotoObj b where b.objID=x", dataRelease="DR14")
a=np.transpose(a)
Answer.loc[I]=[a]
I+=1
#Answer.loc[I]= ['z','zerr']
#I+=1
a=SkyServer.sqlSearch(sql="select h.z,h.zerr from Photoz h where h.objID=x", dataRelease="DR14")
a=np.transpose(a)
Answer.loc[I]=[a]
I+=1       
            
        ### getting values from table zooSpec on shape of object  ###
#Answer.loc[I]=['Morphology']
#I+=1

s=(SkyServer.sqlSearch(sql="select z.spiral from zooSpec z where z.objID=x", dataRelease="DR14"))
e=(SkyServer.sqlSearch(sql="select z.elliptical from zooSpec z where z.objID=x", dataRelease="DR14"))
u=(SkyServer.sqlSearch(sql="select z.uncertain from zooSpec z where z.objID=x", dataRelease="DR14"))
if ((s==1) or (s>e)):
    Answer.loc[I]=['Morphology','Spiral']
    I+=1
elif ((e==1) or (e>s)) :
    Answer.loc[I]=['Morphology','Elliptical']
    I+=1
else:
    Answer.loc[I]=['Morphology','Uncertain']
    I+=1
    

   
    
    


