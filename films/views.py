
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import pandas as pd


import services.transformData.addDataToMovies as addDataToMovies
import  services.api.OMDB as omdb
import services.api.GoogleSheets as gsheets


testArray = ['The fast and the furious']
# fastAndFuriousTitles = ['The fast and the furious', '2 fast 2 furious'
#     'The fast and the furious', '2 fast 2 furious', 'The Fast and the Furious: Tokyo Drift', 'Fast %26 Furious',
#     'Fast Five', 'Fast %26 Furious 6', 'Furious 7', 'The Fate of the Furious', 'F9', 'Fast X']
#
# piratesTitles = ["Pirates+of+the+Caribbean%3A+The+Curse+of+the+Black+Pearl"
#                      ,"Pirates+of+the+Caribbean%3A+Dead+Man's+Chest" ,"Pirates+of+the+Caribbean%3A+At+World's+End",
#                      "Pirates of the Caribbean: On Stranger Tides" ,"Pirates of the Caribbean: Dead Men Tell No Tales"]
# uses by search parameters of API
def globalMovieSearch(request):
    movieArray = omdb.sendQuery("s=Fast+%26+Furious&type=movie")
    pageCount = int(movieArray['totalResults'] )//10
    movieList = []
    for pageIterator in range(1,pageCount):
        movieList = omdb.sendQuery("s=Fast+%26+Furious&type=movie&page= " +str(pageIterator))
        for movieIterator in range(0,9):
            movieList.append(movieList['Search'][movieIterator])
    return HttpResponse(json.dumps(movieList))


# uses by title parameters of API (no parasitic data)
def specificMovieFromArray(request):
    returnedData = []
    for it in testArray:
        returnedData.append(addDataToMovies.transformData(it))
    # for it in fastAndFuriousTitles:
    #     returnedData.append(addDataToMovies.transformData(it))
    # for it in piratesTitles:
    #     returnedData.append(addDataToMovies.transformData(it))
    movieDataframe = pd.DataFrame(returnedData)
    gsheets.sendToGoogleSheets(movieDataframe,1,1)
    return HttpResponse(returnedData)


