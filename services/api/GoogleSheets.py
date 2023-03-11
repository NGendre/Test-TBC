import pygsheets


def sendToGoogleSheets(dataFrame, column,line):
    googleCredentials = pygsheets.authorize(service_file='resources/test-tpc-380213-2638c9d7cb06.json')
    googleSheet = googleCredentials.open('Test-TBC')
    currentGoogleSheet = googleSheet[0]
    currentGoogleSheet.set_dataframe(dataFrame,(column,line))