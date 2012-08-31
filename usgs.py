from lxml import etree
import urllib

def getAltitudeUSGS(lat, lon):
    print "getAltitudeUSGS(%s, %s)" % (lat, lon)

    url = "http://gisdata.usgs.net/xmlwebservices2/elevation_service.asmx/getElevation"

    params = {
        'X_Value'           : lon,
        'Y_Value'           : lat,
        'Elevation_Units'   : 'meters',
        'Source_Layer'      : '',
        'Elevation_Only'    : ''
    }
    
    print "Params: %s" % (str(params))

    print "URL: %s?%s" % (url, urllib.urlencode(params))
    
    f = urllib.urlopen(url,  urllib.urlencode(params))

    doc = etree.fromstring(f.read())

    alt = float(doc.find('Elevation_Query').find('Elevation').text)

    f.close()

    return alt

print getAltitudeUSGS(41.7296877, -87.5578934)