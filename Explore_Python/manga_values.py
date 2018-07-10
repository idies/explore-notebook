# coding: utf-8
#!/usr/bin/env python
'''MaNGA values
~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
from Image_cut_out import *
from imports import *
fron fn_imports import *
from __main__ inport *
token= Authentication.getToken()

def display_manga():
    """
    
    :Display the main values for the Imaging portion of the query.
    :Attributes:: No input needed.
    :Return:: Pandas data frame with organized values to be printed.
    :Raises an exception if the query is invalid.
    
    ..seealso::
    """
    
    print("MaNGA")
    
    
    
    sql_query=("select h.ifura, h.ifudec, h.mangaid, h.mngtarg1, h.mngtarg2, h.mngtarg3, h.objdec, h.objra, h.plateifu, h.mjdmax, h.redsn2. h.drp3qual, h.bluesn2 from manDrpAll h where h.mangaid =" +str(m))
    a=SciServer.CasJobs.executeQuery(sql=sql_query, context="DR14", format='pandas')
    a=np.transpose(a)
    if a.empty:
        print("There are no MaNGA values for this celestial object")
        return 0
    else:
        man.loc[I]=('MaNGA Observation(s)','*'); I+=1;
        for index,row in a.iterrows():
            man.loc[I]=((row.name,row[0]))
            I+=1
            return man
         
    
    