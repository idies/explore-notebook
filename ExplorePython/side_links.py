#coding: utf-8
#!/usr/bin/env python import *


from imports import *


def ExploreQueries():
    {

     # Left Side panel of the Explore Page
     #photoObj
    public static string PhotoObjQuery = "select * from PhotoObjAll where objId=@objId";


     #photoTag
    public static string PhotoTagQuery = "select * from PhotoTag where objId=@objId";


     #Field
    public static string FieldQuery = "select * from Field where fieldId =@fieldId";


     #Frame: this are all columns except for column "img"
    public static string FrameQuery = "select fieldID,zoom,run,rerun,camcol,field,stripe,strip,a,b,c,d,e,f,node,incl,raMin,raMax,decMin,decMax,mu,nu,ra,dec,cx,cy,cz,htmID,'not displayed' as 'img' from Frame where fieldId=@fieldId";
     #public static string FrameQuery = "select * from Frame where fieldId=@fieldId";
     #specObjall
    public static string SpecObjQuery = "select * from SpecObjAll where specObjId=@specId";


     #sppLines
    public static string sppLinesQuery = "select * from sppLines where specObjId=@specId";


     #sppParams
    public static string sppParamsQuery = "select * from sppParams where specObjId=@specId";


     #galspec
    public static string galSpecLineQuery = "select * from galSpecLine where specObjId=@specId";


     #galspecIndex
    public static string galSpecIndexQuery = "select * from galSpecIndx where specObjId=@specId";


     #galspecInfo
    public static string galSpecInfoQuery = "select * from galSpecInfo where specObjId=@specId";


     #stellarMassStarformingPort
    public static string stellarMassStarformingPortQuery = @"select * from stellarMassStarformingPort where specObjId=@specId";

     #stellarMassPassivePort
    public static string stellarMassPassivePortQuery = @"select * from stellarMassPassivePort where specObjId=@specId ";


     #emissionLinesPort
    public static string emissionLinesPortQuery = "select * from emissionLinesPort where specObjId=@specId";


     #stellarMassPCAWiscBC03
    public static string stellarMassPCAWiscBC03Query = "select * from stellarMassPCAWiscBC03 where specObjId=@specId";


     #stellarMassPCAWiscM11
    public static string stellarMassPCAWiscM11Query = "select * from stellarMassPCAWiscM11 where specObjId=@specId";


     #For DR10 and above
     #stellarMassFSPSGranEarlyDust
    public static string stellarMassFSPSGranEarlyDust = "select * from stellarMassFSPSGranEarlyDust where specObjId=@specId";


     #stellarMassFSPSGranEarlyNoDust
    public static string stellarMassFSPSGranEarlyNoDust = "select * from stellarMassFSPSGranEarlyNoDust where specObjId=@specId";


     #stellarMassFSPSGranWideDust
    public static string stellarMassFSPSGranWideDust = "select * from stellarMassFSPSGranWideDust where specObjId=@specId";


     #stellarMassFSPSGranWideDust
    public static string stellarMassFSPSGranWideNoDust = "select * from stellarMassFSPSGranWideNoDust where specObjId=@specId";


     #apogeeStar
    public static string apogeeStar = "select * from apogeeStar where apstar_id=@apid"; # note that @apid is a string, and has to be checked against sql injection before sending the query.
     # HttpUtility.UrlEncode("'" + apogeeId + "'");

     #aspcapStar
    public static string aspcapStar = "select * from aspcapStar where apstar_id=@apid"; # note that @apid is a string, and has to be checked against sql injection before sending the query.
     #+HttpUtility.UrlEncode("'" + apogeeId + "'");      

     #PhotoZ
    public static string PhotoZ = "select * from Photoz where objid=@objId";
     #string c1 = "select * from Photoz2 where objid=" + objid;       

     #PhotzRF
     #public static string PhotozRF= "select * from PhotozRF where objid=@objId";
     #string c2 = "select * from Photoz2 where objid=" + objid;

    #region plate
     #Plate
    public static string Plate = "select * from PlateX where plateId=@plateId";

    public static string PlateShow = @" select cast(specObjID as binary(8)) as specObjId, fiberId, class as name, str(z,5,3) as z 
                            from SpecObjAll where plateID=@plateId order by fiberId";

    #endregion
    #region AllSpectra
         # #AllSpec Queries
    public static string AllSpec1 = @"select s.specObjId, s.plate as plate, s.mjd as MJD, s.fiberID as fiber, 
                        str(t.ra,10,5) as ra, str(t.dec,10,5) as dec, str(s.ra,10,5) as specRa, str(s.dec,10,5) as specDec, s.sciencePrimary, 
                        str(dbo.fDistanceArcMinEq(t.ra,t.dec,s.ra,s.dec),10,8) as distanceArcMin, s.class as class  
                        from SpecObjAll s, photoobjall t
                        where t.objid=@objId  and s.bestobjid=t.objid  order by scienceprimary desc, plate, MJD, fiber";


    public static string AllSpec2 = @"select s.specObjId, s.plate as plate, s.mjd as MJD, s.fiberID as fiber, str(t.ra,10,5) as ra, str(t.dec,10,5) as dec, 
                        str(s.ra,10,5) as specRa, str(s.dec,10,5) as specDec,  s.sciencePrimary, 
                        str(dbo.fDistanceArcMinEq(t.ra,t.dec,s.ra,s.dec),10,8) as distanceArcMin, s.class as class  
                        from SpecObjAll s, photoobjall t 
                        where t.objid=@objId  and s.fluxobjid=t.objid order by  plate, MJD, fiber, 
                        scienceprimary desc, distanceArcMin asc";

    #endregion

    #region matches
     # # #Matches Queries
    public static string matches1 = @"select dbo.fIAUFromEq(p.ra,p.dec) as 'IAU name', p.objid, p.thingid, dbo.fPhotoModeN(p.mode) as 'mode description'
                                    from Photoobjall p where p.objid=@objId";


     #*        public static string matches2  = @" select t.objid, t.thingid, p.mode, dbo.fPhotoModeN(p.mode) as '(mode description)'
                                            from thingindex t join photoobjall p on t.objid = p.objid 
                                            where t.objid=@objId and p.mode != 1 order by p.mode";
    * #
    public static string matches2 = @" select d.objid, d.thingid, p2.mode, dbo.fPhotoModeN(p2.mode) as 'mode description'
                                    from thingIndex t join detectionIndex d on t.thingId=d.thingId join phototag p on t.objid = p.objid join phototag p2 on d.objid = p2.objid 
                                    where t.objid=@objId order by p2.mode";






    #endregion

    #region neighbors
     # # #Neighbors
    public static string neighbors1 = @" select dbo.fIAUFromEq(p.ra,p.dec) as 'IAU name', p.objid, p.thingid from photoobjall p where p.objid=@objId";


    public static string neighbors2 = @" select n.neighborObjId as objId,str(t.ra,10,5) as ra, str(t.dec,10,5) as dec, str(n.distance,5,3) as 'distance (arcmin)',
                            dbo.fPhotoTypeN(n.neighborType) as type, neighborMode as mode, dbo.fPhotoModeN(n.neighborMode) as '(mode description)'
                            from Neighbors n, photoobjall t where n.neighborObjid=t.objid and n.objId=@objId order by n.distance asc ";

    #endregion

    #region fits_parameters
     # # # Fits Parameters Queries
    public static string fitsParametersSppParams = @" select targetstring as 'Targeting criteria', flag as 'SEGUE flags',spectypehammer as 'HAMMER spectral type', SPECTYPESUBCLASS as 'Spectral subclass',
                    str(elodiervfinal,7,2) as 'Radial velocity (km #s)', str(elodiervfinalerr,8,3) as 'RV error', str(teffadop,6,0) as 'Effective temp (K)', 
                    str(teffadopunc,6,1) as 'Teff error' , str(fehadop,7,2) as '[Fe #H] (dex)', str(fehadopunc,8,3) as '[Fe #H] error', str(loggadop,7,2) as 'log<sub>10< #sub>(g) (dex)', 
                    str(loggadopunc,8,3) as 'log<sub>10< #sub>(g) error' from sppParams where specObjId=@specId";


    public static string fitsParametersStellarMassStarformingPort = @"  select logMass as 'Best-fit log<sub>10< #sub>(stellar mass)',minLogMass as '1-&#963 min', maxLogMass as '1-&#963 max',
                    age as 'Best-fit age (Gyr)', minAge as '1-&#963 min Age', maxAge as '1-&#963 max Age',
                    SFR as 'Best-fit SFR (M<sub>&#9737< #sub>  # yr)', minSFR as '1-&#963 min SFR', maxSFR as '1-&#963 max SFR' 
                    from stellarMassStarformingPort where specObjId=@specId";

    public static string fitsParameterSstellarMassPassivePort = @" select logMass as 'Best-fit log<sub>10< #sub>(stellar mass)', minLogMass as '1-&#963 min', maxLogMass as '1-&#963 max'
                     , age as 'Best-fit age (Gyr)', minAge as '1-&#963 min Age', maxAge as '1-&#963 max Age', SFR as 'Best-fit SFR (M<sub>&#9737< #sub>  # yr)',
                     minSFR as '1-&#963 min SFR', maxSFR as '1-&#963 max SFR' 
                     from stellarMassPassivePort where specObjId=@specId";

    public static string fitsParametersEmissionLinesPort = @" select velstars as 'Stellar velocity (km #s)',sigmaStars as 'Stellar velocity disperson (km #s)', 
                                                            sigmaStarsErr as 'Velocity dispersion error' ,chisq as 'Chi-squared fit of template',
                                                            bpt as 'BPT classification' from emissionLinesPort where specObjId=@specId";


    public static string fitsParametersStellarMassPCAWiscBC03 = @" select str(mstellar_median,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)',
                                                                str(mstellar_err,8,3) as 'Error', str(vdisp_median,8,2) as 'Median veldisp (km #s)', str(vdisp_err,9,3) as 'Error VelDisp'
                                                                from stellarMassPCAWiscBC03 where specObjId=@specId";

    public static string fitsParametersstellarMassPCAWiscM11 = @"select str(mstellar_median,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', str(mstellar_err,8,3) as 'Error',
                                                                str(vdisp_median,8,2) as 'Median veldisp (km #s)', str(vdisp_err,9,3) as 'Error VelDisp'
                                                                from stellarMassPCAWiscM11 where specObjId=@specId";

    public static string fitsParametersStellarmassFSPSGranEarlyDust = @"select str(logmass,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', str(logmass_err,8,3) as 'Error', 
                                                                      str(age,8,2) as 'Age (Gyr)', 
                                                                      str(ssfr,8,2) as 'SSFR', str(metallicity,8,2) as 'metallicity'
                                                                      from stellarmassFSPSGranEarlyDust where specObjId=@specId";

    public static string fitsParametersStellarmassFSPSGranEarlyNoDust = @"select str(logmass,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', 
                                                                        str(logmass_err,8,3) as 'Error', str(age,8,2) as 'Age (Gyr)', 
                                                                        str(ssfr,8,2) as 'SSFR', str(metallicity,8,2) as 'metallicity'
                                                                        from stellarmassFSPSGranEarlyNoDust where specObjId=@specId";

    public static string fitsParametersStellarmassFSPSGranWideDust = @"select str(logmass,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', str(logmass_err,8,3) as 'Error',
                                                                    str(age,8,2) as 'Age (Gyr)', 
                                                                    str(ssfr,8,2) as 'SSFR', str(metallicity,8,2) as 'metallicity'
                                                                    from stellarmassFSPSGranWideDust where specObjId=@specId";

    public static string fitsParametersStellarmassFSPSGranWideNoDust = @"select str(logmass,7,2) as 'Best-fit log<sub>10< #sub>(stellar mass)', str(logmass_err,8,3) as 'Error',
                                                                        str(age,8,2) as 'Age (Gyr)', 
                                                                        str(ssfr,8,2) as 'SSFR', str(metallicity,8,2) as 'metallicity'
                                                                        from stellarmassFSPSGranWideNoDust where specObjId=@specId";

    #endregion

    #region galaxyzoo
     # #GalaxyZooQueries
    public static string zooSpec = "select * from zooSpec where objid=@objId";


    public static string zooSpec1 = @"select objid,nvote as 'Votes',str(p_el_debiased,5,3) 'Elliptical proabability (debiased)',
                         str(p_cs_debiased,5,3) 'Spiral probability (debiased)'
                         from zooSpec where objid=@objId";

    public static string zooSpec2 = @" select str(p_cw,5,3) as 'Clockwise spiral probability', str(p_acw,5,3) as 'Anticlockwise spiral probability',
                        str(p_edge,5,3) as 'Edge-on spiral probablity', str(p_mg,5,3) as 'Merger system probability'
                        from zooSpec where objid=@objId";

    public static string zooNoSpec = "select  * from  zooNoSpec where objid =@objId";

    public static string galaxyZoo3 = "select objid,nvote,p_el,p_cs  from zooNoSpec where objid=@objId";

    public static string zooConfidence = "select * from zooConfidence where objid=@objId";

    public static string zooConfidence2 = " select objid,f_unclass_clean,f_misclass_clean from zooConfidence where objid=@objId";

    public static string zooMirrorBias = "select * from zooMirrorBias where objid=@objId";

    public static string zooMirrorBias2 = " select objid,nvote_mr1,nvote_mr2 from zooMirrorBias where objid=@objId";

    public static string zooMonochromeBias = "select * from zooMonochromeBias where objid=@objId";

    public static string zooMonochromeBias2 = "select objid,nvote_mon from zooMonochromeBias where objid=@objId";

    public static string zoo2MainSpecz = "select * from zoo2MainSpecz where dr8objid=@objId";

    public static string zoo2MainSpecz2 = @"select dr8objid, total_classifications, total_votes
                                           from zoo2MainSpecz where dr8objid=@objId";

    public static string zoo2MainPhotoz = "select * from zoo2MainPhotoz where dr8objid=@objId";

    public static string zoo2MainPhotoz2 = @"select dr8objid, total_classifications, total_votes
                                           from zoo2MainPhotoz where dr8objid=@objId";

    public static string zoo2Stripe82Normal = "select * from zoo2Stripe82Normal where dr8objid=@objId";

    public static string zoo2Stripe82Normal2 = @"select dr8objid, total_classifications, total_votes
                                                from zoo2Stripe82Normal where dr8objid=@objId";

    public static string zoo2Stripe82Coadd1 = "select * from zoo2Stripe82Coadd1 where dr8objid=@objId";

    public static string zoo2Stripe82Coadd1_2 = @"select dr8objid, total_classifications, total_votes
                                                from zoo2Stripe82Coadd1 where dr8objid=@objId";

    public static string zoo2Stripe82Coadd2 = "select * from zoo2Stripe82Coadd2 where dr8objid=@objId";

    public static string zoo2Stripe82Coadd2_2 = @"select dr8objid, total_classifications, total_votes
                                                from zoo2Stripe82Coadd2 where dr8objid=@objId";
        #endregion
    }