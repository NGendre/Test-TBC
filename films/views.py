import json

from django.shortcuts import render
from django.http import HttpResponse
import requests

def globalFastAndFuriousSearch(request):
    req = requests.get("http://www.omdbapi.com/?apikey=e5675762&s=Fast+%26+Furious&type=movie")
    aaaa = req.json()
    pageCount = int(aaaa['totalResults'])//10
    movieList = []
    for pageIterator in range(1,pageCount):
        req = requests.get("http://www.omdbapi.com/?apikey=e5675762&s=Fast+%26+Furious&type=movie&page="+str(pageIterator))
        jsonFile = req.json()
        for movieIterator in range (0,9):
            movieList.append(jsonFile['Search'][movieIterator])
    return HttpResponse(json.dumps(movieList))

def specificFastAndFuriousSearchFromArray(request):
    fastAndFuriousTitles = ['The fast and the furious']
    # , '2 fast 2 furious', 'The Fast and the Furious: Tokyo Drift', 'Fast %26 Furious',
    # 'Fast Five', 'Fast %26 Furious 6', 'Furious 7', 'The Fate of the Furious', 'F9', 'Fast X'
    returnedData = []
    for it in fastAndFuriousTitles:
        req = requests.get('http://www.omdbapi.com/?apikey=e5675762&t='+it)
        json = req.json()
        json['producedBefore2015'] = 'false'
        if (int(json['Year'])<2015):
            json['producedBefore2015'] = 'true'
        json['hasPaulWalker'] = 'false'
        for i in json['Actors']:
            if (json['Actors'][i] == 'Paul Walker'):
                json['hasPaulWalker'] = 'true'

        returnedData.append(json)
    print(returnedData)

    return HttpResponse(returnedData+'\n'+)
