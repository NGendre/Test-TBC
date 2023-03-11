import json

import services.api.OMDB as omdb
import services.api.GoogleSheets as gsheets
import pandas as pd
import numpy as np

def transformData(movie):
    movie = omdb.sendQuery('type=movie&t=' +movie)
    movie = producesBefore2015(movie)
    movie = hasPaulWalker(movie)
    return movie

def producesBefore2015(movie):
    movie['producedBefore2015'] = False
    if (int(movie['Year']) < 2015):
        movie['producedBefore2015'] = True
    return movie

def hasPaulWalker(movie):
    movie['hasPaulWalker'] = False
    arrayActors = movie['Actors'].split(', ')
    for actor in arrayActors:
        if (actor == 'Paul Walker'):
            movie['hasPaulWalker'] = True
    return movie

def findActorsInCommonStarWars(actorsFromOtherMovies,starWarsTitles):
    starWarsActors = []
    for title in starWarsTitles:
        movie = omdb.sendQuery('t='+title)
        actors = movie['Actors'].split(', ')
        for actor in actors:
            starWarsActors.append(actor)
    print(starWarsActors)
    actorsInCommon = np.intersect1d(np.array(actorsFromOtherMovies),np.array(starWarsActors))
    gsheets.sendToGoogleSheets(pd.DataFrame(actorsInCommon),20,20)