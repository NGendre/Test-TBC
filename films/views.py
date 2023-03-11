

from django.shortcuts import render
from django.http import HttpResponse
import requests

import  services.api.OMDB as omdb
def globalFastAndFuriousSearch(request):
    movieArrau = omdb.sendQuery("s=Fast+%26+Furious&type=movie")
    pageCount = int(aaaa['totalResults'])//10
    movieList = []
    for pageIterator in range(1,pageCount):
        movie = ombd.sendQuery("s=Fast+%26+Furious&type=movie&page="+str(pageIterator))
        jsonFile = req.json()
        for movieIterator in range (0,9):
            movieList.append(jsonFile['Search'][movieIterator])
    return HttpResponse(json.dumps(movieList))

def specificFastAndFuriousSearchFromArray(request):
    fastAndFuriousTitles = ['Fast X']
    # 'The fast and the furious', '2 fast 2 furious', 'The Fast and the Furious: Tokyo Drift', 'Fast %26 Furious',
    # 'Fast Five', 'Fast %26 Furious 6', 'Furious 7', 'The Fate of the Furious', 'F9', 'Fast X'
    returnedData = []
    for it in fastAndFuriousTitles:
        movieJson = omdb.sendQuery('t='+it)
        movieJson['producedBefore2015'] = 'false'
        if (int(movieJson['Year'])<2015):
            movieJson['producedBefore2015'] = 'true'
        movieJson['hasPaulWalker'] = 'false'
        arrayActors = movieJson['Actors'].split(', ')
        for actor in arrayActors:
            if (actor == 'Paul Walker'):
                movieJson['hasPaulWalker'] = 'true'
        returnedData.append(movieJson)
    # TODO transform pandas dataframe
    return HttpResponse(returnedData)
