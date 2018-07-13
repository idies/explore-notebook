# coding: utf-8
#!/usr/bin/env python
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~
IFU spectrum values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Spectrum values observed using IFU(Integral Field Units) for the celestial body in question.

:param:: 'a' - temporary data frame that consolidates o/p to a single format  
:param:: I(capital i["eye"]) is the counter; indicating the next row of the data frame. 
'''

from img_cut import *
from __main__ import *

token=Authentication.getToken()
#data_release="DR14"

def display_manga():
    '''

    :Display:: Primary values for the MaNGA portion of the query.
    :param:: No input parameters
    :Return:: A pandas' data frame, 'manga' 
    :Raise:: Warning for missing or corrupted output
    
    ..seealso:: manga_values.__doc__
    '''
    
    print("MaNGA") 
    I=0
    manga=pd.dataFrame(index=[0], columns=['N','V'])
    try:
        sql_query=("select h.ifura, h.ifudec, h.mangaid, h.mngtarg1, h.mngtarg2, h.mngtarg3,h.objdec"+
                   " h.objra, h.plateifu, h.mjdmax, h.redsn2. h.drp3qual, h.bluesn2 from manDrpAll h where h.mangaid=" + str(manga_id))
        a=SciServer.CasJobs.executeQuery(sql=sql_query, context=data_release, format='pandas')
        a=np.transpose(a)
        if a.empty:
            print("There are no MaNGA values for this celestial object")
            pass
        else:
            manga.loc[I]=('MaNGA Observation(s)','*'); I+=1;
            for index,row in a.iterrows():
                man.loc[I]=((row.name,row[0]))
                I+=1
    except:
        print("Unexpected error: "+ sys.exc_info()[0])
    else:
        return manga
