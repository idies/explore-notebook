#coding: utf-8
#!/usr/bin/env python import *
''' CasJobs.executequery(sql,contex,format)'''

from imports import *


def ExploreQueries():
    {

     # Left Side panel of the Explore Page
     #photoObj
     PhotoObjQuery = "select * from PhotoObjAll where objId=@objId";


     #photoTag
     PhotoTagQuery = "select * from PhotoTag where objId=@objId";


     #Field
     FieldQuery = "select * from Field where fieldId =@fieldId";


     #Frame: this are all columns except for column "img"
     FrameQuery = "select fieldID,zoom,run,rerun,camcol,field,stripe,strip,a,b,c,d,e,f,node,incl,raMin,raMax,decMin,decMax,mu,nu,ra,dec,cx,cy,cz,htmID,'not displayed' as 'img' from Frame where fieldId=@fieldId";
     #  FrameQuery = "select * from Frame where fieldId=@fieldId";
     #specObjall
     SpecObjQuery = "select * from SpecObjAll where specObjId=@specId";


     #sppLines
     sppLinesQuery = "select * from sppLines where specObjId=@specId";


     #sppParams
     sppParamsQuery = "select * from sppParams where specObjId=@specId";


     #galspec
     galSpecLineQuery = "select * from galSpecLine where specObjId=@specId";


     #galspecIndex
     galSpecIndexQuery = "select * from galSpecIndx where specObjId=@specId";


     #galspecInfo
     galSpecInfoQuery = "select * from galSpecInfo where specObjId=@specId";


     #stellarMassStarformingPort
     stellarMassStarformingPortQuery = @"select * from stellarMassStarformingPort where specObjId=@specId";

     #stellarMassPassivePort
     stellarMassPassivePortQuery = @"select * from stellarMassPassivePort where specObjId=@specId ";


     #emissionLinesPort
     emissionLinesPortQuery = "select * from emissionLinesPort where specObjId=@specId";


     #stellarMassPCAWiscBC03
     stellarMassPCAWiscBC03Query = "select * from stellarMassPCAWiscBC03 where specObjId=@specId";


     #stellarMassPCAWiscM11
     stellarMassPCAWiscM11Query = "select * from stellarMassPCAWiscM11 where specObjId=@specId";


     #For DR10 and above
     #stellarMassFSPSGranEarlyDust
     stellarMassFSPSGranEarlyDust = "select * from stellarMassFSPSGranEarlyDust where specObjId=@specId";


     #stellarMassFSPSGranEarlyNoDust
     stellarMassFSPSGranEarlyNoDust = "select * from stellarMassFSPSGranEarlyNoDust where specObjId=@specId";


     #stellarMassFSPSGranWideDust
     stellarMassFSPSGranWideDust = "select * from stellarMassFSPSGranWideDust where specObjId=@specId";


     #stellarMassFSPSGranWideDust
     stellarMassFSPSGranWideNoDust = "select * from stellarMassFSPSGranWideNoDust where specObjId=@specId";


     #apogeeStar
     apogeeStar = "select * from apogeeStar where apstar_id=@apid"; # note that @apid is a string, and has to be checked against sql injection before sending the query.
     # HttpUtility.UrlEncode("'" + apogeeId + "'");

     #aspcapStar
     aspcapStar = "select * from aspcapStar where apstar_id=@apid"; # note that @apid is a string, and has to be checked against sql injection before sending the query.
     #+HttpUtility.UrlEncode("'" + apogeeId + "'");      

     #PhotoZ
     PhotoZ = "select * from Photoz where objid=@objId";
     #string c1 = "select * from Photoz2 where objid=" + objid;       

     #PhotzRF
     #  PhotozRF= "select * from PhotozRF where objid=@objId";
     #string c2 = "select * from Photoz2 where objid=" + objid;

    #region plate
     #Plate
     Plate = "select * from PlateX where plateId=@plateId";

     PlateShow = @" select cast(specObjID as binary(8)) as specObjId, fiberId, class as name, str(z,5,3) as z 
                            from SpecObjAll where plateID=@plateId order by fiberId";

    #endregion
    #region AllSpectra
         # #AllSpec Queries
     AllSpec1 = @"select s.specObjId, s.plate as plate, s.mjd as MJD, s.fiberID as fiber, 
                        str(t.ra,10,5) as ra, str(t.dec,10,5) as dec, str(s.ra,10,5) as specRa, str(s.dec,10,5) as specDec, s.sciencePrimary, 
                        str(dbo.fDistanceArcMinEq(t.ra,t.dec,s.ra,s.dec),10,8) as distanceArcMin, s.class as class  
                        from SpecObjAll s, photoobjall t
                        where t.objid=@objId  and s.bestobjid=t.objid  order by scienceprimary desc, plate, MJD, fiber";


     AllSpec2 = @"select s.specObjId, s.plate as plate, s.mjd as MJD, s.fiberID as fiber, str(t.ra,10,5) as ra, str(t.dec,10,5) as dec, 
                        str(s.ra,10,5) as specRa, str(s.dec,10,5) as specDec,  s.sciencePrimary, 
                        str(dbo.fDistanceArcMinEq(t.ra,t.dec,s.ra,s.dec),10,8) as distanceArcMin, s.class as class  
                        from SpecObjAll s, photoobjall t 
                        where t.objid=@objId  and s.fluxobjid=t.objid order by  plate, MJD, fiber, 
                        scienceprimary desc, distanceArcMin asc";

    #endregion

    #region matches
     # # #Matches Queries
     matches1 = @"select dbo.fIAUFromEq(p.ra,p.dec) as 'IAU name', p.objid, p.thingid, dbo.fPhotoModeN(p.mode) as 'mode description'
                                    from Photoobjall p where p.objid=@objId";


     #*          matches2  = @" select t.objid, t.thingid, p.mode, dbo.fPhotoModeN(p.mode) as '(mode description)'
                                            from thingindex t join photoobjall p on t.objid = p.objid 
                                            where t.objid=@objId and p.mode != 1 order by p.mode";
    * #
     matches2 = @" select d.objid, d.thingid, p2.mode, dbo.fPhotoModeN(p2.mode) as 'mode description'
                                    from thingIndex t join detectionIndex d on t.thingId=d.thingId join phototag p on t.objid = p.objid join phototag p2 on d.objid = p2.objid 
                                    where t.objid=@objId order by p2.mode";






    #endregion

    #region neighbors
     # # #Neighbors
     neighbors1 = @" select dbo.fIAUFromEq(p.ra,p.dec) as 'IAU name', p.objid, p.thingid from photoobjall p where p.objid=@objId";


     neighbors2 = @" select n.neighborObjId as objId,str(t.ra,10,5) as ra, str(t.dec,10,5) as dec, str(n.distance,5,3) as 'distance (arcmin)',
                            dbo.fPhotoTypeN(n.neighborType) as type, neighborMode as mode, dbo.fPhotoModeN(n.neighborMode) as '(mode description)'
                            from Neighbors n, photoobjall t where n.neighborObjid=t.objid and n.objId=@objId order by n.distance asc ";

    #endregion

    #region fits_parameters
     # # # Fits Parameters Queries
     fitsParametersSppParams = @" select targetstring as 'Targeting criteria', flag as 'SEGUE flags',spectypehammer as 'HAMMER spectral type', SPECTYPESUBCLASS as 'Spectral subclass',
                    str(elodiervfinal,7,2) as 'Radial velocity (km #s)', str(elodiervfinalerr,8,3) as 'RV error', str(teffadop,6,0) as 'Effective temp (K)', 
                    str(teffadopunc,6,1) as 'Teff error' , str(fehadop,7,2) as '[Fe #H] (dex)', str(fehadopunc,8,3) as '[Fe #H] error', str(loggadop,7,2) as 'log<sub>10< #sub>(g) (dex)', 
                    str(loggadopunc,8,3) as 'log<sub>10< #sub>(g) error' from sppParams where specObjId=@specId";


     fitsParametersStellarMassStarformingPort = @"  select logMass as 'Best-fit log<sub>10< #sub>(stellar mass)',minLogMass as '1-&#963 min', maxLogMass as '1-&#963 max',
                    age as 'Best-fit age (Gyr)', minAge as '1-&#963 min Age', maxAge as '1-&#963 max Age',
                    SFR as 'Best-fit SFR (M<sub>&#9737< #sub>  # yr)', minSFR as '1-&#963 min SFR', maxSFR as '1-&#963 max SFR' 
                    from stellarMassStarformingPort where specObjId=@specId";

     fitsParameterSstellarMassPassivePort = @" select logMass as 'Best-fit log<sub>10< #sub>(stellar mass)', minLogMass as '1-&#963 min', maxLogMass as '1-&#963 max'
                     , age as 'Best-fit age (Gyr)', minAge as '1-&#963 min Age', maxAge as '1-&#963 max Age', SFR as 'Best-fit SFR (M<sub>&#9737< #sub>  # yr)',
                     minSFR as '1-&#963 min SFR', maxSFR as '1-&#963 max SFR' 
                     from stellarMassPassivePort where specObjId=@specId";

     fitsParametersEmissionLinesPort = @" select velstars as 'Stellar velocity (km #s)',sigmaStars as 'Stellar velocity disperson (km #s)', 
                                                            sigmaStarsErr as 'Velocity dispersion error' ,chisq as 'Chi-squared fit of template',
                                                            bpt as 'BPT classification' from emissionLinesPort where specObjId=@specId";


     fitsParametersStellarMassPCAWiscBC03 = @" select str(mstellar_median,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)',
                                                                str(mstellar_err,8,3) as 'Error', str(vdisp_median,8,2) as 'Median veldisp (km #s)', str(vdisp_err,9,3) as 'Error VelDisp'
                                                                from stellarMassPCAWiscBC03 where specObjId=@specId";

     fitsParametersstellarMassPCAWiscM11 = @"select str(mstellar_median,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', str(mstellar_err,8,3) as 'Error',
                                                                str(vdisp_median,8,2) as 'Median veldisp (km #s)', str(vdisp_err,9,3) as 'Error VelDisp'
                                                                from stellarMassPCAWiscM11 where specObjId=@specId";

     fitsParametersStellarmassFSPSGranEarlyDust = @"select str(logmass,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', str(logmass_err,8,3) as 'Error', 
                                                                      str(age,8,2) as 'Age (Gyr)', 
                                                                      str(ssfr,8,2) as 'SSFR', str(metallicity,8,2) as 'metallicity'
                                                                      from stellarmassFSPSGranEarlyDust where specObjId=@specId";

     fitsParametersStellarmassFSPSGranEarlyNoDust = @"select str(logmass,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', 
                                                                        str(logmass_err,8,3) as 'Error', str(age,8,2) as 'Age (Gyr)', 
                                                                        str(ssfr,8,2) as 'SSFR', str(metallicity,8,2) as 'metallicity'
                                                                        from stellarmassFSPSGranEarlyNoDust where specObjId=@specId";

     fitsParametersStellarmassFSPSGranWideDust = @"select str(logmass,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', str(logmass_err,8,3) as 'Error',
                                                                    str(age,8,2) as 'Age (Gyr)', 
                                                                    str(ssfr,8,2) as 'SSFR', str(metallicity,8,2) as 'metallicity'
                                                                    from stellarmassFSPSGranWideDust where specObjId=@specId";

     fitsParametersStellarmassFSPSGranWideNoDust = @"select str(logmass,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', str(logmass_err,8,3) as 'Error',
                                                                        str(age,8,2) as 'Age (Gyr)', 
                                                                        str(ssfr,8,2) as 'SSFR', str(metallicity,8,2) as 'metallicity'
                                                                        from stellarmassFSPSGranWideNoDust where specObjId=@specId";

    #endregion

    #region galaxyzoo
     # #GalaxyZooQueries
     zooSpec = "select * from zooSpec where objid=@objId";


     zooSpec1 = @"select objid,nvote as 'Votes',str(p_el_debiased,5,3) 'Elliptical proabability (debiased)',
                         str(p_cs_debiased,5,3) 'Spiral probability (debiased)'
                         from zooSpec where objid=@objId";

     zooSpec2 = @" select str(p_cw,5,3) as 'Clockwise spiral probability', str(p_acw,5,3) as 'Anticlockwise spiral probability',
                        str(p_edge,5,3) as 'Edge-on spiral probablity', str(p_mg,5,3) as 'Merger system probability'
                        from zooSpec where objid=@objId";

     zooNoSpec = "select  * from  zooNoSpec where objid =@objId";

     galaxyZoo3 = "select objid,nvote,p_el,p_cs  from zooNoSpec where objid=@objId";

     zooConfidence = "select * from zooConfidence where objid=@objId";

     zooConfidence2 = " select objid,f_unclass_clean,f_misclass_clean from zooConfidence where objid=@objId";

     zooMirrorBias = "select * from zooMirrorBias where objid=@objId";

     zooMirrorBias2 = " select objid,nvote_mr1,nvote_mr2 from zooMirrorBias where objid=@objId";

     zooMonochromeBias = "select * from zooMonochromeBias where objid=@objId";

     zooMonochromeBias2 = "select objid,nvote_mon from zooMonochromeBias where objid=@objId";

     zoo2MainSpecz = "select * from zoo2MainSpecz where dr8objid=@objId";

     zoo2MainSpecz2 = @"select dr8objid, total_classifications, total_votes
                                           from zoo2MainSpecz where dr8objid=@objId";

     zoo2MainPhotoz = "select * from zoo2MainPhotoz where dr8objid=@objId";

     zoo2MainPhotoz2 = @"select dr8objid, total_classifications, total_votes
                                           from zoo2MainPhotoz where dr8objid=@objId";

     zoo2Stripe82Normal = "select * from zoo2Stripe82Normal where dr8objid=@objId";

     zoo2Stripe82Normal2 = @"select dr8objid, total_classifications, total_votes
                                                from zoo2Stripe82Normal where dr8objid=@objId";

     zoo2Stripe82Coadd1 = "select * from zoo2Stripe82Coadd1 where dr8objid=@objId";

     zoo2Stripe82Coadd1_2 = @"select dr8objid, total_classifications, total_votes
                                                from zoo2Stripe82Coadd1 where dr8objid=@objId";

     zoo2Stripe82Coadd2 = "select * from zoo2Stripe82Coadd2 where dr8objid=@objId";

     zoo2Stripe82Coadd2_2 = @"select dr8objid, total_classifications, total_votes
                                                from zoo2Stripe82Coadd2 where dr8objid=@objId";
        #endregion
    }  	