
# coding: utf-8

#!/usr/bin/env python import *
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
IR Spectrum values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Infrared spectrum aspects of the celestial body in question.

:param:: 'a' - temporary data frame; consolidates o/p to a single format  
:param:: I(capital i["eye"]) is the counter; indicating the next row of the data frame. 
'''
from img_cut import *
from __main__ import *

token=Authentication.getToken
#data_release="DR14"

def display_apoge():
    '''

    :Display:: Primary values for the imaging portion of the query.
    :Return:: A pandas' data frame, 'Answer' 
    :Raise:: an exception in the event of a erroneous object ID.
    
    ..seealso:: imaging_values.__doc__
    '''
    
    print("APOGEE")
    I=0
    p=apo_id
    p_id=ob_id
    Apoge=pd.DataFrame(index=[0], columns=['N','V'])
    a=np.transpose(a)
    sql_query=("select p.j,p.j_err,p.h,p.h_err,p.k,p.k_err, p.irac_4_5, p.irac_4_5_err, p.src_4_5 from apogeeObject p where p.apogee_id= " + str(p))
    a=SciServer.CasJobs.executeQuery(sql=sql_query, context="DR14", format="pandas")
    
    if a.empty:
        print("Currently no data is avaliable for this celestial body's APOGEE ")
        return 0
    else:
        Apoge.loc[I]=('Targeting Information','*'); I+=1;
        for index,row in a.iterrows():
            Apoge.loc[I]=((row.name,row[0]))
            I+=1
    
    sql_query=("select p.j,p.j_err,p.h,p.h_err,p.k,p.k_err, p.irac_4_5, p.irac_4_5_err, p.src_4_5 from apogeeObject p where p.apogee_id= " + str(p))
    a=SciServer.CasJobs.executeQuery(sql=sql_query, context="DR14", format="pandas")
    a=np.transpose(a)
    if a.empty:
        print("Currently no data is avaliable for this celestial body's APOGEE ")
        return 0
    else:
        Apoge.loc[I]=('Targeting Information','*'); I+=1;
        for index,row in a.iterrows():
            Apoge.loc[I]=((row.name,row[0]))
            I+=1
        Apoge.loc[I]=('*','*')
        I+=1
    sql_query=("select l.vhelio_avg, l.vscatter from apogeeStar l where l.apogee_id= " + str(p))
    a=SciServer.CasJobs.executeQuery(sql=sql_query, context="DR14", format="pandas")
    np.transpose(a)
    if a.empty:
        print("Stellar parameters are currently unavailable ")
        
    else:
        Apoge.loc[I]=('Stellar Parameters','*'); I+=1;
        for index,row in a.iterrows():
            Apoge.loc[I]=((row.name,row[0]))
            I+=1
        Apoge.loc[I]=("Best-fit temperature (K)","N/A")
        I+=1
        Apoge.loc[I]=("Temp error","N/A")
        I+=1
        Apoge.loc[I]=("Surface Gravity log10(g)	","N/A")
        I+=1
        Apoge.loc[I]=("Log g error","N/A")
        I+=1
        Apoge.loc[I]=("Metallicity [Fe/H]","N/A")
        I+=1
        Apoge.loc[I]=("[Fe/H] error","N/A")
        I+=1
        Apoge.loc[I]=("[α/Fe]","N/A")
        I+=1
        Apoge.loc[I]=("[α/Fe] error","N/A")
        I+=1
        return Apoge    


def link_visit():
    print("....")


def link_apogestar():
    sql_query="select * from apogeeStar n where n.apogee_id="+ str(p)
    a=SciServer,CasJobs,executeQuery(sql=sql_query, context='DR14',format='pandas')
    if a.empty:
        val="No APOGEE star data (APOGEEE data in derived radial velocity) is available for the IR spectrum of this object"
        return val
    else:
        return a

def link_aspcap():
    
    sql_query="select * from aspcapStar n where n.apogee_id="+ str(p)
    a=SciServer,CasJobs,executeQuery(sql=sql_query, context='DR14',format='pandas')
    if a.empty:
        val="No ASPCAP data is available for the IR spectrum of this object"
        return val
    else:
        return a

