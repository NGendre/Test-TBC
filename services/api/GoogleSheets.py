import pandas
import pygsheets


def sendToGoogleSheets(dataFrame, column,line):
    googleCredentials = pygsheets.authorize(service_file='resources/test-tpc-380213-2638c9d7cb06.json')
    googleSheet = googleCredentials.open('Test-TBC')
    currentGoogleSheet = googleSheet[0]
    # dataframe = pandas.DataFrame()
    # dataframe['test'] = ['coucou','google','sheets']

    currentGoogleSheet.set_dataframe(dataframe,(1,1))
# TODO: tout deplacer dans dans le meme controller + supprimer view spreadsheet + scinder code en methodes si possible