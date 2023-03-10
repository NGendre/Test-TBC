from django.shortcuts import render

from django.http import HttpResponse
import pandas
import pygsheets

def index(request):
    googleCredentials = pygsheets.authorize(service_file='resources/test-tpc-380213-2638c9d7cb06.json')
    dataframe = pandas.DataFrame()
    dataframe['test'] = ['coucou','google','sheets']
    googleSheet = googleCredentials.open('Test-TBC')
    currentGoogleSheet = googleSheet[0]
    currentGoogleSheet.set_dataframe(dataframe,(1,1))
    return HttpResponse(dataframe['test'])
# TODO: tout deplacer dans dans le meme controller + supprimer view spreadsheet + scinder code en methodes si possible