from datetime import datetime

import requests
import urllib.request
import zipfile
import os

downloadFolder = "D://repos/Uni/BA/ALKIS-transform/TestData/"


def getDataAsDownload(bundesland, gemeindenummer):
# alkisdatenschlüssel = 2oAZg0U07akQOCK
# download zip archive mit gemeindenummer von sachsen als zip
    urllib.request.urlretrieve("https://geocloud.landesvermessung.sachsen.de/index.php/s/UXVzrdm4WeOhkhR/download?path=%2F&files="
                               + gemeindenummer +".xml.zip", downloadFolder +"/" + bundesland + gemeindenummer + ".xml.zip")
    unZipFiles(bundesland, gemeindenummer)
    deleteZip(bundesland, gemeindenummer)

def unZipFiles(bundesland, gemeindenummer):
    with zipfile.ZipFile(downloadFolder + bundesland + gemeindenummer + ".xml.zip", "r") as zip_ref:
        zip_ref.extractall(downloadFolder + bundesland + gemeindenummer)
    for files in os.listdir(downloadFolder + bundesland + gemeindenummer):
        with zipfile.ZipFile(downloadFolder + bundesland + gemeindenummer + "/" + files, "r") as zip_ref:
            zip_ref.extractall(downloadFolder + bundesland + gemeindenummer)
    deleteZip(bundesland, gemeindenummer)


def getDataFromWFS(bundesland, gemarkung=None):


    response = requests.get(createGetFeatureURL(bundesland, gemarkung), allow_redirects=True)

    if "NAS" in bundesland:
        with open("TestData/"+bundesland[0:3]+"/NAS-konform.xml", 'wb') as file:
            file.write(response.content)
    elif "AAA" in bundesland:
        with open("TestData/"+bundesland[0:3]+"/AAA-basiert.xml", 'wb') as file:
            file.write(response.content)
    elif "vereinfacht" in bundesland:
        with open("TestData/"+bundesland[0:3]+"/vereinfachtes-schema.xml", 'wb') as file:
            file.write(response.content)
    else:
        with open("TestData/"+bundesland[0:3]+"/unbekanntes-schema.xml", 'wb') as file:
            file.write(response.content)


def createGetFeatureURL(bundesland, gemarkung=None):
    if ("vereinfacht" in bundesland):
        typenames = "ave:Flurstueck"
        namespaces = "xmlns(ave,http://repository.gdi-de.org/schemas/adv/produkt/alkis-vereinfacht/2.0)"
        count = "10"
        if gemarkung != None:
            filter = "<fes:Filter xmlns='http://www.opengis.net/ogc' xmlns:fes='http://www.opengis.net/fes/2.0' xmlns:gml='http://www.opengis.net/gml/3.2'>" \
                     "  <fes:PropertyIsEqualTo>" \
                     "  <fes:ValueReference>ave:gemarkung</fes:ValueReference>" \
                     "    <fes:Literal>" + gemarkung + "</fes:Literal>" \
                                                       "  </fes:PropertyIsEqualTo>" \
                                                       "</fes:Filter>"
            urlGETFeature = WFS_dictionary[bundesland] + "Service=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=" + \
                            typenames + "&NAMESPACES=" + namespaces + "&COUNT=" + count + "&FILTER=" + filter
        else:
            urlGETFeature = WFS_dictionary[bundesland] + "Service=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=" + \
                            typenames + "&NAMESPACES=" + namespaces + "&COUNT=" + count
    else:
        typenames = "AX_Flurstueck"
        count = "10"
        namespaces = "xmlns(ave,http://repository.gdi-de.org/schemas/adv/produkt/alkis-vereinfacht/2.0)"
        filter = "<fes:Filter xmlns='http://www.opengis.net/ogc' xmlns:fes='http://www.opengis.net/fes/2.0' xmlns:gml='http://www.opengis.net/gml/3.2'>" \
             "  <fes:PropertyIsEqualTo>" \
             "  <fes:ValueReference>gemarkungsnummer</fes:ValueReference>" \
             "    <fes:Literal>" + gemarkung + "</fes:Literal>" \
            "  </fes:PropertyIsEqualTo>" \
                 "</fes:Filter>"
        urlGETFeature = WFS_dictionary[bundesland] + "Service=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=" + \
                    typenames + "&COUNT=" + count + "&FILTER=" + filter
    return urlGETFeature


