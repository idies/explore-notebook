# coding: utf-8
#!/usr/bin/env python import *
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Identification values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cross identification aspects of the celestial body in question.

:param:: 'a' - temporary data frame; consolidates o/p to a single format  
:param:: I(capital i["eye"]) is the counter; indicating the next row of the data frame. 
'''
from imports import *
import missing_values as mv
'''

:Display:: Primary values for the cross identification section of the query.
:param:: No input parameters necessary
:Return:: A pandas' data frame, 'table' 
:Raise:: Warnings for corrupted or missing values.

..seealso:: cross_id_values.__doc__
'''

try:
    if(bool(output_text1.value)):
        ra1=output_text1.value
        dec1=output_text2.value
    print("Cross Identification")
    tabel=pd.DataFrame(index=[0,0], columns=['N','V']) 
    I=0       
    if (ra1 is 0.0 and dec1 is 0.0):
        print("No input given. Displaying cross id values for default celestial body")
        raise ValueError("no values for ra and dec have been provided")
    elif (ra1 is 197.614455635 and dec1 is 18.438168849):
        ob_id=1237668296598749280
    else:
        ra=ra1
        dec=dec1
        ob_id=missing_values.get_objid(ra,dec)
    sql_query=("select PROPERMOTION, MURAERR, MUDECERR, ANGLE from USNO where OBJID=" + str(ob_id))
    a=SciServer.CasJobs.executeQuery(sql=sql_query, context=data_release, format='pandas')
    a=np.transpose(a)
    if a.empty:
        print("There's no UNSO data available for this object")
        pass
    else:
        tabel.loc[I]=('CATALOG','UNSO'); I+=1;
        for index,row in a.iterrows():
            tabel.loc[I]=((row.name,row[0]))
            I+=1
        tabel.loc[I]=('*','*')
        I+=1
    sql_query=("select t.cntr, t.w1mag, t.w2mag, t.w3mag, t.w4mag from WISE_allsky t where t.ra=" + str(ra) + "and t.dec=" + str(dec))
    a=SciServer.CasJobs.executeQuery(sql=sql_query,context=data_release,format='pandas')
    a=np.transpose(a)
    if a.empty:
        print("There's no WISE data available for this object")
        pass
    else:
        tabel.loc[I]=('CATALOG','WISE'); I+=1;
        for index,row in a.iterrows():
            tabel.loc[I]=((row.name,row[0]))
            I+=1
        tabel.loc[I]=('*','*')
        I+=1   
    sql_query=("select f.peak,f.major,f.minor from FIRST f where f.objID="+str(ob_id))
    a=SciServer.CasJobs.executeQuery(sql=sql_query,context=data_release,format='pandas')
    a=np.transpose(a)
    if a.empty:
        print("There's no FIRST data available for this object")
        pass
    else:
        tabel.loc[I]=('CATALOG','FIRST'); I+=1;
        for index,row in a.iterrows():
            tabel.loc[I]=((row.name,row[0]))
            I+=1
        tabel.loc[I]=('*','*')
        I+=1
    sql_query=("select j,h,k, phQual from TwoMASS s where s.OBJID="+str(ob_id))
    a=SciServer.CasJobs.executeQuery(sql=sql_query, context='DR14', format='pandas')
    a=np.transpose(a)
    if a.empty:
        print("There is no TwoMASS data available for this object")
        pass
    else:
        tabel.loc[I]=('CATALOG','TwoMASS'); I+=1;
        for index,row in a.iterrows():
            tabel.loc[I]=((row.name,row[0]))
            I+=1
        tabel.loc[I]=('*','*')
        I+=1         
    sql_query=("select q.CPS, q.HR1,q.HR2,q.EXT,q.CAT from ROSAT q where q.OBJID="+ str(ob_id))
    q= SciServer.CasJobs.executeQuery(sql=sql_query, context=data_release, format='pandas')
    if q.empty:
        print('There is no ROSAT data available for this object')
        pass
    else:
        tabel.loc[I]=('CATALOG','ROSAT'); I+=1;
        q=np.transpose(q)
        for index,row in q.iterrows():
            tabel.loc[I]=((row.name,row[0]))
            I+=1
        tabel.loc[I]=('*','*')
        I+=1
    sql_query=("select r.HUBBLE, r.M21, r.HI from RC3 r where r.objID="+str(ob_id))
    q=SciServer.CasJobs.executeQuery(sql=sql_query, context=data_release, format='pandas')
    if q.empty:
        print('There is no RC3 data available for this object')
        pass
    else:
        tabel.loc[I]=('CATALOG','RC3'); I+=1;
        q=np.transpose(q)
        for index,row in q.iterrows():
            tabel.loc[I]=((row.name,row[0]))
            I+=1
        print(tabel)
except (TimeoutError,ValueError) as e:
    print(str(e)+" Please check the request or increase the queue")
    pass

