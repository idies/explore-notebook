#!/usr/bin/python
# -*- coding: utf-8 -*-
from imports import *



class Explore:

    def __init__(self, **kwargs):
        """
        constructor for explore object, uses kwargs
        
        Keyword Arguments:
        objID -- the object ID of the celestial body
        
        ra -- right ascension, must be used with dec
        dec -- declination, must be used with ra
        
        skyVersion 
        run
        rerun
        field
        obj
        
        plate -- plate observation was taken on
        fiber
        mjd -- modified julian date of observation
        """
        
        if "objID" in kwargs:
            self.exploreObjID(kwargs.pop('objID'))
        elif 'ra' in kwargs and 'dec' in kwargs:
            self.exploreRaDec(kwargs.pop('ra'), kwargs.pop('dec'))
        elif 'skyVersion' in kwargs and 'run' in kwargs and 'rerun' in kwargs and 'camcol' in kwargs and 'field' in kwargs and 'obj' in kwargs:
            self.exploreSDSS(skyVersion = kwargs.pop('skyVersion'), run = kwargs.pop('run'), rerun = kwargs.pop('rerun'), camcol = kwargs.pop('camcol'), field = kwargs.pop('field'), obj = kwargs.pop('obj'))
        elif 'plate' in kwargs and 'fiber' in kwargs and 'mjd' in kwargs:
            self.explorePlateMJDFiber(plate = kwargs.pop('plate'), mjd = kwargs.pop('mjd'), fiber = kwargs.pop('fiber'))
        else:
            raise ValueError("Invalid arguments")
    
    def _ipython_display_(self):
        CSS = """
        <style>
        body {
            margin: 0;
            font-family: Arial;
        }
        table.dataframe {
            border-collapse: collapse;
            border: none;
        }
        table.dataframe tr, table.dataframe th {
            border: none;
        }
        table.dataframe tr td:nth-child(odd), table.dataframe tr th:nth-child(odd){ 
            background: white;
        }
        table.dataframe tr td:nth-child(even), table.dataframe tr th:nth-child(even){
            background: lightgray
        }
        table.dataframe thead {
            border-bottom: 2px gray solid;
        }
        table.dataframe td, table.dataframe th {
            margin: 0;
            padding-left: 0.25em;
            padding-right: 0.25em;
        }
        </style>
        """
        
        
        try:
            self.alldata
            basic = "<h3>Basic Data</h3>" + self.getBasicData().to_html(index = False)
            imaging = "<h3>Imaging Data</h3>" +self.getImagingData().to_html(index = False)
            spec = "<h3>Spectral Data</h3>" +self.getSpecData().to_html(index = False)
            display(HTML(CSS))
            display(HTML(basic))
            display(HTML(self.getFlagHTML()))
            display(HTML(imaging))
            self.getImage()
            if self.image is not None:
                plt.axis('off')
                plt.imshow(self.image, interpolation = 'nearest', shape = (400, 400))
                plt.show()
            display(HTML(spec))
            self.getSpectrumImage()
            if self.specIm is not None:
                self.specThumbnail = self.specIm.copy()
                self.specThumbnail.thumbnail((512, 512))
                display(self.specThumbnail)
        except Exception as e:
            print ("ERROR in disp")
            print(e)

    def exploreObjID(self, objID):
        """
        Retrieves data from SkyServer using the given objID
        Stores most data in the data object, a dataframe
        parsed flags are stored in flagStrs
        images are not generated for performance reasons
        """

        sql_query = """
        SELECT p.type, p.ra, p.dec, p.run, p.rerun, p.camcol, p.field, p.obj, p.specObjID, p.objID, p.l, p.b, p.type, p.u, p.g, p.r, p.i, p.z, p.err_u, p.err_g, p.err_r, p.err_i, p.err_z, p.flags, p.mjd AS ImageMJD, p.mode, p.parentID, p.nChild, p.extinction_r, p.petroRad_r, p.petroRadErr_r, Photoz.z AS Photoz, Photoz.zerr AS Photoz_err, zooSpec.spiral AS Zoo1Morphology_spiral, zooSpec.elliptical AS Zoo1Morphology_elliptical, zooSpec.uncertain AS Zoo1Morphology_uncertain, s.instrument, s.class, s.z, s.zErr, s.survey, s.programname, s.sourcetype, s.velDisp, s.velDispErr, s.plate, s.mjd AS specMJD, s.fiberID
        FROM PhotoObj AS p
        LEFT JOIN Photoz 
        ON Photoz.objID = p.objID
        LEFT JOIN zooSpec 
        ON zooSpec.objID = p.objID
        LEFT JOIN SpecObj AS s 
        ON s.specObjID = p.specObjID
        WHERE p.objID=
        """ + str(objID)
        try:
            datadf = SkyServer.sqlSearch(sql=sql_query)
        except Exception as e:
            print(e)
        else:
            if datadf.empty:
                print('There are currently no objects with this object ID. Please verify your input and try again')
            else:
                datadf['mode'] = pd.Series([parseMode(datadf['mode'][0])])
                datadf['mjd_date'] = pd.Series([mjdToYYYYMMDD(datadf['ImageMJD'][0])])
                datadf['type'] = pd.Series([parseType(datadf['type'][0])])
                datadf.insert(2, 'ra_sexagesimal',
                              pd.Series([raToSexagesimal(datadf['ra'][0])]))
                datadf.insert(3, 'dec_sexagesimal',
                              pd.Series([decToSexagesimal(datadf['dec'][0])]))

                self.alldata = datadf
                self.flagStrs = getFlagStrings(self.alldata['flags'][0])

    def exploreRaDec(self, ra, dec):
        sql_query = """
        SELECT objID
        from dbo.fGetNearestObjEq(""" + str(ra) + """, """ + str(dec) + """,1) 
        """
        try:
            objID = SkyServer.sqlSearch(sql = sql_query)['objID'][0]
        except Exception as e:
            print(e)
        else:
            self.exploreObjID(objID)

    def exploreSDSS(self, skyVersion, run, rerun, camcol, field, obj):
        sql_query = """
        SELECT [dbo].[fObjidFromSDSS](""" + str(skyVersion) + """, """ + str(run) + """, """ + str(rerun) + """, """ + str(camcol) + """, """ + str(field) + """, """ + str(obj) + """) AS Objid
        """
        print(sql_query)
        objID = SkyServer.sqlSearch(sql = sql_query)['Objid'][0]
        self.exploreObjID(objID)
        
    def explorePlateMJDFiber(self, plate, mjd, fiber):
        sql_query = """
        SELECT p.objID
        FROM SpecObj AS s
        LEFT JOIN PhotoObj as p
        ON p.specObjID = s.specObjID
        WHERE s.plate = """ + str(plate) + " AND s.mjd = " + str(mjd) + " AND s.fiberID = " + str(fiber)
        try:
            objID = SkyServer.sqlSearch(sql = sql_query)['objID'][0]
        except Exception as e:
            print("ERROR: ")
            print(e)
        else:
            self.exploreObjID(objID)
        
        

    def getImage(self):
        """Retrieve the image from SkyServer using already retreived coordinates"""

        try:
            self.alldata
            retrImage = getImage(self.alldata['ra'][0], self.alldata['dec'][0])
            if retrImage is None:
                raise Exception
            self.image = retrImage
        except Exception as e:
            self.image = None
            print(e)
            
    def getSpectrumImage(self):
        """Retrieve the spectrum image from specobj"""
        try:
            self.alldata
            sql_query = """
            SELECT img 
            FROM SpecObj AS s
            WHERE s.specObjID = """ + str(self.get('specObjID'))
            imgStr = SkyServer.sqlSearch(sql = sql_query)['img'][0]
            img = Image.open(io.BytesIO(bytes.fromhex(imgStr[2:])))
            self.specIm = img
            return img
        except Exception as e:
            self.specIm = None
            return None

    def getSpecData(self):
        """
        Returns the spectral datapoints from the dataframe. Expects an explore function to have already been called
        so the dataframe is populated. Will return nothing if the dataframe isn't populated.
        """

        try:
            self.alldata
            specCols = [
                'instrument',
                'class',
                'z',
                'zErr',
                'survey',
                'programname',
                'sourcetype',
                'velDisp',
                'velDispErr',
                'plate',
                'specMJD',
                'fiberID',
                ]
            return self.alldata[specCols]
        except:
            print('No data retrieved yet. Use an explore function')

    def getImagingData(self):
        """
        Returns the imaging datapoints from the dataframe. Expects an explore function to have already been called
        so the dataframe is populated. Will return nothing if the dataframe isn't populated.
        """

        try:
            self.alldata
            imagingCols = [
                'u',
                'g',
                'r',
                'i',
                'z',
                'err_u',
                'err_g',
                'err_r',
                'err_i',
                'err_z',
                'ImageMJD',
                'mode',
                'parentID',
                'nChild',
                'extinction_r',
                'petroRad_r',
                'mjd_date',
                'Photoz',
                'Photoz_err',
                'Zoo1Morphology_elliptical',
                'Zoo1Morphology_spiral',
                'Zoo1Morphology_uncertain',
                ]
            return self.alldata[imagingCols]
        except:
            print('No data retrieved yet. Use an explore function')

    def getBasicData(self):
        """
        Returns the basic datapoints from the dataframe. Expects an explore function to have already been called
        so the dataframe is populated. Will return nothing if the dataframe isn't populated.
        """

        try:
            self.alldata
            basicCols = [
                'type',
                'ra',
                'dec',
                'ra_sexagesimal',
                'dec_sexagesimal',
                'run',
                'rerun',
                'camcol',
                'field',
                'obj',
                'specObjID',
                'l',
                'b',
                ]
            return self.alldata[basicCols]
        except:
            print('No data retrieved yet. Use an explore function')
            
    def getFlagHTML(self):
        """
        Returns the flags in html form for ipython display
        """
        list = "<h4>Flags:</h4><p>"
        for f in self.flagStrs:
            list += f
            list += ", "
        list = list[0: -2]
        list += "</p>"
        return list
        
    def get(self, field):
        """syntactic sugar to make accessing data easier"""
        return self.alldata[field][0]


