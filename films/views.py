
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import pandas as pd


import services.transformData.addDataToMovies as addDataToMovies
import  services.api.OMDB as omdb
import services.api.GoogleSheets as gsheets


# ARRAY TITRES NECESSAIRES

fastAndFuriousTitles = ['The fast and the furious', '2 fast 2 furious', 'The Fast and the Furious: Tokyo Drift', 'Fast %26 Furious',
    'Fast Five', 'Fast %26 Furious 6', 'Furious 7', 'The Fate of the Furious', 'F9']

piratesTitles = ["Pirates+of+the+Caribbean%3A+The+Curse+of+the+Black+Pearl"
                     ,"Pirates+of+the+Caribbean%3A+Dead+Man's+Chest" ,"Pirates+of+the+Caribbean%3A+At+World's+End",
                     "Pirates of the Caribbean: On Stranger Tides" ,"Pirates of the Caribbean: Dead Men Tell No Tales"]
starWarsTitles = ['Star Wars','The Empire Strikes Back','Return of the Jedi','Episode I - The Phantom Menace','Episode II - Attack of the Clones',
                 'Revenge of the Sith','The Force Awakens','The Last Jedi','The Rise of Skywalker']
# uses by search parameters of API


def globalMovieSearch(request):  # DOES NOT WORK: adds parasitic data (too much movies not from the franchise) and not enough data (no actors)
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
    # for it in testArray:
    #     returnedData.append(addDataToMovies.transformData(it))
    for it in fastAndFuriousTitles:
        returnedData.append(addDataToMovies.transformData(it))
    for it in piratesTitles:
        returnedData.append(addDataToMovies.transformData(it))
    actorList = []
    for movie in returnedData:
        actors = movie['Actors'].split(', ')
        for actor in actors:
            actorList.append(actor)
    gsheets.sendToGoogleSheets(pd.DataFrame(returnedData),1,1)
    addDataToMovies.findActorsInCommonStarWars(actorList,starWarsTitles)
    return HttpResponse(returnedData)


