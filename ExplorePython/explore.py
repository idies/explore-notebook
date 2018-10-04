from imports import *

class Explore:

    def __init__(self):
        pass

    def exploreObjID(self, objID):
        """
        Retrieves data from SkyServer using the given objID
        Stores most data in the data object, a dataframe
        parsed flags are stored in flagStrs\
        images are not generated for performance reasons
        """
        sql_query="""
        SELECT p.ra,p.dec,p.run,p.rerun,p.camcol,p.field,p.obj,p.specObjID,p.l,p.b,p.type,p.u,p.g,p.r,p.i,p.z,p.err_u,p.err_g,p.err_r,p.err_i,p.err_z,p.flags,p.mjd,p.mode,p.parentID,p.nChild,p.extinction_r,p.petroRad_r,p.petroRadErr_r,Photoz.z AS Photoz,Photoz.zerr AS Photoz_err
        FROM PhotoObj AS p 
        LEFT JOIN Photoz ON Photoz.objID = p.objID
        WHERE p.objID=
        """+str(objID)
        datadf=SkyServer.sqlSearch(sql=sql_query)
        if (datadf.empty):
            print("There are currently no objects with this object ID. Please verify your input and try again")
            raise ValueError
        else:
            datadf['mode'] = pd.Series([parseMode(datadf['mode'][0])])
            datadf['mjd_date'] = pd.Series([mjdToYYYYMMDD(datadf['mjd'][0])])
            datadf['ra_sexagesimal'] = pd.Series([raToSexagesimal(datadf['ra'][0])])
            datadf['dec_sexagesimal'] = pd.Series([decToSexagesimal(datadf['dec'][0])])

            self.data = datadf
            self.flagStrs = getFlagStrings(self.data['flags'][0])
            return self.data

    def getImage(self):
        """Retrieve the image from SkyServer using already retreived coordinates"""
        try:
            self.data
            self.image = getImage(self.data['ra'][0], self.data['dec'][0])
            return self.image
        except:
            print("No data retreived yet. Use an explore function")

def getImage(ra, dec, scale=0.7, width=512, height=512):
    """Retrieve the image from SkyServer using the passed coordinates"""
    return SkyServer.getJpegImgCutout(ra, dec, scale, width, height, opt="")

def decToSexagesimal(dec):
    a = Angle(dec * u.deg)
    return a.to_string(sep=':')
def raToSexagesimal(ra):
    ras = ''
    if ra < 0:
        ras = '-'
        ra = abs(ra)
    h = int(ra / 15)
    m = int((ra / 15 - h) * 60)
    s = (((ra / 15 - h) * 60) - m) * 60
    return "{}:{}:{}".format(h,m,s)



def parseMode(i):
    modeMappings = {
        1: "PRIMARY",
        2: "SECONDARY",
        3: "OTHER"
    }
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
        'DEBLEND_PEEPHOLE': 1 << 60
    }
    flagStrs = []
    for k, v in flagBits.items():
        if flags & v:
            flagStrs.append(k)
    return flagStrs
