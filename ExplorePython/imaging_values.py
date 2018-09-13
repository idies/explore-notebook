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
from imports import *
import missing_values as mv
import getpass

''' 
:Display:: Primary values for the imaging portion of the query.
:param:: No input parameters.
:Return:: A pandas' data frame, 'imgval'.

..seealso:: imaging_values.__doc__
'''

try:


    print("Imaging")

    I=0 
    if(bool(output_text1.value) is True):
        ra=output_text1.value
        dec=output_text2.value
    if(ra is 0.0 and dec is 0.0):
        print("Missing: function arguments(ra,dec)")
        pass
    elif (ra is 197.614455635 and dec is 18.438168849):
        print("Invalid input argument. Display: Default object specs displayed")
        ob_id=1237668296598749280.0
    else:
        ob_id=objid
#         ob_id='f{:.0f}'.format(missing_values.get_objid())
#          t=np.transpose(t)
#         t1=str(t)      
#         t2=t1[(len(t1)) - 1]

#         if (int(t2) is not 0):
#             ob_id=float(t1)
#             #ob_id=float(ob_id)
#             #ob_id=t1
#     t3=t1+"1"
#     print(t3)
#     ob_id=float(t3)
#     print("obid %f" %ob_id)
#     ob_id='f{:.1f}'.format(ob_id)
#     ob_id=float(ob_id)
    print(ob_id)    
    imgval=pd.DataFrame(index=[0,0], columns=["N","V"])
    imgval["N"]=pd.Series([], dtype=str)
    imgval["V"]=pd.Series([], dtype=object)

    sql_query=("select p.clean, p.type, p.u, p.g, p.r ,p.I, p.z, p.err_u, p.err_g, p.err_r, p.err_i, p.err_z from PhotoObjAll p where p.objID= " +str(ob_id))

    a=(CasJobs.executeQuery(sql=sql_query,context=data_release, format='pandas'))
    a=np.transpose(a)

    if a.empty:
        print("Warning: There is no imaging data for this object. Indistinct features hinder observations. Check input and try again")
        pass
    else:
        for index,row in a.iterrows():
            imgval.loc[I]=((row.name,row[0]))
            I+=1

    sql_query=("select z.spiral from zooSpec z where z.objid="+ str(ob_id))
    a=(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release))

    if a.empty:
        s=0
    else:
        s=a.iloc[0][0]
    sql_query=("select z.elliptical from zooSpec z where z.objid="+ str(ob_id))
    a=(SkyServer.sqlSearch(sql=sql_query, dataRelease=data_release))

    if a.empty:
        e=0
    else:
        e=a.iloc[0][0]
    if ((s is 1) or (s>e)):
        imgval.iloc[I]=('Morphology','Spiral')
        I+=1
    elif ((e is 1) or (e>s)) :
        imgval.iloc[I]=('Morphology','Elliptical')
        I+=1
    else:
        imgval.iloc[I]=('Morphology','Uncertain')
        I+=1
        imgval
except (NameError, TypeError, TimeoutError) as e:
        print("Unexpected error: "+ str(e))
        pass