def createDir(bundesland):
    directory = bundesland[0:3]
    if os.path.exists(directory):
        os.makedirs("TestData/" + directory)


def getCapabilities():
    urlGetCapabilities = WFS_dictionary["nrw_alkis_vereinfacht"] + "Service=WFS&Request=GetCapabilities"
    request = requests.get(urlGetCapabilities, allow_redirects=True)
    open("TestData/wfs_capabilities.xml", 'wb').write(request.content)


WFS_dictionary = {
    "NRW-vereinfacht": "https://www.wfs.nrw.de/geobasis/wfs_nw_alkis_vereinfacht?",
    "NRW-AAA-basiert": "https://www.wfs.nrw.de/geobasis/wfs_nw_alkis_aaa-modell-basiert?",
    "NRW-NAS-konform": "https://www.wfs.nrw.de/geobasis/wfs_nw_alkis_nas-konform?",
    #"Berlin": "https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_wfs_alkis?", # typenames wird nicht erkannt
    #"Thüringen": "http://www.geoproxy.geoportal-th.de/geoproxy/services?", #auth notwendig
    "Brandenburg-vereinfacht": "https://isk.geobasis-bb.de/ows/alkis_vereinf_wfs?",
    "Brandenburg-AAA-basiert": "https://isk.geobasis-bb.de/ows/alkis_sf_wfs?",
    "Brandenburg-NAS-konform": "https://isk.geobasis-bb.de/ows/alkis_nas_wfs?SERVICE=WFS&",
   # "Mecklenburg-vorpommern": "https://www.geodaten-mv.de/dienste/alkis_wfs_einfach?",#auth
    "Hamburg-vereinfacht": "https://geodienste.hamburg.de/WFS_HH_ALKIS_vereinfacht?",
    "Sachsen-vereinfacht": "https://geodienste.sachsen.de/aaa/public_alkis/vereinf/wfs?",
    #"Bayern": "https://geoservices.bayern.de/wfs/v1/ogc_alkis_ave.cgi?", # muss von kundenservice freigeschaltet werden
    #"Sachsen-Anhalt": "", #kostenpflichtig
    #"Reinland-pfalz": "", #kostenpflichtig https://www.geoportal.rlp.de/spatial-objects/353
    "Hessen-vereinfacht": "https://www.gds.hessen.de/wfs2/aaa-suite/cgi-bin/alkis/vereinf/wfs?",
    "Hessen-NAS-konform": "https://www.gds.hessen.de/wfs2/aaa-suite/cgi-bin/alkis/nas/wfs?",
    #"Niedersachsen": "",
    #"Schleswig-Holtstein": "", #kostenpflichtig https://www.schleswig-holstein.de/DE/Landesregierung/LVERMGEOSH/Service/serviceGeobasisdaten/geodatenService_Geobasisdaten_digALKIS.html
    #"Baden-Württemberg": "",
    #"Bremen": "https://geodienste.bremen.de/wfs_flurstuecke?SERVICE=WFS&REQUEST=GetCapabilities",
    #"Saarland": "" #kostenpflichtig https://geoportal.saarland.de/spatial-objects/325?Service=WFS&Request=GetCapabilities
    #https://fbinter.stadt-berlin.de/fb_daten/beschreibung/datenformatbeschreibung/datenformatbeschreibung_alkis_berlin.pdf
}

# urheberrechtlich geschützt https://metaver.de/trefferanzeige?cmd=doShowDocument&docuuid=FA4D0ED5-EE47-4959-A620-DA34AA76663E&plugid=/ingrid-group:ige-iplug-hb
def outputDic():
    return str(WFS_dictionary.keys())

FeatureTypes = {
    "FlurstueckEigentuemer", "Flurstueck", "FlurstueckPunkt", "GebaeudeBauwerk", "KatasterBezirk", "Nutzung", "NutzungFlurstueck", "VerwaltungsEinheit"
}

#löscht nicht mehr benötigte .zip
def deleteZip(bundesland, gemeindenummer):
    os.remove(downloadFolder + bundesland + gemeindenummer + ".xml.zip")
    for files in os.listdir(downloadFolder + bundesland + gemeindenummer):
        if files[len(files)-3:len(files)] == 'zip':
            os.remove(downloadFolder + bundesland + gemeindenummer + "/" + files)

# alkis data leipzig https://geocloud.landesvermessung.sachsen.de/index.php/s/UXVzrdm4WeOhkhR/download?path=%2F&files=14713000.xml.zip

