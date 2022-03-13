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


def getDataFromWFS():
    typenames = "Flurstueck"
    count = "10"
    namespace = ""

    urlGETFeature = WFS_dictionary["nrw_alkis_vereinfacht"] + "Service=WFS&REQUEST=GetFeature&VERSION=2.0.0&TYPENAMES=" + \
          typenames + "&COUNT=" + count
    urlDescribeFeatureType = WFS_dictionary["nrw_alkis_vereinfacht"] + "Service=WFS&Request=DescribeFeatureType&version=2.0&Typename=" + typenames
    request = requests.get(urlGETFeature, allow_redirects=True)
    open("TestData/dataFromWFS.xml", 'wb').write(request.content)


def getCapabilities():
    urlGetCapabilities = WFS_dictionary["nrw_alkis_vereinfacht"] + "Service=WFS&Request=GetCapabilities"
    request = requests.get(urlGetCapabilities, allow_redirects=True)
    open("TestData/wfs_capabilities.xml", 'wb').write(request.content)


def testCall():
    request = requests.get(WFS_dictionary["Berlin"] + "Service=WFS&Request=GetFeature&VERSION=2.0.0&TYPENAME=flurstueck", allow_redirects=True)
    open("TestData/wfs_test.xml", 'wb').write(request.content)


WFS_dictionary = {
    "nrw_alkis_vereinfacht": "https://www.wfs.nrw.de/geobasis/wfs_nw_alkis_vereinfacht?", # funktioniert
    "Berlin": "https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_wfs_alkis?", # funktioniert, aber erkennt typename=flurstueck nicht
    "Thüringen": "http://www.geoproxy.geoportal-th.de/geoproxy/services?", #auth notwendig
    "Brandenburg": "https://isk.geobasis-bb.de/ows/alkis_vereinf_wfs?",
    "mecklenburg-vorpommern": "https://www.geodaten-mv.de/dienste/alkis_wfs_sf",
    "hamburg": "https://geodienste.hamburg.de/WFS_HH_ALKIS_vereinfacht?",
    "sachsen": "", #kein wfs auffindbar, nur download https://www.geodaten.sachsen.de/batch-download-4719.html



    "bayern": "https://geoservices.bayern.de/wfs/v1/ogc_alkis_ave.cgi?", # muss von kundenservice freigeschaltet werden
    "Sachsen-Anhalt": "", # kostenpflichtig
    "Reinland-pfalz": "", # kostenpflichtig https://www.geoportal.rlp.de/spatial-objects/353

    #https://fbinter.stadt-berlin.de/fb_daten/beschreibung/datenformatbeschreibung/datenformatbeschreibung_alkis_berlin.pdf
}

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

