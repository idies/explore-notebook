
import os
import sys

def cross(oid): #CASJOBS#
    ### getting all values under cross identification with OBJID###
    #casjobs clear mydb. insert into mydb
    def unso(x):
        #vales from table USNO#
        tabel=SciServer.CasJobs.executeQuery(sql="select propermotion, muraerr, mudecerr, angle from USNO n where n.OBJID=x",context='DR14',format='pandas')
        print(tabel)
        tabel=None #clearing table before next query
        
    def wse(y):
        #values from tables WISE_xmatch and WISE_allsky#
        tabel=SciServer.CasJobs.executeQuery(sql="select wise_cntr,w1mag, w2mag, w3mag, w4mag, from WISE_xmatch h and WISE_skyall t where h.OBJID=y and t.OBJID=y",context='DR14',format='pandas')
        print(tabel)
        tabel=None
        
    def rose(z):
    #values from ROSAT and RC3#
        tabel= SciServer.CasJobs.executeQuery(sql="select cps, hr1, hr2, ext,cps, hr1, hr2, ext from RC3 c and ROSAT q where c.OBJID=q.OBJID=z",context='DR14',format='pandas')
        if (tabel == NONE):
            print("There is no ROSAT, RC3 data for this object")
        print(tabel)
        tabel=None
        
    def reall(w):
    #values from tables FIRST and TwoMASS #
        tabel=SciServer.CasJobs.executeQuery(sql="select j,h,k, phQual, from TwoMASS s and First f where s.OBJID=f.OBJID=w",context='DR14',format='pandas')
        print(tabel)
        tabel=None
    
    unso(oid)
    wse(oid)
    rose(oid)
    reall(oid)