def getImage(
    ra,
    dec,
    scale=0.7,
    width=600,
    height=600,
    ):
    """Retrieve the image from SkyServer using the passed coordinates"""
    try:
        img = SkyServer.getJpegImgCutout(ra, dec, scale, width, height, opt='GLS')
        return img
    except Exception as e: 
        print("ERROR: ")
        print(e)


def decToSexagesimal(dec):
    """converts declination coordinates in decimal degrees to sexagesimal"""
    a = Angle(dec * u.deg)
    return a.to_string(sep=':')


def raToSexagesimal(ra):
    """converts right ascension coordinates in decimal degrees to sexagesimal"""
    ras = ''
    if ra < 0:
        ras = '-'
        ra = abs(ra)
    h = int(ra / 15)
    m = int((ra / 15 - h) * 60)
    s = ((ra / 15 - h) * 60 - m) * 60
    return '{}:{}:{}'.format(h, m, s)


def parseType(i):
    """parses the type of the object to a string"""
    typeMappings = {
        0: 'UNKNOWN',
        1: 'COSMIC_RAY',
        2: 'DEFECT',
        3: 'GALAXY',
        4: 'GHOST',
        5: 'KNOWNOBJ',
        6: 'STAR',
        7: 'TRAIL',
        8: 'SKY',
        9: 'NOTATYPE',
        }
    return typeMappings[i]


