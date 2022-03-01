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
    urlGetCapabilities = WFS_dictionary["sachsen2"] + "Service=WFS&Request=getcapabilities&version=2.0"
    urlDescribeFeatureType = WFS_dictionary["sachsen2"] + "Service=WFS&Request=DescribeFeatureType&version=2.0&Typename=" + typenames
    request = requests.get(urlGETFeature, allow_redirects=True)
    open("TestData/dataFromWFS.xml", 'wb').write(request.content)

WFS_dictionary = {
    "nrw_alkis_vereinfacht": "https://www.wfs.nrw.de/geobasis/wfs_nw_alkis_vereinfacht?",
    "sachsen": "https://gdi-sbv.list.smwa.sachsen.de/alkis/wfs?", # not working
    "sachsen2": "https://geoportal.sachsen.de/md/ca666411-fba1-472e-8bb5-873543ca0b11?",

    "Mecklenburg-Vorpommern": "",
    "Hamburg": "",
    "Thüringen": "",
    "Brandenburg_Inspire_Boden": "https://inspire.brandenburg.de/services/so_alkis_wfs?",
    "Berlin": "https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_wfs_alkis"
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