def parseMode(i):
    """parses the mode of a the photo to a string"""
    modeMappings = {1: 'PRIMARY', 2: 'SECONDARY', 3: 'OTHER'}
    return modeMappings[i]


def mjdToYYYYMMDD(mjd):
    """converts mjd date of the observation of the star to YYYY/MM/DD format"""

    t = Time(mjd, format='mjd', scale='utc', out_subfmt='date')
    return t.iso


def getFlagStrings(flags):
    """Parses the flag Bitmask to the strings they represent"""

    flagBits = {
        'CANONICAL_CENTER': 1 << 0,
        'BRIGHT': 1 << 1,
        'EDGE': 1 << 2,
        'BLENDED': 1 << 3,
        'CHILD': 1 << 4,
        'PEAKCENTER': 1 << 5,
        'NODEBLEND': 1 << 6,
        'NOPROFILE': 1 << 7,
        'NOPETRO': 1 << 8,
        'MANYPETRO': 1 << 9,
        'NOPETRO_BIG': 1 << 10,
        'DEBLEND_TOO_MANY_PEAKS': 1 << 11,
        'CR': 1 << 12,
        'MANYR50': 1 << 13,
        'MANYR90': 1 << 14,
        'BAD_RADIAL': 1 << 15,
        'INCOMPLETE_PROFILE': 1 << 16,
        'INTERP': 1 << 17,
        'SATUR': 1 << 18,
        'NOTCHECKED': 1 << 19,
        'SUBTRACTED': 1 << 20,
        'NOSTOKES': 1 << 21,
        'BADSKY': 1 << 22,
        'PETROFAINT': 1 << 23,
        'TOO_LARGE': 1 << 24,
        'DEBLENDED_AS_PSF': 1 << 25,
        'DEBLEND_PRUNED': 1 << 26,
        'ELLIPFAINT': 1 << 27,
        'BINNED1': 1 << 28,
        'BINNED2': 1 << 29,
        'BINNED4': 1 << 30,
        'MOVED': 1 << 31,
        'DEBLENDED_AS_MOVING': 1 << 32,
        'NODEBLEND_MOVING': 1 << 33,
        'TOO_FEW_DETECTIONS': 1 << 34,
        'BAD_MOVING_FIT': 1 << 35,
        'STATIONARY': 1 << 36,
        'PEAKS_TOO_CLOSE': 1 << 37,
        'BINNED_CENTER': 1 << 38,
        'LOCAL_EDGE': 1 << 39,
        'BAD_COUNTS_ERROR': 1 << 40,
        'BAD_MOVING_FIT_CHILD': 1 << 41,
        'DEBLEND_UNASSIGNED_FLUX': 1 << 42,
        'SATUR_CENTER': 1 << 43,
        'INTERP_CENTER': 1 << 44,
        'DEBLENDED_AT_EDGE': 1 << 45,
        'DEBLEND_NOPEAK': 1 << 46,
        'PSF_FLUX_INTERP': 1 << 47,
        'TOO_FEW_GOOD_DETECTIONS': 1 << 48,
        'CENTER_OFF_AIMAGE': 1 << 49,
        'DEBLEND_DEGENERATE': 1 << 50,
        'BRIGHTEST_GALAXY_CHILD': 1 << 51,
        'CANONICAL_BAND': 1 << 52,
        'AMOMENT_UNWEIGHTED': 1 << 53,
        'AMOMENT_SHIFT': 1 << 54,
        'AMOMENT_MAXITER': 1 << 55,
        'MAYBE_CR': 1 << 56,
        'MAYBE_EGHOST': 1 << 57,
        'NOTCHECKED_CENTER': 1 << 58,
        'HAS_SATUR_DN': 1 << 59,
        'DEBLEND_PEEPHOLE': 1 << 60,
        }
    flagStrs = []
    for (k, v) in flagBits.items():
        if flags & v:
            flagStrs.append(k)
    return flagStrs



			